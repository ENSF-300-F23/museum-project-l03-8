-- #01: Show all tables and explain how they are related to one another (keys, triggers, etc.)
SELECT
  TABLE_NAME, COLUMN_NAME, DATA_TYPE, COLUMN_KEY
FROM
  INFORMATION_SCHEMA.COLUMNS
WHERE
  TABLE_SCHEMA IN ('ARTMUSEUM');
-- 2) A basic retrieval query
  SELECT * FROM ARTIST;

-- 3) A retrieval query with ordered results
SELECT * FROM ART_OBJECT ORDER BY Year;

-- 4) A nested retrieval query
SELECT * FROM EXHIBITION WHERE Name IN (SELECT Exhibition FROM ART_OBJECT);

-- 5) A retrieval query using joined tables
SELECT ART_OBJECT.Title, ARTIST.Name
FROM ART_OBJECT
JOIN ARTIST ON ART_OBJECT.Artist = ARTIST.Name;

-- 6) An update operation with any necessary triggers
UPDATE ARTIST SET DateBorn = '1500-01-01' WHERE Name = 'Anonymous';

-- 7) A deletion operation with any necessary triggers
DELETE FROM ARTIST WHERE Name = 'Anonymous';