# System Architecture Document — Architecture.md

## 1. Technical Stack & Infrastructure

```
┌──────────────────────────────────────────────────────────────┐
│                    Client Browser                            │
│  - HTML5 Semantic Document (TailwindCSS HUD styles)          │
│  - React 19 Client Hydration via Turbopack Chunks            │
│  - Three.js WebGL Particle Canvas                            │
│  - Web Audio API Sound Dispatcher (12 Audio Sprites)        │
│  - Embedded Vis-Network Graphify Visualizer                  │
└──────────────────────────────▲───────────────────────────────┘
                               │ HTTP / Static Asset Pipeline
┌──────────────────────────────▼───────────────────────────────┐
│                    Serving Layer                             │
│  - Node.js High-Throughput Static Server (server.js)        │
│  - Local Port: 3000 | Bind: 0.0.0.0                          │
│  - Multi-MIME Handling: WOFF2, MP3, JS, CSS, JSON, HTML     │
│  - CORS Enabled for Local Mesh Interoperability              │
└──────────────────────────────▲───────────────────────────────┘
                               │ Code & Knowledge Foundations
┌──────────────────────────────┴───────────────────────────────┐
│              Persistent Knowledge & Repositories             │
│  - Graphify Knowledge Graph: graphify-out/ (GraphRAG JSON)   │
│  - Local Resume Projects: RESUME PORJECTS/ (18 Repos)        │
│  - Remote Target: GitHub MANROOP-SINGH-01                    │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Directory & Workspace Structure

```
c:\INFINTY\WORK\HOBBIES - HUSTLE\
├── PORFOLIO\                                 # Main Portfolio Deployment
│   ├── .agents\                             # Antigravity agent rules & workflows
│   │   ├── rules\graphify.md
│   │   └── workflows\graphify.md
│   ├── .git\                                # Git version control (branch: main)
│   ├── _next\static\                        # Next.js / Turbopack Client Bundles
│   │   ├── chunks\                          # 14 JavaScript functional chunks
│   │   │   ├── 00gnyiizlc0um.js             # Nav & Header Components
│   │   │   ├── 1z316l66unarb.js             # Core data, projects, contact state
│   │   │   ├── 2x99l_3kw903_.js             # Three.js 3D WebGL engine
│   │   │   └── ...                          # Tailwind runtime & animations
│   │   └── media\                           # Geist font binary assets (WOFF2)
│   ├── graphify-out\                        # Precomputed GraphRAG Architecture
│   │   ├── graph.html                       # Standalone interactive graph visualizer
│   │   ├── graph.json                       # 3,011 nodes, 8,812 edges network
│   │   └── GRAPH_REPORT.md                  # Comprehensive architectural audit
│   ├── sounds\                              # Mechanical keyboard audio clips
│   │   ├── press\                           # Keydown events (SPACE, ENTER, etc.)
│   │   └── release\                         # Keyup release audio
│   ├── favicon.ico                          # Monogram browser icon
│   ├── icon.png                             # HUD social thumbnail
│   ├── index.html                           # Single-page master application
│   ├── package.json                         # Node project config
│   ├── server.js                            # Local HTTP daemon
│   ├── PRD.md                               # Project requirements
│   ├── Architecture.md                      # System architecture
│   ├── Rules.md                             # AI boundaries and constraints
│   ├── Phases.md                            # Roadmap & milestone execution
│   ├── Design.md                            # Cybernetic HUD design system
│   └── Memory.md                            # Working state & token preservation
│
└── RESUME PORJECTS\                         # Extracted Project Codebases (18 repos)
    ├── OpenVoice\                           # Rust/Tauri push-to-talk dictation
    ├── Kavach-iqoo_hackathon\               # React 19 + WebLLM scam detection
    ├── Secure-Vote-AI\                      # Blockchain & AI voting platform
    ├── gemini-ai-agent\                     # Gemini AI agent implementation
    ├── color_detection\                     # OpenCV real-time HSV detection
    ├── face_detection\                      # OpenCV facial detection
    ├── pencil_sketch_converter\             # Tkinter + OpenCV sketcher
    ├── gold_price_prediction\               # Scikit-learn financial ML model
    ├── Deploying_Machine_Learning_Model\    # Streamlit prediction deploy
    ├── Diabetes_Prediction\                 # SVM classification notebook
    ├── Deep_Learning_Digit_Classification\  # MNIST deep neural network
    ├── Processing-Image-Data-for-Deep...\   # Image tensor processing
    ├── job-scheduler-using-cloudsim\        # Java CloudSim simulator
    ├── Adjacency-Matrix\                    # Java Graph data structure
    ├── Rock-Paper-Scissors-Game\            # Vanilla JS game
    └── AI-for-Bharat-Project\               # Requirements architecture
```

---

## 3. Data Flow & Component Interaction

1. **Bootstrapping Phase**:
   - Browser requests `/` → `server.js` serves `index.html`.
   - `index.html` mounts initial HUD loader (DOM-based percentage counter).
2. **Chunk Loading & Hydration**:
   - `_next/static/chunks/` loaded concurrently.
   - Web Audio context initializes on first user keydown/click.
   - Three.js WebGL canvas mounts into `#hero-canvas` container.
3. **Graphify Exploration Flow**:
   - Visitor navigates to `#graphify` section via nav bar or scroll.
   - Embedded sandboxed iframe streams `/graphify-out/graph.html`.
   - Graph displays clusters, god nodes, and inter-module dependencies without impacting main thread framerates.
4. **Agent Pair-Programming Flow**:
   - Antigravity AI reads `.agents/rules/graphify.md` and `Memory.md`.
   - Instead of reading 150KB bundles or cloning trees, agent queries `graphify query` to access only exact functions, conserving 90% token bandwidth.
