import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const defaultWorkspacePath = path.resolve(__dirname, "..", "..");

function parseBoolean(value, fallback) {
  if (value === undefined) {
    return fallback;
  }

  const normalized = String(value).trim().toLowerCase();
  if (["1", "true", "yes", "on"].includes(normalized)) {
    return true;
  }
  if (["0", "false", "no", "off"].includes(normalized)) {
    return false;
  }
  return fallback;
}

export function getConfig() {
  return {
    port: Number(process.env.PORT || 4317),
    workspacePath: process.env.WORKSPACE_PATH || defaultWorkspacePath,
    model: process.env.CODEX_MODEL || "gpt-5.4",
    sandboxMode: process.env.CODEX_SANDBOX_MODE || "workspace-write",
    approvalPolicy: process.env.CODEX_APPROVAL_POLICY || "on-request",
    networkAccessEnabled: parseBoolean(process.env.CODEX_NETWORK_ACCESS_ENABLED, true),
    skipGitRepoCheck: parseBoolean(process.env.CODEX_SKIP_GIT_REPO_CHECK, false),
    modelReasoningEffort: process.env.CODEX_MODEL_REASONING_EFFORT || "medium",
    webSearchMode: process.env.CODEX_WEB_SEARCH_MODE || "disabled",
    deepLinkTemplate: process.env.CODEX_DEEP_LINK_TEMPLATE || "codex://threads/{thread_id}"
  };
}
