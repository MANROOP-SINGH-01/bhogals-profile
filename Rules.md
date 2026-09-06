# AI Engineering Rules & Operational Boundaries — Rules.md

## 1. Core Engineering Philosophy
> **"The best code is the code never written."** — Channel the senior developer who avoids speculative abstractions, reinvention of standard libraries, and dependency bloat.

---

## 2. Strict Technical Boundaries

### 2.1. Library & Dependency Rules
- **DO NOT** install heavyweight front-end frameworks (Tailwind CLI, Next.js compilers, Webpack) unless explicitly demanded. The existing bundle is already optimized and served via lightweight Vanilla Node.js `server.js`.
- **DO NOT** introduce external analytics, telemetry tracking, or cloud surveillance scripts.
- **DO** use native Node.js core modules (`http`, `fs`, `path`) for serving infrastructure.
- **DO** use Graphify (`graphifyy`) for codebase intelligence and GraphRAG operations.

### 2.2. Branding & Identity Integrity
- **Target Persona**: **Manroop Singh Bhogal**
- **Monogram**: `MSB.`
- **Email**: `imbhogal17@gmail.com`
- **GitHub Root**: `https://github.com/MANROOP-SINGH-01`
- **LinkedIn**: `https://www.linkedin.com/in/manroop-singh-b58125354/`
- **X / Twitter**: `https://x.com/realManroop`
- **NEVER** re-introduce the original creator's name ("Aditya Shelke", "adityashelke04") into any file.
- **NEVER** link out to broken or external third-party repositories when Manroop's own fork/mirror exists.

### 2.3. Token & Context Conservation Rules
- **DO NOT** re-read or dump massive bundled files (`index.html`, `1z316l66unarb.js`, `2x99l_3kw903_.js`) in full into conversation context.
- **DO** consult `Memory.md` for fast state restoration across chat checkpoints.
- **DO** execute targeted Python inspection scripts or `graphify query` commands to extract specific AST chunks or regex matches.
- **DO NOT** loop or poll asynchronously; utilize `schedule` or reactive event wakeups.

### 2.4. File & Artifact Preservation
- **Preserve** all functional audio files (`sounds/`), fonts (`_next/static/media/`), and favicon binaries.
- **Preserve** `RESUME PORJECTS/` contents intact. When modifying projects, make clean targeted edits or git commits.
- **Never execute destructive cleanups** (`rmdir /s`, `Remove-Item -Recurse *`) on root directories.

### 2.5. Git & Deployment Standards
- All changes to the portfolio must be committed to git branch `main`.
- Commit messages must be concise, structured, and descriptive.
- Remote pushes must always target `MANROOP-SINGH-01/bhogals-profile` or the respective project repository on GitHub.
