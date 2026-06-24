# 失败类型与修复手册

先识别失败类型，再决定改哪一层。不要在一个回合里同时改世界观、镜头、光线和材质。

## 修复梯度

1. 约束补丁：加负面约束或收紧已有描述。
2. 结构补丁：明确主体位置、数量、接触关系、解剖边界。
3. 镜头补丁：改机位、焦段、裁切、景深。
4. 光线补丁：改光源方向、反差、时间段、反射控制。
5. 世界补丁：改场景、地面、空间尺度、道具系统。
6. 概念重做：当主体逻辑、品牌气质和商业用途同时失败时，直接重建。

## 失败类型

### 1. 主体结构错误

症状：

- 手脚数量不对
- 主体轮廓塌陷
- 产品形体左右不一致

常见原因：

- 主体描述过短
- 同时塞入太多动作和道具
- 广角和复杂姿态叠加

修复动作：

```text
明确主体数量与姿态，强调 clean silhouette, correct anatomy / product geometry, clear separation from background。
```

### 2. 接地感与重力失败

症状：

- 漂浮
- 没有接触阴影
- 站姿不稳

修复动作：

```text
加入 grounded contact, visible contact shadow, firm placement on [ground material], stable weight distribution。
```

### 3. 反射与玻璃逻辑失败

症状：

- 镜面里出现第二个真实主体
- 玻璃没有厚度
- 水面反射方向乱

修复动作：

```text
只保留一个主要反射面，明确 real subject vs reflection，加入 accurate reflection logic, controlled highlight edges。
```

### 4. 光线脏或不统一

症状：

- 不同物体像在不同棚里拍的
- 亮部发灰，暗部没层次
- 面部与主体光向不一致

修复动作：

```text
明确单一主光方向、补光强度、反差等级，减少互相冲突的氛围词。
```

### 5. 材质廉价

症状：

- 金属像塑料
- 皮肤像蜡
- 包装没有真实边缘和厚度

修复动作：

```text
点名材质和它的光学表现：brushed metal highlight, glass thickness, matte paper grain, controlled skin texture。
```

### 6. 构图失焦

症状：

- 主体不明确
- 画面太满
- 留白和标题区冲突

修复动作：

```text
明确 hero subject, camera height, crop, negative space placement, foreground/background separation。
```

### 7. 品牌气质不对

症状：

- 高端品牌变成电商图
- 科技品牌像婚纱影楼
- 儿童品牌像惊悚片

修复动作：

```text
重建品牌语境：受众、价位、空间、色温、造型、道具密度、后期强度。
```

### 8. 文字 / logo 翻车

症状：

- 乱码标签
- 随机招牌
- 假 logo 抢画面

修复动作：

```text
改成 clean label area, blank typography space, no random text, no fake logo, no license plate characters。
```

### 9. 商业不可用

症状：

- 缩略图看不出卖点
- 海报裁切就断头断脚
- 没有标题区

修复动作：

```text
增加留白、减背景噪音、拉开主体尺度，并明确 4:5 / 16:9 / 1:1 裁切策略。
```

### 10. 风格堆词但没有画面逻辑

症状：

- 全是 cinematic、premium、luxury、epic
- 画面没有具体机位、光线、材质关系

修复动作：

```text
删掉空泛形容词，用具体的机位、光向、材质、地面、背景结构替换。
```

## 修复输出模板

```text
失败定位：
- 核心失败类型：
- 次级失败类型：
- 最可能原因：

修复策略：
- Keep：
- Change：
- Remove：

最小修复 Prompt：
[下一版 prompt]

Iteration note：
- Preserve：
- Test next：
- Watch：
```
