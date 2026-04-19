# F1 Race Visualizer

A Python-based real-time Formula 1 race visualization system built using telemetry data. This project simulates race replays with smooth animation, multiple drivers, and track rendering using real-world F1 data.

---

## Project Overview

This project aims to recreate an F1 race replay system similar to broadcast-level visualization tools using Python.

It leverages telemetry data to:

- Render real F1 tracks
- Animate multiple drivers
- Simulate race movement
- Build a foundation for advanced replay controls and analytics

---

## Features (Completed)

### Data Pipeline

- Fetches real race data using FastF1
- Processes telemetry including position (X, Y), speed, and lap data

### Track Visualization

- Renders actual F1 track layout using telemetry coordinates
- Handles scaling and normalization for screen display

### Multi-Driver Animation

- Simulates multiple drivers moving simultaneously on track
- Each driver represented with unique color

### Smooth Animation Engine

- Implemented interpolation (LERP) for smooth movement
- Eliminates choppy transitions between telemetry points
- Uses frame-based animation with Arcade game loop

### Robust Debugging & Handling

- Fixed coordinate scaling issues
- Handled missing telemetry jumps
- Prevented rendering bugs and crashes

---

## Tech Stack

- Python 3.11+
- FastF1 (Telemetry & race data)
- Arcade (Graphics & animation)
- NumPy / Pandas (Data processing)
- Matplotlib (Track visualization)

---

## Project Structure

```
f1-race-visualizer/
│
├── main.py              # Data loading & testing
├── track_map.py         # Track visualization (matplotlib)
├── race_sim.py          # Core animation engine (Arcade)
├── cache/               # FastF1 cache (ignored)
├── .gitignore
└── README.md
```

---

## How to Run

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/f1-race-visualizer.git
cd f1-race-visualizer
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install fastf1 arcade matplotlib pandas numpy
```

### 4. Run Simulation

```
python race_sim.py
```

---

## Current Progress

| Day   | Progress                                      |
| ----- | ----------------------------------------------|
| Day 1 | Data loading & telemetry extraction           |
| Day 2 | Track rendering                               |
| Day 3 | Multi-driver smooth animation                 |
| Day 4 | Playback controls                             |
| Day 4 | Live leaderboard (position + tyre compounds)  |

---

## Upcoming Features

-  Driver telemetry panel (speed, gear, DRS)
-  Weather system integration
-  Race flags (yellow, safety car, red flag)
-  Qualifying mode with telemetry graphs

---

## Key Learnings

- Real-time animation using game loops
- Telemetry data processing and visualization
- Coordinate normalization and scaling
- Interpolation for smooth motion
- Debugging graphical applications

---

## Disclaimer

This project uses publicly available data via FastF1 and is intended for educational purposes only.
Formula 1 and related trademarks belong to their respective owners.

---

## Author

Built with passion by Aryan
