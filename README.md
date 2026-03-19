# 🎵 Hirsch Music Engine

**All-in-One KI Musik Generator** – Das Beste aus Suno, Udio, TopMediai und deinem Hirsch Music Hit Maker in einem System.

## 🚀 Features

### Tab 1: Lyrics & Story (Text-Brain)
- **Idee → Fertige Lyrics** in Sekunden
- Unterstützt Deutsch & Englisch
- Automatische Song-Struktur: [Intro], [Verse], [Pre-Chorus], [Chorus], [Bridge], [Outro]
- Silben-Metrik passend zu BPM/Takt
- Reim-Checker & Style-Anpassung (poetisch bis direkt/politisch)

### Tab 2: Song Fusion & Style Lab (Hirsch-DNA)
- **Zwei oder mehr Songs mischen** (z.B. 60% Outlaw Country + 40% Industrial Rock)
- Referenz-Song-Analyse (BPM, Key, Groove, Vibe)
- Generiert Master-Prompts für alle Musik-Engines
- Deine Song-Fusion-Logik aus dem Hirsch Music Hit Maker

### Tab 3: Musik-Generator (Core Engine)
- **Text → Kompletter Song mit Vocals**
- **Lyrics + Prompt → Studio-Track**
- **Referenz-Audio → Style Transfer**
- Modi:
  - Voller Song mit Vocals
  - Instrumental (Backing für echte Vocals)
  - Loop (16-Takt Hooks)
- Backend: MusicGen + AudioLDM + Voice Cloning

### Tab 4: Stems, Remix & Arrange (Udio-Power)
- **Stem-Splitter**: Vocals, Drums, Bass, Guitars, Other
- **Timeline-View**: Parts verlängern, kürzen, neu generieren
- **Inpainting**: Nur einzelne Teile (z.B. Bridge) regenerieren
- Export: WAV-Stems für DAW, Vollmix, MIDI/Chords

## 🛠️ Tech Stack

### Backend
- **Python 3.10+**
- **FastAPI** (REST API)
- **MusicGen** / **AudioLDM** (Musik-Generierung)
- **Voice Cloning** (TTS mit Singing Support)
- **MDX-Net** (Stem Separation)
- **LLM** (Lyrics & Prompt Engineering)

### Frontend
- **HTML5 + Vanilla JS**
- **Tabs-Navigation** mit modernem Dark Theme
- **Audio-Player** mit Waveform
- **Drag & Drop** für Referenz-Audio

## 📦 Installation

```bash
# 1. Repository klonen
git clone https://github.com/martinbinderhirsch-sys/hirsch-music-engine.git
cd hirsch-music-engine

# 2. Python Dependencies installieren
pip install -r requirements.txt

# 3. Config anpassen
cp config.example.yaml config.yaml
# Trage deine API-Keys ein (optional für externe LLMs)

# 4. Server starten
python app.py

# 5. Browser öffnen
# http://localhost:8000
```

## ⚙️ Konfiguration

Bearbeite `config.yaml`:

```yaml
server:
  host: 0.0.0.0
  port: 8000

models:
  music_backend: "musicgen"  # oder "audioldm"
  llm_provider: "local"      # oder "openai", "anthropic"
  llm_model: "mistral-7b"    # lokales Modell
  
audio:
  sample_rate: 44100
  max_duration: 480  # 8 Minuten (wie TopMediai)
  
stem_separation:
  model: "mdx_extra"  # oder "demucs"
  
output:
  projects_dir: "./projects"
  stems_format: "wav"
```

## 🎯 Workflow-Beispiel

### Schneller Song (Suno-Style)
1. **Tab 1**: Idee eingeben → "German outlaw country about freedom"
2. **Tab 2**: Fusion → 70% Johnny Cash + 30% Die Toten Hosen
3. **Tab 3**: Generate → Song in 2 Min fertig
4. **Tab 4**: Stems exportieren → in Ableton/Logic weiter produzieren

### Professioneller Track (Udio-Style)
1. **Tab 1**: Komplette Lyrics schreiben/generieren
2. **Tab 2**: Detaillierter Prompt (BPM, Key, Instrumentierung)
3. **Tab 3**: High-Quality Mode → 8-Min-Track
4. **Tab 4**: Timeline → Bridge verlängern, Refrain duplizieren
5. Export: Stems + Vollmix

## 🎼 Genre-Support

- **Rock**: Classic, Hard, Industrial, Grunge
- **Country**: Outlaw, Country Pop, Americana
- **Rap/Hip-Hop**: Deutsch & Englisch
- **Protest Songs**: Singer-Songwriter, Folk
- **Balladen**: Akustisch & elektrisch
- **Fusion**: Beliebige Kombinationen

## 🔒 Privacy & Tokens

- **Kein Token-System** – läuft komplett lokal oder auf deinem Server
- Keine Cloud-Abhängigkeit (außer du willst externe LLM-APIs nutzen)
- Alle Projekte bleiben auf deinem Rechner

## 📝 Projekt-Struktur

```
hirsch-music-engine/
├── app.py                 # FastAPI Main Server
├── config.yaml            # Konfiguration
├── requirements.txt       # Python Dependencies
├── backend/
│   ├── lyrics_engine.py   # LLM Lyrics Generator
│   ├── style_fusion.py    # Song Fusion Logic
│   ├── music_generator.py # MusicGen/AudioLDM Wrapper
│   ├── vocal_engine.py    # Voice Cloning
│   └── stem_splitter.py   # MDX-Net Separation
├── frontend/
│   ├── index.html         # 4-Tab UI
│   ├── style.css          # Dark Theme
│   └── app.js             # Frontend Logic
└── projects/              # Generierte Songs
    └── [song-id]/
        ├── metadata.json
        ├── full_mix.wav
        └── stems/
```

## 🚧 Roadmap

- [x] Repository Setup
- [ ] MVP: Lyrics + Music Generator
- [ ] Song Fusion Tab komplett
- [ ] Stem Splitter Integration
- [ ] Timeline-Editor für Remix
- [ ] MIDI/Chord Export
- [ ] Mobile UI
- [ ] Docker Support

## 🎤 Made for Producers

Dieses Tool wurde für **Vocalisten, Songwriter & Produzenten** entwickelt, die:
- Schnell Song-Ideen testen wollen (Demo-Phase)
- Backing-Tracks für echte Vocals brauchen
- Genre-Fusionen experimentieren
- Von der Idee bis zum fertigen Mix alles in einem Tool haben wollen

## 📜 License

MIT License – nur für persönlichen Gebrauch.

---

**Entwickelt mit ❤️ für Rock, Country & Protest Songs**
