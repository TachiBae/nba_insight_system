# NBA Game and Player Performance Insight System
A Python + MySQL + Flask web application for analyzing 
NBA game and player statistics.

Holy Angel University | School of Computing | AY 2025-2026

## Tech Stack
- Python 3.10+
- MySQL via XAMPP
- Flask (web frontend)
- Pandas (data loading)

## Setup
1. Start XAMPP and run MySQL
2. Run sql/schema.sql in MySQL Workbench
3. Run sql/seed_data.sql for sample data
4. Install dependencies: pip install flask mysql-connector-python pandas tabulate
5. Run: python load_data.py
6. Run: python app.py
7. Open browser: http://localhost:5000

## Dataset
Download CSV files from Kaggle and place in data/ folder:
- NBA Players: kaggle.com/datasets/justinas/nba-players-data
- NBA Games: kaggle.com/datasets/nathanlauga/nba-games
