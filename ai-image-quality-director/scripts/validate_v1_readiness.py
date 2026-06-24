from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/quality-diagnosis-framework.md",
    "references/failure-taxonomy-and-repair.md",
    "references/iteration-strategy.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "scripts/smoke_tests.py",
]

SKILL_MARKERS = [
    "专业评审包",
    "案例复盘",
    "v1 专业质量门",
    "质量分",
]

SCORECARD_MARKERS = [
    "结构",
    "真实感",
    "光影",
    "品牌气质",
    "商业可用性",
    "文字 / logo 风险",
    "修复效率",
]

CASE_MARKERS = [
    "案例 1：夜景汽车图氛围好，但轮胎漂浮",
    "案例 2：护肤瓶材质高级，但标签乱码",
    "案例 3：时尚海报脸能用，但手部翻车",
    "案例 4：快闪店效果图入口炫，但人和装置比例失真",
    "案例 5：高端香水图主体没坏，但气质像电商白底",
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
