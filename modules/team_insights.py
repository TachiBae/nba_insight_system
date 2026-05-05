from db_connection import get_connection

def get_all_teams():
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT team_id, name, city, conference FROM teams')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_team_stats(team_id):
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT t.name, AVG(tgs.score), AVG(tgs.turnovers)
        FROM team_game_stats tgs
        JOIN teams t ON tgs.team_id = t.team_id
        WHERE tgs.team_id = %s GROUP BY t.name
    ''', (team_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

