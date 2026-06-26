from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/research-framework.md",
    "references/source-intake-and-compliance.md",
    "references/prompt-translation-rules.md",
    "references/compact-research-bank.md",
    "references/professional-quality-gate.md",
    "references/case-library.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "scripts/smoke_tests.py",
]

SKILL_MARKERS = [
    "专业研究包",
    "案例复用",
    "v1 专业质量门",
    "适合做什么 / 不适合做什么 / 还缺什么资料",
]

GATE_MARKERS = [
    "证据质量",
    "研究结论质量",
    "合规与风险",
    "可交付性",
]

CASE_MARKERS = [
    "案例 1：Apple 式消费电子研究，用于耳机主视觉方向",
    "案例 2：Nike 运动鞋研究，用于运动饮料广告前置",
    "案例 3：Porsche 911 研究，用于高端腕表夜景方向",
    "案例 4：Dyson Airwrap i.d. 研究，用于美容仪产品演示图",
    "案例 5：Aesop 研究，用于酒店备品与空间方向",
]

BENCHMARK_MARKERS = [f"验收基准 {index}" for index in range(1, 11)]


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
    require_contains("references/professional-quality-gate.md", GATE_MARKERS, failures)
    require_contains("references/case-library.md", CASE_MARKERS, failures)
    require_contains("references/benchmark-suite.md", BENCHMARK_MARKERS, failures)

    benchmark_text = read("references/benchmark-suite.md")
    if benchmark_text.count("Fail if：") < 10:
        failures.append("references/benchmark-suite.md: expected 10 Fail if sections")

    case_text = read("references/case-library.md")
    for required in ["Transfer：", "Risk control："]:
        if case_text.count(required) < 5:
            failures.append(f"references/case-library.md: expected at least 5 {required!r} sections")

    if failures:
        print("v1 readiness failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("v1 readiness passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
