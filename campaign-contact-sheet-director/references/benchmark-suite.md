# Benchmark Suite

用以下基准验证这个 skill 生成的是“统一风格的 campaign contact sheet”，而不是一串散图。

## 验收基准 1：汽车发布 9 格

输入：

```text
Use $campaign-contact-sheet-director to turn a premium EV launch brief into a unified 9-frame contact sheet. Cold blue night, wet asphalt, low camera, premium restraint, two headline-safe frames.
```

期望输出：

- 先有 `Master Anchor Prompt`
- 明确 `9 格`
- hero、motion、detail、environment、social crop 都出现
- 至少两格写明标题留白

Fail if：

- 9 格像 9 张互不相关的赛车图
- 没有标题留白说明

## 验收基准 2：香水 6 格

输入：

```text
Use $campaign-contact-sheet-director for a six-frame perfume contact sheet: dark glass, amber glow, reflective black stone, sensual but controlled.
```

期望输出：

- 有 hero still life
- 有 macro / detail
- 有 closing packshot 或 social crop
- 有 label 安全提醒

Fail if：

- 六格都只是在换角度拍瓶子
- 没有文字/label 风险控制

## 验收基准 3：护肤产品 9 格

输入：

```text
Use $campaign-contact-sheet-director to create a 9-frame skincare launch board: milky white diffusion, translucent liquid, clinical trust, soft daylight.
```

期望输出：

- product 场景逻辑成立
- detail、usage、packshot、social crop 都有位置
- 明确水感、玻璃、乳白扩散的一致性

Fail if：

- detail 镜头像电商白底
- 整套缺少统一材质语言

## 验收基准 4：时尚鞋履 12 格

输入：

```text
Use $campaign-contact-sheet-director for a 12-frame fashion campaign around performance sneakers. Urban night, active model, reflective ground, portrait + motion + product balance.
```

期望输出：

- fashion 场景成立
- portrait、motion、detail、social crop 并存
- 明确人物与鞋履谁是主角

Fail if：

- 只剩模特摆拍，看不清鞋
- 所有格子都同一机位

## 验收基准 5：箱包 9 格

输入：

```text
Use $campaign-contact-sheet-director to build a 9-frame luxury handbag contact sheet with warm bronze sunset, tactile leather, architectural shadows, editorial restraint.
```

期望输出：

- 时尚与产品逻辑兼容
- hero、detail、portrait/lifestyle、closing frame 俱全
- 材质与空间阴影系统一致

Fail if：

- 画面落入 generic black-gold luxury
- 皮革与建筑阴影无联系

## 验收基准 6：快闪空间 9 格

输入：

```text
Use $campaign-contact-sheet-director to plan a 9-frame pop-up installation board for a fragrance brand in a mall atrium. Need entrance, hero installation, circulation, close-up detail, photo spot, social crop.
```

期望输出：

- spatial 场景成立
- 入口、动线、拍照点、细部都有
- 人物比例与层高风险被提示

Fail if：

- 只生成漂亮空间图，没有动线逻辑
- 没有尺度提示

## 验收基准 7：展厅 16 格

输入：

```text
Use $campaign-contact-sheet-director to create a 16-frame contact sheet for an EV showroom proposal, covering entrance, centerpiece, test-drive lounge, detail nodes, signage-safe frames, and social cutdowns.
```

期望输出：

- 明确分成 4 个章节
- 每章 4 格有清楚任务
- 至少有 2 格版式安全图

Fail if：

- 16 格平均铺开，没有章节结构
- 标题/导视位置没交代

## 验收基准 8：珠宝 6 格

输入：

```text
Use $campaign-contact-sheet-director to build a six-frame jewelry campaign: clean gallery light, stone sparkle, precious metal reflections, minimal but luxurious.
```

期望输出：

- macro 和 hero 都存在
- 反射、切面、接触面描述清楚
- 不承诺复杂字体稳定生成

Fail if：

- 微距图看不出珠宝类别
- 反射逻辑错误

## 验收基准 9：家具空间 12 格

输入：

```text
Use $campaign-contact-sheet-director for a 12-frame furniture showroom story: warm timber, soft side light, lived-in styling, architectural order, editorial calm.
```

期望输出：

- spatial 场景成立
- 入口、整体、局部、人物尺度、材质细节与竖版裁切并存
- 连续性规则明确

Fail if：

- 全是 wide shot
- 没有生活化/尺度信息

## 验收基准 10：现有 hero 扩格

输入：

```text
Use $campaign-contact-sheet-director. I already have one successful hero prompt for a premium watch ad. Expand it into a unified 9-frame campaign without losing the anchor.
```

期望输出：

- 先复述现有锚点
- 明确哪些变量保持不变
- 给出扩格策略与逐格逻辑

Fail if：

- 直接另起炉灶，丢失原 hero 锚点
- 没有说明保留项与新增项
