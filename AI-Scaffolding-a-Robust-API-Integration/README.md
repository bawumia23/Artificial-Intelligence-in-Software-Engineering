# AI: Scaffolding a Robust API Integration

## Objective

Use a **Contextual Prompting** technique to get an AI assistant to refactor
`sentiment_analyzer.py` so it (1) securely reads an API key from an
environment variable and sends it as a `Bearer` token in the request
headers, and (2) handles two additional, specific failure modes
(`Timeout` and `ConnectionError`) with distinct error messages.

## AI tool used

Claude (Anthropic)

## Files in this folder

- **`sentiment_analyzer_initial.py`** — the starting version of the tool,
  exactly as given in the assignment (minor formatting/typo fixes only,
  no logic changes). It posts to the Text Processing API with no
  authentication and handles three categories of exception:
  `HTTPError`, the general `RequestException`, and `(KeyError, ValueError)`.

- **`contextual_prompt.txt`** — the full, single contextual prompt
  submitted to the AI. It supplies the entire initial file as context and
  asks for two specific changes: (1) reading `TEXT_PROCESSING_API_KEY`
  from the environment via `os` and attaching it as an
  `Authorization: Bearer <key>` header, and (2) adding
  `requests.exceptions.Timeout` and `requests.exceptions.ConnectionError`
  handlers, each printing a distinct message to `sys.stderr`.

- **`sentiment_analyzer_refactored.py`** — the AI's response to that
  prompt: the same tool, now reading the API key from the environment,
  attaching it as a Bearer token, and handling five distinct exception
  categories in order of specificity (`Timeout`, `ConnectionError`,
  `HTTPError`, general `RequestException`, then `(KeyError, ValueError)`).

- **`mock_sentiment_api.py`** — a small local Flask stand-in for the
  external API, used only to demonstrate the full request/response flow
  end-to-end (checking for the `Bearer` header and returning a
  `positive` label), since the real public API intermittently blocks
  requests from cloud/sandboxed IP ranges.

## How it was verified

The refactored script was run against the local mock server with
`TEXT_PROCESSING_API_KEY` set, returning `positive` for a positive test
sentence with exit code 0. It was also run with the environment variable
unset, correctly reporting an `HTTP Error: 401` through the existing
`HTTPError` handler rather than crashing — confirming the header wiring
and the new exception handling both work as intended.
