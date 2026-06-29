# nTrust Repository Rules

## Client/MVP Sandbox Organization
- **Do NOT leak Spine internals**: When working inside this client repository, you must **never** copy or commit Spine's internal framework files (such as `spine.db`, `spine_core_*`, `server.py` from Spine root, or `sent_emails.jsonl`).
- **Use structural folders**: Do not dump dozens of MVP scripts directly into the root directory. Organize them into appropriate folders (e.g., `src/`, `api/`, `tests/`, `docs/`).
- **Use .gitignore**: Ensure you are actively utilizing `.gitignore` to avoid committing local scratch files, testing evidence, and ephemeral databases.
