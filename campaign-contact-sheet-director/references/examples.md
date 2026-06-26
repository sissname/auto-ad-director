# Examples

以下示例用于快速判断输出格式是否足够像“整套 campaign 方案”。

## 示例 1：电动车 9 格发布套图

输入：

```text
用 campaign-contact-sheet-director 帮我把一组新能源轿跑发布会主视觉做成 9 格 contact sheet。品牌气质冷静、未来、克制，深蓝夜景，湿地反射，既要有速度，也要有两格可排版标题。
```

你应该输出：

- `9 格`
- advertising 场景
- 明确 style anchor：深蓝夜景、湿地反射、低机位、冷光轮廓、负空间标题区
- 镜头类型至少覆盖 hero、motion、detail、environment、social crop
- 每格都带平台 prompts

## 示例 2：护肤产品 6 格 launch board

输入：

```text
用 campaign-contact-sheet-director 给一款高端修护精华做 6 格 launch board。关键词是乳白扩散、玻璃半透明、水感、临床感但不冷。
```

你应该输出：

- `6 格`
- product 场景
- 包含 hero still life、macro、usage/lifestyle、closing packshot
- 明确“包装文案后期补字”

## 示例 3：时尚鞋履 12 格 campaign

输入：

```text
把这双跑鞋的 campaign 扩成 12 格，要有模特态度、跑动感、材质细节和竖版社媒图。参考氛围是城市夜跑，但不要像汽车广告。
```

你应该输出：

- `12 格`
- fashion 场景
- 至少包含 portrait、motion、detail、social crop
- 明确避免“汽车广告式过度金属反射”

## 示例 4：快闪空间 16 格提案页

输入：

```text
给一个商场中庭香氛快闪做 16 格效果图框架。需要入口、动线、装置细节、拍照点、产品陈列、夜间灯光版本和社媒传播图。
```

你应该输出：

- `16 格`
- spatial 场景
- 分为 4 个章节
- 包含入口 hero、动线、细部、拍照点、social crop
- 明确空间尺度与人物比例风险
