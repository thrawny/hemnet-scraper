SELECT hemnet_id, COUNT(hemnet_id) as count FROM hemnet_items GROUP BY hemnet_id ORDER BY count DESC LIMIT 5;

SELECT DISTINCT(COUNT(hemnet_id)) FROM hemnet_items;

SELECT * FROM hemnet_items ORDER BY sold_date DESC LIMIT 20;


-- Brokers with same name but different emails.
SELECT DISTINCT ON (h1.broker_email)
  h1.broker_email,
  h1.broker_name,
  h1.broker_phone,
  h1.url
FROM hemnet_items h1
  INNER JOIN hemnet_items h2 ON h1.broker_name = h2.broker_name
WHERE h1.broker_email != h2.broker_email;


-- Top seller
SELECT
  broker_email,
  sum(price) AS total
FROM hemnet_items
GROUP BY broker_email
ORDER BY total DESC;

-- Top objects sold
SELECT
  broker_email,
  count(broker_email) AS objects_sold,
  sum(price)          AS total
FROM hemnet_items
WHERE geographic_area LIKE '%Göteborg%' AND sold_date > '2016-01-01'
GROUP BY broker_email
ORDER BY objects_sold DESC;

-- Rooms and area
SELECT broker_email, sum(price) AS total FROM hemnet_items
WHERE rooms BETWEEN 2 AND 3 AND geographic_area LIKE '%Borlänge%'
GROUP BY broker_email ORDER BY total DESC;

SELECT * FROM hemnet_items
WHERE rooms BETWEEN 2 AND 3 AND geographic_area LIKE '%Skräddarbacken%';

SELECT url FROM hemnet_items WHERE broker_email = '';

SELECT COUNT(*), SUM(price) FROM hemnet_items WHERE broker_email = '';


SELECT AVG(price_per_square_meter)
FROM hemnet_items
WHERE hemnet_items.address LIKE '%Andra Långgatan 28%' AND sold_date > '2012-01-01' AND hemnet_items.geographic_area LIKE '%Göteborg%';

SELECT * FROM hemnet_items WHERE geographic_area LIKE '%Göteborg%';
SELECT COUNT(*) FROM hemnet_items WHERE geographic_area LIKE '%Stockholm%';
SELECT COUNT(*) FROM hemnet_items;



SELECT DISTINCT type FROM hemnet_items;
