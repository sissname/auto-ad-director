from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/luxury-visual-framework.md",
    "references/category-material-camera-logic.md",
    "references/examples.md",
    "references/prompt-bible-examples.md",
    "references/benchmark-suite.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "references/iteration-playbook.md",
    "scripts/smoke_tests.py",
]

SKILL_MARKERS = [
    "专业评审包",
    "案例复盘",
    "v1 专业质量门",
    "质量分",
]

SCORECARD_MARKERS = [
    "主体结构",
    "材质真实度",
    "光影纪律",
    "品类正确性",
    "商业可用性",
    "文字 / logo 风险",
]

CASE_MARKERS = [
    "案例 1：香水气质对了，但瓶体像电商白底",
    "案例 2：腕表有戏剧性，但反光失控",
    "案例 3：珠宝很亮，但廉价闪爆",
    "案例 4：包袋结构好，但皮革和五金廉价",
    "案例 5：整套图很贵，但全靠黑金模板",
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
