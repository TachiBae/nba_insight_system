import pandas as pd
from db_connection import get_connection

conn   = get_connection()
cursor = conn.cursor()

# --- Load Players ---
players_df     = pd.read_csv('data/players.csv')
players_unique = players_df.drop_duplicates(subset='player_name')

for _, row in players_unique.iterrows():
    # Look up team_id using abbreviation
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
cursor.close()
conn.close()

print("Players loaded successfully!")