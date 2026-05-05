from db_connection import get_connection

def search_players(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT p.player_id, p.name, t.name AS team'
        ' FROM players p LEFT JOIN teams t ON p.team_id = t.team_id'
        ' WHERE p.name LIKE %s', (f'%{name}%',)
    )

    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results

def get_player_stats(player_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT AVG(points), AVG(rebounds), AVG(assists),
               AVG(fg_pct), AVG(games_played)
        FROM player_season_stats WHERE player_id = %s
    ''', (player_id,))

    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result