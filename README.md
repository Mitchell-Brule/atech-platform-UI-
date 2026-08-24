# Atech — Hardware from a chat

An interactive, responsive platform designed for **Atech** ([atech.dev](https://atech.dev/)), embodying the vision of **"Hardware from a chat"** and **"Vibe-engineering for physical hardware"**.

Backed by **$800K Pre-Seed** from **Emblem, Nordic Makers, Lovable, Sequoia, and a16z**.

---

## 🌟 Features & Architecture

### 1. 🛠️ 4-Stage Hardware Creation Pipeline
1. **Stage 1: Prompt & Ideation**
   - Natural language prompt synthesis (*Air piano*, *Tilt marble maze*, *Robot deck*, *WiFi lights*).
   - **"Want to use your own agent?"**: Connect custom AI agents, Claude Code, Cursor, Copilot, Antigravity CLI (`agy run`), or local LLMs.
   - 14-Port auto-negotiating motherboard port routing.
2. **Stage 2: 3D Concept & Parametric Studio**
   - Real-time **Three.js WebGL 3D Canvas** with orbit, rotate, pan, and zoom controls.
   - Exploded view disassembly animation, X-Ray mode, and wireframe toggle.
   - Conversational AI geometry refinement with real-time bounding box adjustments.
   - Multi-material rendering (Household paper/glue, 3D Print PLA, CNC Factory Aluminum).
3. **Stage 3: Design & Engineering**
   - **Precision CAD**: STL & STEP AP242 with PMI export + Creative CAD bridge (SolidWorks, Fusion 360, Siemens NX, Onshape).
   - **Ribbon Wiring**: Interactive 14-Port motherboard wire harness schematics.
   - **C++ Firmware**: WebUSB direct one-click flashing to connected microcontrollers.
   - **Exploded Assembly Schematic**: LEGO-style step-by-step build manual with complete BOM table.
4. **Stage 4: Pre-order Kit & Standalone Modules**
   - **Early Adopter Kit · Small ($99.00 USD)**: 10 essential modules.
   - **Early Adopter Kit · Big ($159.00 USD - Most Popular)**: 20 modules.
   - Standalone module catalog ($9 to $49) and early access waitlist capture.

---

### 2. ⚡ Pro Studio Mode & Undercover Toggle
* Discreet **Pro Mode** toggle in the profile dropdown modal.
* **Parametric Solid B-Rep CAD Engine**: Real-time sliders for wall thickness, mold draft angles, brass standoff engagement, snap cantilever clearance, and fillet radii.
* **14-Port Dynamic Bus Multiplexer & Power Matrix**: Live I2C address conflict resolver, 3.3V/5V load auditor, and 500mAh LiPo battery life calculator.
* **RTOS Multi-Core Studio & Live WebSerial Oscilloscope**: Real-time dual-channel waveform streamer for sensor telemetry.
* **DFM & GD&T Tolerance Audit**: ISO 2768-m medium tolerance stackup and 2-plate mold pull vector verification.

---

### 3. 👥 Strict Profile Isolation
* 🎓 **Student & 🛠️ Hobbyist**: Identical standard maker studios.
* 🏫 **Teacher**: Exclusive **Programs** portal with Kahoot-style classroom join room PIN (`849-210`), student tool scaffolding policies, and vetted syllabi matcher.
* 🏭 **Industry**: Exclusive **Enterprise** portal with GD&T tolerance checks, STEP AP242 with PMI, dedicated TinyML edge-AI integration contracts, and a 100 Hz live streaming telemetry demo.

---

### 4. 🌐 Community Hub & Stay Connected
* **Rich Showcase**: Community builds with high-res mock hardware photos, rating stars, live remix counts, and like counters.
* **Idea Voting**: 1,500-vote threshold to trigger hardware manufacturing.
* **Stay Connected**: Direct links to Discord (4.2k Makers), GitHub (Open Source SDK), YouTube (Teardowns), X (@atech_dev), LinkedIn, and Instagram (@atech.dev).
* **Creator Module Bounties**: $1,500 + 12% revenue royalties for community hardware designs.

---

### 5. 👥 The Ateam
* **Tomas Harmer** — CEO • Vision & Strategy
* **David Stålmarck** — CTO • AI & Software
* **Mitchell Brule** — Mitchify
* **Gustav Hugod** — Head of Sales & Growth
* **Julius Thunström** — Head of AI/ML

---

## 🚀 Running Locally

### Option 1: Direct in Browser
Open `index.html` in any modern web browser (Chrome, Edge, Brave, Firefox, Safari).

### Option 2: Local Python Server
```bash
python server.py
```
Open **[http://localhost:8088](http://localhost:8088)** in your browser.

---

## 🤝 Collaborating & Sharing

### 1. Push to GitHub
```bash
git remote add origin https://github.com/<YOUR-USERNAME>/<REPO-NAME>.git
git branch -M main
git push -u origin main
```

### 2. Granting Access to Collaborators
1. Go to your repository on [GitHub](https://github.com/).
2. Navigate to **Settings** > **Collaborators** > Click **Add people**.
3. Enter their GitHub username or email address and send the invitation.

### 3. Free 1-Click Live Web Hosting (GitHub Pages)
1. Go to repository **Settings** > **Pages**.
2. Under **Branch**, select `main` and root `/`, then click **Save**.
3. Your interactive Atech platform will be live at `https://<YOUR-USERNAME>.github.io/<REPO-NAME>/`.

---

## 📜 License
MIT License. Built for the Atech Maker Community.

