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
    "scripts/validate_v1_readiness.py",
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "## 核心工作流",
        "## 任务接收清单",
        "## Reference Routing",
        "## 输出模式",
        "## 案例复盘",
        "## v1 专业质量门",
    ],
    "references/contact-sheet-framework.md": [
        "### 6 格",
        "### 9 格",
        "### 12 格",
        "### 16 格",
        "### 广告场景",
        "### 产品场景",
        "### 时尚场景",
        "### 空间场景",
    ],
    "references/shot-taxonomy.md": [
        "### Hero",
        "### Detail",
        "### Lifestyle",
        "### Motion",
        "### Environment",
        "### Macro",
        "### Portrait",
        "### Social Crop",
    ],
    "references/platform-prompt-formats.md": [
        "## Midjourney",
        "## 即梦",
        "## 通用中文模型",
    ],
    "references/benchmark-suite.md": [
        "## Smoke Prompt 1",
        "## Smoke Prompt 5",
        "## 验收基准 1",
        "## 验收基准 10",
    ],
    "references/quality-scorecard.md": [
        "## 评分维度",
        "### Anchor 一致性",
        "### 平台可执行性",
    ],
    "references/case-library.md": [
        "## 案例 1：雨夜汽车 9 格广告板",
        "## 案例 5：商场中庭 16 格空间提案",
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
