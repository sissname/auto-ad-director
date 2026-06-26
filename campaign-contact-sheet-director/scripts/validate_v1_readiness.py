from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/contact-sheet-framework.md",
    "references/shot-taxonomy.md",
    "references/scenario-playbooks.md",
    "references/platform-prompt-matrix.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "scripts/smoke_tests.py",
]

SKILL_MARKERS = [
    "Contact Sheet Blueprint",
    "Per-frame Prompt Package",
    "Adapt Existing Direction",
    "Review and Repair",
    "v1 专业质量门",
]

SCORECARD_MARKERS = [
    "锚点统一度",
    "镜头覆盖度",
    "逐格逻辑清晰度",
    "平台提示可执行度",
    "版式与裁切可用性",
]

CASE_MARKERS = [
    "案例 1：高端汽车发布主视觉套图",
    "案例 2：高端护肤 launch board",
    "案例 3：时尚鞋履夜跑 campaign",
    "案例 4：香氛快闪中庭提案",
    "案例 5：珠宝 gallery light campaign",
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
    require_contains("references/quality-scorecard.md", SCORECARD_MARKERS, failures)
    require_contains("references/case-library.md", CASE_MARKERS, failures)
    require_contains("references/benchmark-suite.md", BENCHMARK_MARKERS, failures)

    benchmark_text = read("references/benchmark-suite.md")
    if benchmark_text.count("Fail if：") < 10:
        failures.append("references/benchmark-suite.md: expected 10 Fail if sections")

    case_text = read("references/case-library.md")
    for required in ["Transfer：", "Repair logic：", "Risk control："]:
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
