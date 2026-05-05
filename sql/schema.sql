-- ============================================
-- NBA Game and Player Performance Insight System
-- Database Schema
-- ============================================

CREATE DATABASE IF NOT EXISTS nba_insight_db;
USE nba_insight_db;

-- ── 1. Teams ────────────────────────────────
CREATE TABLE IF NOT EXISTS teams (
    team_id       INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    abbreviation  VARCHAR(10),
    city          VARCHAR(100),
    conference    VARCHAR(20),
    division      VARCHAR(50)
);

-- ── 2. Seasons ──────────────────────────────
CREATE TABLE IF NOT EXISTS seasons (
    season_id   INT AUTO_INCREMENT PRIMARY KEY,
    year        VARCHAR(10) NOT NULL,
    type        ENUM('Regular','Playoff') DEFAULT 'Regular',
    start_date  DATE,
    end_date    DATE
);

-- ── 3. Players ──────────────────────────────
CREATE TABLE IF NOT EXISTS players (
    player_id   INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(150) NOT NULL,
    team_id     INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- ── 4. Games ────────────────────────────────
CREATE TABLE IF NOT EXISTS games (
    game_id      INT AUTO_INCREMENT PRIMARY KEY,
    game_date    DATE NOT NULL,
    home_team_id INT,
    away_team_id INT,
    season_id    INT,
    venue        VARCHAR(150),
    FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams(team_id),
    FOREIGN KEY (season_id)    REFERENCES seasons(season_id)
);

-- ── 5. Player Season Stats ──────────────────
CREATE TABLE IF NOT EXISTS player_season_stats (
    stat_id      INT AUTO_INCREMENT PRIMARY KEY,
    player_id    INT NOT NULL,
    season_id    INT,
    games_played INT DEFAULT 0,
    points       DECIMAL(5,2) DEFAULT 0,
    rebounds     DECIMAL(5,2) DEFAULT 0,
    assists      DECIMAL(5,2) DEFAULT 0,
    fg_pct       DECIMAL(5,2),
    ast_pct      DECIMAL(5,2),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);

-- ── 6. Team Game Stats ──────────────────────
CREATE TABLE IF NOT EXISTS team_game_stats (
    tstat_id   INT AUTO_INCREMENT PRIMARY KEY,
    team_id    INT NOT NULL,
    game_id    INT NOT NULL,
    score      INT DEFAULT 0,
    turnovers  INT DEFAULT 0,
    fouls      INT DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- ── 7. Standings ────────────────────────────
CREATE TABLE IF NOT EXISTS standings (
    standing_id     INT AUTO_INCREMENT PRIMARY KEY,
    team_id         INT NOT NULL,
    season_id       INT NOT NULL,
    wins            INT DEFAULT 0,
    losses          INT DEFAULT 0,
    streak          VARCHAR(20),
    conference_rank INT,
    FOREIGN KEY (team_id)   REFERENCES teams(team_id),
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);