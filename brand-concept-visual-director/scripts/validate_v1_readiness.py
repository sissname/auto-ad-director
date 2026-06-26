from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/brand-concept-framework.md",
    "references/reference-and-logo-boundaries.md",
    "references/creative-review-scorecard.md",
    "references/case-library.md",
    "references/examples.md",
    "references/benchmark-suite.md",
    "scripts/smoke_tests.py",
]

REQUIRED_SKILL_MARKERS = [
    "品牌定位",
    "参考图角色",
    "禁区",
    "3-5 个方向",
    "创意总监评审",
    "下一轮问题",
    "不是最终 logo",
]

CASE_MARKERS = ["案例 1", "案例 2", "案例 3", "案例 4", "案例 5"]
BENCHMARK_MARKERS = [
    "Smoke Prompt 1",
    "Smoke Prompt 2",
    "Smoke Prompt 3",
    "Acceptance Benchmark 4",
    "Acceptance Benchmark 5",
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    failures = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"missing {rel}")
    if failures:
        print("v1 readiness failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    skill = read("SKILL.md")
    for marker in REQUIRED_SKILL_MARKERS:
        if marker not in skill:
            failures.append(f"SKILL.md missing {marker!r}")

    cases = read("references/case-library.md")
    for marker in CASE_MARKERS:
        if marker not in cases:
            failures.append(f"case-library.md missing {marker!r}")

    benchmark = read("references/benchmark-suite.md")
    for marker in BENCHMARK_MARKERS:
        if marker not in benchmark:
            failures.append(f"benchmark-suite.md missing {marker!r}")

    review = read("references/creative-review-scorecard.md")
    for marker in ["品牌贴合", "识别性", "延展性", "生成可控性", "风险", "下一轮价值"]:
        if marker not in review:
            failures.append(f"creative-review-scorecard.md missing {marker!r}")

    boundary = read("references/reference-and-logo-boundaries.md")
    for marker in ["可以借鉴", "不应复制", "SVG / 草图处理", "这不是最终 logo"]:
        if marker not in boundary:
            failures.append(f"reference-and-logo-boundaries.md missing {marker!r}")

    if failures:
        print("v1 readiness failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("v1 readiness passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
