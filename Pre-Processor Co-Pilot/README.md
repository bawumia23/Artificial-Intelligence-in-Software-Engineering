# Pre-Processor Co-Pilot – AI Lab Assignment

## Files
- `flawed_macro.c` – unsafe MAX macro (precedence + side‑effect bugs)
- `safe_macro.c` – corrected version using parentheses
- `conditional_logging.h` – debug logging macro with `#ifdef DEBUG`, `__FILE__`, `__LINE__`

## AI Tool Used
ChatGPT (GPT-4)

## Prompt Summary
- Safety inspection: asked for precedence and side‑effect analysis.
- Code generation: three requirements – conditional compilation, `__FILE__`/`__LINE__`, variadic macro.
