from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/contact-sheet-framework.md",
    "references/shot-taxonomy.md",
    "references/platform-prompt-formats.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "references/quality-scorecard.md",
    "references/case-library.md",
    "scripts/smoke_tests.py",
]


SKILL_MARKERS = [
    "### 专业提案版输出",
    "## 案例复盘",
    "## v1 专业质量门",
]


SCORECARD_MARKERS = [
    "### Anchor 一致性",
    "### Narrative 覆盖度",
    "### Shot 多样性",
    "### 平台可执行性",
    "### 裁切与版面可用性",
    "### 商业清晰度",
    "### 生产可信度",
]


CASE_MARKERS = [
    "## 案例 1：雨夜汽车 9 格广告板",
    "## 案例 2：护肤精华 6 格产品发布",
    "## 案例 3：秋冬 lookbook 12 格时尚系列",
    "## 案例 4：耳机新品 9 格产品 campaign",
    "## 案例 5：商场中庭 16 格空间提案",
]


BENCHMARK_MARKERS = [f"## 验收基准 {index}" for index in range(1, 11)]


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
