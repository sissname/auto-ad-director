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
    "scripts/validate_v1_readiness.py",
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "任务接收清单",
        "Reference Routing",
        "Prompt Bible",
        "专业评审包",
        "案例复盘",
        "v1 专业质量门",
        "generic black-gold luxury",
    ],
    "references/luxury-visual-framework.md": [
        "Hero Still Life",
        "Macro / Material Detail",
        "Hand / Body Relation",
    ],
    "references/category-material-camera-logic.md": [
        "香水",
        "腕表",
        "珠宝",
        "包袋",
    ],
    "references/benchmark-suite.md": [
        "验收基准 1",
        "验收基准 8",
        "验收基准 10",
        "Fail if：",
    ],
    "references/quality-scorecard.md": [
        "主体结构",
        "材质真实度",
        "商业可用性",
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

    benchmark_text = (ROOT / "references/benchmark-suite.md").read_text(encoding="utf-8")
    if benchmark_text.count("验收基准 ") < 10:
        failures.append("references/benchmark-suite.md: expected 10 benchmark cases")

    if failures:
        print("Smoke test failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
