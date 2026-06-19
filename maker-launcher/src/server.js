import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { CodexBootstrapError, CodexLauncher } from "./codexLauncher.js";
import { getConfig } from "./config.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const publicDir = path.resolve(__dirname, "..", "public");
const config = getConfig();
const launcher = new CodexLauncher(config);

function sendJson(response, statusCode, payload) {
  response.writeHead(statusCode, { "Content-Type": "application/json; charset=utf-8" });
  response.end(JSON.stringify(payload));
}

function sendHtml(response, html) {
  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end(html);
}

function readRequestBody(request) {
  return new Promise((resolve, reject) => {
    let raw = "";

    request.on("data", (chunk) => {
      raw += chunk;
      if (raw.length > 1024 * 1024) {
        reject(new Error("Request body is too large."));
      }
    });

    request.on("end", () => {
      if (!raw) {
        resolve({});
        return;
      }

      try {
        resolve(JSON.parse(raw));
      } catch {
        reject(new Error("Invalid JSON body."));
      }
    });

    request.on("error", reject);
  });
}

const server = createServer(async (request, response) => {
  try {
    if (request.method === "GET" && request.url === "/health") {
      sendJson(response, 200, { status: "ok" });
      return;
    }

    if (request.method === "POST" && request.url === "/maker/threads") {
      const body = await readRequestBody(request);
      const workspace = typeof body.workspace === "string" ? body.workspace : "maker-agent-v2";
      const mode = typeof body.mode === "string" ? body.mode : "blank";
      const briefContext = typeof body.briefContext === "string" ? body.briefContext : "";

      try {
        const result = await launcher.createMakerThread({ workspace, mode, briefContext });
        sendJson(response, 200, result);
        return;
      } catch (error) {
        if (error instanceof CodexBootstrapError && error.details?.threadId) {
          sendJson(response, 200, {
            status: "thread_created_seed_failed",
            thread_id: error.details.threadId,
            thread_url: error.details.threadUrl || null,
            workspace,
            mode,
            error: error.message
          });
          return;
        }

        sendJson(response, 500, {
          status: "launch_failed",
          error: error instanceof Error ? error.message : "Failed to create a new Maker thread."
        });
        return;
      }
    }

    if (request.method === "GET" && (request.url === "/" || request.url === "/index.html")) {
      const html = await readFile(path.join(publicDir, "index.html"), "utf8");
      sendHtml(response, html);
      return;
    }

    sendJson(response, 404, { status: "not_found" });
  } catch (error) {
    sendJson(response, 500, {
      status: "server_error",
      error: error instanceof Error ? error.message : "Unexpected server error."
    });
  }
});

server.listen(config.port, () => {
  console.log(`Maker Launcher listening on http://localhost:${config.port}`);
  console.log(`Workspace path: ${config.workspacePath}`);
});
