# Awesome Agent Stack

[English](README.md) · [浏览导航站](https://henryli777.github.io/awesome-agent-stack/) · [Contributing](CONTRIBUTING.md)

精选 AI Agent 开源工具：按用途查找框架、MCP、编码工具、观测、评测和安全项目。每项说明适用场景，并链接到核实版本的官方 README 和许可证。

![Directory preview](docs/preview.png)

**收录: 34 项 · 人工证据核验日期: 2026-10-09**

**GitHub 元数据刷新: 完整成功 · 2026-10-30T07:16:39Z** · 0 项保留上次成功快照。

网页支持中英文、跨语言搜索、类别和许可证筛选、排序及可分享的筛选链接。默认按名称排列。

## 如何选择

- [Agent 框架](#frameworks): 构建工作流、状态管理和多 Agent 协作。
- [MCP 与集成](#mcp): 连接 Agent 客户端与工具，检查协议交互。
- [编码与 Skills](#coding): 使用编码 Agent 和可复用的任务指令。
- [观测与诊断](#observability): 追踪工具调用，调试运行并检查执行元数据。
- [评测](#evaluation): 通过数据集、任务和质量标准比较效果。
- [安全与护栏](#security): 在授权环境中探查失败模式并约束行为。

## 收录与核实规则

- 收录有实际代码、明确开源许可和具体用途的项目；官方仓库、README、许可证是依据。
- 部分仓库包含企业功能或托管服务；收录范围和许可备注会明确指出。开源 SDK 不等同于开源服务。
- 星数、推送时间、归档和 Fork 状态按每日计划读取 GitHub 官方 API，独立记录元数据刷新时间；不自动重核 README、许可或用途。失败时保留上次成功快照。数据不能证明质量、当前维护状态或安全性，收录工具未逐一安装、运行或安全审计。
- 标注「维护者项目」的条目由本目录维护者开发，与其他条目接受相同收录规则。
- 初始排除归档项目、占位实现和仅采用非开源许可证的项目；后续归档会标记而不自动删除。欢迎提交带官方证据的 PR。

<a id="frameworks"></a>

## Agent 框架

### [CrewAI](https://github.com/crewAIInc/crewAI)

将按角色协作的智能体团队与事件驱动工作流控制结合起来的 Python 框架。

- **适合:** 通过 Crews 组织专职智能体，再用 Flows 控制任务流程。
- **许可范围:** [MIT](https://github.com/crewAIInc/crewAI/blob/ed71a6f4d631917d8384b4ad44f08bb09647eecd/LICENSE)
- **核实:** [README](https://github.com/crewAIInc/crewAI/blob/ed71a6f4d631917d8384b4ad44f08bb09647eecd/README.md) · 2026-10-09 · 标签: python, multi-agent, workflows, automation

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/crewAIInc/crewAI) · Stars: 60276 · 代码推送: 2026-10-30T05:28:37Z · 归档: false

### [Google ADK \(Python\)](https://github.com/google/adk-python)

用于组合智能体、工具集成和图工作流运行时的 Python 工具包。

- **适合:** 开发具有任务委派、工作流状态管理和工具确认机制的模块化智能体系统。
- **许可范围:** [Apache-2.0](https://github.com/google/adk-python/blob/128faabb6dddacf26e029aa8c28c903c3a7a6b61/LICENSE)
- **核实:** [README](https://github.com/google/adk-python/blob/128faabb6dddacf26e029aa8c28c903c3a7a6b61/README.md) · 2026-10-09 · 标签: python, multi-agent, workflows, tools

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/google/adk-python) · Stars: 22047 · 代码推送: 2026-10-30T06:28:40Z · 归档: false

### [LangGraph](https://github.com/langchain-ai/langgraph)

面向有状态智能体的图编排库，支持持久化执行和人工审核。

- **适合:** 设计跨步骤保留状态、支持分支和恢复的智能体工作流。
- **许可范围:** [MIT](https://github.com/langchain-ai/langgraph/blob/bfcfea554ed5c7f7be562cebf8825e911b493ab1/LICENSE)
- **核实:** [README](https://github.com/langchain-ai/langgraph/blob/bfcfea554ed5c7f7be562cebf8825e911b493ab1/README.md) · 2026-10-09 · 标签: python, workflows, state, human-in-the-loop

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/langchain-ai/langgraph) · Stars: 44140 · 代码推送: 2026-10-29T19:10:23Z · 归档: false

### [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

支持检查点、中间件和遥测的 Python 与 .NET 智能体及图工作流框架。

- **适合:** 在 Python 或 .NET 应用中编排多智能体协作，并加入人工审核和检查点。
- **许可范围:** [MIT](https://github.com/microsoft/agent-framework/blob/2d9cc3f8ae465baf1aed3022f89b6848db4ffa7b/LICENSE)
- **核实:** [README](https://github.com/microsoft/agent-framework/blob/2d9cc3f8ae465baf1aed3022f89b6848db4ffa7b/README.md) · 2026-10-09 · 标签: python, dotnet, multi-agent, workflows

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/microsoft/agent-framework) · Stars: 14384 · 代码推送: 2026-10-30T07:02:37Z · 归档: false

### [OpenAI Agents SDK \(Python\)](https://github.com/openai/openai-agents-python)

通过工具、交接、护栏、会话和追踪机制组合智能体的 Python SDK。

- **适合:** 构建需要任务委派和执行过程追踪的 Python 智能体工作流。
- **许可范围:** [MIT](https://github.com/openai/openai-agents-python/blob/125efa029b4bfd84238bd2c4fd69c3406f802663/LICENSE)
- **核实:** [README](https://github.com/openai/openai-agents-python/blob/125efa029b4bfd84238bd2c4fd69c3406f802663/README.md) · 2026-10-09 · 标签: python, multi-agent, tools, tracing

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/openai/openai-agents-python) · Stars: 30386 · 代码推送: 2026-10-27T19:44:03Z · 归档: false

### [Pydantic AI](https://github.com/pydantic/pydantic-ai)

提供输出校验、模型接入和可扩展工具的类型化 Python 智能体 SDK。

- **适合:** 构建返回结构化数据、便于接入现有类型化 Python 应用的智能体。
- **许可范围:** [MIT](https://github.com/pydantic/pydantic-ai/blob/36529f3a8ebc5a5675129fe6262223b9da0815ec/LICENSE)
- **核实:** [README](https://github.com/pydantic/pydantic-ai/blob/36529f3a8ebc5a5675129fe6262223b9da0815ec/README.md) · 2026-10-09 · 标签: python, typed-output, tools, validation

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/pydantic/pydantic-ai) · Stars: 20950 · 代码推送: 2026-10-30T04:48:13Z · 归档: false

<a id="mcp"></a>

## MCP 与集成

### [FastMCP](https://github.com/PrefectHQ/fastmcp)

面向 MCP 服务器、客户端和交互式工具应用的 Python 框架。

- **适合:** 把 Python 函数转成 MCP 工具，并通过高层 API 连接本地或远程服务器。
- **许可范围:** [Apache-2.0](https://github.com/PrefectHQ/fastmcp/blob/e2fcc412001ff7414095c5dc282f94c70299a612/LICENSE)
- **核实:** [README](https://github.com/PrefectHQ/fastmcp/blob/e2fcc412001ff7414095c5dc282f94c70299a612/README.md) · 2026-10-09 · 标签: python, mcp, tools, apps

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/PrefectHQ/fastmcp) · Stars: 28242 · 代码推送: 2026-10-30T06:48:16Z · 归档: false

### [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

可通过 Web、命令行和终端界面检查 MCP 服务器的开发工具。

- **适合:** 在开发集成时查看服务器能力，并调用 MCP 接口进行调试。
- **许可范围:** [Apache-2.0 / MIT](https://github.com/modelcontextprotocol/inspector/blob/0d2bc1d91ce177ea8d497ee3efe91bcc59e40a1c/LICENSE) — 代码正从 MIT 迁移至 Apache-2.0：新贡献及已获重授权同意的代码采用 Apache-2.0；未获重授权同意的历史贡献仍采用 MIT；非规范文档采用 CC-BY-4.0。
- **核实:** [README](https://github.com/modelcontextprotocol/inspector/blob/0d2bc1d91ce177ea8d497ee3efe91bcc59e40a1c/README.md) · 2026-10-09 · 标签: typescript, mcp, debugging, cli

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/inspector) · Stars: 11192 · 代码推送: 2026-10-29T06:32:33Z · 归档: false

### [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

用于在服务器与客户端之间交换工具、资源和提示的官方 MCP Python SDK。

- **适合:** 通过 MCP 暴露 Python 函数和数据，或让应用连接 MCP 服务器。
- **许可范围:** [MIT](https://github.com/modelcontextprotocol/python-sdk/blob/91941ed4d3985d59def99e090baa3f880c626cc8/LICENSE)
- **核实:** [README](https://github.com/modelcontextprotocol/python-sdk/blob/91941ed4d3985d59def99e090baa3f880c626cc8/README.md) · 2026-10-09 · 标签: python, mcp, server, client

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/python-sdk) · Stars: 24710 · 代码推送: 2026-10-27T11:15:12Z · 归档: false

### [MCP Registry](https://github.com/modelcontextprotocol/registry)

用于发现和登记 MCP 服务器元数据的 Go 注册服务与发布 CLI。

- **适合:** 发布 MCP 服务器元数据，或构建通过注册 API 发现服务器的客户端。
- **许可范围:** [Apache-2.0 / MIT](https://github.com/modelcontextprotocol/registry/blob/970df037919faa70456dde08c295473002d850e5/LICENSE) — 代码正从 MIT 迁移至 Apache-2.0：新贡献及已获重授权同意的代码采用 Apache-2.0；未获重授权同意的历史贡献仍采用 MIT；非规范文档采用 CC-BY-4.0。
- **核实:** [README](https://github.com/modelcontextprotocol/registry/blob/970df037919faa70456dde08c295473002d850e5/README.md) · 2026-10-09 · 标签: go, mcp, registry, discovery

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/registry) · Stars: 7423 · 代码推送: 2026-10-29T23:34:03Z · 归档: false

### [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

官方 TypeScript MCP SDK，提供服务器、客户端和 Web 框架传输适配包。

- **适合:** 构建 MCP 工具，或在 TypeScript 与 Node.js 服务中接入 MCP 客户端。
- **许可范围:** [Apache-2.0 / MIT](https://github.com/modelcontextprotocol/typescript-sdk/blob/b022522089a0c8b632595c6e7b536453945ed5a9/LICENSE) — 代码正从 MIT 迁移至 Apache-2.0：新贡献及已获重授权同意的代码采用 Apache-2.0；未获重授权同意的历史贡献仍采用 MIT；非规范文档采用 CC-BY-4.0。
- **核实:** [README](https://github.com/modelcontextprotocol/typescript-sdk/blob/b022522089a0c8b632595c6e7b536453945ed5a9/README.md) · 2026-10-09 · 标签: typescript, mcp, server, client

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/typescript-sdk) · Stars: 13685 · 代码推送: 2026-10-28T15:47:55Z · 归档: false

### [REA](https://github.com/morluto/rea)

连接智能体与本地二进制、JavaScript 和应用分析工具的 MCP 服务器及 CLI。

- **适合:** 利用本地工具返回的分析证据研究应用行为和原生代码。
- **许可范围:** [MIT](https://github.com/morluto/rea/blob/e6905c18e09c41e04525fb1a84575483df789204/LICENSE)
- **核实:** [README](https://github.com/morluto/rea/blob/e6905c18e09c41e04525fb1a84575483df789204/README.md) · 2026-10-09 · 标签: typescript, mcp, reverse-engineering, cli

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/morluto/rea) · Stars: 409185 · 代码推送: 2026-10-30T07:08:25Z · 归档: false

<a id="coding"></a>

## 编码与 Skills

### [Codex CLI](https://github.com/openai/codex)

OpenAI 开源的本地终端编程智能体。

- **适合:** 在本地终端中借助编程智能体处理仓库任务。
- **许可范围:** [Apache-2.0](https://github.com/openai/codex/blob/2351d9e1b608e6f9d9a3699b71d7eb39ee41cfa4/LICENSE)
- **核实:** [README](https://github.com/openai/codex/blob/2351d9e1b608e6f9d9a3699b71d7eb39ee41cfa4/README.md) · 2026-10-09 · 标签: rust, coding-agent, cli, local

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/openai/codex) · Stars: 131629 · 代码推送: 2026-10-30T07:12:14Z · 归档: false

### [Gemini CLI](https://github.com/google-gemini/gemini-cli)

提供文件操作、Shell 工具、搜索和 MCP 集成的 Gemini 终端智能体。

- **适合:** 在终端中探索和修改代码，或通过脚本运行非交互开发任务。
- **许可范围:** [Apache-2.0](https://github.com/google-gemini/gemini-cli/blob/2ce1a6963e9e53a04afaf76111e4527cfa7c5dd7/LICENSE)
- **核实:** [README](https://github.com/google-gemini/gemini-cli/blob/2ce1a6963e9e53a04afaf76111e4527cfa7c5dd7/README.md) · 2026-10-09 · 标签: typescript, coding-agent, cli, mcp

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/google-gemini/gemini-cli) · Stars: 108624 · 代码推送: 2026-10-30T01:22:16Z · 归档: false

### [OpenCode](https://github.com/anomalyco/opencode)

提供构建与规划模式，并支持子智能体的开源编程智能体。

- **适合:** 先用规划模式理解代码，再切换到可执行修改的智能体。
- **许可范围:** [MIT](https://github.com/anomalyco/opencode/blob/388406238bd5ca15564a762840a2362c3a45bd9c/LICENSE)
- **核实:** [README](https://github.com/anomalyco/opencode/blob/388406238bd5ca15564a762840a2362c3a45bd9c/README.md) · 2026-10-09 · 标签: typescript, coding-agent, cli, multi-agent

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/anomalyco/opencode) · Stars: 223141 · 代码推送: 2026-10-30T07:15:08Z · 归档: false

### [OpenHands Agent Canvas](https://github.com/OpenHands/OpenHands)

可自托管的编程智能体与自动化控制中心，支持本地、远程和云端后端。

- **适合:** 在同一工作区运行 OpenHands 或兼容 ACP 的智能体，并调度开发工作流。
- **许可范围:** [MIT](https://github.com/OpenHands/OpenHands/blob/553d4519113192a80fb18376fdb6c1e39fa06387/LICENSE)
- **核实:** [README](https://github.com/OpenHands/OpenHands/blob/553d4519113192a80fb18376fdb6c1e39fa06387/README.md) · 2026-10-09 · 标签: typescript, coding-agent, automation, self-hosted

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/OpenHands/OpenHands) · Stars: 92230 · 代码推送: 2026-10-30T04:08:59Z · 归档: false

### [Skills CLI](https://github.com/vercel-labs/skills)

可为多种编程智能体查找、安装、更新和使用技能的 CLI。

- **适合:** 在项目支持的多种智能体工具之间管理共享的 SKILL.md 技能包。
- **许可范围:** [MIT](https://github.com/vercel-labs/skills/blob/e878c4502674f84094dc27b5ad94ddaf64f22551/LICENSE)
- **核实:** [README](https://github.com/vercel-labs/skills/blob/e878c4502674f84094dc27b5ad94ddaf64f22551/README.md) · 2026-10-09 · 标签: typescript, skills, cli, tooling

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/vercel-labs/skills) · Stars: 37183 · 代码推送: 2026-10-29T00:49:36Z · 归档: false

<a id="observability"></a>

## 观测与诊断

### [AgentOps SDK](https://github.com/AgentOps-AI/agentops)

用于 Agent 追踪、会话事件和 LLM 成本统计的 MIT Python SDK；另行采用 ELv2 的 app/ 不在收录范围内。

- **适合:** 通过 SDK 和 AgentOps 后端采集 Agent 执行过程与模型费用。
- **许可范围:** [MIT](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/LICENSE) — 根目录 LICENSE 采用 MIT；SDK 的 CrewAI 插桩另有 Apache-2.0 声明。app/LICENSE 采用 ELv2，与根目录 README 中的应用 MIT 表述冲突；此条目不收录 app/ 和托管服务。
- **核实:** [README](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/README.md) · 2026-10-09 · 标签: tracing, sdk, cost-tracking

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/AgentOps-AI/agentops) · Stars: 5928 · 代码推送: 2026-06-25T08:25:03Z · 归档: false

### [Helicone](https://github.com/Helicone/helicone)

采用 Apache-2.0 的网关与可观测源码，支持 LLM 请求日志、Agent 追踪、成本和延迟分析。

- **适合:** 使用自托管的可观测服务查看模型请求与 Agent 会话。
- **许可范围:** [Apache-2.0](https://github.com/Helicone/helicone/blob/067d9290acb4f1fc9320e902fc67b4b399b50363/LICENSE) — 固定版本根目录 LICENSE 确认为 Apache-2.0；完整固定版本目录树未显示企业目录的额外授权文件。README 另行介绍托管套餐和商业 Helm 访问。
- **核实:** [README](https://github.com/Helicone/helicone/blob/067d9290acb4f1fc9320e902fc67b4b399b50363/README.md) · 2026-10-09 · 标签: gateway, tracing, self-hosted

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/Helicone/helicone) · Stars: 6246 · 代码推送: 2026-10-28T15:59:52Z · 归档: false

### [Langfuse](https://github.com/langfuse/langfuse)

可自托管的 MIT 核心，支持 LLM 调用追踪、提示词版本、数据集和评测；企业目录另行授权。

- **适合:** 在自有基础设施上调试 Agent 执行，比较提示词和评测结果。
- **许可范围:** [MIT](https://github.com/langfuse/langfuse/blob/ab8afebee5bfaec4dc60b7a9f214ce5d2d67c074/LICENSE) — GitHub API 返回 NOASSERTION，已依据固定版本 LICENSE 手动确认。MIT 适用于 ee/、web/src/ee/、worker/src/ee/ 之外的核心；企业目录另行授权。
- **核实:** [README](https://github.com/langfuse/langfuse/blob/ab8afebee5bfaec4dc60b7a9f214ce5d2d67c074/README.md) · 2026-10-09 · 标签: tracing, llmops, self-hosted

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/langfuse/langfuse) · Stars: 36734 · 代码推送: 2026-10-30T07:09:14Z · 归档: false

### [LangSmith SDKs](https://github.com/langchain-ai/langsmith-sdk)

用于接入 LangSmith 追踪和评测的 MIT Python 与 JavaScript SDK；此仓库仅收录客户端。

- **适合:** 为使用 LangSmith 服务的应用记录模型与工具调用。
- **许可范围:** [MIT](https://github.com/langchain-ai/langsmith-sdk/blob/19d9fe45dc0d156d7507d983cd23f80daa39693a/LICENSE) — 已依据所引提交中的实际授权文件确认 MIT；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/langchain-ai/langsmith-sdk/blob/19d9fe45dc0d156d7507d983cd23f80daa39693a/README.md) · 2026-10-09 · 标签: tracing, sdk, python, typescript

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/langchain-ai/langsmith-sdk) · Stars: 1083 · 代码推送: 2026-10-16T17:24:02Z · 归档: true

### [MCP Session Profiler](https://github.com/henryli777/mcp-session-profiler) · **维护者项目**

本地 stdio 代理，记录有界 MCP 调用元数据并生成离线诊断报告；当前为 Alpha 版本。

- **适合:** 检查实际 MCP 工具调用的延迟、错误和响应字节，不保存参数与结果正文。
- **许可范围:** [MIT](https://github.com/henryli777/mcp-session-profiler/blob/426cfd965161e4dd955f8e7c69de3a85302732eb/LICENSE)
- **核实:** [README](https://github.com/henryli777/mcp-session-profiler/blob/426cfd965161e4dd955f8e7c69de3a85302732eb/README.md) · 2026-10-09 · 标签: mcp, python, stdio, diagnostics

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/henryli777/mcp-session-profiler) · Stars: 0 · 代码推送: 2026-10-09T07:33:39Z · 归档: false

### [OpenInference](https://github.com/Arize-ai/openinference)

采用 Apache-2.0 的 OpenTelemetry 语义约定与插桩库，记录模型、检索和工具调用轨迹。

- **适合:** 将 AI 应用的调用跨度导出至兼容 OpenTelemetry 的后端。
- **许可范围:** [Apache-2.0](https://github.com/Arize-ai/openinference/blob/12f2cc035edfb00b60b656d977f07abfb7a69900/LICENSE) — 已依据所引提交中的实际授权文件确认 Apache-2.0；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/Arize-ai/openinference/blob/12f2cc035edfb00b60b656d977f07abfb7a69900/README.md) · 2026-10-09 · 标签: opentelemetry, instrumentation, tracing

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/Arize-ai/openinference) · Stars: 1295 · 代码推送: 2026-10-30T03:40:58Z · 归档: false

<a id="evaluation"></a>

## 评测

### [DeepEval](https://github.com/confident-ai/deepeval)

用于 LLM 应用测试的 Python 框架，提供任务、工具调用、检索和 LLM 裁判指标。

- **适合:** 为完整 Agent 轨迹与单个执行步骤编写自动化评测。
- **许可范围:** [Apache-2.0](https://github.com/confident-ai/deepeval/blob/0fb05d028b5ded9e4c466140ab3f3af90b801944/LICENSE.md) — 已依据所引提交中的实际授权文件确认 Apache-2.0；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/confident-ai/deepeval/blob/0fb05d028b5ded9e4c466140ab3f3af90b801944/README.md) · 2026-10-09 · 标签: evals, metrics, python

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/confident-ai/deepeval) · Stars: 19191 · 代码推送: 2026-10-29T10:36:04Z · 归档: false

### [Giskard](https://github.com/Giskard-AI/giskard-oss)

模块化 Python 测试库，支持 Agent 场景、LLM 裁判检查、RAG 质量评估和漏洞扫描。

- **适合:** 生成并执行多轮 Agent 测试场景，结合断言与裁判评分。
- **许可范围:** [Apache-2.0](https://github.com/Giskard-AI/giskard-oss/blob/48814003452c07c19339278e77a13fa07956d1b7/LICENSE) — 已依据所引提交中的实际授权文件确认 Apache-2.0；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/Giskard-AI/giskard-oss/blob/48814003452c07c19339278e77a13fa07956d1b7/README.md) · 2026-10-09 · 标签: evals, agents, red-teaming

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/Giskard-AI/giskard-oss) · Stars: 5934 · 代码推送: 2026-10-30T03:12:14Z · 归档: false

### [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)

MIT 评测框架，支持数据集、工具调用、多轮执行器、评分和评测日志。

- **适合:** 构建并运行可复现的模型与 Agent 评测任务。
- **许可范围:** [MIT](https://github.com/UKGovernmentBEIS/inspect_ai/blob/ba238b00c6da2b61da97577bf839370b1674e847/LICENSE) — 已依据所引提交中的实际授权文件确认 MIT；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/UKGovernmentBEIS/inspect_ai/blob/ba238b00c6da2b61da97577bf839370b1674e847/README.md) · 2026-10-09 · 标签: evals, python, tool-use

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/UKGovernmentBEIS/inspect_ai) · Stars: 3136 · 代码推送: 2026-10-29T21:57:02Z · 归档: false

### [Inspect Evals \(MIT modules\)](https://github.com/UKGovernmentBEIS/inspect_evals)

基于 Inspect AI 的基准实现，包含 MIT Agent 行为偏差测试；此条目不收录有用途限制的模块。

- **适合:** 通过 Inspect AI 复用 MIT 基准，包含多步 Agent 行为测试。
- **许可范围:** [MIT](https://github.com/UKGovernmentBEIS/inspect_evals/blob/eb5383efecd8ac6d23fd276757b811f3db05a1f5/LICENSE) — 根目录 LICENSE 与 agentic\_misalignment/LICENSE 采用 MIT。AgentHarm 的 LICENSE 增加非 OSI 的用途限制；NOTICE 对部分 CyberSecEval 组件列出 Llama 3.2 条款。此条目不将完整仓库或 AgentHarm 统一标为 MIT。
- **核实:** [README](https://github.com/UKGovernmentBEIS/inspect_evals/blob/eb5383efecd8ac6d23fd276757b811f3db05a1f5/README.md) · 2026-10-09 · 标签: benchmarks, evals, python

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/UKGovernmentBEIS/inspect_evals) · Stars: 725 · 代码推送: 2026-10-30T05:08:47Z · 归档: false

### [Promptfoo](https://github.com/promptfoo/promptfoo)

MIT CLI 与库，支持提示词和 Agent 评测、模型比较及可配置的红队测试。

- **适合:** 在 CI 中运行可复现的提示词回归与对抗测试用例。
- **许可范围:** [MIT](https://github.com/promptfoo/promptfoo/blob/e4347d3d0d50b706d9a079d0d96bd1cc5f1c0695/LICENSE) — 已根据固定版本根目录 LICENSE 与 Crescendo 提供程序的独立 MIT 声明确认 MIT。此条目收录社区 CLI 与库；Enterprise SaaS 和本地部署产品另行提供。
- **核实:** [README](https://github.com/promptfoo/promptfoo/blob/e4347d3d0d50b706d9a079d0d96bd1cc5f1c0695/README.md) · 2026-10-09 · 标签: evals, red-teaming, ci

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/promptfoo/promptfoo) · Stars: 26610 · 代码推送: 2026-10-30T00:34:58Z · 归档: false

### [Ragas](https://github.com/vibrantlabsai/ragas)

面向 LLM 与 RAG 应用的评测工具，提供模型指标、传统指标和测试数据生成。

- **适合:** 生成 RAG 测试集，评估回答质量与检索变更。
- **许可范围:** [Apache-2.0](https://github.com/vibrantlabsai/ragas/blob/298b68274234c060deacab3cf5fb52aa3a20e885/LICENSE) — 已依据所引提交中的实际授权文件确认 Apache-2.0；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/vibrantlabsai/ragas/blob/298b68274234c060deacab3cf5fb52aa3a20e885/README.md) · 2026-10-09 · 标签: rag, metrics, test-generation

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/vibrantlabsai/ragas) · Stars: 16186 · 代码推送: 2026-02-24T07:47:19Z · 归档: false

<a id="security"></a>

## 安全与护栏

### [Garak](https://github.com/NVIDIA/garak)

采用 Apache-2.0 的命令行漏洞扫描器，通过探针和检测器检查 LLM 与对话系统的失效模式。

- **适合:** 对模型端点运行提示词注入、信息泄露等对抗行为探测。
- **许可范围:** [Apache-2.0](https://github.com/NVIDIA/garak/blob/6cea0c92ac8c8dfae0165a3ec47ed4e228299354/LICENSE) — 扫描器源码已确认为 Apache-2.0；内置 HarmBench 数据另有 MIT 授权声明。
- **核实:** [README](https://github.com/NVIDIA/garak/blob/6cea0c92ac8c8dfae0165a3ec47ed4e228299354/README.md) · 2026-10-09 · 标签: red-teaming, scanner, python

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/NVIDIA/garak) · Stars: 9774 · 代码推送: 2026-10-27T18:16:24Z · 归档: false

### [Guardrails AI](https://github.com/guardrails-ai/guardrails)

采用 Apache-2.0 的 Python 框架，可组合输入输出验证器并生成结构化 LLM 输出。

- **适合:** 在应用代码中为模型输入和输出添加验证规则。
- **许可范围:** [Apache-2.0](https://github.com/guardrails-ai/guardrails/blob/06d0ff2c5f9bcb493d976b76f885e37e41ce845d/LICENSE) — 已依据所引提交中的实际授权文件确认 Apache-2.0；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/guardrails-ai/guardrails/blob/06d0ff2c5f9bcb493d976b76f885e37e41ce845d/README.md) · 2026-10-09 · 标签: guardrails, validation, python

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/guardrails-ai/guardrails) · Stars: 7571 · 代码推送: 2026-10-29T03:19:37Z · 归档: false

### [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant)

采用 Apache-2.0 的策略引擎，以类似 Python 的规则匹配 Agent 消息、工具调用和数据流。

- **适合:** 在本地检查 Agent 轨迹，或通过 LLM 与 MCP 网关执行策略。
- **许可范围:** [Apache-2.0](https://github.com/invariantlabs-ai/invariant/blob/2340fe2d9cd619f73d5b67fa05bf8a08c7cad515/LICENSE) — 已依据所引提交中的实际授权文件确认 Apache-2.0；内置第三方组件保留各自的授权声明。
- **核实:** [README](https://github.com/invariantlabs-ai/invariant/blob/2340fe2d9cd619f73d5b67fa05bf8a08c7cad515/README.md) · 2026-10-09 · 标签: guardrails, policy, mcp

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/invariantlabs-ai/invariant) · Stars: 475 · 代码推送: 2026-01-12T12:50:28Z · 归档: false

### [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

面向 LLM 对话的可编程防护库，支持对话流程与输入输出控制。

- **适合:** 定义对话策略，并在 LLM 调用周围接入防护配置。
- **许可范围:** [Apache-2.0](https://github.com/NVIDIA-NeMo/Guardrails/blob/7de04a5252ac470e2d562bd281814952672a9bde/LICENSE.md) — 固定版本 LICENSE.md 明确声明 Apache-2.0，已手动确认；GitHub API 返回 NOASSERTION。
- **核实:** [README](https://github.com/NVIDIA-NeMo/Guardrails/blob/7de04a5252ac470e2d562bd281814952672a9bde/README.md) · 2026-10-09 · 标签: guardrails, dialog, python

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/NVIDIA-NeMo/Guardrails) · Stars: 7398 · 代码推送: 2026-10-29T21:55:09Z · 归档: false

### [REA Pentest Playbook Skill](https://github.com/henryli777/rea--pentest-playbook-skill) · **维护者项目**

精简 skill 与 Python CLI，提供授权范围内的信息收集、扫描、验证和报告流程，并保存证据。

- **适合:** 对自有或明确授权目标执行有界观察，生成带证据和局限的报告。
- **许可范围:** [MIT](https://github.com/henryli777/rea--pentest-playbook-skill/blob/228ae444714bae7f3dce1ee8cbee0ce0cf334664/LICENSE)
- **核实:** [README](https://github.com/henryli777/rea--pentest-playbook-skill/blob/228ae444714bae7f3dce1ee8cbee0ce0cf334664/README.md) · 2026-10-09 · 标签: skill, python, pentest, evidence

- **元数据刷新:** 2026-10-30T07:16:39Z · [GitHub API](https://api.github.com/repos/henryli777/rea--pentest-playbook-skill) · Stars: 1 · 代码推送: 2026-10-29T08:39:01Z · 归档: false

## 本地预览与维护

Python 3.10+ · Node.js 22+ (tests only). No npm install required.

```sh
git clone https://github.com/henryli777/awesome-agent-stack.git
cd awesome-agent-stack
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v
node --test tests/*.test.mjs
python3 -m http.server 8000 --directory site
```

[Local preview](http://localhost:8000) · [Contribution guide](CONTRIBUTING.md) · [MIT license](LICENSE)

修改 `data/catalog.json` 后运行生成命令。核实日期由贡献者检查官方证据后填写；生成器不进行网络查询，也不会自动声称内容已重新核实。

<!-- Generated by scripts/catalog.py from data/catalog.json. Do not edit directly. -->
