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
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "任务接收清单",
        "Frame Count Decision",
        "Reference Routing",
        "Per-frame Prompt Package",
        "Review and Repair",
    ],
    "references/contact-sheet-framework.md": [
        "统一 Style Anchor 的 8 个锚点",
        "6 / 9 / 12 / 16 格默认配比",
        "Per-frame Shot Logic 的固定写法",
    ],
    "references/shot-taxonomy.md": [
        "Hero",
        "Detail",
        "Motion",
        "Social Crop",
    ],
    "references/scenario-playbooks.md": [
        "Advertising",
        "Product",
        "Fashion",
        "Spatial",
    ],
    "references/platform-prompt-matrix.md": [
        "Midjourney",
        "即梦",
        "可灵",
        "Seedream",
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
