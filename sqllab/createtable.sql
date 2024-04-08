DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  longitude real,
  mag real,
  dmin real, 
  ms real,
  id text,
  place text,
  status text
);
