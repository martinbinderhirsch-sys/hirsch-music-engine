#!/usr/bin/env python3
"""Hirsch Music Engine - FastAPI Main Server"""
import os
import yaml
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

# Basis-Pfad
BASE_DIR = Path(__file__).resolve().parent

# Config laden
with open(BASE_DIR / "config.yaml") as f:
    config = yaml.safe_load(f)

# FastAPI App
app = FastAPI(
    title="Hirsch Music Engine",
    description="All-in-One KI Musik Generator",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Frontend static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Models
class LyricsRequest(BaseModel):
    idea: str
    language: str = "de"
    structure: Optional[List[str]] = None
    bpm: Optional[int] = 90
    style: Optional[str] = "default"

class StyleFusionRequest(BaseModel):
    reference_songs: List[str]
    mix_ratios: List[float]
    target_genre: Optional[str] = None

class MusicGenRequest(BaseModel):
    prompt: str
    lyrics: Optional[str] = None
    duration: int = 120
    mode: str = "full"  # full, instrumental, loop
    seed: Optional[int] = None

class StemRequest(BaseModel):
    song_id: str
    regenerate_part: Optional[str] = None

# === ENDPOINTS ===

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

@app.post("/api/lyrics/generate")
async def generate_lyrics(req: LyricsRequest):
    """Tab 1: Lyrics Generator"""
    try:
        from backend.lyrics_engine import LyricsEngine
        engine = LyricsEngine(config)
        result = await engine.generate(
            idea=req.idea,
            language=req.language,
            structure=req.structure,
            bpm=req.bpm,
            style=req.style
        )
        return JSONResponse(result)
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/fusion/analyze")
async def analyze_fusion(req: StyleFusionRequest):
    """Tab 2: Song Fusion"""
    try:
        from backend.style_fusion import StyleFusion
        fusion = StyleFusion(config)
        result = await fusion.mix_styles(
            references=req.reference_songs,
            ratios=req.mix_ratios,
            target=req.target_genre
        )
        return JSONResponse(result)
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/music/generate")
async def generate_music(req: MusicGenRequest):
    """Tab 3: Music Generator"""
    try:
        from backend.music_generator import MusicGenerator
        from backend.vocal_engine import VocalEngine
        
        gen = MusicGenerator(config)
        vocal = VocalEngine(config)
        
        # Musik generieren
        audio_path = await gen.generate(
            prompt=req.prompt,
            duration=req.duration,
            mode=req.mode,
            seed=req.seed
        )
        
        # Vocals hinzufügen
        if req.lyrics and req.mode != "instrumental":
            audio_path = await vocal.add_vocals(
                instrumental=audio_path,
                lyrics=req.lyrics,
                language="de"  # oder aus req
            )
        
        return {"song_id": Path(audio_path).stem, "audio_url": f"/audio/{Path(audio_path).name}"}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/stems/split")
async def split_stems(req: StemRequest):
    """Tab 4: Stem Splitter"""
    try:
        from backend.stem_splitter import StemSplitter
        splitter = StemSplitter(config)
        result = await splitter.split(req.song_id)
        return JSONResponse(result)
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/api/stems/remix")
async def remix_part(req: StemRequest):
    """Regeneriere nur einen Teil"""
    try:
        from backend.music_generator import MusicGenerator
        gen = MusicGenerator(config)
        result = await gen.inpaint(
            song_id=req.song_id,
            part=req.regenerate_part
        )
        return JSONResponse(result)
    except Exception as e:
        raise HTTPException(500, str(e))

@app.get("/api/projects")
async def list_projects():
    """Liste alle generierten Songs"""
    projects_dir = Path(config["output"]["projects_dir"])
    projects = []
    if projects_dir.exists():
        for p in projects_dir.iterdir():
            if p.is_dir():
                meta = p / "metadata.json"
                if meta.exists():
                    import json
                    projects.append(json.load(open(meta)))
    return {"projects": projects}

if __name__ == "__main__":
    # Ordner erstellen
    Path(config["output"]["projects_dir"]).mkdir(exist_ok=True)
    Path(config["cache"]["dir"]).mkdir(exist_ok=True)
    
    uvicorn.run(
        "app:app",
        host=config["server"]["host"],
        port=config["server"]["port"],
        reload=config["server"].get("reload", True)
    )
