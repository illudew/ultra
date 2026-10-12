# 物理认知引擎 — Code Wiki

> 项目代号：**ultra**（README 中标注）
> 文档生成日期：2026-10-12
> 仓库状态：单文件应用，无构建流程，无外部依赖

---

## 目录

- [1. 项目概述](#1-项目概述)
- [2. 技术栈与运行环境](#2-技术栈与运行环境)
- [3. 项目结构](#3-项目结构)
- [4. 整体架构](#4-整体架构)
- [5. 数据模型](#5-数据模型)
  - [5.1 静态数据](#51-静态数据)
  - [5.2 用户运行时数据](#52-用户运行时数据)
- [6. 模块职责详解](#6-模块职责详解)
  - [6.1 样式系统（CSS）](#61-样式系统css)
  - [6.2 视图与路由（Section 4）](#62-视图与路由section-4)
  - [6.3 数据持久化层（Section 2）](#63-数据持久化层section-2)
  - [6.4 通用工具层（Section 3）](#64-通用工具层section-3)
  - [6.5 总览仪表盘（Section 5 · 部分）](#65-总览仪表盘section-5--部分)
  - [6.6 知识地图（Section 5 · 部分）](#66-知识地图section-5--部分)
  - [6.7 物理学习器（Section 6）](#67-物理学习器section-6)
  - [6.8 做题训练（Section 7）](#68-做题训练section-7)
  - [6.9 物理应用（Section 8）](#69-物理应用section-8)
  - [6.10 科研工作台（Section 9）](#610-科研工作台section-9)
  - [6.11 认知记录（Section 10）](#611-认知记录section-10)
  - [6.12 导入/导出/重置（Section 11）](#612-导入导出重置section-11)
  - [6.13 初始化（Section 12）](#613-初始化section-12)
- [7. 关键函数索引](#7-关键函数索引)
- [8. 事件委托与交互流](#8-事件委托与交互流)
- [9. 状态管理](#9-状态管理)
- [10. 依赖关系图](#10-依赖关系图)
- [11. 项目运行方式](#11-项目运行方式)
- [12. 扩展指南](#12-扩展指南)
- [13. 设计哲学](#13-设计哲学)

---

## 1. 项目概述

**物理认知引擎（Physics Cognition Engine）** 是一个纯前端的物理学习辅助工具，帮助用户构建、检验和修正物理模型。项目聚焦于**主动学习方法论**——不只是记住结论，而是建立能够解释世界的模型。

### 核心功能一览

| 视图 ID | 功能 | 核心交互 |
|---------|------|----------|
| `home` | 总览仪表盘 | 统计指标、引导入口 |
| `cognition` | 学习本质 | 认知循环四环节 + 认知检查表 |
| `map` | 知识地图 | 5 层级 28 知识点的搜索/筛选/详情 |
| `learn` | 物理学习器 | 4 阶段主动学习（诊断→重构→解释→连接） |
| `practice` | 做题训练 | 因果链选择题，即时反馈 |
| `applications` | 物理应用 | 3 个可交互参数模拟器 |
| `research` | 科研工作台 | 研究记录 CRUD + 假设自检验证 |
| `settings` | 数据设置 | 导入 / 导出 / 重置 |

### 设计原则

- **零依赖**：纯原生 HTML/CSS/JS，不引入任何 CDN 或 npm 包
- **零构建**：无需打包、编译或热更新
- **本地优先**：所有用户数据存储在浏览器 `localStorage`，不上传服务器
- **响应式**：支持桌面 / 平板 / 手机三档布局

---

## 2. 技术栈与运行环境

| 维度 | 选择 |
|------|------|
| 语言 | HTML5 + CSS3 + 原生 JavaScript (ES2021+) |
| 框架 | 无（Vanilla JS） |
| 构建工具 | 无 |
| 包管理 | 无 |
| 存储 | `localStorage`（键名 `physics_cognition_engine_v2`） |
| 浏览器 API | `Blob` / `URL.createObjectURL` / `File.text()` / 事件委托 |
| 兼容浏览器 | Chrome / Edge / Firefox / Safari 最近版本 |
| 运行方式 | 直接用浏览器打开 `index.html` |

### 外部资源

**无**。所有代码、样式、图标（使用 Unicode 字符如 Φ ⌂ ◎ ◇ ↗ ∑ ⌁ ⌘ ⚙）全部内联在单个 HTML 文件中。

---

## 3. 项目结构

```
/workspace/
├── README.md              # 极简项目标识（仅 "# ultra"）
├── CODE_WIKI.md           # 本文件
└── index.html             # 全部应用代码（3485 行 / ~114 KB）
```

### index.html 内部结构（代码分区）

| 行范围 | 内容 | 说明 |
|--------|------|------|
| 1 – 1184 | HTML `<head>` + `<style>` | 完整设计系统 CSS（~1175 行） |
| 1186 – 1912 | HTML `<body>` | 8 个视图的 DOM 骨架 |
| 1912 – 3485 | `<script>` JavaScript | 应用逻辑，按 12 节注释分区 |

JavaScript 内部分区：

```
// ============================================================
// Section 1:  数据定义（LEVELS, CONCEPTS, PRACTICE_QUESTIONS, ...）  ~L1915
// Section 2:  本地数据管理（STORAGE_KEY, loadData, saveData）         ~L2120
// Section 3:  通用工具函数（$, $$, escapeHTML, notify, ...）          ~L2200
// Section 4:  页面导航（switchView, 事件委托）                         ~L2250
// Section 5:  总览仪表盘 + 知识地图                                    ~L2300
// Section 6:  物理学习器（4 阶段）                                     ~L2550
// Section 7:  因果链做题器                                             ~L2850
// Section 8:  物理应用（参数模拟器）                                   ~L3000
// Section 9:  科研工作台                                               ~L3200
// Section 10: 认知记录                                                 ~L3330
// Section 11: 导入/导出/重置                                           ~L3400
// Section 12: 页面初始化                                               ~L3460
```

---

## 4. 整体架构

```
┌───────────────────────────────────────────────────────────┐
│                      index.html                           │
│                                                           │
│  ┌─────────────┐  ┌─────────────────────┐                │
│  │    <style>   │  │       <body>        │                │
│  │  (CSS 系统)  │  │  侧栏 + Topbar + 8  │                │
│  │             │  │     个 View <section>│                │
│  └──────┬──────┘  └──────────┬──────────┘                │
│         │                    │                            │
│         ▼                    ▼                            │
│  ┌──────────────────────────────────────┐                │
│  │         <script> (应用逻辑)            │                │
│  │                                       │                │
│  │  ┌─────────────────┐  ┌────────────┐ │                │
│  │  │   静态数据层     │  │  DOM 操作层 │ │                │
│  │  │  LEVELS         │  │  $, $$,    │ │                │
│  │  │  CONCEPTS       │  │  innerHTML  │ │                │
│  │  │  APPLICATIONS   │  │  事件监听   │ │                │
│  │  │  PRACTICE_...   │  └─────┬──────┘ │                │
│  │  └────────┬────────┘        │        │                │
│  │           │                 │        │                │
│  │           ▼                 ▼        │                │
│  │  ┌──────────────────────────────┐    │                │
│  │  │      运行时状态 (闭包变量)     │    │                │
│  │  │  appData, selectedConceptId,  │    │                │
│  │  │  learningStage, practice...   │    │                │
│  │  └──────────────┬───────────────┘    │                │
│  │                 │                     │                │
│  │                 ▼                     │                │
│  │  ┌──────────────────────────────┐    │                │
│  │  │    localStorage 持久化         │    │                │
│  │  │  STORAGE_KEY = ..._engine_v2  │    │                │
│  │  └──────────────────────────────┘    │                │
│  └──────────────────────────────────────┘                │
└───────────────────────────────────────────────────────────┘
```

### 架构特征

- **MVC 变体**：视图 = HTML section，模型 = 静态数组 + `localStorage`，控制器 = 全局函数集合（非严格 MVC）
- **渲染模式**：Serverless SPA，每次视图切换都重新从状态渲染 DOM，不使用虚拟 DOM
- **状态管理**：顶层闭包中的 let 变量 + 模块化 Object（`APPLICATIONS`）
- **数据流**：用户操作 → 事件委托 → 修改状态 → `saveData()` → `localStorage` + 重新渲染

---

## 5. 数据模型

### 5.1 静态数据

#### `LEVELS` — 知识层级定义

```js
const LEVELS = [
  { id: 1, name: "层级一 · 观察与测量" },
  { id: 2, name: "层级二 · 基础物理规律" },
  { id: 3, name: "层级三 · 数学与理论方法" },
  { id: 4, name: "层级四 · 现代物理理论" },
  { id: 5, name: "层级五 · 应用、实验与前沿" }
];
```

- 共 5 个层级，用于导航知识点
- 字段：`id`（数值）、`name`（显示文本）

#### `LEVEL_DESCRIPTIONS` — 层级描述（辅助数组）

5 元素字符串数组，按索引对应 LEVELS 的 id。

#### `CONCEPTS` — 知识地图（28 个知识点）

每个知识点的 schema：

```ts
interface Concept {
  id:          string;    // 唯一标识，如 "newton", "quantum"
  name:        string;    // 中文名称
  level:       number;    // 所属层级 1-5
  group:       string;    // 学科分组，如 "经典力学"、"电磁学"、"数学基础"
  summary:     string;    // 一句话摘要
  model:       string;    // 核心物理模型 / 公式
  detail:      string;    // 详细物理含义
  conditions:  string;    // 适用条件与注意事项
  related:     string[];  // 关联知识点名称
}
```

**学科分组统计**：

| 分组 | 知识点数 |
|------|---------|
| 经典力学 | 5 |
| 热学 | 1 |
| 波动与光学 | 2 |
| 电磁学 | 2 |
| 数学基础 | 4 |
| 理论力学 | 1 |
| 量子理论 | 1 |
| 统计物理 | 1 |
| 相对论 | 1 |
| 凝聚态物理 | 1 |
| 应用与工程 | 3 |
| 材料科学 | 1 |
| 实验方法 | 1 |
| 能量守恒 / 动量 / 转动 / 万有引力（分散） | — |

#### `LEARNING_STAGES` — 学习阶段

4 元素字符串数组：`["01 · 诊断", "02 · 重构", "03 · 解释", "04 · 连接"]`

#### `PRACTICE_QUESTIONS` — 题库（5 题）

```ts
interface PracticeQuestion {
  topic:      string;      // 主题标签
  title:      string;      // 题目标题
  question:   string;      // 题目描述
  options:    string[];    // 4 个选项
  correct:    number;      // 正确选项索引（0-3）
  explanation:string;      // 解释反馈
}
```

#### `APPLICATIONS` — 物理应用模拟器（3 个）

```ts
interface Application {
  title:     string;
  subtitle:  string;
  question:  string;    // 引导性思考问题
  hint:      string;    // 模型提示（可折叠显示）
  render():  string;    // 返回该模拟器的 HTML 控件
}
```

当前包含：`pendulum`（单摆）、`ohm`（欧姆定律）、`photon`（光子能量）

---

### 5.2 用户运行时数据

存储在 `localStorage`，键名 `physics_cognition_engine_v2`（历史版本为 v2）。

#### `appData` — 主数据对象

```ts
interface AppData {
  learning:     Record<string, LearningRecord>;   // 以 concept.id 为 key
  cognition:    CognitionRecord;
  research:     ResearchRecord[];
  applications: Record<string, ApplicationRecord>; // 以 app.id 为 key
  practice:     { answered: number; correct: number };
}
```

#### 各子类型

**LearningRecord** — 单个知识点的学习进度：

```ts
interface LearningRecord {
  steps: Record<number, string>;  // stage index (0-3) → 用户填写文本
  updatedAt: string | null;       // ISO 时间戳
}
```

**CognitionRecord** — 认知检查表：

```ts
interface CognitionRecord {
  fields: {
    observation: string;
    model:       string;
    prediction:  string;
    evidence:    string;
  };
  updatedAt: string;
}
```

**ResearchRecord** — 研究记录：

```ts
interface ResearchRecord {
  id:          string;    // "research-" + 时间戳
  title:       string;
  observation: string;
  question:    string;
  hypothesis:  string;
  method:      string;
  reflection:  string;
  createdAt:   string;    // ISO 时间戳
}
```

**ApplicationRecord** — 应用练习记录：

```ts
interface ApplicationRecord {
  reflection: string;
  completed:  boolean;
  updatedAt:  string;
}
```

---

## 6. 模块职责详解

### 6.1 样式系统（CSS）

**位置**：`<style>` 标签，第 9–1183 行。

**设计系统**：

| 类别 | 变量名 | 取值 |
|------|--------|------|
| 背景 | `--bg` | `#f3f6fa` |
| 主色 | `--blue` | `#3978e8` |
| 辅助色 | `--green`, `--orange`, `--purple`, `--red` | 语义化命名 |
| 圆角 | `--radius` | `16px` |
| 阴影 | `--shadow` | `0 8px 28px rgba(...)` |

**布局核心类**：

| 类名 | 用途 |
|------|------|
| `.app` | 顶层 Grid：`238px 侧栏 + 主内容` |
| `.sidebar` | 深色侧栏，position: sticky |
| `.main` / `.topbar` / `.content` | 主区域三段式 |
| `.view` | 视图容器，默认 `display:none`，`.active` 时显示 |
| `.grid-2/3/4` | 响应式栅格 |
| `.layout-main` / `.layout-equal` | 1.5:1 主副布局 / 等分布局 |

**组件类**：`.panel`、`.btn`、`.stat-card`、`.concept-card`、`.choice`、`.range-row`、`.progress-track`

**响应式断点**：

| 断点 | 行为 |
|------|------|
| ≤ 1100px | 侧栏收窄、concept-grid 变 2 列 |
| ≤ 760px | 侧栏变顶部横滑条、主布局单列 |
| ≤ 380px | concept-grid 单列、隐藏 topbar-meta |
| `prefers-reduced-motion` | 禁用动画和滚动平滑 |

---

### 6.2 视图与路由（Section 4）

#### `VIEW_TITLES: Record<string, string>`

视图 ID → 顶部标题文本的映射。

#### `switchView(name: string)` — 视图切换核心

流程：
1. 通过 `$("#view-" + name)` 获取目标视图 DOM
2. 切换 `.active` 类，显示目标视图、隐藏其他
3. 同步更新侧栏导航按钮的 `.active` 态
4. 更新 topbar 标题
5. 滚动到顶部
6. **触发对应视图的懒渲染**：map / learn / practice / applications / research / cognition

#### 事件委托入口

```js
document.addEventListener("click", event => {
  const nav = event.target.closest("[data-view]");
  const go  = event.target.closest("[data-go]");
  if (nav) switchView(nav.dataset.view);
  if (go)  switchView(go.dataset.go);
});
```

**路由方式**：基于 `data-view` 和 `data-go` 属性的声明式路由，无 URL hash 或 History API。

---

### 6.3 数据持久化层（Section 2）

#### `STORAGE_KEY = "physics_cognition_engine_v2"`

localStorage 键名。带版本号，预留迁移空间。

#### `createDefaultData()` → AppData

返回全新的默认数据结构。所有子字段都有初始值，避免 null 检查。

#### `loadData()` → AppData

容错加载：
- JSON 解析失败 → 返回默认值
- 子字段类型不匹配（如 `research` 不是数组）→ 降级为默认值
- 不存在时 → 返回默认值

#### `saveData()`

将 `appData` 序列化为 JSON 存入 localStorage，然后调用 `updateDashboard()`。

#### 运行时状态变量

```js
let appData;              // 全部用户数据
let selectedConceptId;    // 当前选中的知识点 id（默认 "newton"）
let learningStage;        // 学习器当前阶段（0-3）
let currentPracticeIndex; // 当前做题器题目索引
let selectedPracticeChoice; // 用户选择的选项索引
let practiceAnswered;     // 当前题目是否已作答
let selectedApplication; // 当前应用 id（默认 "pendulum"）
```

---

### 6.4 通用工具层（Section 3）

| 函数/常量 | 签名 | 用途 |
|-----------|------|------|
| `$` | `(selector, parent?) => Element \| null` | 单元素查询 |
| `$$` | `(selector, parent?) => Element[]` | 多元素查询 |
| `escapeHTML` | `(value) => string` | 转义 HTML 特殊字符，防 XSS |
| `notify` | `(message) => void` | 显示底部 Toast 通知（2.6s 自动消失） |
| `getConcept` | `(id) => Concept` | 按 id 查找知识点，找不到时返回第一个 |
| `conceptLevelName` | `(level) => string` | 层级 id → 层级名称 |
| `todayString` | `() => string` | 格式化今日日期 |
| `downloadFile` | `(filename, content, type) => void` | 通过 Blob + `<a download>` 触发下载 |

---

### 6.5 总览仪表盘（Section 5 · 部分）

#### `updateDashboard()`

从 `appData` 计算四个统计卡片的值：

| 统计项 | 计算方式 |
|--------|----------|
| 已探索知识点 | `Object.keys(appData.learning).length` |
| 学习记录 | 所有 learning record 的 `steps` 键总数之和 |
| 科研记录 | `appData.research.length` |
| 已复提取应用 | `applications` 中 `completed === true` 的数量 |

---

### 6.6 知识地图（Section 5 · 部分）

#### `renderLevels()`

渲染五个层级卡片 + 填充学科下拉选项。

#### `renderConcepts()` — 搜索与筛选

过滤条件：
- 文本搜索：`name`、`summary`、`detail`、`group` 全字段模糊匹配（toLowerCase）
- 层级筛选：`level === "all"` 或精确匹配
- 学科筛选：`group === "all"` 或精确匹配

结果显示 3 列 concept-grid，底部显示 `X / 28 个知识点`。

#### `renderConceptDetail()`

在右侧面板渲染选中知识点的完整详情，包括：层级标签、名称、摘要、核心模型（`.equation` 蓝色块）、物理含义、适用条件、相关知识标签、"学习该知识点"按钮。

**交互**：
- 点击层级卡片 → 自动设置层级筛选
- 点击 concept-card → 更新 `selectedConceptId` 并重新渲染
- 点击详情中的 "学习该知识点" → 切换到 learn 视图

---

### 6.7 物理学习器（Section 6）

#### 四阶段设计

| Stage | 名称 | 目标 | 用户动作 |
|-------|------|------|----------|
| 0 | 诊断 | 暴露当前理解的缺口 | 写出自己的理解（不看答案） |
| 1 | 重构 | 掩蔽状态下重建模型 | 从基本定义独立推导 |
| 2 | 解释 | 费曼技巧 | 用通俗语言解释原理 |
| 3 | 连接 | 建立知识网络 | 写出关联与边界条件 |

#### `getLearningRecord()`

懒初始化：若 `appData.learning[id]` 不存在，创建 `{ steps: {}, updatedAt: null }`。

#### `renderLearning()`

根据 `learningStage` 动态生成学习面板 HTML，以及：
- Stepper 四步指示器（active / done 状态）
- Sidebar 参考模型面板（**仅 stage ≥ 2 时显示**，强制先写再看）

#### 事件处理

| 按钮 | 行为 |
|------|------|
| `data-learn-next="N"` | 保存当前阶段文本 → 进入下阶段 → saveData() |
| `data-learn-back` | 回到上一阶段（不清除已写内容） |
| `data-learn-finish` | 保存最后阶段 → 重置为 stage 0 → 提示间隔重复 |

**关键设计**：强制用户先写自己的理解（Stage 0、1 时参考模型面板为空状态），只有进入 Stage 2 才能看到参考模型。

---

### 6.8 做题训练（Section 7）

#### `renderPractice()`

渲染当前题目：主题标签、题目标题、四选一选项（A/B/C/D）、即时反馈、统计进度。

**反馈逻辑**：
- 选中后立即判对判错
- 正确选项高亮绿色，用户选错高亮红色
- 显示 explanation 面板（好/坏状态）
- 统计数字累加

#### 状态变量控制流程

```
practiceAnswered = false
    → 用户点击选项
        → practiceAnswered = true
        → 累加 answered/correct
        → saveData()
        → renderPractice() （重新渲染显示结果）
    → "下一题" → currentPracticeIndex++ → 重置状态 → renderPractice()
    → "重新分析" → 只重置选择状态，不影响累计统计
```

**设计**：题目通过取模循环 `PRACTICE_QUESTIONS.length`，支持无限练习。

---

### 6.9 物理应用（Section 8）

#### `APPLICATIONS` 对象模式

每个 app 是一个独立对象，包含 `title / subtitle / question / hint / render()` 接口。扩展新模拟器只需向对象中增加一个新 key。

#### `renderApplicationCalculation()`

硬编码分支判断 `selectedApplication`，直接读写 DOM 控件值并调用 `Math` API 计算。

| 应用 | 物理公式 | 实现精度 |
|------|----------|----------|
| pendulum | `T = 2π√(L/g)` | 原始 JS Math |
| ohm | `I = V/R` | 原始 JS Math |
| photon | `E = hc/λ ≈ 1239.841984/λ` | 使用高精度常数 |

#### 交互控件

- `<input type="range">` 实时触发 input 事件 → 重新计算 → 更新显示
- "查看模型提示" 可折叠 hint 文本
- "保存解释" 记录用户对变量关系的理解到 `appData.applications`

---

### 6.10 科研工作台（Section 9）

#### 表单字段

| 字段 id | 语义 |
|---------|------|
| `researchTitle` | 研究主题 |
| `researchObservation` | 观察到的现象 |
| `researchQuestion` | 研究问题（必填） |
| `researchHypothesis` | 假设与机制 |
| `researchMethod` | 验证方案 |
| `researchReflection` | 结果与反思 |

#### `getResearchForm()` → ResearchRecord

收集表单值并生成带时间戳和唯一 id 的记录对象。

#### 启发式自检（"检查假设"按钮）

基于已填字段动态生成 4-8 条提示性问题（纯前端逻辑，不调用任何 LLM），引导用户：
- 是否记录了可观察现象
- 研究问题是否明确
- 假设是否可被否定
- 是否存在替代机制
- 验证方案如何排除混杂变量

#### `renderResearchRecords()`

渲染已保存记录列表，支持删除（带确认对话框）。

---

### 6.11 认知记录（Section 10）

#### 认知循环四环节

| data-cognition | 显示文本 |
|----------------|----------|
| `observe` | 观察现象 |
| `model` | 提出内部模型 |
| `predict` | 进行预测 |
| `correct` | 比较并修正 |

#### `updateCognitionProgress()`

计算四项认知检查表的填写比例（已填 / 总数 = 4），更新进度条和文字提示。

#### `restoreCognition()`

从 `appData.cognition.fields` 恢复上次保存的填写内容到表单。

#### 持久化时机

- 点击"保存认知记录"按钮时写入 `appData.cognition`
- 下次进入 cognition 视图时自动恢复

---

### 6.12 导入/导出/重置（Section 11）

#### 导出（`#exportData`）

生成带格式头的 JSON 文件：

```json
{
  "format": "physics-cognition-engine",
  "version": 2,
  "exportedAt": "ISO timestamp",
  "data": { /* appData 完整内容 */ }
}
```

调用 `downloadFile()` 触发浏览器下载。

#### 导入（`#importFile`）

- 读取 `.text()` → JSON.parse
- 接受 `parsed.data` 或直接 `parsed`
- 类型校验 + 合并默认值
- 用户确认后替换 `appData`
- 刷新所有视图

#### 重置（`#clearData`）

- confirm 二次确认
- `localStorage.removeItem(STORAGE_KEY)`
- 重置为默认数据
- 清空所有表单和记录列表

---

### 6.13 初始化（Section 12）

#### `initializeApp()`

按顺序执行：

1. 设置 topbar 今日日期
2. `renderLevels()` — 渲染层级列表 + 学科选项
3. `renderConcepts()` — 渲染知识点网格
4. `renderLearning()` — 渲染学习器面板
5. `renderPractice()` — 渲染做题器
6. `renderApplications()` — 渲染应用模拟器
7. `renderResearchRecords()` — 渲染科研记录列表
8. `restoreCognition()` — 恢复认知检查表
9. `updateDashboard()` — 更新总览统计

初始化后，若 `appData.learning` 中已存在 `selectedConceptId` 的记录，会额外调用一次 `renderLearning()`（确保显示用户之前的学习数据）。

---

## 7. 关键函数索引

| 函数名 | 行号（约） | 功能 |
|--------|------------|------|
| `createDefaultData` | ~2125 | 返回全新默认 AppData 对象 |
| `loadData` | ~2130 | 从 localStorage 容错加载 |
| `saveData` | ~2170 | 持久化 + 刷新仪表板 |
| `$` / `$$` | ~2195 | DOM 查询别名 |
| `escapeHTML` | ~2200 | XSS 防护 |
| `notify` | ~2210 | Toast 提示 |
| `getConcept` | ~2225 | 按 id 查找知识点 |
| `switchView` | ~2260 | 切换视图（核心路由） |
| `updateDashboard` | ~2310 | 更新总览四统计卡片 |
| `renderLevels` | ~2325 | 渲染层级列表 |
| `renderConcepts` | ~2340 | 搜索/筛选/渲染知识点网格 |
| `renderConceptDetail` | ~2380 | 渲染知识点右侧详情 |
| `getLearningRecord` | ~2605 | 懒初始化学习记录 |
| `renderLearning` | ~2620 | 四阶段学习面板渲染 |
| `renderPractice` | ~2900 | 做题器完整渲染 |
| `renderApplications` | ~3120 | 应用选择器 + 控件渲染 |
| `renderApplicationCalculation` | ~3155 | 实时参数计算 |
| `getResearchForm` | ~3220 | 收集研究表单数据 |
| `renderResearchRecords` | ~3290 | 研究记录列表渲染 |
| `updateCognitionProgress` | ~3340 | 认知检查表完成度 |
| `restoreCognition` | ~3355 | 恢复认知表单 |
| `initializeApp` | ~3460 | 应用启动入口 |

---

## 8. 事件委托与交互流

项目大量使用事件委托模式，避免在循环渲染的元素上逐个绑定监听器。

### 全局委托（唯一 document 级别）

```js
document.addEventListener("click", event => {
  const nav = event.target.closest("[data-view]");
  const go  = event.target.closest("[data-go]");
  // ...
});
```

### 局部委托（视图级别）

| 父容器 | 委托属性 | 处理逻辑 |
|--------|----------|----------|
| `#conceptGrid` | `[data-concept]` | 切换选中知识点 |
| `#conceptDetail` | `[data-start-learning]` | 从详情跳到学习器 |
| `#learnStage` | `[data-learn-next]` / `[data-learn-back]` / `[data-learn-finish]` | 学习阶段流转 |
| `#practiceChoices` | `[data-practice-choice]` | 选项选择 + 判对 |
| `#applicationSelector` | `[data-app]` | 切换应用场景 |
| `#researchRecords` | `[data-delete-research]` | 删除研究记录 |
| `#cognitionNodes` | `[data-cognition]` | 认知环节说明 |

### 直接绑定（非委托）

搜索框 input、range 控件 input、表单按钮等直接绑定。

---

## 9. 状态管理

### 状态分层

```
┌──────────────────────────────────────┐
│        静态不可变数据 (const)          │
│  LEVELS / CONCEPTS / APPLICATIONS     │
│  PRACTICE_QUESTIONS / LEARNING_STAGES  │
└────────────────┬─────────────────────┘
                 │ 作为渲染数据源
                 ▼
┌──────────────────────────────────────┐
│      闭包运行时状态 (let)              │
│  selectedConceptId                    │
│  learningStage                        │
│  currentPracticeIndex                 │
│  selectedPracticeChoice              │
│  practiceAnswered                     │
│  selectedApplication                  │
└────────────────┬─────────────────────┘
                 │ 驱动 + 读写
                 ▼
┌──────────────────────────────────────┐
│      持久化状态 (appData)              │
│  learning / cognition / research      │
│  applications / practice.stats        │
└────────────────┬─────────────────────┘
                 │ saveData()
                 ▼
┌──────────────────────────────────────┐
│     localStorage (STORAGE_KEY)        │
└──────────────────────────────────────┘
```

### 状态更新模式

**统一入口**：所有修改 appData 的操作最终都调用 `saveData()`。

**状态修改 → 重渲染**：每个 handler 的典型流程为：
```
读取 → 修改 appData → saveData() → 调用对应 render 函数
```

**不使用框架特性**：无 reactivity、无 computed、无 action dispatch。

---

## 10. 依赖关系图

```
                    ┌──────────────┐
                    │  initializeApp │
                    └──────┬───────┘
                           │
     ┌─────────┬──────────┼──────────┬──────────┬──────────┐
     ▼         ▼          ▼          ▼          ▼          ▼
renderLevels renderConcept renderLearning renderPractice renderApp updateDashboard
     │         │          │          │          │          │
     │         │          │          │          │          │
     └─────┬───┴──┬───┬───┴──┬───┬───┴──┬───┬───┴──┬───┬───┴──┐
           │      │   │      │   │      │   │      │   │      │
           ▼      ▼   ▼      ▼   ▼      ▼   ▼      ▼   ▼      ▼
        getConcept saveData escapeHTML notify $ / $$ renderAppCalc
                 ↑                    ↑    ↑
                 │                    │    │
    ┌────────────┴────────────────────┴────┴─────────┐
    │          静态数据源 (LEVELS/CONCEPTS/...)        │
    │          用户状态变量 (selectedConceptId 等)     │
    │          appData (持久化数据)                    │
    │          localStorage                           │
    └────────────────────────────────────────────────┘
```

---

## 11. 项目运行方式

### 最简单的方式

```bash
# 方法 A：直接在文件管理器中双击 index.html
# 方法 B：命令行快速启动（Python）
cd /workspace
python3 -m http.server 8000
# 然后浏览器打开 http://localhost:8000
```

### 为什么用 http.server 而不是 file://？

- file:// 协议下部分浏览器会限制 localStorage 和 Blob URL
- http.server 是零依赖方案，Python 3 标准库自带

### 浏览器打开后

1. 确认状态栏显示 "本地运行"
2. 进入"知识地图"浏览或"学习本质"开始认知训练
3. 所有进度自动保存在浏览器 localStorage 中
4. 可在"数据设置"中导出/导入 JSON 备份

---

## 12. 扩展指南

### 新增知识点

在 `CONCEPTS` 数组中追加一个新对象，遵循 `Concept` 接口（见第 5.1 节）。**建议**：
- `id` 使用小写英文 + 连字符
- `level` 选择 1–5 中已有的层级，或同步修改 `LEVELS` 和 `LEVEL_DESCRIPTIONS`
- `related` 引用其他知识点的 **name 字符串**（不是 id）

### 新增做题

向 `PRACTICE_QUESTIONS` 数组追加 `PracticeQuestion` 对象。系统取模循环，自动覆盖。

### 新增物理应用模拟器

向 `APPLICATIONS` 对象添加新 key，值为：
```js
newApp: {
  title: "...",
  subtitle: "...",
  question: "...",
  hint: "...",
  render() { return `...HTML with input IDs...`; }
}
```

然后在 `renderApplicationCalculation()` 中增加对应的 `if (selectedApplication === "newApp")` 分支。

### 新增视图（页面）

1. HTML 中增加 `<section class="view" id="view-newview">`
2. JS 中 `VIEW_TITLES.newview = "..."`
3. 侧栏 nav-button 增加 `<button class="nav-button" data-view="newview">`
4. 实现 `renderNewView()` 并在 `switchView()` 中增加懒渲染钩子

### 版本升级

修改 `STORAGE_KEY` 中的版本号（如 `_v3`），并在 `loadData()` 中实现旧版本迁移逻辑。

---

## 13. 设计哲学

本项目贯彻以下设计理念，与普通在线教育产品形成对照：

| 常规做法 | 本项目做法 |
|----------|-----------|
| 进度条表示"学了多少" | 进度条表示"你记录了多少思考" |
| 强制先修顺序 | 知识地图完全开放，点击即达 |
| 正确答案 = 模型正确 | 模型有适用边界，条件变化结论可错 |
| 记忆后做题 | 先判断因果，再看选项 |
| 统一 AI 反馈 | 启发式问题引导自我检验 |
| 排名 / 积分 | 无分数、无排名、无社交压力 |
| 数据上云 | 完全本地，导出 JSON 即可迁移 |

核心主张：**学习不是获取信息，而是改变对事物的内部表征**。

---

*文档结束* — 如需深入特定模块，请直接查看 [index.html](file:///workspace/index.html) 中对应 Section 的源码。
