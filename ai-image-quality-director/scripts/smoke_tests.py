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
    "scripts/validate_v1_readiness.py",
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "任务接收清单",
        "Reference Routing",
        "只做诊断",
        "修复 Prompt",
        "专业评审包",
        "v1 专业质量门",
    ],
    "references/quality-diagnosis-framework.md": [
        "结构与主体完整性",
        "真实感与物理逻辑",
        "商业可用性",
        "文字 / logo 风险",
    ],
    "references/quality-scorecard.md": [
        "结构",
        "真实感",
        "光影",
        "品牌气质",
    ],
    "references/benchmark-suite.md": [
        "验收基准 1",
        "验收基准 5",
        "验收基准 10",
        "Fail if：",
    ],
}


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing files:")
        for path in missing:
            print(f"- {path}")
        return 1

    failures: list[str] = []
    for rel_path, phrases in REQUIRED_PHRASES.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                failures.append(f"{rel_path}: missing {phrase!r}")

    if failures:
        print("Smoke test failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
