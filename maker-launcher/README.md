# Maker Launcher

A thin internal launcher for the Cars24 Maker Agent.

This app creates a fresh Codex thread, sends a single seed prompt so Maker starts the conversation, then opens the created thread in the native Codex app via the official `codex://threads/<thread-id>` deep link.

## What it does

- renders a minimal internal page with one primary action: `New Maker Thread`
- exposes `POST /maker/threads`
- starts a Codex thread in the Maker workspace
- sends the bootstrap prompt as the first user message
- returns the created thread id and a Codex deep link

It intentionally does **not** replace the agent with a form workflow or a custom chat surface.

## Setup

```bash
cd maker-launcher
npm install
cp .env.example .env
npm start
```

Then open [http://localhost:4317](http://localhost:4317).

## Configuration

- `PORT`: HTTP port for the launcher
- `WORKSPACE_PATH`: absolute path to the Maker workspace to open in Codex
- `CODEX_MODEL`: Codex model name
- `CODEX_SANDBOX_MODE`: `read-only`, `workspace-write`, or `danger-full-access`
- `CODEX_APPROVAL_POLICY`: `never`, `on-request`, `on-failure`, or `untrusted`
- `CODEX_NETWORK_ACCESS_ENABLED`: `true` or `false`
- `CODEX_SKIP_GIT_REPO_CHECK`: `true` or `false`
- `CODEX_MODEL_REASONING_EFFORT`: `minimal`, `low`, `medium`, `high`, or `xhigh`
- `CODEX_WEB_SEARCH_MODE`: `disabled`, `cached`, or `live`
- `CODEX_DEEP_LINK_TEMPLATE`: defaults to `codex://threads/{thread_id}`

## API

### `POST /maker/threads`

Request body:

```json
{
  "workspace": "maker-agent-v2",
  "mode": "blank"
}
```

Success response:

```json
{
  "status": "ready",
  "thread_id": "thr_123",
  "thread_url": "codex://threads/thr_123",
  "workspace": "maker-agent-v2",
  "mode": "blank"
}
```

Recoverable bootstrap failure:

```json
{
  "status": "thread_created_seed_failed",
  "thread_id": "thr_123",
  "thread_url": "codex://threads/thr_123",
  "error": "Codex failed while sending the onboarding seed prompt."
}
```

## Notes

- This app uses the official Codex SDK server-side and expects a local Codex setup that can start threads.
- The deep-link handoff relies on the official Codex app command format for opening an existing local thread.
- V1 targets blank-thread bootstrap only. Later launch-from-context flows can append brief details to the seed prompt.
