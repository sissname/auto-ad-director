from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/visual-breakdown-framework.md",
    "references/platform-output-formats.md",
    "references/risk-and-constraints.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "scripts/validate_v1_readiness.py",
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "Reference Intake Checklist",
        "Professional Quality Gate",
        "Prompt Bible",
        "Case Replay",
        "analysis only",
    ],
    "references/platform-output-formats.md": [
        "Midjourney",
        "Jimeng",
        "Kling",
        "Seedream",
        "Nano Banana",
        "Generic Chinese",
    ],
    "references/benchmark-suite.md": [
        "Acceptance Benchmark 1",
        "Acceptance Benchmark 2",
        "Acceptance Benchmark 3",
        "Acceptance Benchmark 4",
        "Acceptance Benchmark 5",
    ],
}


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing files:")
        for path in missing:
            print(f"- {path}")
        return 1

    failures = []
    for rel_path, phrases in REQUIRED_PHRASES.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                failures.append(f"{rel_path}: missing {phrase!r}")

    if failures:
        print("Smoke test failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
