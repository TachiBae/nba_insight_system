# app.py
from flask import Flask, render_template, request
from modules import player_insights, team_insights
from modules import leaderboard, comparison, trends


app = Flask(__name__)


# ── Home Page ──────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')


# ── Player Insights ────────────────────────────
@app.route('/players')
def players():
    name    = request.args.get('name', '')
    results = player_insights.search_players(name) if name else []
    return render_template('players.html', results=results, name=name)


@app.route('/players/<int:player_id>')
def player_detail(player_id):
    stats = player_insights.get_player_stats(player_id)
    return render_template('player_detail.html', stats=stats, pid=player_id)


# ── Team Insights ──────────────────────────────
@app.route('/teams')
def teams():
    all_teams = team_insights.get_all_teams()
    return render_template('teams.html', teams=all_teams)


@app.route('/teams/<int:team_id>')
def team_detail(team_id):
    stats = team_insights.get_team_stats(team_id)
    return render_template('team_detail.html', stats=stats)


# ── Leaderboard ────────────────────────────────
@app.route('/leaderboard')
def leaderboard_view():
    stat    = request.args.get('stat', 'points')
    results = leaderboard.get_leaderboard(stat)
    return render_template('leaderboard.html', results=results, stat=stat)


# ── Player Comparison ──────────────────────────
@app.route('/comparison')
def comparison_view():
    pid1 = request.args.get('pid1')
    pid2 = request.args.get('pid2')
    p1   = comparison.get_player_avg(pid1) if pid1 else None
    p2   = comparison.get_player_avg(pid2) if pid2 else None
    return render_template('comparison.html', p1=p1, p2=p2)


# ── Trend Analysis ─────────────────────────────
@app.route('/trends')
def trends_view():
    pid   = request.args.get('pid')
    n_raw = request.args.get('n', 10)
    try:
        n = int(n_raw)
    except (TypeError, ValueError):
        n = 10
    if n <= 0:
        n = 10
    rows, avg_pts, streak = trends.get_trends(pid, n) if pid else ([], 0, '')
    return render_template('trends.html', rows=rows,
                           avg_pts=avg_pts, streak=streak)


# ── Run the App ────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)