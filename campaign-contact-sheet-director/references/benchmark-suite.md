# Benchmark Suite

## 适合谁

- 需要验证 skill 是否真的能做出“像同一 campaign”的多格方案的人

## 解决什么问题

- 用固定测试题检查格数、场景、逐格逻辑和平台 prompt 是否齐全

## Smoke Prompt 1

- 任务：把运动鞋新品 brief 拆成 6 格产品 contact sheet
- 必须看到：6 格分工、style anchor、至少 1 格 detail、至少 1 格 social crop

## Smoke Prompt 2

- 任务：把雨夜汽车发布 brief 拆成 9 格广告 campaign
- 必须看到：9 格顺序、hero + motion + environment、Midjourney prompt

## Smoke Prompt 3

- 任务：把女装 lookbook 拆成 12 格时尚系列
- 必须看到：portrait、full look、movement、editorial crop

## Smoke Prompt 4

- 任务：把商场装置提案拆成 16 格空间板
- 必须看到：入口、节点、拍照点、夜景、标题位

## Smoke Prompt 5

- 任务：基于已有 hero 图，为护肤产品补出 6 格延展
- 必须看到：保留项、扩格原则、逐格新增逻辑

## 验收基准 1

- 任务：把城市夜雨汽车发布 brief 拆成 9 格广告 campaign
- 通过标准：hero、detail、motion、environment、social crop 都有清楚分工
- Fail if：9 格只是 9 个同风格 hero 句子

## 验收基准 2

- 任务：把高端耳机新品拆成 6 格产品发布板
- 通过标准：主体识别、材质证明、使用关系、裁切位都存在
- Fail if：没有 detail proof 或者没有标题位

## 验收基准 3

- 任务：把秋冬女装系列拆成 12 格时尚 lookbook
- 通过标准：full look、portrait、movement、texture、editorial crop 都出现
- Fail if：全部镜头都是半身站姿

## 验收基准 4

- 任务：把商场节庆装置提案拆成 16 格空间板
- 通过标准：入口、主装置、路径节点、夜景、拍照点、封面位俱全
- Fail if：只有漂亮局部，没有动线说明

## 验收基准 5

- 任务：在同一 brief 下同时输出 Midjourney 和即梦版本
- 通过标准：两套 prompt 保持同一 style anchor，但语言结构适配平台
- Fail if：只是翻译，没有平台差异

## 验收基准 6

- 任务：用户只要结构策划，不要平台 prompt
- 通过标准：仍然输出 style anchor、grid plan、逐格 role
- Fail if：因为没写 prompt 就省掉分格逻辑

## 验收基准 7

- 任务：基于单张 hero 图扩展 6 格产品系列
- 通过标准：明确保留项、扩格原则、新增格子职责
- Fail if：没有解释哪些内容沿用 hero 图

## 验收基准 8

- 任务：空间项目要求兼顾横版提案和竖版社媒
- 通过标准：至少有一格专门服务竖版传播，一格专门服务封面或标题
- Fail if：所有格子都默认横版

## 验收基准 9

- 任务：用户要求“统一但不要重复”
- 通过标准：明确固定锚点与变化变量
- Fail if：只说“保持统一风格”，没有具体约束

## 验收基准 10

- 任务：用户要求提案级输出
- 通过标准：有提案摘要、Frame Matrix、执行提醒、风险说明
- Fail if：只有逐格 prompt，没有提案结论

## 常见坑

- 只有 prompt，没有逐格 role
- 只有格数，没有统一性约束
- 只有主视觉，没有裁切位

## 原始来源

- 路线要求：`J:\005-Auto-Ad-Director-Skill-发布归档\00-总览索引\NEXT-SKILL-ROADMAP.md`
