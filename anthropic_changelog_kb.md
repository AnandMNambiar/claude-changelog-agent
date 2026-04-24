# Anthropic Claude — Changelog & Product Knowledge Base

> This document serves as a structured knowledge base covering Anthropic's Claude model releases, API changes, feature launches, pricing updates, deprecations, and migrations from 2023 through April 2026.

---

## Table of Contents

1. [Model Release Timeline](#1-model-release-timeline)
2. [Model Specifications](#2-model-specifications)
3. [Feature Launches](#3-feature-launches)
4. [API Versioning & Changes](#4-api-versioning--changes)
5. [Pricing History](#5-pricing-history)
6. [Deprecations & Retirements](#6-deprecations--retirements)
7. [SDK & Platform Updates](#7-sdk--platform-updates)
8. [Migration Guides](#8-migration-guides)
9. [Breaking Changes Log](#9-breaking-changes-log)

---

## 1. Model Release Timeline

### Claude 1.x Era (2023)

| Date | Model | Key Details |
|------|-------|-------------|
| Mar 2023 | Claude 1.0 | Anthropic's first publicly available LLM. Text-only. |
| Mar 2023 | Claude Instant 1.0 | Faster, cheaper variant for simpler tasks. |
| Jul 2023 | Claude 1.1, 1.2, 1.3 | Iterative improvements to Claude 1 family. |
| Jul 2023 | Claude Instant 1.1, 1.2 | Faster inference and improved instruction following. |
| Nov 2023 | Claude 2.0 | Major upgrade: 100k context window, improved reasoning, coding, and math. |
| Nov 2023 | Claude 2.1 | 200k context window. Reduced hallucination rates. Tool use (beta). |

### Claude 3.x Era (2024)

| Date | Model | Key Details |
|------|-------|-------------|
| Feb 29, 2024 | Claude 3 Opus (`claude-3-opus-20240229`) | Most capable model at launch. 200k context. Vision support. |
| Feb 29, 2024 | Claude 3 Sonnet (`claude-3-sonnet-20240229`) | Balanced speed/intelligence. 200k context. Vision. |
| Mar 7, 2024 | Claude 3 Haiku (`claude-3-haiku-20240307`) | Fastest model. Near-instant responses. 200k context. Vision. |
| Jun 20, 2024 | Claude 3.5 Sonnet (`claude-3-5-sonnet-20240620`) | Major leap in coding and reasoning. Surpassed Opus 3 on many benchmarks. |
| Oct 22, 2024 | Claude 3.5 Sonnet v2 (`claude-3-5-sonnet-20241022`) | Updated snapshot. Computer use (beta). Improved tool use. |
| Oct 22, 2024 | Claude 3.5 Haiku (`claude-3-5-haiku-20241022`) | Faster, cheaper. Matched Claude 3 Sonnet performance at Haiku pricing. |

### Claude 3.7 (2025)

| Date | Model | Key Details |
|------|-------|-------------|
| Feb 19, 2025 | Claude 3.7 Sonnet (`claude-3-7-sonnet-20250219`) | Extended thinking (hybrid reasoning). First model with visible chain-of-thought. |

### Claude 4.x Era (2025–2026)

| Date | Model | Key Details |
|------|-------|-------------|
| May 14, 2025 | Claude Sonnet 4 (`claude-sonnet-4-20250514`) | Part of Claude 4 family launch. 200k context, 64k output. |
| May 14, 2025 | Claude Opus 4 (`claude-opus-4-20250514`) | Strongest reasoning at launch. 200k context, 32k output. Extended thinking. |
| Aug 5, 2025 | Claude Opus 4.1 (`claude-opus-4-1-20250805`) | Improved over Opus 4. 200k context, 32k output. $15/$75 MTok pricing. |
| Sep 29, 2025 | Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) | Fast, capable. 200k context, 64k output. $3/$15 MTok. |
| Oct 1, 2025 | Claude Haiku 4.5 (`claude-haiku-4-5-20251001`) | Fastest frontier model. 200k context, 64k output. $1/$5 MTok. |
| Nov 1, 2025 | Claude Opus 4.5 (`claude-opus-4-5-20251101`) | 200k context, 64k output. $5/$25 MTok. Extended thinking. |
| Feb 5, 2026 | Claude Opus 4.6 (`claude-opus-4-6`) | 1M context window. 128k output. Agentic coding, computer use, search, finance. |
| Feb 17, 2026 | Claude Sonnet 4.6 (`claude-sonnet-4-6`) | 1M context. 64k output. Frontier coding and agents. |
| Apr 16, 2026 | Claude Opus 4.7 (`claude-opus-4-7`) | Latest flagship. 1M context (new tokenizer). 128k output. Step-change in agentic coding. |

### Special Models

| Date | Model | Key Details |
|------|-------|-------------|
| 2026 | Claude Mythos Preview | Research preview for defensive cybersecurity. Invitation-only via Project Glasswing. |

---

## 2. Model Specifications

### Current Models (Active)

| Model | API ID | Context | Max Output | Input $/MTok | Output $/MTok | Knowledge Cutoff | Extended Thinking | Adaptive Thinking |
|-------|--------|---------|-----------|-------------|--------------|-----------------|-------------------|-------------------|
| Opus 4.7 | `claude-opus-4-7` | 1M | 128k | $5 | $25 | Jan 2026 | No | Yes |
| Sonnet 4.6 | `claude-sonnet-4-6` | 1M | 64k | $3 | $15 | Aug 2025 | Yes | Yes |
| Haiku 4.5 | `claude-haiku-4-5-20251001` | 200k | 64k | $1 | $5 | Feb 2025 | Yes | No |

### Legacy Models (Active but superseded)

| Model | API ID | Context | Max Output | Input $/MTok | Output $/MTok |
|-------|--------|---------|-----------|-------------|--------------|
| Opus 4.6 | `claude-opus-4-6` | 1M | 128k | $5 | $25 |
| Sonnet 4.5 | `claude-sonnet-4-5-20250929` | 200k | 64k | $3 | $15 |
| Opus 4.5 | `claude-opus-4-5-20251101` | 200k | 64k | $5 | $25 |
| Opus 4.1 | `claude-opus-4-1-20250805` | 200k | 32k | $15 | $75 |

### Deprecated Models

| Model | API ID | Deprecated | Retirement Date | Replacement |
|-------|--------|-----------|-----------------|-------------|
| Sonnet 4 | `claude-sonnet-4-20250514` | Apr 14, 2026 | Jun 15, 2026 | Sonnet 4.6 |
| Opus 4 | `claude-opus-4-20250514` | Apr 14, 2026 | Jun 15, 2026 | Opus 4.7 |

### Retired Models

| Model | API ID | Retired |
|-------|--------|---------|
| Sonnet 3.7 | `claude-3-7-sonnet-20250219` | Feb 19, 2026 |
| Haiku 3.5 | `claude-3-5-haiku-20241022` | Feb 19, 2026 |
| Haiku 3 | `claude-3-haiku-20240307` | Apr 20, 2026 |
| Sonnet 3.5 v1 | `claude-3-5-sonnet-20240620` | Oct 28, 2025 |
| Sonnet 3.5 v2 | `claude-3-5-sonnet-20241022` | Oct 28, 2025 |
| Opus 3 | `claude-3-opus-20240229` | Jan 5, 2026 |
| Claude 2.0 | `claude-2.0` | Jul 21, 2025 |
| Claude 2.1 | `claude-2.1` | Jul 21, 2025 |
| Sonnet 3 | `claude-3-sonnet-20240229` | Jul 21, 2025 |
| Claude 1.x | `claude-1.0` through `claude-1.3` | Nov 6, 2024 |
| Instant 1.x | `claude-instant-1.0` through `claude-instant-1.2` | Nov 6, 2024 |

---

## 3. Feature Launches

### 2023

| Date | Feature | Details |
|------|---------|---------|
| Jan 2023 | Initial API Release | API version `2023-01-01`. First public API access. |
| Jun 2023 | Streaming SSE Overhaul | API version `2023-06-01`. Incremental completions. Named events. Removed `data: [DONE]`. |
| Nov 2023 | 200k Context Window | Claude 2.1 introduced 200k token context. |
| Nov 2023 | Tool Use (Beta) | Claude 2.1 gained ability to use external tools via function calling. |

### 2024

| Date | Feature | Details |
|------|---------|---------|
| Feb 2024 | Vision / Image Input | Claude 3 family launched with multimodal vision support (images in messages). |
| Feb 2024 | Messages API | New structured Messages API replaced legacy Completions API. |
| Mar 2024 | System Prompts | First-class support for system prompts in Messages API. |
| Jun 2024 | Tool Use (GA) | Tool use moved from beta to general availability with Claude 3.5 Sonnet. |
| Aug 2024 | Prompt Caching | Launched for Claude 3.5 Sonnet and Claude 3 Haiku. Reduces cost by up to 90% for repeated prefixes. 5-minute TTL. |
| Oct 2024 | Computer Use (Beta) | Claude 3.5 Sonnet v2 gained ability to interact with computer desktops — clicking, typing, screenshots. |
| Oct 2024 | Batch API | Process large volumes of requests asynchronously with 50% discount on tokens. |
| Nov 2024 | Model Context Protocol (MCP) | Open protocol for connecting LLMs to external data sources and tools. Anthropic open-sourced the spec. |
| Nov 2024 | PDF Support | Direct PDF file input support added to the API. |

### 2025

| Date | Feature | Details |
|------|---------|---------|
| Feb 2025 | Extended Thinking | Claude 3.7 Sonnet introduced visible chain-of-thought reasoning. Model "thinks" before responding. |
| Feb 2025 | Citations | API support for grounding responses with citations from provided documents. |
| May 2025 | Claude 4 Family Launch | Opus 4 and Sonnet 4 launched simultaneously. Top-tier coding, reasoning, multilingual. |
| May 2025 | Text Editor Tool | `text_editor_20250429` — built-in tool for file editing in agentic workflows. 700 token overhead. |
| Mid 2025 | Web Search Tool | Server-side tool enabling Claude to search the web. $10 per 1,000 searches. |
| Mid 2025 | Web Fetch Tool | Server-side tool to fetch and read web pages. No additional cost beyond tokens. |
| Mid 2025 | Code Execution Tool | Sandboxed code execution. 1,550 free hours/month. $0.05/hr beyond that. Free with web search/fetch. |
| Jul 2025 | Token Counting API | Endpoint to count tokens before sending requests. Helps with cost estimation. |
| Sep 2025 | Prompt Caching — 1-Hour TTL | New `"ttl": "1h"` option for prompt caching. 2x base input price for write, same 0.1x for reads. |

### 2026

| Date | Feature | Details |
|------|---------|---------|
| Jan 2026 | Anthropic Labs | Experimental product initiative. New capabilities and products. |
| Jan 2026 | Healthcare & Life Sciences | HIPAA-ready infrastructure. Connectors for Medidata and ClinicalTrials.gov. |
| Feb 2026 | 1M Context Window | Claude Opus 4.6 and Sonnet 4.6 introduced 1M token context at standard pricing. No long-context premium. |
| Feb 2026 | 128k Output Tokens | Opus 4.6 and 4.7 support 128k max output tokens. |
| Feb 2026 | 300k Output (Batch API) | Opus 4.7, 4.6, and Sonnet 4.6 support 300k output tokens via Batch API with `output-300k-2026-03-24` beta header. |
| Feb 2026 | Fast Mode | Research preview for Opus 4.6. 6x standard pricing ($30/$150 MTok). Significantly faster output. |
| Feb 2026 | Apple Xcode + Claude Agent SDK | Apple's Xcode integrated Claude Agent SDK support. |
| Feb 2026 | Claude Code Security | Limited preview. Scans codebases for security vulnerabilities and suggests patches. |
| Feb 2026 | Workspace-Level Cache Isolation | Prompt caches isolated per workspace instead of organization-level. |
| Feb 2026 | Data Residency | `inference_geo` parameter for US-only inference. 1.1x pricing multiplier. |
| Feb 2026 | Adaptive Thinking | New feature on Opus 4.7 and Sonnet 4.6 — model adapts reasoning depth dynamically. |
| Mar 2026 | Priority Tier | Service tier for guaranteed capacity and prioritized access. Available on all current models. |
| Apr 2026 | Claude Opus 4.7 | New tokenizer. Step-change in agentic coding. 1M context. |
| Apr 2026 | Claude Design | Anthropic Labs product for visual collaboration — designs, prototypes, slides. |
| Apr 2026 | Claude Managed Agents | Stateful, long-running agent sessions. $0.08/session-hour + token costs. |
| Apr 2026 | Models API | Programmatic endpoint to query model capabilities, token limits, and availability. |

---

## 4. API Versioning & Changes

| API Version | Date | Changes |
|-------------|------|---------|
| `2023-01-01` | Jan 2023 | Initial API release. |
| `2023-06-01` | Jun 2023 | **Current version.** Streaming SSE overhaul: incremental completions, named events, removed `data: [DONE]`. Removed legacy `exception` and `truncated` response values. |

### API Stability Guarantees

For any given version, Anthropic preserves:
- Existing input parameters
- Existing output parameters

Anthropic may:
- Add additional optional inputs
- Add additional values to output
- Change conditions for specific error types
- Add new variants to enum-like output values (e.g., streaming event types)

---

## 5. Pricing History

### Current Pricing (as of April 2026)

| Model | Input $/MTok | Output $/MTok | Batch Input | Batch Output |
|-------|-------------|--------------|-------------|--------------|
| Opus 4.7 | $5 | $25 | $2.50 | $12.50 |
| Opus 4.6 | $5 | $25 | $2.50 | $12.50 |
| Opus 4.5 | $5 | $25 | $2.50 | $12.50 |
| Opus 4.1 | $15 | $75 | $7.50 | $37.50 |
| Opus 4 | $15 | $75 | $7.50 | $37.50 |
| Sonnet 4.6 | $3 | $15 | $1.50 | $7.50 |
| Sonnet 4.5 | $3 | $15 | $1.50 | $7.50 |
| Sonnet 4 | $3 | $15 | $1.50 | $7.50 |
| Haiku 4.5 | $1 | $5 | $0.50 | $2.50 |
| Haiku 3.5 | $0.80 | $4 | $0.40 | $2 |
| Haiku 3 | $0.25 | $1.25 | $0.125 | $0.625 |

### Prompt Caching Pricing

| Cache Operation | Multiplier | Duration |
|----------------|------------|----------|
| 5-minute cache write | 1.25x base input | 5 min TTL |
| 1-hour cache write | 2x base input | 1 hour TTL |
| Cache read (hit) | 0.1x base input | Same as write |

### Special Pricing

| Feature | Price |
|---------|-------|
| Fast Mode (Opus 4.6) | $30/$150 MTok (6x standard) |
| Web Search | $10 per 1,000 searches |
| Web Fetch | Free (token costs only) |
| Code Execution | 1,550 free hrs/mo, then $0.05/hr |
| Managed Agents | $0.08/session-hour + tokens |
| US Data Residency | 1.1x multiplier on all token pricing |

### Pricing Trends

- **Opus tier**: Dropped from $15/$75 (Opus 4, 4.1) → $5/$25 (Opus 4.5+). ~67% reduction.
- **Sonnet tier**: Stable at $3/$15 since Claude 3.5 Sonnet.
- **Haiku tier**: Rose from $0.25/$1.25 (Haiku 3) → $1/$5 (Haiku 4.5). Higher cost but dramatically higher capability.
- **Context window pricing**: 1M context at same per-token rate as smaller contexts (no long-context premium).

---

## 6. Deprecations & Retirements

### Deprecation Policy

- **Active**: Fully supported, recommended for use.
- **Legacy**: No more updates, may be deprecated in future.
- **Deprecated**: Still functional, not recommended. Replacement assigned. Retirement date set.
- **Retired**: No longer available. Requests fail.
- **Notice period**: Minimum 60 days before retirement for publicly released models.

### Deprecation Timeline

| Announcement Date | Model(s) | Retirement Date | Replacement |
|-------------------|----------|-----------------|-------------|
| Sep 4, 2024 | Claude 1.0–1.3, Instant 1.0–1.2 | Nov 6, 2024 | Haiku 4.5 |
| Jan 21, 2025 | Claude 2.0, 2.1, Sonnet 3 | Jul 21, 2025 | Opus 4.7 / Sonnet 4.6 |
| Jun 30, 2025 | Opus 3 | Jan 5, 2026 | Opus 4.7 |
| Aug 13, 2025 | Sonnet 3.5 v1 & v2 | Oct 28, 2025 | Sonnet 4.6 |
| Oct 28, 2025 | Sonnet 3.7 | Feb 19, 2026 | Sonnet 4.6 |
| Dec 19, 2025 | Haiku 3.5 | Feb 19, 2026 | Haiku 4.5 |
| Feb 19, 2026 | Haiku 3 | Apr 20, 2026 | Haiku 4.5 |
| Apr 14, 2026 | Sonnet 4, Opus 4 | Jun 15, 2026 | Sonnet 4.6, Opus 4.7 |

### Earliest Possible Retirement (Active Models)

| Model | Not Sooner Than |
|-------|----------------|
| Opus 4.7 | Apr 16, 2027 |
| Sonnet 4.6 | Feb 17, 2027 |
| Opus 4.6 | Feb 5, 2027 |
| Opus 4.5 | Nov 24, 2026 |
| Opus 4.1 | Aug 5, 2026 |
| Haiku 4.5 | Oct 15, 2026 |
| Sonnet 4.5 | Sep 29, 2026 |

---

## 7. SDK & Platform Updates

### Client SDKs

| SDK | Language | Notes |
|-----|----------|-------|
| `anthropic` | Python | Official Python SDK. Auto-sets `anthropic-version` header. |
| `@anthropic-ai/sdk` | TypeScript/Node.js | Official TypeScript SDK. |
| Claude Agent SDK | Multi-platform | For building agentic applications. Integrated with Apple Xcode (Feb 2026). |

### Platform Availability

| Platform | Availability | Notes |
|----------|-------------|-------|
| Claude API (1P) | All models | Direct access. Global by default. US residency option. |
| AWS Bedrock | All models | Global + regional endpoints (Sonnet 4.5+). 10% regional premium. |
| Google Vertex AI | All models | Global + multi-region + regional endpoints (Sonnet 4.5+). 10% regional premium. |
| Microsoft Foundry | Select models | Added in 2026. |

### Cloud Endpoint Changes (Sonnet 4.5+)

Starting with Claude Sonnet 4.5 and all subsequent models:
- **AWS Bedrock**: Two endpoint types — global (dynamic routing) and regional (guaranteed geographic routing).
- **Google Vertex AI**: Three endpoint types — global, multi-region, and regional.
- Regional/multi-region endpoints carry a 10% price premium over global.

---

## 8. Migration Guides

### Migrating to Claude Opus 4.7 (from Opus 4.6 or earlier)

**Key changes:**
1. **New tokenizer**: Opus 4.7 uses a new tokenizer that may use up to 35% more tokens for the same text. Adjust token budgets accordingly.
2. **Adaptive thinking**: Opus 4.7 supports adaptive thinking (dynamic reasoning depth) instead of extended thinking. Update any `thinking` configuration.
3. **Improved agentic coding**: Step-change improvement — existing agent prompts may need re-tuning to take advantage.
4. **Same pricing**: $5/$25 MTok — no cost increase over Opus 4.6.
5. **API ID change**: `claude-opus-4-6` → `claude-opus-4-7`.

### General Migration Best Practices

1. Test thoroughly before switching — model behavior differs across versions.
2. Update API model IDs in code and configuration.
3. Check for deprecated features or changed default behaviors.
4. Monitor token usage — newer models may tokenize differently.
5. Review prompts — newer models may respond differently to the same prompts.
6. Use the Models API to programmatically check model availability.

---

## 9. Breaking Changes Log

| Date | Change | Impact | Migration |
|------|--------|--------|-----------|
| Jun 2023 | Streaming SSE format changed | All streaming clients | Update event parsing. Completions now incremental, events are named. |
| Jun 2023 | Removed `exception` and `truncated` response fields | Clients checking these fields | Remove references to these fields. |
| Nov 2024 | Claude 1.x and Instant retired | All Claude 1.x users | Migrate to Haiku 4.5. |
| Jul 2025 | Claude 2.0, 2.1, Sonnet 3 retired | All Claude 2.x and Sonnet 3 users | Migrate to Opus 4.7 / Sonnet 4.6. |
| Oct 2025 | Sonnet 3.5 v1 & v2 retired | All Sonnet 3.5 users | Migrate to Sonnet 4.6. |
| Jan 2026 | Opus 3 retired | All Opus 3 users | Migrate to Opus 4.7. |
| Feb 2026 | Sonnet 3.7 and Haiku 3.5 retired | All users of these models | Migrate to Sonnet 4.6 and Haiku 4.5. |
| Feb 2026 | Prompt cache isolation moved to workspace level | Organizations sharing caches across workspaces | Caches no longer shared across workspaces. May see increased cache misses initially. |
| Apr 2026 | Haiku 3 retired | All Haiku 3 users | Migrate to Haiku 4.5. |
| Jun 2026 (upcoming) | Sonnet 4 and Opus 4 retirement | All Sonnet 4 / Opus 4 users | Migrate to Sonnet 4.6 / Opus 4.7 before Jun 15, 2026. |

---

## Appendix: Platform IDs Quick Reference

| Model | Claude API | AWS Bedrock | GCP Vertex AI |
|-------|-----------|-------------|---------------|
| Opus 4.7 | `claude-opus-4-7` | `anthropic.claude-opus-4-7` | `claude-opus-4-7` |
| Sonnet 4.6 | `claude-sonnet-4-6` | `anthropic.claude-sonnet-4-6` | `claude-sonnet-4-6` |
| Haiku 4.5 | `claude-haiku-4-5-20251001` | `anthropic.claude-haiku-4-5-20251001-v1:0` | `claude-haiku-4-5@20251001` |
| Opus 4.6 | `claude-opus-4-6` | `anthropic.claude-opus-4-6-v1` | `claude-opus-4-6` |
| Sonnet 4.5 | `claude-sonnet-4-5-20250929` | `anthropic.claude-sonnet-4-5-20250929-v1:0` | `claude-sonnet-4-5@20250929` |
| Opus 4.5 | `claude-opus-4-5-20251101` | `anthropic.claude-opus-4-5-20251101-v1:0` | `claude-opus-4-5@20251101` |
| Opus 4.1 | `claude-opus-4-1-20250805` | `anthropic.claude-opus-4-1-20250805-v1:0` | `claude-opus-4-1@20250805` |

---

*Knowledge base compiled: April 24, 2026*
*Sources: Anthropic official documentation (platform.claude.com/docs), Anthropic news (anthropic.com/news)*
