export const BLANK_THREAD_SEED_PROMPT = `Start Maker onboarding now.

Show the mandatory 1–4 menu first.

If no real user brief is provided yet, stop after the menu and wait for the user.`;

export function buildSeedPrompt({ mode = "blank", briefContext = "" } = {}) {
  const trimmedContext = briefContext.trim();

  if (mode !== "blank" && trimmedContext) {
    return `${BLANK_THREAD_SEED_PROMPT}

Additional launch context:
${trimmedContext}`;
  }

  return BLANK_THREAD_SEED_PROMPT;
}
