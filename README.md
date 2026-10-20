# Awesome Agent Stack

[简体中文](README.zh-CN.md) · [Browse the directory](https://henryli777.github.io/awesome-agent-stack/) · [Contributing](CONTRIBUTING.md)

A curated collection of open-source tools to build, connect, code, observe, evaluate and secure AI agents. Each entry explains when to use it and links to a verified version of its official README and license.

![Directory preview](docs/preview.png)

**Catalog: 34 projects · Human evidence snapshot: 2026-10-09**

**GitHub metadata refresh: complete · 2026-10-20T06:07:55Z** · Last successful snapshots preserved for 0 projects.

The website supports bilingual copy, cross-language search, category/license filters, sorting and shareable filter URLs. Default order is alphabetical.

## Choose by your next task

- [Agent frameworks](#frameworks): Build workflows, state and multi-agent coordination.
- [MCP &amp; integrations](#mcp): Connect agent clients to tools and inspect protocol behavior.
- [Coding &amp; skills](#coding): Use coding agents and reusable task instructions.
- [Observability](#observability): Trace tool calls, debug runs and inspect execution metadata.
- [Evaluation](#evaluation): Compare behavior against datasets, tasks and quality criteria.
- [Security &amp; guardrails](#security): Probe failures and constrain actions in authorized environments.

## Curation and verification

- Include concrete implementations with an explicit open-source license and a useful role; official repositories, READMEs and licenses are the evidence.
- Some repositories also contain enterprise features or hosted services. Scope notes identify what is included; an open-source SDK does not imply an open-source service.
- Stars, push dates, archive and fork status are read from the official GitHub API on a daily schedule, with separate metadata refresh timestamps. This does not recheck README, license or use-case evidence. Failures preserve last successful snapshots. These values do not prove quality, maintenance or security; listed tools have not all been installed, executed or security-audited.
- Entries marked **Curator project** are developed by this directory's maintainer and follow the same inclusion rules.
- Initial curation excludes archived projects, placeholders and software offered only under non-open-source licenses. Later archive status is marked without automatically deleting entries. Evidence-backed PRs are welcome.

<a id="frameworks"></a>

## Agent frameworks

### [CrewAI](https://github.com/crewAIInc/crewAI)

A Python framework that combines role-based agent teams with event-driven workflow control.

- **Use it for:** Organize specialized agents into Crews and coordinate their work through Flows.
- **License scope:** [MIT](https://github.com/crewAIInc/crewAI/blob/ed71a6f4d631917d8384b4ad44f08bb09647eecd/LICENSE)
- **Evidence:** [README](https://github.com/crewAIInc/crewAI/blob/ed71a6f4d631917d8384b4ad44f08bb09647eecd/README.md) · 2026-10-09 · Tags: python, multi-agent, workflows, automation

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/crewAIInc/crewAI) · Stars: 59898 · Code push: 2026-10-20T05:33:18Z · Archived: false

### [Google ADK \(Python\)](https://github.com/google/adk-python)

A Python toolkit for composing agents, tool integrations, and graph-based workflow runtimes.

- **Use it for:** Develop modular agent systems with delegation, workflow state, and tool confirmation.
- **License scope:** [Apache-2.0](https://github.com/google/adk-python/blob/128faabb6dddacf26e029aa8c28c903c3a7a6b61/LICENSE)
- **Evidence:** [README](https://github.com/google/adk-python/blob/128faabb6dddacf26e029aa8c28c903c3a7a6b61/README.md) · 2026-10-09 · Tags: python, multi-agent, workflows, tools

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/google/adk-python) · Stars: 21916 · Code push: 2026-10-20T04:51:08Z · Archived: false

### [LangGraph](https://github.com/langchain-ai/langgraph)

A graph-based orchestration library for stateful agents with durable execution and human review.

- **Use it for:** Model branching, resumable agent workflows that must preserve state across steps.
- **License scope:** [MIT](https://github.com/langchain-ai/langgraph/blob/bfcfea554ed5c7f7be562cebf8825e911b493ab1/LICENSE)
- **Evidence:** [README](https://github.com/langchain-ai/langgraph/blob/bfcfea554ed5c7f7be562cebf8825e911b493ab1/README.md) · 2026-10-09 · Tags: python, workflows, state, human-in-the-loop

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/langchain-ai/langgraph) · Stars: 43549 · Code push: 2026-10-19T14:06:21Z · Archived: false

### [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

A Python and .NET framework for agents and graph workflows with checkpointing, middleware, and telemetry.

- **Use it for:** Compose multi-agent orchestration across Python or .NET applications with human review and checkpoints.
- **License scope:** [MIT](https://github.com/microsoft/agent-framework/blob/2d9cc3f8ae465baf1aed3022f89b6848db4ffa7b/LICENSE)
- **Evidence:** [README](https://github.com/microsoft/agent-framework/blob/2d9cc3f8ae465baf1aed3022f89b6848db4ffa7b/README.md) · 2026-10-09 · Tags: python, dotnet, multi-agent, workflows

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/microsoft/agent-framework) · Stars: 14221 · Code push: 2026-10-19T21:20:01Z · Archived: false

### [OpenAI Agents SDK \(Python\)](https://github.com/openai/openai-agents-python)

A Python SDK that composes tool-using agents with handoffs, guardrails, sessions, and tracing.

- **Use it for:** Build Python agent workflows that need delegated tasks and inspectable execution.
- **License scope:** [MIT](https://github.com/openai/openai-agents-python/blob/125efa029b4bfd84238bd2c4fd69c3406f802663/LICENSE)
- **Evidence:** [README](https://github.com/openai/openai-agents-python/blob/125efa029b4bfd84238bd2c4fd69c3406f802663/README.md) · 2026-10-09 · Tags: python, multi-agent, tools, tracing

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/openai/openai-agents-python) · Stars: 30157 · Code push: 2026-10-20T05:01:33Z · Archived: false

### [Pydantic AI](https://github.com/pydantic/pydantic-ai)

A typed Python agent SDK with validated outputs, model integrations, and extensible tools.

- **Use it for:** Build agents that return structured data and fit existing typed Python applications.
- **License scope:** [MIT](https://github.com/pydantic/pydantic-ai/blob/36529f3a8ebc5a5675129fe6262223b9da0815ec/LICENSE)
- **Evidence:** [README](https://github.com/pydantic/pydantic-ai/blob/36529f3a8ebc5a5675129fe6262223b9da0815ec/README.md) · 2026-10-09 · Tags: python, typed-output, tools, validation

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/pydantic/pydantic-ai) · Stars: 20744 · Code push: 2026-10-20T05:54:58Z · Archived: false

<a id="mcp"></a>

## MCP &amp; integrations

### [FastMCP](https://github.com/PrefectHQ/fastmcp)

A Python framework for MCP servers, clients, and interactive tool applications.

- **Use it for:** Turn Python functions into MCP tools and connect local or remote servers with higher-level APIs.
- **License scope:** [Apache-2.0](https://github.com/PrefectHQ/fastmcp/blob/e2fcc412001ff7414095c5dc282f94c70299a612/LICENSE)
- **Evidence:** [README](https://github.com/PrefectHQ/fastmcp/blob/e2fcc412001ff7414095c5dc282f94c70299a612/README.md) · 2026-10-09 · Tags: python, mcp, tools, apps

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/PrefectHQ/fastmcp) · Stars: 28140 · Code push: 2026-10-20T02:36:41Z · Archived: false

### [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

A developer utility for inspecting MCP servers through web, command-line, and terminal interfaces.

- **Use it for:** Inspect server capabilities and exercise MCP calls while developing integrations.
- **License scope:** [Apache-2.0 / MIT](https://github.com/modelcontextprotocol/inspector/blob/0d2bc1d91ce177ea8d497ee3efe91bcc59e40a1c/LICENSE) — Code is transitioning from MIT to Apache-2.0: new and relicensed contributions use Apache-2.0, while historical contributions without relicensing consent remain MIT; non-specification documentation uses CC-BY-4.0.
- **Evidence:** [README](https://github.com/modelcontextprotocol/inspector/blob/0d2bc1d91ce177ea8d497ee3efe91bcc59e40a1c/README.md) · 2026-10-09 · Tags: typescript, mcp, debugging, cli

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/inspector) · Stars: 11105 · Code push: 2026-10-20T06:02:48Z · Archived: false

### [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

The official Python SDK for MCP servers and clients that exchange tools, resources, and prompts.

- **Use it for:** Expose Python functions and data through MCP or connect an application to MCP servers.
- **License scope:** [MIT](https://github.com/modelcontextprotocol/python-sdk/blob/91941ed4d3985d59def99e090baa3f880c626cc8/LICENSE)
- **Evidence:** [README](https://github.com/modelcontextprotocol/python-sdk/blob/91941ed4d3985d59def99e090baa3f880c626cc8/README.md) · 2026-10-09 · Tags: python, mcp, server, client

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/python-sdk) · Stars: 24625 · Code push: 2026-10-17T13:54:39Z · Archived: false

### [MCP Registry](https://github.com/modelcontextprotocol/registry)

A Go registry service and publishing CLI for discovering and registering MCP server metadata.

- **Use it for:** Publish MCP server metadata or build a client that discovers servers through a registry API.
- **License scope:** [Apache-2.0 / MIT](https://github.com/modelcontextprotocol/registry/blob/970df037919faa70456dde08c295473002d850e5/LICENSE) — Code is transitioning from MIT to Apache-2.0: new and relicensed contributions use Apache-2.0, while historical contributions without relicensing consent remain MIT; non-specification documentation uses CC-BY-4.0.
- **Evidence:** [README](https://github.com/modelcontextprotocol/registry/blob/970df037919faa70456dde08c295473002d850e5/README.md) · 2026-10-09 · Tags: go, mcp, registry, discovery

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/registry) · Stars: 7382 · Code push: 2026-10-14T23:34:50Z · Archived: false

### [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

The official TypeScript MCP SDK provides server, client, and web-framework transport packages.

- **Use it for:** Build MCP tools or integrate MCP clients into TypeScript and Node.js services.
- **License scope:** [Apache-2.0 / MIT](https://github.com/modelcontextprotocol/typescript-sdk/blob/b022522089a0c8b632595c6e7b536453945ed5a9/LICENSE) — Code is transitioning from MIT to Apache-2.0: new and relicensed contributions use Apache-2.0, while historical contributions without relicensing consent remain MIT; non-specification documentation uses CC-BY-4.0.
- **Evidence:** [README](https://github.com/modelcontextprotocol/typescript-sdk/blob/b022522089a0c8b632595c6e7b536453945ed5a9/README.md) · 2026-10-09 · Tags: typescript, mcp, server, client

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/modelcontextprotocol/typescript-sdk) · Stars: 13618 · Code push: 2026-10-20T00:17:05Z · Archived: false

### [REA](https://github.com/morluto/rea)

An MCP server and CLI that connect agents to local binary, JavaScript, and application analysis tools.

- **Use it for:** Investigate application behavior and native code using analysis evidence from local tools.
- **License scope:** [MIT](https://github.com/morluto/rea/blob/e6905c18e09c41e04525fb1a84575483df789204/LICENSE)
- **Evidence:** [README](https://github.com/morluto/rea/blob/e6905c18e09c41e04525fb1a84575483df789204/README.md) · 2026-10-09 · Tags: typescript, mcp, reverse-engineering, cli

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/morluto/rea) · Stars: 339512 · Code push: 2026-10-20T05:53:13Z · Archived: false

<a id="coding"></a>

## Coding &amp; skills

### [Codex CLI](https://github.com/openai/codex)

OpenAI's open-source coding agent that runs locally from the terminal.

- **Use it for:** Work on repository tasks from a local terminal with a coding agent.
- **License scope:** [Apache-2.0](https://github.com/openai/codex/blob/2351d9e1b608e6f9d9a3699b71d7eb39ee41cfa4/LICENSE)
- **Evidence:** [README](https://github.com/openai/codex/blob/2351d9e1b608e6f9d9a3699b71d7eb39ee41cfa4/README.md) · 2026-10-09 · Tags: rust, coding-agent, cli, local

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/openai/codex) · Stars: 129983 · Code push: 2026-10-20T05:26:02Z · Archived: false

### [Gemini CLI](https://github.com/google-gemini/gemini-cli)

A terminal agent for Gemini with file operations, shell tools, search, and MCP integrations.

- **Use it for:** Explore and edit code from the terminal or run noninteractive development tasks in scripts.
- **License scope:** [Apache-2.0](https://github.com/google-gemini/gemini-cli/blob/2ce1a6963e9e53a04afaf76111e4527cfa7c5dd7/LICENSE)
- **Evidence:** [README](https://github.com/google-gemini/gemini-cli/blob/2ce1a6963e9e53a04afaf76111e4527cfa7c5dd7/README.md) · 2026-10-09 · Tags: typescript, coding-agent, cli, mcp

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/google-gemini/gemini-cli) · Stars: 107458 · Code push: 2026-10-20T01:33:51Z · Archived: false

### [OpenCode](https://github.com/anomalyco/opencode)

An open-source coding agent with separate build and planning modes plus subagent support.

- **Use it for:** Explore code in planning mode and switch to an agent that can implement changes.
- **License scope:** [MIT](https://github.com/anomalyco/opencode/blob/388406238bd5ca15564a762840a2362c3a45bd9c/LICENSE)
- **Evidence:** [README](https://github.com/anomalyco/opencode/blob/388406238bd5ca15564a762840a2362c3a45bd9c/README.md) · 2026-10-09 · Tags: typescript, coding-agent, cli, multi-agent

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/anomalyco/opencode) · Stars: 218070 · Code push: 2026-10-20T06:05:01Z · Archived: false

### [OpenHands Agent Canvas](https://github.com/OpenHands/OpenHands)

A self-hosted control center for coding agents and automations across local, remote, and cloud backends.

- **Use it for:** Run OpenHands or ACP-compatible agents and schedule development workflows from one workspace.
- **License scope:** [MIT](https://github.com/OpenHands/OpenHands/blob/553d4519113192a80fb18376fdb6c1e39fa06387/LICENSE)
- **Evidence:** [README](https://github.com/OpenHands/OpenHands/blob/553d4519113192a80fb18376fdb6c1e39fa06387/README.md) · 2026-10-09 · Tags: typescript, coding-agent, automation, self-hosted

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/OpenHands/OpenHands) · Stars: 91328 · Code push: 2026-10-20T06:05:38Z · Archived: false

### [Skills CLI](https://github.com/vercel-labs/skills)

A CLI for finding, installing, updating, and using agent skills across supported coding agents.

- **Use it for:** Manage shared SKILL.md packages across a project's supported agent tools.
- **License scope:** [MIT](https://github.com/vercel-labs/skills/blob/e878c4502674f84094dc27b5ad94ddaf64f22551/LICENSE)
- **Evidence:** [README](https://github.com/vercel-labs/skills/blob/e878c4502674f84094dc27b5ad94ddaf64f22551/README.md) · 2026-10-09 · Tags: typescript, skills, cli, tooling

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/vercel-labs/skills) · Stars: 35733 · Code push: 2026-10-19T20:34:22Z · Archived: false

<a id="observability"></a>

## Observability

### [AgentOps SDK](https://github.com/AgentOps-AI/agentops)

MIT Python SDK for agent traces, session events, and LLM cost tracking; the separately ELv2-licensed app/ is excluded.

- **Use it for:** Capture agent execution and provider spend through the SDK, with an AgentOps backend.
- **License scope:** [MIT](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/LICENSE) — The root LICENSE is MIT. The SDK's CrewAI instrumentation has an Apache-2.0 notice. app/LICENSE is ELv2, despite the root README's conflicting MIT app statement; this entry excludes app/ and the hosted service.
- **Evidence:** [README](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/README.md) · 2026-10-09 · Tags: tracing, sdk, cost-tracking

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/AgentOps-AI/agentops) · Stars: 5897 · Code push: 2026-06-25T08:25:03Z · Archived: false

### [Helicone](https://github.com/Helicone/helicone)

Apache-2.0 gateway and observability source for LLM request logging, agent traces, cost, and latency analysis.

- **Use it for:** Inspect model requests and agent sessions using a self-hosted observability stack.
- **License scope:** [Apache-2.0](https://github.com/Helicone/helicone/blob/067d9290acb4f1fc9320e902fc67b4b399b50363/LICENSE) — Apache-2.0 confirmed in the pinned root LICENSE. The complete pinned tree contains no additional license file for enterprise directories. Hosted plans and commercial Helm access are separate offerings described in the README.
- **Evidence:** [README](https://github.com/Helicone/helicone/blob/067d9290acb4f1fc9320e902fc67b4b399b50363/README.md) · 2026-10-09 · Tags: gateway, tracing, self-hosted

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/Helicone/helicone) · Stars: 6227 · Code push: 2026-10-20T06:02:39Z · Archived: false

### [Langfuse](https://github.com/langfuse/langfuse)

Self-hostable MIT core for LLM traces, prompt versioning, datasets, and evaluations; enterprise directories have a separate license.

- **Use it for:** Debug agent runs and compare prompts and evaluations on your own infrastructure.
- **License scope:** [MIT](https://github.com/langfuse/langfuse/blob/ab8afebee5bfaec4dc60b7a9f214ce5d2d67c074/LICENSE) — Manually confirmed from the pinned LICENSE because GitHub API reports NOASSERTION. MIT applies to the core outside ee/, web/src/ee/, and worker/src/ee/; enterprise directories use a separate license.
- **Evidence:** [README](https://github.com/langfuse/langfuse/blob/ab8afebee5bfaec4dc60b7a9f214ce5d2d67c074/README.md) · 2026-10-09 · Tags: tracing, llmops, self-hosted

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/langfuse/langfuse) · Stars: 36056 · Code push: 2026-10-20T05:59:32Z · Archived: false

### [LangSmith SDKs](https://github.com/langchain-ai/langsmith-sdk)

MIT Python and JavaScript clients for tracing and evaluating apps with LangSmith; the repository covers SDKs, not the service.

- **Use it for:** Instrument model and tool calls when your application uses the LangSmith service.
- **License scope:** [MIT](https://github.com/langchain-ai/langsmith-sdk/blob/19d9fe45dc0d156d7507d983cd23f80daa39693a/LICENSE) — MIT was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/langchain-ai/langsmith-sdk/blob/19d9fe45dc0d156d7507d983cd23f80daa39693a/README.md) · 2026-10-09 · Tags: tracing, sdk, python, typescript

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/langchain-ai/langsmith-sdk) · Stars: 1081 · Code push: 2026-10-16T17:24:02Z · Archived: true

### [MCP Session Profiler](https://github.com/henryli777/mcp-session-profiler) · **Curator project**

A local stdio proxy that records bounded MCP call metadata and generates offline diagnostic reports; alpha release.

- **Use it for:** Inspect actual MCP tool-call latency, errors and response bytes without storing argument/result bodies.
- **License scope:** [MIT](https://github.com/henryli777/mcp-session-profiler/blob/426cfd965161e4dd955f8e7c69de3a85302732eb/LICENSE)
- **Evidence:** [README](https://github.com/henryli777/mcp-session-profiler/blob/426cfd965161e4dd955f8e7c69de3a85302732eb/README.md) · 2026-10-09 · Tags: mcp, python, stdio, diagnostics

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/henryli777/mcp-session-profiler) · Stars: 0 · Code push: 2026-10-09T07:33:39Z · Archived: false

### [OpenInference](https://github.com/Arize-ai/openinference)

Apache-2.0 OpenTelemetry conventions and instrumentation libraries for model, retrieval, and tool-call traces.

- **Use it for:** Export AI application spans to an OpenTelemetry-compatible backend.
- **License scope:** [Apache-2.0](https://github.com/Arize-ai/openinference/blob/12f2cc035edfb00b60b656d977f07abfb7a69900/LICENSE) — Apache-2.0 was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/Arize-ai/openinference/blob/12f2cc035edfb00b60b656d977f07abfb7a69900/README.md) · 2026-10-09 · Tags: opentelemetry, instrumentation, tracing

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/Arize-ai/openinference) · Stars: 1272 · Code push: 2026-10-20T05:40:56Z · Archived: false

<a id="evaluation"></a>

## Evaluation

### [DeepEval](https://github.com/confident-ai/deepeval)

Python framework for LLM app tests with task, tool-use, retrieval, and LLM-judge metrics.

- **Use it for:** Write automated tests for complete agent trajectories and individual steps.
- **License scope:** [Apache-2.0](https://github.com/confident-ai/deepeval/blob/0fb05d028b5ded9e4c466140ab3f3af90b801944/LICENSE.md) — Apache-2.0 was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/confident-ai/deepeval/blob/0fb05d028b5ded9e4c466140ab3f3af90b801944/README.md) · 2026-10-09 · Tags: evals, metrics, python

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/confident-ai/deepeval) · Stars: 18975 · Code push: 2026-10-19T06:25:04Z · Archived: false

### [Giskard](https://github.com/Giskard-AI/giskard-oss)

Modular Python testing library for agent scenarios, LLM-judge checks, RAG quality, and vulnerability scans.

- **Use it for:** Generate and run multi-turn agent scenarios with assertions and judges.
- **License scope:** [Apache-2.0](https://github.com/Giskard-AI/giskard-oss/blob/48814003452c07c19339278e77a13fa07956d1b7/LICENSE) — Apache-2.0 was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/Giskard-AI/giskard-oss/blob/48814003452c07c19339278e77a13fa07956d1b7/README.md) · 2026-10-09 · Tags: evals, agents, red-teaming

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/Giskard-AI/giskard-oss) · Stars: 5911 · Code push: 2026-10-20T05:58:16Z · Archived: false

### [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)

MIT evaluation framework with datasets, tool use, multi-turn solvers, scoring, and evaluation logs.

- **Use it for:** Build and run reproducible model and agent evaluation tasks.
- **License scope:** [MIT](https://github.com/UKGovernmentBEIS/inspect_ai/blob/ba238b00c6da2b61da97577bf839370b1674e847/LICENSE) — MIT was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/UKGovernmentBEIS/inspect_ai/blob/ba238b00c6da2b61da97577bf839370b1674e847/README.md) · 2026-10-09 · Tags: evals, python, tool-use

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/UKGovernmentBEIS/inspect_ai) · Stars: 3046 · Code push: 2026-10-19T21:33:21Z · Archived: false

### [Inspect Evals \(MIT modules\)](https://github.com/UKGovernmentBEIS/inspect_evals)

Inspect AI benchmark implementations, including MIT agentic-misalignment tests; this entry excludes use-restricted modules.

- **Use it for:** Run existing MIT benchmarks, including multi-step agent behavior tests, with Inspect AI.
- **License scope:** [MIT](https://github.com/UKGovernmentBEIS/inspect_evals/blob/eb5383efecd8ac6d23fd276757b811f3db05a1f5/LICENSE) — The root LICENSE and agentic\_misalignment/LICENSE are MIT. AgentHarm's LICENSE adds a non-OSI purpose restriction; NOTICE lists Llama 3.2 terms for some CyberSecEval components. This entry does not label the full repository or AgentHarm uniformly MIT.
- **Evidence:** [README](https://github.com/UKGovernmentBEIS/inspect_evals/blob/eb5383efecd8ac6d23fd276757b811f3db05a1f5/README.md) · 2026-10-09 · Tags: benchmarks, evals, python

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/UKGovernmentBEIS/inspect_evals) · Stars: 706 · Code push: 2026-10-19T19:20:23Z · Archived: false

### [Promptfoo](https://github.com/promptfoo/promptfoo)

MIT CLI and library for prompt and agent evaluations, model comparisons, and configurable red-team tests.

- **Use it for:** Run repeatable prompt regressions and adversarial test cases in CI.
- **License scope:** [MIT](https://github.com/promptfoo/promptfoo/blob/e4347d3d0d50b706d9a079d0d96bd1cc5f1c0695/LICENSE) — MIT confirmed in the pinned root LICENSE and the Crescendo provider's separate MIT notice. This entry covers the community CLI/library; Enterprise SaaS and on-prem offerings are documented separately.
- **Evidence:** [README](https://github.com/promptfoo/promptfoo/blob/e4347d3d0d50b706d9a079d0d96bd1cc5f1c0695/README.md) · 2026-10-09 · Tags: evals, red-teaming, ci

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/promptfoo/promptfoo) · Stars: 26166 · Code push: 2026-10-20T03:54:47Z · Archived: false

### [Ragas](https://github.com/vibrantlabsai/ragas)

Evaluation toolkit with LLM-based and traditional metrics plus test-data generation for LLM and RAG applications.

- **Use it for:** Generate RAG test sets and score answers and retrieval changes.
- **License scope:** [Apache-2.0](https://github.com/vibrantlabsai/ragas/blob/298b68274234c060deacab3cf5fb52aa3a20e885/LICENSE) — Apache-2.0 was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/vibrantlabsai/ragas/blob/298b68274234c060deacab3cf5fb52aa3a20e885/README.md) · 2026-10-09 · Tags: rag, metrics, test-generation

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/vibrantlabsai/ragas) · Stars: 16082 · Code push: 2026-02-24T07:47:19Z · Archived: false

<a id="security"></a>

## Security &amp; guardrails

### [Garak](https://github.com/NVIDIA/garak)

Apache-2.0 command-line vulnerability scanner with probes and detectors for LLM and dialog-system failure modes.

- **Use it for:** Probe model endpoints for prompt injection, leakage, and other adversarial behaviors.
- **License scope:** [Apache-2.0](https://github.com/NVIDIA/garak/blob/6cea0c92ac8c8dfae0165a3ec47ed4e228299354/LICENSE) — Apache-2.0 confirmed for the scanner source. The bundled HarmBench data has a separate MIT notice.
- **Evidence:** [README](https://github.com/NVIDIA/garak/blob/6cea0c92ac8c8dfae0165a3ec47ed4e228299354/README.md) · 2026-10-09 · Tags: red-teaming, scanner, python

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/NVIDIA/garak) · Stars: 9623 · Code push: 2026-10-16T20:15:19Z · Archived: false

### [Guardrails AI](https://github.com/guardrails-ai/guardrails)

Apache-2.0 Python framework for composing input/output validators and generating structured LLM outputs.

- **Use it for:** Add validation rules to model inputs and outputs in application code.
- **License scope:** [Apache-2.0](https://github.com/guardrails-ai/guardrails/blob/06d0ff2c5f9bcb493d976b76f885e37e41ce845d/LICENSE) — Apache-2.0 was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/guardrails-ai/guardrails/blob/06d0ff2c5f9bcb493d976b76f885e37e41ce845d/README.md) · 2026-10-09 · Tags: guardrails, validation, python

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/guardrails-ai/guardrails) · Stars: 7540 · Code push: 2026-10-15T02:25:34Z · Archived: false

### [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant)

Apache-2.0 policy engine for matching agent messages, tool calls, and data flows with Python-inspired rules.

- **Use it for:** Check agent traces locally or enforce policies through an LLM or MCP gateway.
- **License scope:** [Apache-2.0](https://github.com/invariantlabs-ai/invariant/blob/2340fe2d9cd619f73d5b67fa05bf8a08c7cad515/LICENSE) — Apache-2.0 was confirmed in the actual license file at the cited commit. Bundled third-party components retain their own notices.
- **Evidence:** [README](https://github.com/invariantlabs-ai/invariant/blob/2340fe2d9cd619f73d5b67fa05bf8a08c7cad515/README.md) · 2026-10-09 · Tags: guardrails, policy, mcp

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/invariantlabs-ai/invariant) · Stars: 472 · Code push: 2026-01-12T12:50:28Z · Archived: false

### [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

Programmable guardrails library for LLM conversations, dialog flows, and input/output controls.

- **Use it for:** Define conversation policies and integrate guardrail configurations around LLM calls.
- **License scope:** [Apache-2.0](https://github.com/NVIDIA-NeMo/Guardrails/blob/7de04a5252ac470e2d562bd281814952672a9bde/LICENSE.md) — Manually confirmed from the pinned LICENSE.md, which explicitly states Apache-2.0; GitHub API reports NOASSERTION.
- **Evidence:** [README](https://github.com/NVIDIA-NeMo/Guardrails/blob/7de04a5252ac470e2d562bd281814952672a9bde/README.md) · 2026-10-09 · Tags: guardrails, dialog, python

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/NVIDIA-NeMo/Guardrails) · Stars: 7332 · Code push: 2026-10-20T03:22:45Z · Archived: false

### [REA Pentest Playbook Skill](https://github.com/henryli777/rea--pentest-playbook-skill) · **Curator project**

A thin skill and Python CLI for an authorized recon, scan, verify and report workflow with preserved evidence.

- **Use it for:** Run bounded observations on owned or explicitly authorized targets and produce an evidence-backed report.
- **License scope:** [MIT](https://github.com/henryli777/rea--pentest-playbook-skill/blob/228ae444714bae7f3dce1ee8cbee0ce0cf334664/LICENSE)
- **Evidence:** [README](https://github.com/henryli777/rea--pentest-playbook-skill/blob/228ae444714bae7f3dce1ee8cbee0ce0cf334664/README.md) · 2026-10-09 · Tags: skill, python, pentest, evidence

- **Metadata refreshed:** 2026-10-20T06:07:55Z · [GitHub API](https://api.github.com/repos/henryli777/rea--pentest-playbook-skill) · Stars: 1 · Code push: 2026-10-19T07:55:19Z · Archived: false

## Preview and maintain

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

Edit `data/catalog.json`, then regenerate. Contributors set verification dates after checking official evidence; the generator makes no network calls and never claims it re-verified the content.

<!-- Generated by scripts/catalog.py from data/catalog.json. Do not edit directly. -->
