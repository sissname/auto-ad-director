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
]

MARKERS = {
    "SKILL.md": ["输入检查清单", "品牌方向稿交付包", "Logo 前期探索安全输出", "专业质量门"],
    "references/benchmark-suite.md": ["Smoke Prompt 1", "Smoke Prompt 2", "Smoke Prompt 3"],
    "references/examples.md": ["示例 1", "示例 2", "示例 3"],
}


def main() -> int:
    failures = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"missing {rel}")
    for rel, markers in MARKERS.items():
        if not (ROOT / rel).exists():
            continue
        text = (ROOT / rel).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"{rel} missing {marker!r}")
    if failures:
        print("Smoke tests failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("Smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
