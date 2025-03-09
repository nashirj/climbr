# Data dump
This is a dump of the data in the heroku db on 03-08-2025. The file format is PostgreSQL custom database dump.

Use the pg_restore command to restore it:

createdb climbr

If you see an error like role "nashir" does not exist, you need to create it first:
sudo -u postgres createuser -s nashir

If the file is a custom format dump, use pg_restore instead of psql:
pg_restore --verbose --clean --no-owner --dbname=climbr 606cee26-db39-4737-9eda-c6a62c31d2c7

Connect to the database and check if the tables are restored:
psql climbr
\dt  -- List tables
SELECT * FROM some_table LIMIT 10;
