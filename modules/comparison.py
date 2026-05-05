
from db_connection import get_connection

def get_player_avg(player_id):
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.name,
               ROUND(AVG(pss.points),1),   ROUND(AVG(pss.rebounds),1),
               ROUND(AVG(pss.assists),1),  ROUND(AVG(pss.fg_pct),1)
        FROM player_season_stats pss
        JOIN players p ON pss.player_id = p.player_id
        WHERE pss.player_id = %s GROUP BY p.name
    ''', (player_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

