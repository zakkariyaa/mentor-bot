# mentor/utils.py

import re

def static_warnings(code: str) -> list[str]:
    warnings = []

    # Check for recursion without base case
    if "def" in code and re.search(r"\breturn\b.*\b\w+\(.*\)", code):
        if "if" not in code or "base case" in code.lower():
            warnings.append("🌀 This function may be recursive but lacks a clear base case.")

    # Detect infinite loop
    if "while True" in code:
        warnings.append("♾️ This code contains an infinite loop (`while True`) — is that intentional?")

    # Dangerous functions
    if re.search(r"\b(eval|exec)\(", code):
        warnings.append("⚠️ Avoid using `eval()` or `exec()` unless absolutely necessary.")

    # Suspiciously short
    if len(code.strip().splitlines()) < 2:
        warnings.append("🧼 The snippet is very short — consider providing more context.")

    return warnings
