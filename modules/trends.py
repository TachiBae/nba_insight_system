from db_connection import get_connection

def get_trends(player_id, n=10):
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.year, pss.points, pss.rebounds, pss.assists, pss.fg_pct
        FROM player_season_stats pss
        JOIN seasons s ON pss.season_id = s.season_id
        WHERE pss.player_id = %s
        ORDER BY s.year DESC LIMIT %s
    ''', (player_id, int(n)))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    avg_pts = round(sum(float(r[1]) for r in rows) / len(rows), 1) if rows else 0
    streak  = 'HOT' if avg_pts >= 25 else ('COLD' if avg_pts <= 10 else 'NORMAL')
    return rows, avg_pts, streak

