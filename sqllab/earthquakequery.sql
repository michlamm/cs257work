— Find all earthquake magnitudes that are less than 6 and order by descending order
SELECT * FROM earthquakes WHERE mag>6 ORDER BY mag DESC;


— Adds all the seconds from all earthquakes together
SELECT SUM(ms) FROM earthquakes;

— Selects the earthquakes where their status is not reviewed but automatic.
SELECT * FROM earthquakes  WHERE NOT status = 'reviewed';
