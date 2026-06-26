from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/research-workflow.md",
    "references/official-source-rules.md",
    "references/prompt-translation-rules.md",
    "references/compact-research-bank.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "scripts/smoke_tests.py",
]

SKILL_MARKERS = [
    "来源优先级",
    "Compact Research Bank",
    "Prompt Translation Rules",
    "Failure Risks",
    "专业质量门",
]

QUALITY_FIELDS = [
    "来源覆盖",
    "证据纪律",
    "视觉具体度",
    "可转译性",
    "风险清晰度",
    "交付可用性",
    "非官方措辞",
]

CASE_MARKERS = [
    "案例 1：Apple",
    "案例 2：Nike",
    "案例 3：Porsche",
    "案例 4：Dyson",
    "案例 5：Xiaomi EV",
]

BENCHMARK_MARKERS = [
    "验收基准 1",
    "验收基准 2",
    "验收基准 3",
    "验收基准 4",
    "验收基准 5",
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
    require_contains("references/quality-scorecard.md", QUALITY_FIELDS, failures)
    require_contains("references/case-library.md", CASE_MARKERS, failures)
    require_contains("references/benchmark-suite.md", BENCHMARK_MARKERS, failures)

    benchmark_text = read("references/benchmark-suite.md")
    if benchmark_text.count("Fail if:") < 5:
        failures.append("references/benchmark-suite.md: expected 5 'Fail if:' sections")

    case_text = read("references/case-library.md")
    for required in ["Transfer:", "Prompt logic:"]:
        if case_text.count(required) < 5:
            failures.append(
                f"references/case-library.md: expected at least 5 {required!r} sections"
            )

    if failures:
        print("v1 readiness failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("v1 readiness passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
