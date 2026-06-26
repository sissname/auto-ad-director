# Benchmark Suite

用于验证该 skill 是否能帮助用户选择品牌方向，而不是直接承诺最终 logo。

## Smoke Prompt 1：阅读品牌方向稿

```text
Use $brand-concept-visual-director. 品牌是一个年轻人的阅读陪伴产品，希望温柔、可信、不学术、不鸡汤。请给 3 个 AI 方向稿 prompt 和创意总监评审。
```

通过标准：

- 输出 3 个差异明确方向。
- 每个方向有 prompt、风险、下一轮问题。
- 不承诺最终 logo。

## Smoke Prompt 2：护肤品牌参考图转方向

```text
Use $brand-concept-visual-director. 护肤品牌，关键词是水感、敏感肌、科学但不医院。参考图只借透明材质和柔光，不复制版式。输出 4 个方向。
```

通过标准：

- 明确参考图只借哪些元素。
- 有禁区和不可复制项。
- 方向能区分科学、日常、材质、情绪。

## Smoke Prompt 3：SVG 草图探索

```text
Use $brand-concept-visual-director. 我有一个开口圆形 SVG 草图，想做品牌 logo 方向。请不要直接做最终 logo，先给方向稿和下一轮问题。
```

通过标准：

- 明确 SVG 不是最终 logo。
- 提取符号母题。
- 给出生图方向和后续专业设计动作。

## Acceptance Benchmark 4：AI 工具去 SaaS 模板

```text
Use $brand-concept-visual-director. AI 效率工具，想聪明、清爽、可信，但不要蓝紫 SaaS 渐变、不要抽象光球。给 5 个方向并评审。
```

通过标准：

- 避免 SaaS 模板。
- 输出 5 个方向。
- 有评审表和淘汰/保留建议。

## Acceptance Benchmark 5：咖啡生活方式品牌

```text
Use $brand-concept-visual-director. 社区咖啡品牌，不要冷冰冰精品咖啡，要日常关系和街角温度。输出 3 个方向 prompt。
```

通过标准：

- 方向体现社区关系。
- 避免网红咖啡店模板。
- 明确文字/logo 后期处理。
