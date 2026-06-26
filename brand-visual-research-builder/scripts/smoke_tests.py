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
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "Compact Research Bank",
        "Prompt Translation Rules",
        "Failure Risks",
        "不保存原图",
        "不宣称官方授权",
    ],
    "references/compact-research-bank.md": [
        "Brand 1：Apple",
        "Brand 2：Nike",
        "Brand 3：Porsche",
        "Brand 4：Dyson",
        "Brand 5：Xiaomi EV",
    ],
    "references/benchmark-suite.md": [
        "验收基准 1",
        "验收基准 2",
        "验收基准 3",
        "验收基准 4",
        "验收基准 5",
    ],
}


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing files:")
        for path in missing:
            print(f"- {path}")
        return 1

    failures = []
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
