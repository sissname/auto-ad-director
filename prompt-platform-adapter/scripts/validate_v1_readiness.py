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
    "scripts/smoke_tests.py",
]

PLATFORMS = [
    "Midjourney",
    "Jimeng",
    "Kling",
    "Nano Banana",
    "Seedream",
    "Generic Chinese",
]

SCORE_FIELDS = [
    "Intent Preservation",
    "Platform Fit",
    "Parameter Discipline",
    "Risk Handling",
    "Visual Specificity",
    "Negative Prompt Usefulness",
    "Iteration Value",
]

CASE_MARKERS = [
    "Case 1: Perfume Product Hero",
    "Case 2: Fashion Editorial",
    "Case 3: Spatial Skincare Pop-Up",
    "Case 4: Automotive Reflection to Running Shoes",
    "Case 5: Failed Prompt Repair",
]

BENCHMARK_MARKERS = [
    "Acceptance Benchmark 1",
    "Acceptance Benchmark 2",
    "Acceptance Benchmark 3",
    "Acceptance Benchmark 4",
    "Acceptance Benchmark 5",
]

SKILL_MARKERS = [
    "Platform Intake Checklist",
    "Professional Conversion Gate",
    "Failed Prompt Repair",
    "Prompt Bible Conversion",
    "A/B Test Conversion",
    "Quality score",
    "Iteration note",
]


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def require_contains(rel_path: str, markers: list[str], failures: list[str]) -> None:
    text = read(rel_path)
    for marker in markers:
        if marker not in text:
            failures.append(f"{rel_path}: missing {marker!r}")


def main() -> int:
    failures: list[str] = []

    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            failures.append(f"missing required file: {rel_path}")

    if failures:
        print("v1 readiness failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    require_contains("SKILL.md", SKILL_MARKERS, failures)
    require_contains("references/platform-matrix.md", PLATFORMS, failures)
    require_contains("references/platform-rules.md", PLATFORMS, failures)
    require_contains("references/quality-scorecard.md", SCORE_FIELDS, failures)
    require_contains("references/case-library.md", CASE_MARKERS, failures)
    require_contains("references/benchmark-suite.md", BENCHMARK_MARKERS, failures)

    examples = read("references/examples.md")
    if examples.count("Conversion note:") < 3:
        failures.append("references/examples.md: expected at least 3 Conversion note sections")

    risk_controls = read("references/risk-controls.md")
    for marker in ["Text and Logo", "Realism", "Negative Prompts", "Reference Image Weight", "Conversion Note Checklist"]:
        if marker not in risk_controls:
            failures.append(f"references/risk-controls.md: missing {marker!r}")

    benchmark = read("references/benchmark-suite.md")
    if benchmark.count("Fail if:") < 5:
        failures.append("references/benchmark-suite.md: every acceptance benchmark needs a Fail if section")

    matrix = read("references/platform-matrix.md")
    for marker in ["Best for:", "Parameter strategy:", "Avoid:", "Failure modes:", "Adaptation focus:"]:
        if matrix.count(marker) < 6:
            failures.append(f"references/platform-matrix.md: expected six {marker!r} entries")

    if failures:
        print("v1 readiness failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("v1 readiness passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
