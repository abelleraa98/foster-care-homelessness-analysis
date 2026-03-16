</> SQL

-- Foster Care and Youth Homelessness Analysis
-- National Trends and Youth Outcomes

-- 1. View national trends data
SELECT
    Year,
    [Youth Homeless 18-24],
    [Youth Aging Out]
FROM national_trends
ORDER BY Year;


-- 2. Calculate year-over-year change in youth homelessness
SELECT
    Year,
    [Youth Homeless 18-24],
    [Youth Homeless 18-24]
        - LAG([Youth Homeless 18-24]) OVER (ORDER BY Year) AS Homeless_Change
FROM national_trends
ORDER BY Year;


-- 3. Calculate year-over-year change in youth aging out
SELECT
    Year,
    [Youth Aging Out],
    [Youth Aging Out]
        - LAG([Youth Aging Out]) OVER (ORDER BY Year) AS Aging_Out_Change
FROM national_trends
ORDER BY Year;


-- 4. Compare percent change from first year to last year
SELECT
    MIN(Year) AS Start_Year,
    MAX(Year) AS End_Year,
    MIN([Youth Homeless 18-24]) AS Start_Youth_Homeless,
    MAX([Youth Homeless 18-24]) AS End_Youth_Homeless,
    MIN([Youth Aging Out]) AS Lowest_Youth_Aging_Out,
    MAX([Youth Aging Out]) AS Highest_Youth_Aging_Out
FROM national_trends;


-- 5. View youth outcomes by cohort
SELECT
    Cohort,
    [Educational Attainment],
    [Employment Rate],
    [Homeless Risk],
    [Health Coverage Access]
FROM youth_outcomes;


-- 6. Compare average youth outcomes across cohorts
SELECT
    AVG([Educational Attainment]) AS Avg_Educational_Attainment,
    AVG([Employment Rate]) AS Avg_Employment_Rate,
    AVG([Homeless Risk]) AS Avg_Homeless_Risk,
    AVG([Health Coverage Access]) AS Avg_Health_Coverage_Access
FROM youth_outcomes;


-- 7. Show cohorts ordered by homelessness risk
SELECT
    Cohort,
    [Homeless Risk],
    [Employment Rate],
    [Educational Attainment],
    [Health Coverage Access]
FROM youth_outcomes
ORDER BY [Homeless Risk] DESC;
