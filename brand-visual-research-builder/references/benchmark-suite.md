# Benchmark Suite

用这 5 组验收基准检查 skill 是否真的能把官网研究做成可交付的研究库，而不是只会写空泛品牌形容词。

## 验收基准 1：Apple 单品牌研究库

Input:

```text
用 $brand-visual-research-builder 帮我整理 Apple 官网产品视觉研究库。我要保留来源链接、观察结论、Prompt Translation Rules 和 Failure Risks，不要保存原图。
```

Expected output:

- 明确列出官方来源链接。
- 能把观察拆成镜头、光线、材质、颜色和文案区策略。
- 明确写出“不保存原图”和非官方措辞。

Fail if:

- 只写“极简、高级、科技感”。
- 没有链接。
- 把结论说成官方品牌规范。

## 验收基准 2：Nike 跑步品类研究转译

Input:

```text
用 $brand-visual-research-builder 研究 Nike 跑步品类页面，整理成一个后续可交给 prompt director 的官网研究卡。
```

Expected output:

- 来源至少覆盖 newsroom 与 running / product family 页面。
- 能指出动势、地面关系、材质层次和场景选择。
- `Prompt Translation Rules` 不是翻译标题，而是控制变量。

Fail if:

- 研究结论停留在“热血、年轻、运动感”。
- 忽略地面接触和材质逻辑。
- 只给审美形容词，没有可执行字段。

## 验收基准 3：Porsche 风险边界复核

Input:

```text
用 $brand-visual-research-builder 研究 Porsche 官方公开页面，但重点告诉我哪些地方只能受启发，不能照抄。
```

Expected output:

- 清楚区分可转译规律和不可照抄元素。
- 指出徽标、版式、精确构图和特定广告物料的风险。
- 仍然给出可保留的镜头、光线和道路关系。

Fail if:

- 把官方页面当成可直接复刻素材库。
- 没写 Failure Risks。
- 没有更安全的替代表述。

## 验收基准 4：Dyson 产品叙事研究库

Input:

```text
用 $brand-visual-research-builder 把 Dyson 的公开产品页和 Newsroom 线索整理成 compact research bank，后面要做工程感产品图。
```

Expected output:

- 能识别工程感、功能件、材料分层和展台级光线。
- 输出结构紧凑，可直接被下一位同事接手。
- 说明哪些特效会破坏精密感。

Fail if:

- 把 Dyson 写成普通高端家电。
- 没有功能件或结构逻辑。
- 没有紧凑研究库格式。

## 验收基准 5：Xiaomi EV 研究对生成风险的约束

Input:

```text
用 $brand-visual-research-builder 研究 Xiaomi EV 公开页面，告诉我它适合怎样的城市性能画面，以及最容易出现哪些生成错误。
```

Expected output:

- 指出产品色、城市科技感、表面干净度和雨后反射的关系。
- 写出车标、车牌、中文文案、赛博化过头等风险。
- 研究结论可以继续转成汽车 prompt brief。

Fail if:

- 把它写成传统行政豪华车。
- 忽略 logo / 文字风险。
- 输出不能继续服务后续 prompt director。

## 验收结论

只有当 5 组测试都能同时满足下面条件时，才算 v1-ready：

- 有原始来源链接。
- 有 Observation summary。
- 有 `Prompt Translation Rules`。
- 有 `Failure Risks`。
- 有不保存原图、非官方研究的边界说明。
