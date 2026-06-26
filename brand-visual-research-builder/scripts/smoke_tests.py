from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/research-framework.md",
    "references/source-intake-and-compliance.md",
    "references/prompt-translation-rules.md",
    "references/compact-research-bank.md",
    "references/examples.md",
    "references/benchmark-suite.md",
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "核心工作流",
        "Reference Routing",
        "Compact Research Bank",
        "只做研究不写 Prompt",
        "品牌对标",
    ],
    "references/source-intake-and-compliance.md": [
        "不保存",
        "官方授权",
        "来源可信度标记",
    ],
    "references/compact-research-bank.md": [
        "Apple",
        "Nike",
        "Porsche",
        "Dyson",
        "Aesop",
    ],
    "references/benchmark-suite.md": [
        "验收基准 1",
        "验收基准 5",
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
        print("Smoke tests failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
