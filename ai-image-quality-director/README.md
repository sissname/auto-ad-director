# AI Image Quality Director

AI Image Quality Director 是一个面向 AI 生图质量评审、失败定位和修复迭代的 Codex skill。

它的目标不是“夸图好看”，而是把一张图到底能不能用、哪里坏了、值不值得修、下一轮该怎么改，拆成清晰可执行的判断。

## 适合谁

- 在做 AI 生图但经常遇到“感觉不对，却说不清哪里不对”的团队
- 需要给客户、设计师、运营或内部评审会做选图说明的人
- 想把失败图快速归因，并输出下一轮修复 prompt 的使用者

## 能解决什么问题

- 单张图评分：这张图是保留、小修、抢救还是重做
- 多张图选优：哪张最值得继续，哪张应该放弃
- 失败诊断：结构、真实感、光影、材质、品牌气质、商业可用性、文字 / logo 风险
- 修复 prompt：把失败类型翻译成最小修复动作
- 下一轮策略：A/B 测试、版本记录、保留项与风险观察点

## 目录结构

```text
ai-image-quality-director/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-suite.md
│  ├─ case-library.md
│  ├─ examples.md
│  ├─ failure-taxonomy-and-repair.md
│  ├─ iteration-strategy.md
│  ├─ quality-diagnosis-framework.md
│  └─ quality-scorecard.md
└─ scripts/
   ├─ smoke_tests.py
   └─ validate_v1_readiness.py
```

## 安装

复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force . "$env:USERPROFILE\.codex\skills\ai-image-quality-director"
```

然后在 Codex 里使用：

```text
Use $ai-image-quality-director to review this AI-generated image, score it, and propose the next repair prompt.
```

中文也可以直接用：

```text
用 ai-image-quality-director 帮我评审这张 AI 生图，告诉我值不值得修，并给下一轮修复方案。
```

## 交付原则

- 先修致命问题，再谈风格优化
- 评分必须能转成动作，不停留在审美形容词
- 能小修就不大改，必须重做时要明确说明原因
- 文字、logo、包装文案优先建议后期补字，不承诺模型稳定生成
- 没看到图片时要明确写“基于描述推断”

## 本地验证

```powershell
$env:PYTHONUTF8='1'
python C:\Users\windows\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\windows\.codex\skills\ai-image-quality-director
python C:\Users\windows\.codex\skills\ai-image-quality-director\scripts\smoke_tests.py
python C:\Users\windows\.codex\skills\ai-image-quality-director\scripts\validate_v1_readiness.py
```

## English Summary

This skill helps Codex review AI-generated images with a practical production lens: scoring, failure diagnosis, repair prompts, and next-iteration planning. It is designed for commercial usability reviews rather than generic aesthetic commentary.

## License

MIT
