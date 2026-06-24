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
    "scripts/smoke_tests.py",
]

PLATFORMS = [
    "Midjourney",
    "Jimeng",
    "Kling",
    "Seedream",
    "Nano Banana",
    "Generic Chinese",
]

SCORECARD_FIELDS = [
    "Visual Specificity",
    "Transferability",
    "Composition Logic",
    "Lighting Control",
    "Platform Fit",
    "Risk Handling",
    "Iteration Usefulness",
]

CASE_MARKERS = [
    "Case 1: Rainy Automotive Night Reference to Running Shoes",
    "Case 2: Low-Key Fashion Portrait to Perfume Still Life",
    "Case 3: Warm Hotel Lobby Analysis Only",
    "Case 4: Mall Light Tunnel to Skincare Pop-Up",
    "Case 5: Distinctive Illustrated Poster Risk Review",
]

BENCHMARK_MARKERS = [
    "Acceptance Benchmark 1",
    "Acceptance Benchmark 2",
    "Acceptance Benchmark 3",
    "Acceptance Benchmark 4",
    "Acceptance Benchmark 5",
]

SKILL_MARKERS = [
    "Reference Intake Checklist",
    "Professional Quality Gate",
    "Prompt Bible",
    "Case Replay",
    "Quality score",
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
    require_contains("references/platform-output-formats.md", PLATFORMS, failures)
    require_contains("references/quality-scorecard.md", SCORECARD_FIELDS, failures)
    require_contains("references/case-library.md", CASE_MARKERS, failures)
    require_contains("references/benchmark-suite.md", BENCHMARK_MARKERS, failures)

    benchmark_text = read("references/benchmark-suite.md")
    if benchmark_text.count("Fail if:") < 5:
        failures.append("references/benchmark-suite.md: each benchmark needs a Fail if section")

    case_text = read("references/case-library.md")
    for required in ["Transfer:", "Prompt logic:"]:
        if case_text.count(required) < 5:
            failures.append(f"references/case-library.md: expected at least 5 {required!r} sections")

    platform_text = read("references/platform-output-formats.md")
    for required in ["Use:", "Avoid:", "Failure modes:"]:
        if platform_text.count(required) < 6:
            failures.append(f"references/platform-output-formats.md: expected platform-level {required!r} guidance for 6 platforms")

    if failures:
        print("v1 readiness failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("v1 readiness passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
