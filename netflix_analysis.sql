-- Netflix Data Analytics SQL
-- Assumes cleaned data is loaded into a table named netflix.

-- 1. Total titles
SELECT COUNT(*) AS total_titles FROM netflix;

-- 2. Movies vs TV Shows
SELECT type, COUNT(*) AS total_titles
FROM netflix
GROUP BY type
ORDER BY total_titles DESC;

-- 3. Titles by release year
SELECT release_year, COUNT(*) AS total_titles
FROM netflix
GROUP BY release_year
ORDER BY release_year;

-- 4. Top ratings
SELECT rating, COUNT(*) AS total_titles
FROM netflix
WHERE rating <> 'Unknown'
GROUP BY rating
ORDER BY total_titles DESC;

-- 5. Top primary genres
SELECT listed_in_primary AS genre, COUNT(*) AS total_titles
FROM netflix
GROUP BY listed_in_primary
ORDER BY total_titles DESC
LIMIT 10;

-- 6. Top countries
SELECT country_primary AS country, COUNT(*) AS total_titles
FROM netflix
WHERE country_primary <> 'Unknown'
GROUP BY country_primary
ORDER BY total_titles DESC
LIMIT 10;

-- 7. Titles added by year
SELECT date_added_year, COUNT(*) AS titles_added
FROM netflix
WHERE date_added_year IS NOT NULL
GROUP BY date_added_year
ORDER BY date_added_year;

-- 8. Movies with duration over 150 minutes
SELECT title, duration
FROM netflix
WHERE type = 'Movie'
  AND duration_value > 150
ORDER BY duration_value DESC;

-- 9. TV shows with the most seasons
SELECT title, duration_value AS seasons
FROM netflix
WHERE type = 'TV Show'
  AND duration_unit = 'Season'
ORDER BY seasons DESC
LIMIT 10;

-- 10. Content by type and release year
SELECT type, release_year, COUNT(*) AS total_titles
FROM netflix
GROUP BY type, release_year
ORDER BY release_year, type;
