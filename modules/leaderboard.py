from db_connection import get_connection

def get_leaderboard(stat):
    allowed = {'points', 'rebounds', 'assists', 'fg_pct'}
    if stat not in allowed:
        return []
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT p.name, t.name AS team, AVG(pss.{stat}) AS avg_stat
        FROM player_season_stats pss
        JOIN players p ON pss.player_id = p.player_id
        LEFT JOIN teams t ON p.team_id = t.team_id
        GROUP BY p.player_id ORDER BY avg_stat DESC LIMIT 10
    ''')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

