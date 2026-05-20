# Universal Gaming Oracle 🎮🔍

An AI-powered search engine for gaming that delivers intelligent, synthesized answers with citations from gaming wikis. Think of it as a "Perplexity for Gaming"—instead of returning blue links, it provides contextual, conversational answers about game mechanics, lore, and strategies.

**Status:** Development Roadmap Ready | Free-tier Cloud Hybrid Architecture

---

## 🎯 Project Overview

The **Universal Gaming Oracle** is a specialized Retrieval-Augmented Generation (RAG) system that allows users to ask complex, cross-game questions and receive accurate, synthesized answers with direct citations to the source wikis.

### Example Queries

- _"How does the parry mechanic in Sekiro compare to Elden Ring?"_
- _"What are the best weapons for a Dexterity build in Dark Souls 3?"_
- _"Where is the third shrine located in the Gerudo Highlands in Tears of the Kingdom, and what elemental resistance do I need?"_

### Why This Project?

1. **Portfolio Impact:** Demonstrates full-stack capabilities + modern AI/ML knowledge
2. **Zero Cost:** Entirely built on free tiers and local hardware
3. **Impressive Scope:** Shows ability to handle complex architectures and cloud services
4. **Domain Expertise:** Leverages your gaming knowledge for credible, accurate results

---

## 🏗️ Architecture Overview

This project uses a **Hybrid Cloud-Local Architecture** to minimize latency while maximizing free resources:

```
┌─────────────────────────────────────────────────────────────────┐
│                     User's M4 Mac (Local)                       │
│                                                                   │
│  ┌──────────────────┐    ┌──────────────────┐                   │
│  │  React Frontend  │───▶│  Node.js Backend │                   │
│  │  (Next.js)       │    │  (Express/API)   │                   │
│  └──────────────────┘    └────────┬─────────┘                   │
│                                    │                             │
│                         ┌──────────▼──────────┐                 │
│                         │   ChromaDB Local    │                 │
│                         │  Vector Database    │                 │
│                         │ (2TB Google Drive)  │                 │
│                         └─────────┬──────────┘                  │
│                                    │ (30ms latency)             │
└────────────────────────────────────┼──────────────────────────┘
                                     │
                        ┌────────────▼──────────────┐
                        │   Google Colab (Cloud)    │
                        │   ┌──────────────────┐    │
                        │   │  Ollama Instance │    │
                        │   │ Llama 3.1 (8B)   │    │
                        │   └────────┬─────────┘    │
                        │            │              │
                        │  ┌─────────▼─────────┐   │
                        │  │ Pinggy/Ngrok      │   │
                        │  │ Tunnel (Public)   │   │
                        │  └───────────────────┘   │
                        └──────────────────────────┘
```

### Key Components

| Component           | Technology                              | Rationale                                          |
| ------------------- | --------------------------------------- | -------------------------------------------------- |
| **Frontend**        | Next.js / React (TypeScript)            | Fast, modern, supports syntax-highlighted results  |
| **Backend**         | Node.js (Express) or Python (FastAPI)   | Orchestrates queries between UI, database, and LLM |
| **Vector DB**       | ChromaDB (Local)                        | Open-source, runs in-process, zero setup overhead  |
| **Embedding Model** | Hugging Face `all-MiniLM-L6-v2`         | Free, fast semantic search                         |
| **LLM**             | Ollama + Llama 3.1 (8B) on Colab        | Free cloud GPUs, no API costs                      |
| **Web Scraper**     | LangChain WebBaseLoader / BeautifulSoup | Cleans wiki HTML into readable text                |
| **Tunneling**       | Pinggy or Ngrok                         | Exposes local Colab endpoint to your Mac           |
| **Data Storage**    | Google Drive (2TB)                      | Syncs ChromaDB between cloud and local             |

---

## 💾 Hardware & Infrastructure

### Your Machine

- **M4 MacBook Air**
- **24GB Unified Memory** → Sufficient for local LLM running + database queries
- **512GB SSD** (+ 2TB external) → Plenty for all game wikis + models

### Cloud Resources (All Free)

- **Google Colab:** T4 GPU for scraping, embedding, and LLM inference
- **Google Drive:** 2TB for syncing ChromaDB vector database
- **Pinggy/Ngrok:** Free tunnel service for exposing Colab LLM to your backend

**Total Cost:** $0 ✅

---

## 🗄️ Data Strategy: Tiered Indexing

### Tier 1: Deep Dive (Top 50 Games)

- Fully scraped and embedded gaming wikis stored in local ChromaDB
- Examples: Elden Ring, Dark Souls, Zelda, Skyrim, League of Legends, Path of Exile
- **Result:** Ultra-fast, highly accurate responses (30ms latency)

### Tier 2: Live Search (Everything Else)

- For obscure or newly released games not in your database
- Backend detects unknown game and triggers live web search (Tavily API)
- **Result:** Broad coverage without massive local storage

### Metadata Tagging

Every chunk in ChromaDB includes:

```json
{
  "game": "Elden Ring",
  "category": "Lore",
  "source_url": "https://eldenring.wiki/...",
  "chunk_id": "42"
}
```

This prevents the AI from mixing up lore from different games.

---

## 🛠️ Tech Stack

### Frontend

```
Next.js / React + TypeScript
├── Search bar with game selector
├── Real-time "thinking" indicators
├── Markdown rendering for responses
├── Syntax highlighting for code/builds
└── Citation numbers linked to source URLs
```

### Backend

```
Node.js + Express (or Python + FastAPI)
├── /api/search - Query endpoint
├── /api/games - List available games
├── /api/sources - Get source metadata
└── Middleware for error handling & rate limiting
```

### Database Pipeline

```
Google Colab (GPU)
├── Web scraper (MediaWiki API / BeautifulSoup)
├── Text preprocessing & chunking
├── Embedding model (Hugging Face)
└── Save to Google Drive
        ↓
ChromaDB (Local on Mac)
├── Vector similarity search
├── Metadata filtering
└── Instant retrieval (30ms)
```

### LLM Inference

```
Google Colab
├── Ollama server (11434 port)
├── Llama 3.1 (8B) model
├── Pinggy tunnel
└── Exposed at https://[random].pinggy.link
        ↓
Node.js Backend
└── Makes POST requests to tunnel URL
```

---

## 📋 Development Roadmap

### Level 1: The Prototype (Single Game) ✅ START HERE

**Goal:** Prove the core RAG pipeline works end-to-end

- [ ] Set up Google Colab notebook
- [ ] Write web scraper for one game wiki (e.g., Elden Ring)
- [ ] Extract & clean ~100 pages of text
- [ ] Test local embedding + ChromaDB storage
- [ ] Write simple CLI script to query the database

**Deliverable:** Terminal output showing semantic search results

---

### Level 2: The Brain Connection

**Goal:** Add AI reasoning to database results

- [ ] Set up Ollama in Colab notebook
- [ ] Generate Pinggy tunnel URL
- [ ] Configure local backend to call Colab LLM
- [ ] Build RAG prompt: _"Use only this context to answer the question"_
- [ ] Test end-to-end: Query → Search → LLM Answer

**Deliverable:** CLI that returns AI-synthesized answers with reasoning

---

### Level 3: Full-Stack Application

**Goal:** Ship a complete web app

- [ ] Build React search interface
- [ ] Deploy Next.js frontend (Vercel)
- [ ] Build Node.js backend (Express)
- [ ] Add game selector dropdown
- [ ] Display citations with source links
- [ ] Add loading states & error handling

**Deliverable:** Working web app at your-domain.vercel.app

---

### Level 4: The Universal Engine

**Goal:** Expand to multiple games + live search

- [ ] Scrape top 10-20 games into Tier 1
- [ ] Add metadata filtering to prevent game confusion
- [ ] Implement Tavily API for live web search (Tier 2)
- [ ] Add "Did you know?" related queries
- [ ] User feedback loop (thumbs up/down on answers)

**Deliverable:** Production-ready search engine for gaming

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+ (for scraping scripts)
- Node.js 18+ (for backend)
- Google account (for Colab + Drive)
- VS Code (or your IDE)

### Installation

#### 1. Clone & Setup Local Environment

```bash
# Clone repo (when ready)
git clone https://github.com/yourusername/gaming-oracle.git
cd gaming-oracle

# Create virtual environment (Python)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt      # Python packages
npm install                          # Node packages
```

#### 2. Set Up Google Drive Sync

```bash
# Install Google Drive desktop app (Mac)
# Create folder: ~/Google Drive/gaming-oracle-data
# Your backend will point ChromaDB to this location
```

#### 3. Create Colab Notebook

- Go to [Google Colab](https://colab.research.google.com)
- Create new notebook
- Set runtime to **GPU (T4)**
- Copy the setup script (see below)

#### 4. Run Initial Scraper (Colab)

```python
# In Google Colab cell
!curl -fsSL https://ollama.com/install.sh | sh

import subprocess
subprocess.Popen(['ollama', 'serve'])

# Install tunneling
!pip install pinggy
import pinggy
tunnel = pinggy.start_tunnel(forwardto="localhost:11434")
print(f"🔗 LLM Endpoint: {tunnel.urls}")

# Download LLM
!ollama pull llama3.1

# Mount Google Drive for ChromaDB storage
from google.colab import drive
drive.mount('/content/drive')
```

#### 5. Configure Backend

```bash
# Create .env file
cat > .env << EOF
COLAB_LLM_URL=https://[your-pinggy-url].pinggy.link
CHROMA_DB_PATH=/path/to/synced/chromadb
TAVILY_API_KEY=your_free_key_here
EOF
```

#### 6. Start Local Backend

```bash
npm run dev        # For Node.js + Express
# or
python app.py      # For Python + FastAPI
```

---

## 📦 File Structure

```
gaming-oracle/
├── README.md                          # This file
├── PROJECT_DISCUSSION_BACKUP.md       # Original chat (reference)
│
├── frontend/
│   ├── pages/
│   │   ├── index.tsx                 # Search page
│   │   └── api/
│   │       └── search.ts             # API route
│   ├── components/
│   │   ├── SearchBar.tsx
│   │   ├── ResultCard.tsx
│   │   └── Citations.tsx
│   ├── styles/
│   ├── package.json
│   └── tsconfig.json
│
├── backend/
│   ├── routes/
│   │   ├── search.js
│   │   ├── games.js
│   │   └── health.js
│   ├── services/
│   │   ├── chromadb.js               # Vector DB queries
│   │   ├── llm.js                    # Colab LLM calls
│   │   └── scraper.js                # Web scraping
│   ├── app.js                         # Express server
│   ├── package.json
│   └── .env                           # Configuration
│
├── scripts/
│   ├── colab_setup.ipynb             # Colab notebook
│   ├── scraper.py                    # Wiki scraper
│   └── embedder.py                   # Text → vectors
│
├── data/
│   ├── chromadb/                     # Local vector DB
│   └── game_metadata.json            # Game info
│
└── requirements.txt                  # Python dependencies
```

---

## 🎮 Supported Games (Roadmap)

### Tier 1 (Priority - Full Scrape)

- Elden Ring
- Dark Souls series (1, 2, 3)
- Zelda: Tears of the Kingdom
- Skyrim
- League of Legends
- Path of Exile
- Cyberpunk 2077
- Baldur's Gate 3
- Diablo IV
- Starfield

### Tier 2 (Live Search)

- Any game with public wiki/documentation
- Fallback to Google search + web scraping

---

## 🔌 API Endpoints

### Search Query

```bash
POST /api/search
Content-Type: application/json

{
  "query": "How does parry work in Elden Ring?",
  "game": "Elden Ring",
  "topK": 5
}

Response:
{
  "answer": "In Elden Ring, parrying is a defensive technique...",
  "sources": [
    {
      "url": "https://eldenring.wiki/Parry",
      "snippet": "The Parry skill is performed by..."
    }
  ],
  "confidence": 0.89
}
```

### List Games

```bash
GET /api/games

Response:
{
  "tier1": ["Elden Ring", "Dark Souls 3", ...],
  "tier2_available": 1000+,
  "last_updated": "2026-05-21T10:30:00Z"
}
```

### Health Check

```bash
GET /api/health

Response:
{
  "status": "ok",
  "chromadb": "connected",
  "llm": "connected",
  "colab_latency_ms": 245
}
```

---

## 🎓 Key Concepts Explained

### RAG (Retrieval-Augmented Generation)

**Problem:** LLMs are trained on static data and can hallucinate.
**Solution:** Give the LLM context first, then ask it to answer based on ONLY that context.

**Flow:**

1. User asks: _"Best weapon for strength build?"_
2. Backend searches ChromaDB for similar text chunks
3. Backend sends to LLM: _"Based on this wiki text: [...], answer the question"_
4. LLM uses ONLY the provided text to generate an answer

### Vector Embeddings

**Concept:** Convert text into mathematical vectors (lists of numbers).
**Benefit:** Similar concepts have similar vectors, enabling semantic search.

Example:

- "Parry mechanic" and "defend against attack" have similar vectors
- Traditional keyword search would miss this relationship

### Semantic Search vs. Keyword Search

| Keyword             | Semantic                            |
| ------------------- | ----------------------------------- |
| "Waterproof boots"  | "Shoes for walking through puddles" |
| Exact word matching | Concept matching                    |
| Fast but inflexible | Slow but intelligent                |

---

## 🔐 Privacy & Security Notes

- ✅ All data stays on your Mac (ChromaDB is local)
- ✅ LLM runs on your own Colab session (private)
- ⚠️ First-time Colab setup requires Google account login
- ⚠️ Pinggy tunnel URL should NOT be shared publicly (anyone could call your LLM)
- ✅ Consider adding API key authentication for production

---

## 📊 Performance Targets

| Metric            | Target        | Why                      |
| ----------------- | ------------- | ------------------------ |
| Database latency  | <50ms         | Local SSD queries        |
| LLM response time | 2-5s          | Cloud GPU processing     |
| Total response    | 2.5-5.5s      | Acceptable for search UX |
| Memory usage      | <4GB          | M4 Mac comfort zone      |
| Concurrent users  | 1 (prototype) | Personal project         |

---

## 🚨 Known Limitations & Challenges

1. **Colab Session Timeouts:** Free tier disconnects after 12 hours. Restart the notebook to get a new Pinggy URL.
2. **Data Freshness:** Wiki data is static. Game patches/updates require re-scraping.
3. **LLM Hallucinations:** Even with RAG, the LLM might invent details. Users should fact-check citations.
4. **Scraping Overhead:** Converting 10,000 wiki pages to vectors takes ~4-6 hours on Colab GPU (one-time cost).
5. **Rate Limiting:** Tavily API has free tier limits. Design accordingly for Tier 2 queries.

---

## 📚 Resources & References

### Documentation

- [ChromaDB Docs](https://docs.trychroma.com)
- [Ollama Installation](https://ollama.com)
- [LangChain RAG Guide](https://python.langchain.com/docs/modules/data_connection/rag/)
- [Hugging Face Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

### Similar Projects

- **Perplexity.ai** - Inspiration for the RAG + citations pattern
- **OpenAI's ChatGPT with Plugins** - Example of external data injection
- **YouTube Video Reference:** https://youtu.be/NULWyn8Hqs8 (Project 8)

### Free Tier API Keys

- [Tavily Web Search](https://tavily.com) - Free tier included
- [Groq API](https://groq.com) - Alternative free LLM endpoint
- [Hugging Face](https://huggingface.co) - Free inference endpoints

---

## 💡 Tips for Success

1. **Start Small:** Get Level 1 working perfectly before scaling to multiple games.
2. **Test Locally First:** Use a small wiki subset (50 pages) to debug the pipeline.
3. **Monitor Colab Session:** Keep a browser tab open to check LLM tunnel status.
4. **Version Your Data:** Save ChromaDB snapshots before adding new games.
5. **Iterate on Prompts:** The system prompt to the LLM is the most impactful tuning lever.

---

## 📝 License

This project is personal/educational. Respect the wikis' terms of service when scraping.

---

## 👤 Author

Built by you as a portfolio project demonstrating full-stack + AI engineering skills.

---

## 🤝 Contributing

This is a personal project, but feel free to experiment and extend it!

**Next Steps:**

1. Create a GitHub repository
2. Set up the initial Colab notebook
3. Start with Level 1 prototype
4. Document your progress as you build

---

## 📞 Questions?

Refer to `PROJECT_DISCUSSION_BACKUP.md` for the detailed conversation about architecture, design decisions, and rationale.

---

**Last Updated:** May 21, 2026
**Project Status:** 🚀 Ready to Build
