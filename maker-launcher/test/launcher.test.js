import test from "node:test";
import assert from "node:assert/strict";

import { CodexBootstrapError, CodexLauncher, buildThreadUrl } from "../src/codexLauncher.js";
import { buildSeedPrompt, BLANK_THREAD_SEED_PROMPT } from "../src/seedPrompt.js";

test("buildSeedPrompt returns the blank bootstrap prompt by default", () => {
  assert.equal(buildSeedPrompt(), BLANK_THREAD_SEED_PROMPT);
});

test("buildSeedPrompt appends launch context for non-blank modes", () => {
  const prompt = buildSeedPrompt({
    mode: "prefilled",
    briefContext: "Platform: LinkedIn\nNeed: Write-up + image"
  });

  assert.match(prompt, /Additional launch context:/);
  assert.match(prompt, /Platform: LinkedIn/);
});

test("buildThreadUrl uses the configured deep-link template", () => {
  assert.equal(
    buildThreadUrl("thr_123", "codex://threads/{thread_id}"),
    "codex://threads/thr_123"
  );
});

test("CodexLauncher returns thread metadata after a successful bootstrap", async () => {
  const fakeStream = async function* () {
    yield { type: "thread.started", thread_id: "thr_success" };
    yield { type: "turn.started" };
    yield { type: "turn.completed", usage: null };
  };

  const fakeCodex = {
    startThread() {
      return {
        id: null,
        async runStreamed() {
          return { events: fakeStream() };
        }
      };
    }
  };

  const launcher = new CodexLauncher(
    {
      model: "gpt-5.4",
      sandboxMode: "workspace-write",
      workspacePath: "/tmp/maker",
      skipGitRepoCheck: false,
      modelReasoningEffort: "medium",
      networkAccessEnabled: true,
      webSearchMode: "disabled",
      approvalPolicy: "on-request",
      deepLinkTemplate: "codex://threads/{thread_id}"
    },
    async () => fakeCodex
  );

  const result = await launcher.createMakerThread();
  assert.equal(result.status, "ready");
  assert.equal(result.thread_id, "thr_success");
  assert.equal(result.thread_url, "codex://threads/thr_success");
});

test("CodexLauncher exposes recoverable bootstrap failures with thread details", async () => {
  const fakeStream = async function* () {
    yield { type: "thread.started", thread_id: "thr_partial" };
    yield { type: "turn.failed", error: { message: "Seed prompt failed." } };
  };

  const fakeCodex = {
    startThread() {
      return {
        id: null,
        async runStreamed() {
          return { events: fakeStream() };
        }
      };
    }
  };

  const launcher = new CodexLauncher(
    {
      model: "gpt-5.4",
      sandboxMode: "workspace-write",
      workspacePath: "/tmp/maker",
      skipGitRepoCheck: false,
      modelReasoningEffort: "medium",
      networkAccessEnabled: true,
      webSearchMode: "disabled",
      approvalPolicy: "on-request",
      deepLinkTemplate: "codex://threads/{thread_id}"
    },
    async () => fakeCodex
  );

  await assert.rejects(
    launcher.createMakerThread(),
    (error) => {
      assert.ok(error instanceof CodexBootstrapError);
      assert.equal(error.details.threadId, "thr_partial");
      assert.equal(error.details.threadUrl, "codex://threads/thr_partial");
      return true;
    }
  );
});
