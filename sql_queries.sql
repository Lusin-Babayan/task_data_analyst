
--data were imported into a PostgreSQL database
--find out people's tendention to bet more if they lose or if they win
SELECT COUNT("PlayerID") FILTER(WHERE "Net Amount" < 0 AND prev_net_amount IS NOT NULL AND dr >= 2) as bet_if_lose,
COUNT("PlayerID") FILTER(WHERE "Net Amount" = 0 AND prev_net_amount IS NOT NULL AND dr >= 2) as bet_if_equal,
COUNT("PlayerID") FILTER(WHERE "Net Amount" > 0 AND prev_net_amount IS NOT NULL AND dr >= 2) as bet_if_win
FROM (
SELECT
    "PlayerID",
    "Date",
		"Hour",
		"Bet Amount",
		"Win Amount",
    "Net Amount",
    LAG("Net Amount") OVER (PARTITION BY "PlayerID" ORDER BY "Date", "Hour") AS prev_net_amount,
		"dense_rank"() OVER (PARTITION BY "PlayerID" ORDER BY "Date", "Hour") as dr
FROM
    task_data_analyst_processed
ORDER BY
    "PlayerID", "Date", "Hour") as res;



--find out company's average daily income per player
SELECT (SUM("Bet Amount" - "Win Amount")) / COUNT(DISTINCT "PlayerID") / COUNT(DISTINCT "Date") as avg_daily_income FROM task_data_analyst_processed;