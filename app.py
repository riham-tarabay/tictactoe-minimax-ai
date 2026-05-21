# 🎮 Tic-Tac-Toe AI — Minimax + Alpha-Beta Pruning

> An **unbeatable** game-playing agent built with classic adversarial search.

## Demo
```
  0   1   2
0 X | O | X
  ---------
1 O | O | X
  ---------
2   |   | X

🏆 X wins!
```

## Key Results
| Metric | Value |
|---|---|
| Algorithm | Minimax + Alpha-Beta Pruning |
| Search depth | Full game tree (9! = 362,880 nodes max) |
| Pruning speedup | ~4x fewer nodes evaluated |
| Win rate vs random opponent | 100% |
| Draw rate vs optimal opponent | 100% |

## Architecture
```
game state (board)
      │
      ▼
  Minimax tree
  ├── Maximizer (AI)  → picks highest score
  └── Minimizer (You) → picks lowest score
        │
        ▼
  Alpha-Beta Pruning
  (skip branches that can't change outcome)
        │
        ▼
  Best move returned
```

## Quick Start
```bash
pip install -r requirements.txt

# CLI version
python minimax.py

# Web app
streamlit run app.py
```

## What I Learned
- Implementing adversarial search from scratch without libraries
- How alpha-beta pruning dramatically reduces the search space
- The importance of depth-weighted scoring for preferring faster wins
- Game tree representation and terminal state detection

## Tech Stack
`Python 3.11` · `Streamlit` · `Pure Python (no ML libraries needed)`
