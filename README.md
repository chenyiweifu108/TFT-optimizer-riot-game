# TFT Intelligent Team Planner and Recommendation System

## Overview
This repository contains an interactive web application that assists *Teamfight Tactics (TFT)* players in planning and optimizing their team compositions.  
The system provides a drag-and-drop TFT board, dynamic trait tracking, and real-time composition recommendations based on meta data and player input.

The application integrates Riot’s official static data (via CommunityDragon) with a Python-based recommendation backend that identifies optimal team compositions given the user’s current board and custom trait configurations.

---

## Key Features
- **Interactive Board:** Web-based 7×4 TFT board supporting drag-and-drop champion placement.  
- **Dynamic Synergy Tracking:** Real-time detection of active and potential traits as champions are placed.  
- **Intelligent Recommendations:** Suggests next champions, full compositions, and item builds derived from meta data and win-rate statistics.  
- **Custom Trait Adjustment:** Allows users to manually modify trait counts to account for emblems or augments.  
- **Modular Architecture:** Frontend (React/Vite) and backend (FastAPI) are decoupled for scalability and independent deployment.

---

## System Architecture

**Frontend (GitHub Pages)**  
- `Board/` – Champion placement and grid logic  
- `SynergyPanel/` – Trait visualization and tracking  
- `API/` – Interfaces to backend recommendation service  
- `index.html` – Entry point  

**Backend (FastAPI Service, Render or Hugging Face)**  
- `main.py` – API endpoints  
- `recommender.py` – Core similarity and recommendation algorithms  
- `data_loader.py` – Loads champion, trait, and item data  
- `utils.py` – Helper functions  

**Data**  
- `tft_champions.json` – Champion static data  
- `tft_traits.json` – Trait definitions  
- `tft_items.json` – Item definitions  

---

## Technology Stack

| Layer | Technologies |
|-------|--------------|
| Frontend | React, TypeScript, DnD Kit, Chart.js |
| Backend | FastAPI (Python 3.11), Uvicorn |
| Data | CommunityDragon static JSON (Riot official source) |
| Deployment | GitHub Pages (frontend) + Render / Hugging Face Spaces (backend) |

---

## Installation

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
