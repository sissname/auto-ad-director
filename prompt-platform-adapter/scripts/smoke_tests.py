from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/platform-rules.md",
    "references/platform-matrix.md",
    "references/risk-controls.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "scripts/validate_v1_readiness.py",
]

REQUIRED_MARKERS = {
    "SKILL.md": [
        "Platform Intake Checklist",
        "Professional Conversion Gate",
        "Failed Prompt Repair",
        "Prompt Bible Conversion",
        "A/B Test Conversion",
    ],
    "references/platform-matrix.md": [
        "Midjourney",
        "Jimeng",
        "Kling",
        "Nano Banana",
        "Seedream",
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
    failures = []

    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            failures.append(f"missing {rel_path}")

    if failures:
        print("Smoke tests failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    for rel_path, markers in REQUIRED_MARKERS.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"{rel_path} missing {marker!r}")

    if failures:
        print("Smoke tests failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
