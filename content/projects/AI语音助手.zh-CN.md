---
title: Sound AI Assistant - AI 语音助手
description: 一个基于浏览器原生 API 的智能语音对话助手，支持语音输入、AI 流式对话、边生成边朗读、知识自动提取，数据完全本地存储
date: 2026-06-18
lastmod: 2026-06-18
weight: 4
tags:
  - React
  - 语音识别
  - AI
  - 纯前端
categories:
  - AI开发
cover: https://d-sketon.top/img/backwebp/bg5.webp
photos:
  - https://d-sketon.top/img/backwebp/bg5.webp
---

> Sound AI Assistant — 一个基于浏览器原生 API 的智能语音对话助手，支持语音输入、AI 流式对话、边生成边朗读、知识自动提取，数据完全本地存储。

---

## 项目概述

这是一个**纯前端**的 AI 语音助手应用，核心能力是让用户通过**语音**与 AI 进行自然对话：

- **语音输入**：对着麦克风说话，自动转成文字发送给 AI
- **流式对话**：AI 回复边生成边显示（打字机效果）
- **边生成边朗读**：AI 回复生成过程中就按句子实时朗读，不用等全部生成完
- **知识自动提取**：从对话中自动识别日程、待办、笔记、联系人等信息
- **本地持久化**：所有对话和知识存储在浏览器 IndexedDB 中，无需后端

### 技术栈

| 分类 | 技术 | 说明 |
|------|------|------|
| 框架 | React 18 + TypeScript | 严格类型安全 |
| 构建 | Vite 5 | 极速 HMR，ESM 原生支持 |
| 样式 | Tailwind CSS 3 | 原子化 CSS，自定义主题色 |
| 状态管理 | Zustand 4 | 轻量、灵活、无 Provider |
| 本地数据库 | Dexie 4 (IndexedDB) | 结构化存储，支持索引查询 |
| AI 对话 | Fetch SSE 流式 | 兼容智谱 AI / OpenAI |
| 语音识别 | Web Speech API + 百度 WebSocket | 策略模式多 Provider |
| 语音合成 | Web Speech Synthesis API | 队列播放，流式朗读 |

### 核心亮点

1. **流式语音播放**：AI 回复边生成边朗读，体验流畅
2. **零后端依赖**：纯前端实现，数据全部存本地，部署成本为零
3. **多语音引擎策略模式**：支持浏览器原生和百度语音识别切换
4. **知识自动提取**：正则引擎从对话中自动识别 4 类结构化信息
5. **空对话优化**：新建对话不立即写库，首次发消息才持久化

---

## 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                     UI 组件层 (Components)                │
│   Sidebar │ MessageBubble │ KnowledgePanel │ Settings    │
├─────────────────────────────────────────────────────────┤
│                    状态管理层 (Stores)                    │
│     chatStore      │    voiceStore    │  knowledgeStore  │
├─────────────────────────────────────────────────────────┤
│                   服务层 (Services)                       │
│  AI Service │ Speech Service │ Storage Service │ Knowledge│
├─────────────────────────────────────────────────────────┤
│                   外部服务 / 浏览器 API                    │
│  智谱AI API │ Web Speech API │ IndexedDB │ localStorage  │
└─────────────────────────────────────────────────────────┘
```

**设计原则**：
- **组件层**只负责渲染和交互，不含业务逻辑
- **状态层**用 Zustand 集中管理运行时状态，桥接 UI 和 Service
- **服务层**封装所有 I/O 操作，全部单例模式
- **可替换性**：Service 接口统一，可切换不同 Provider

---

## 核心功能详解

### 流式语音播放（核心亮点）

这是本项目技术含量最高的功能：**AI 回复边生成边朗读**。

**核心思路**：边生成 → 边切句子 → 边入队播放

```
AI 流式输出每个字符
  ↓
speakIfSentence() 检测完整句子（正则匹配句号/问号/感叹号）
  ↓
切出完整句子
  ↓
speakQueued() 加入播放队列（stripMarkdown 过滤格式）
  ↓
Web Speech API 自动排队播放
```

| 技术点 | 实现方式 |
|--------|----------|
| 句子分割 | 正则 exec() 循环匹配，spokenIndex 记录播放位置 |
| 播放队列 | Web Speech API 原生队列 + pendingCount 计数器 |
| 代码块跳过 | inCodeBlock 状态机跟踪边界，流式跳过代码内容 |
| Markdown 过滤 | 朗读前剥离加粗、标题、列表、代码块等格式符号 |
| 不阻塞 UI | setTimeout 放到下一个事件循环 |

### 语音识别（ASR）

采用**策略模式 + 管理器**设计，支持多 Provider 切换：

- **Web Speech API**：浏览器原生，免配置，默认使用
- **百度语音**：WebSocket + PCM 音频流，国内更稳定
- 预留阿里云、讯飞等 Provider 接口，架构可扩展

### 知识自动提取

| 类型 | 触发模式 | 示例 |
|------|----------|------|
| 日程 (schedule) | 日期时间模式 | "明天下午3点开会" |
| 待办 (todo) | "提醒我"、"记得"、"待办：" | "提醒我明天买牛奶" |
| 笔记 (note) | "记住"、"记录"、"笔记：" | "记住这个API的用法" |
| 联系人 (contact) | 电话号码、邮箱模式 | "张三的电话是13800138000" |

### 数据持久化

| 数据类型 | 存储方式 | 说明 |
|----------|----------|------|
| 用户设置 | localStorage | 含版本迁移机制 |
| API Key | localStorage | 加密存储 |
| 对话/消息 | IndexedDB (Dexie) | 支持索引查询 |
| 知识库 | IndexedDB | 独立数据库 |

---

## 技术总结

| 维度 | 技术选型 | 设计考量 |
|------|----------|----------|
| 状态管理 | Zustand | 轻量、灵活、selector 精确订阅 |
| 本地存储 | Dexie (IndexedDB) | 大容量、结构化、异步、索引查询 |
| 流式输出 | Fetch + ReadableStream + SSE | 单向推送场景最优解 |
| 流式朗读 | 正则切句 + 原生队列 + 状态机 | 边生成边播放，不阻塞 UI |
| 语音识别 | 策略模式多 Provider | 可扩展、可替换 |
| 架构分层 | Components → Stores → Services | 关注点分离、可测试、可替换 |
| 类型安全 | TypeScript 严格模式 | 编译时错误检查、自文档化 |
