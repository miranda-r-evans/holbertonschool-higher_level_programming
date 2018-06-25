-- lists number of each score
SELECT score, COUNT(*) as number FROM second_table GROUP BY score;
