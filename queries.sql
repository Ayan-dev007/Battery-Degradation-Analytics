-- Retrieve the first 10 battery cycle records
SELECT * FROM battery_cycles ORDER BY cycle LIMIT 10;

-- Calculate average capacity in groups of 10 cycles
SELECT (cycle -1) / 10 AS grp, AVG(capacity_ah) AS avg_capacity
FROM battery_cycles
GROUP BY grp;

-- Calculate capacity change from the previous cycle
SELECT cycle, capacity_ah,
capacity_ah - LAG(capacity_ah) OVER (ORDER BY cycle) AS capacity_change
FROM battery_cycles;

-- Find cycles with temperatures above 40 degrees
SELECT * FROM battery_cycles
WHERE temperature >40;

-- Retrieve the five cycles with the lowest health scores
SELECT * FROM battery_cycles
ORDER BY health_score ASC LIMIT 5;