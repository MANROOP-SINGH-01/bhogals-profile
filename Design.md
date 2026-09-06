# Visual & Cybernetic Design System — Design.md

## 1. Aesthetic Direction: Tactical Cyber-HUD
The portfolio visual design adheres to a **Dark Tactical Cybernetic HUD (Heads-Up Display)** theme inspired by military avionics, cyberpunk terminal interfaces, and high-performance developer tools.

---

## 2. Color Palette & Token Hierarchy

| Token Name | Hex Code | HSL / RGB | Usage Context |
|:---|:---|:---|:---|
| **Background (Deep Space)** | `#0a0a0f` | `hsl(240, 20%, 5%)` | Global page background, high-contrast canvas |
| **Surface / Card Background**| `#0d0d16` | `rgba(13, 13, 22, 0.85)` | Glassmorphic cards, HUD windows, terminal |
| **Accent Primary (Cyan/Mint)**| `#4ecdc4` | `hsl(175, 58%, 55%)` | Active highlights, glowing accents, badges, buttons |
| **Accent Secondary (Gold)**   | `#f39c12` | `hsl(37, 90%, 51%)` | Achievement trophies, highlight indicators |
| **Status Crimson (Alert)**   | `#ff4757` | `hsl(355, 100%, 64%)`| Gaming / Off Duty section, counter indicators |
| **Text Primary (Foreground)** | `#f8f9fa` | `hsl(210, 20%, 98%)` | Headers, primary titles, active navigation |
| **Text Muted (Telemetry)**    | `#8b949e` | `hsl(215, 14%, 58%)` | Metadata, tags, terminal prompts, breadcrumbs |
| **Border Strong (HUD Grid)**  | `#2a2a4e` | `rgba(42, 42, 78, 0.6)` | Wireframe outlines, corner HUD notches |

---

## 3. Typography & Font Hierarchy

- **Primary Heading Font**: **Geist Sans** (Clean, geometric neo-grotesque with balanced tabular figures).
  - Loaded locally via WOFF2 binaries: `_next/static/media/797e433ab948586e-s.p.0r6juujl39pe6.woff2`.
- **Telemetry & Terminal Font**: **Geist Mono** (High-precision monospace font for telemetry counters, timestamps, command prompts, and badge tags).
  - Loaded locally via WOFF2 binaries: `_next/static/media/caa3a2e1cccd8315-s.p.0wgildi0cnwt9.woff2`.

---

## 4. Cybernetic Micro-Interactions & Audio FX

### 4.1. Visual Micro-Animations
- **TextScramble**: Character-by-character decryption shuffle on page load and section reveals.
- **Glassmorphic Glow**: `backdrop-blur-xl` combined with subtle inset top-borders `rgba(255, 255, 255, 0.06)`.
- **Radar Sweep**: CSS keyframe `eyebrow-scan` animating glowing horizontal scanlines across section numbers.
- **Breath Animation**: Gentle radial glow pulsing behind the `MSB.` monogram.

### 4.2. Sound Design Engine (Web Audio API)
- Keystrokes synthesize authentic mechanical switch sounds (cherry blue profile) using discrete audio sprites:
  - `sounds/press/GENERIC_R0.mp3` through `GENERIC_R4.mp3` (randomized round-robin keydowns).
  - `sounds/press/SPACE.mp3`, `ENTER.mp3`, `BACKSPACE.mp3` (tactile weighted action keys).
  - Paired release triggers in `sounds/release/`.
- Audio toggle switch is accessible via footer and header with persistence in `localStorage`.
