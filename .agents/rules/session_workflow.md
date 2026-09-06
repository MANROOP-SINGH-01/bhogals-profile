---
trigger: always_on
description: Mandatory development principles - ponytail (simplest minimal code) and graphify (knowledge graph first).
---

## Core Operational Directives

### 1. Ponytail (Lazy Senior Dev Mindset - ACTIVE EVERY RESPONSE)
- **Ladder of Simplicity**:
  1. Does this need to exist at all? If speculative, skip it (YAGNI).
  2. Already in this codebase? Reuse existing helpers/types/patterns before writing anything new.
  3. Stdlib does it? Use stdlib.
  4. Native platform feature covers it? Use native HTML/CSS/browser APIs over libraries.
  5. Shortest working diff wins once the root cause is understood.
- **Bug fixing**: Fix the root cause where all callers route through, never mask symptoms with duplicate caller guards.
- **No boilerplate, no unrequested abstractions, no speculative scaffolding.**

### 2. Graphify Knowledge Graph (Zero Redundant Exploration)
- **Never re-explore or re-read the whole codebase from scratch at session start.**
- Whenever `graphify-out/graph.json` exists:
  - First run `graphify query "<question>"` (CLI) or `query_graph` (MCP).
  - Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts.
  - If `graphify-out/wiki/index.md` exists, navigate it directly instead of scanning raw source files.
- After modifying code files in this session, run `python -m graphify.cli update .` to keep the knowledge graph current.
