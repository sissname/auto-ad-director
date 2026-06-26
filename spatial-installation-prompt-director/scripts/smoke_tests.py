from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/spatial-installation-framework.md",
    "references/scenario-playbooks.md",
    "references/site-intake-and-traffic-flow.md",
    "references/prompt-bible-examples.md",
    "references/examples.md",
    "references/benchmark-suite.md",
]


REQUIRED_PHRASES = {
    "SKILL.md": [
        "任务接收清单",
        "Site Intake Decision",
        "Reference Routing",
        "Zone Prompt Package",
        "Review and Repair",
    ],
    "references/spatial-installation-framework.md": [
        "六区交付法",
        "统一 Style Anchor 的 8 个锚点",
        "入口 / 主装置 / 灯光 / 地贴 / 动线 / 拍照点",
    ],
    "references/scenario-playbooks.md": [
        "Mall Display",
        "Pop-up",
        "Exhibition",
        "Immersive Corridor",
    ],
    "references/site-intake-and-traffic-flow.md": [
        "现场照片 intake 最低要求",
        "文字 brief intake 最低要求",
        "动线判断四步法",
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
