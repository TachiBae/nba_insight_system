-- ============================================
-- NBA Insight System — Seed Data
-- Sample data for testing all 5 modules
-- ============================================

USE nba_insight_db;

-- ── 1. Teams ────────────────────────────────
INSERT INTO teams (name, abbreviation, city, conference, division) VALUES
('Los Angeles Lakers',  'LAL', 'Los Angeles',  'West', 'Pacific'),
('Golden State Warriors','GSW','San Francisco', 'West', 'Pacific'),
('Boston Celtics',      'BOS', 'Boston',        'East', 'Atlantic'),
('Miami Heat',          'MIA', 'Miami',         'East', 'Southeast'),
('Chicago Bulls',       'CHI', 'Chicago',       'East', 'Central');

-- ── 2. Seasons ──────────────────────────────
INSERT INTO seasons (year, type) VALUES
('2020-21', 'Regular'),
('2021-22', 'Regular'),
('2022-23', 'Regular');

-- ── 3. Players ──────────────────────────────
INSERT INTO players (name, team_id) VALUES
('LeBron James',    1),
('Anthony Davis',   1),
('Stephen Curry',   2),
('Klay Thompson',   2),
('Jayson Tatum',    3),
('Jaylen Brown',    3),
('Jimmy Butler',    4),
('Bam Adebayo',     4),
('DeMar DeRozan',   5),
('Zach LaVine',     5);

-- ── 4. Games ────────────────────────────────
INSERT INTO games (game_date, home_team_id, away_team_id, season_id) VALUES
('2021-01-15', 1, 2, 1),
('2021-01-20', 3, 4, 1),
('2021-02-10', 2, 3, 1),
('2022-03-05', 1, 4, 2),
('2022-03-18', 5, 2, 2);

-- ── 5. Player Season Stats ──────────────────
INSERT INTO player_season_stats (player_id, season_id, games_played, points, rebounds, assists, fg_pct, ast_pct) VALUES
-- LeBron James
(1, 1, 45, 25.4, 7.7, 7.8, 51.3, 36.2),
(1, 2, 56, 27.1, 8.2, 7.3, 52.4, 37.1),
(1, 3, 55, 28.9, 8.3, 6.8, 50.0, 34.5),
-- Stephen Curry
(3, 1, 63, 32.0, 5.5, 5.8, 48.2, 26.5),
(3, 2, 64, 29.6, 6.1, 6.3, 47.1, 27.0),
(3, 3, 56, 29.4, 6.1, 6.3, 49.3, 27.8),
-- Jayson Tatum
(5, 1, 64, 23.4, 7.0, 4.4, 45.9, 21.1),
(5, 2, 76, 26.9, 8.0, 4.4, 45.3, 20.4),
(5, 3, 74, 30.1, 8.8, 4.6, 46.6, 21.9),
-- Jimmy Butler
(7, 1, 52, 21.5, 6.7, 7.1, 49.7, 33.4),
(7, 2, 57, 21.4, 5.9, 5.5, 48.0, 28.1),
-- Bam Adebayo
(8, 1, 64, 18.7, 9.0, 5.4, 57.1, 25.3),
(8, 2, 56, 19.1, 10.1, 3.4, 55.6, 17.8),
-- Anthony Davis
(2, 1, 36, 21.8, 7.9, 3.1, 49.1, 15.5),
(2, 2, 40, 23.2, 9.9, 2.9, 53.0, 14.3),
-- Klay Thompson
(4, 3, 69, 18.5, 3.7, 2.4, 43.0, 11.2),
-- Jaylen Brown
(6, 2, 66, 23.6, 6.1, 3.5, 47.3, 16.4),
(6, 3, 67, 26.6, 6.9, 3.5, 49.3, 16.9),
-- DeMar DeRozan
(9, 2, 76, 26.9, 5.0, 4.9, 50.4, 22.0),
-- Zach LaVine
(10, 2, 67, 24.4, 4.6, 4.5, 47.8, 21.3);

-- ── 6. Team Game Stats ──────────────────────
INSERT INTO team_game_stats (team_id, game_id, score, turnovers, fouls) VALUES
(1, 1, 112, 12, 18),
(2, 1, 107, 14, 20),
(3, 2, 118, 10, 16),
(4, 2, 104, 15, 22),
(2, 3, 120, 11, 17);

-- ── 7. Standings ────────────────────────────
INSERT INTO standings (team_id, season_id, wins, losses, streak, conference_rank) VALUES
(1, 1, 42, 30, 'W3', 5),
(2, 1, 39, 33, 'L1', 8),
(3, 2, 51, 31, 'W5', 2),
(4, 2, 53, 29, 'W2', 1),
(5, 2, 46, 36, 'W1', 5);