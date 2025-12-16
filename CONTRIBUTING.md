# Contributing to this Repository

Thank you for your interest in making AI safer. We welcome contributions!

## The Architecture Philosophy
This is not a standard Python library. It follows a strict **"Bicameral Architecture"**:
1.  **Layer 1 (Prompt):** Must isolate "Reasoning" from "Result".
2.  **Layer 2 (Sanitizer):** Must treat all user input as untrusted data.
3.  **Layer 3 (Validator):** Must deterministically verify the output.

**If your Pull Request breaks this separation of concerns, it will be rejected.**

## Development Guidelines

### 1. New Features
If you add a new capability, you must update all three layers:
* Update the **Prompt** (The Beak/Door/Quill) to handle the intent.
* Update the **Validator** (The Tentacles/Tumblers/Lens) to verify the new output.

### 2. Red Team Testing (Mandatory)
Every new feature must include a **Hostile Test Case**.
* *Example:* If you add support for `INSERT` statements, you must add a test proving it rejects `INSERT INTO system_tables`.
* Add your tests to the `tests/` directory using `pytest`.

### 3. Style
* Follow PEP 8 standards.
* Do not include API keys in your commits.

## Getting Started
1.  Fork the repo.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run tests: `pytest`
4.  Submit your Pull Request.
5.  
