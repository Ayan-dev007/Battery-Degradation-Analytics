CREATE TABLE IF NOT EXISTS battery_cycles(
    cycle INTEGER PRIMARY KEY,
    charge_rate REAL,
    discharge_rate REAL,
    temperature REAL,
    capacity_ah REAL,
    health_score REAL
);