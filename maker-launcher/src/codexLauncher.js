import { buildSeedPrompt } from "./seedPrompt.js";

export class CodexBootstrapError extends Error {
  constructor(message, details = {}) {
    super(message);
    this.name = "CodexBootstrapError";
    this.details = details;
  }
}

export function buildThreadUrl(threadId, template = "codex://threads/{thread_id}") {
  if (!threadId) {
    return null;
  }

  return template.replaceAll("{thread_id}", threadId);
}

async function createDefaultCodex() {
  const module = await import("@openai/codex-sdk");
  return new module.Codex();
}

export class CodexLauncher {
  constructor(config, codexFactory = createDefaultCodex) {
    this.config = config;
    this.codexFactory = codexFactory;
  }

  async createMakerThread({ workspace = "maker-agent-v2", mode = "blank", briefContext = "" } = {}) {
    const codex = await this.codexFactory();
    const thread = codex.startThread({
      model: this.config.model,
      sandboxMode: this.config.sandboxMode,
      workingDirectory: this.config.workspacePath,
      skipGitRepoCheck: this.config.skipGitRepoCheck,
      modelReasoningEffort: this.config.modelReasoningEffort,
      networkAccessEnabled: this.config.networkAccessEnabled,
      webSearchMode: this.config.webSearchMode,
      approvalPolicy: this.config.approvalPolicy
    });

    const prompt = buildSeedPrompt({ mode, briefContext });
    const streamedTurn = await thread.runStreamed(prompt);

    let threadId = thread.id;
    let bootstrapFailedMessage = null;

    for await (const event of streamedTurn.events) {
      if (event.type === "thread.started") {
        threadId = event.thread_id;
      }

      if (event.type === "turn.failed") {
        bootstrapFailedMessage = event.error.message;
      }

      if (event.type === "error") {
        bootstrapFailedMessage = event.message;
      }
    }

    if (bootstrapFailedMessage) {
      throw new CodexBootstrapError(
        bootstrapFailedMessage,
        {
          threadId,
          workspace,
          mode,
          threadUrl: buildThreadUrl(threadId, this.config.deepLinkTemplate)
        }
      );
    }

    return {
      status: "ready",
      thread_id: threadId,
      thread_url: buildThreadUrl(threadId, this.config.deepLinkTemplate),
      workspace,
      mode
    };
  }
}
