import pandas as pd
from db_connection import get_connection

conn   = get_connection()
cursor = conn.cursor()

# ── 1. Load Teams ───────────────────────────────────────
print("Loading teams...")
teams_df    = pd.read_csv('data/teams.csv')
team_id_map = {}

for _, row in teams_df.iterrows():
    cursor.execute('''
        INSERT IGNORE INTO teams (name, abbreviation, city)
        VALUES (%s, %s, %s)
    ''', (
        row['NICKNAME'],
        row['ABBREVIATION'],
        row['CITY'],
    ))
    conn.commit()

    cursor.execute(
        'SELECT team_id FROM teams WHERE abbreviation = %s',
        (row['ABBREVIATION'],)
    )
    result = cursor.fetchone()
    if result:
        team_id_map[int(row['TEAM_ID'])] = result[0]

print(f"  {len(teams_df)} teams loaded.")

# ── 2. Load Seasons ─────────────────────────────────────
print("Loading seasons...")
players_df     = pd.read_csv('data/players.csv')
seasons_unique = players_df['season'].dropna().unique()

for season in seasons_unique:
    cursor.execute(
        'INSERT IGNORE INTO seasons (year) VALUES (%s)',
        (str(season),)
    )

conn.commit()
print(f"  {len(seasons_unique)} seasons loaded.")

# ── 3. Load Players ─────────────────────────────────────
print("Loading players...")
players_unique = players_df.drop_duplicates(subset='player_name')

for _, row in players_unique.iterrows():
    cursor.execute(
        'SELECT team_id FROM teams WHERE abbreviation = %s',
        (row['team_abbreviation'],)
    )
    team    = cursor.fetchone()
    team_id = team[0] if team else None

    cursor.execute(
        'INSERT IGNORE INTO players (name, team_id) VALUES (%s, %s)',
        (row['player_name'], team_id)
    )

conn.commit()
print(f"  {len(players_unique)} players loaded.")

# ── 4. Load Player Season Stats ─────────────────────────
print("Loading player season stats...")
count = 0

for _, row in players_df.iterrows():
    cursor.execute(
        'SELECT player_id FROM players WHERE name = %s',
        (row['player_name'],)
    )
    player = cursor.fetchone()
    if not player:
        continue

    cursor.execute(
        'SELECT season_id FROM seasons WHERE year = %s',
        (str(row['season']),)
    )
    season = cursor.fetchone()
    if not season:
        continue

    cursor.execute('''
        INSERT IGNORE INTO player_season_stats
            (player_id, season_id, games_played, points, rebounds, assists, fg_pct, ast_pct)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        player[0],
        season[0],
        int(row['gp'])        if pd.notna(row['gp'])      else 0,
        float(row['pts'])     if pd.notna(row['pts'])      else 0.0,
        float(row['reb'])     if pd.notna(row['reb'])      else 0.0,
        float(row['ast'])     if pd.notna(row['ast'])      else 0.0,
        float(row['ts_pct'])  if pd.notna(row['ts_pct'])   else None,
        float(row['ast_pct']) if pd.notna(row['ast_pct'])  else None,
    ))
    count += 1

conn.commit()
print(f"  {count} player season stat rows loaded.")

# ── 5. Load Games ───────────────────────────────────────
print("Loading games...")
games_df   = pd.read_csv('data/games.csv')
game_count = 0

for _, row in games_df.iterrows():
    home_team_id = team_id_map.get(int(row['HOME_TEAM_ID']))
    away_team_id = team_id_map.get(int(row['VISITOR_TEAM_ID']))

    if not home_team_id or not away_team_id:
        continue

    cursor.execute(
        'SELECT season_id FROM seasons WHERE year LIKE %s',
        (f"%{str(row['SEASON'])}%",)
    )
    season    = cursor.fetchone()
    season_id = season[0] if season else None

    cursor.execute('''
        INSERT IGNORE INTO games (game_date, home_team_id, away_team_id, season_id)
        VALUES (%s, %s, %s, %s)
    ''', (
        str(row['GAME_DATE_EST'])[:10],
        home_team_id,
        away_team_id,
        season_id
    ))

    if pd.notna(row['PTS_home']):
        game_id = cursor.lastrowid
        cursor.execute('''
            INSERT IGNORE INTO team_game_stats (team_id, game_id, score)
            VALUES (%s, %s, %s)
        ''', (home_team_id, game_id, int(row['PTS_home'])))

        cursor.execute('''
            INSERT IGNORE INTO team_game_stats (team_id, game_id, score)
            VALUES (%s, %s, %s)
        ''', (away_team_id, game_id, int(row['PTS_away'])))

    game_count += 1

conn.commit()
print(f"  {game_count} games loaded.")

# ── Done ────────────────────────────────────────────────
cursor.close()
conn.close()
print("\nAll data loaded successfully!")