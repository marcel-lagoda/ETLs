import petl as etl
import psycopg2 as pg
from sqlalchemy import *

cnx = {'dvdrental': "dbname=dvdrental user=postgres host=localhost",
       'etldb': "dbname=etldb user=postgres host=localhost"}

# set connection
source_cnx = pg.connect(cnx['dvdrental'])
target_cnx = pg.connect(cnx['etldb'])
source_cursor = source_cnx.cursor()
target_cursor = target_cnx.cursor()

source_cursor.execute("SELECT table_name\n"
                      "FROM information_schema.columns\n"
                      "WHERE table_schema  = 'public'"
                      "AND table_name IN ('actors')"
                      "GROUP BY 1")

source_tables = source_cursor.fetchall()

for t in source_tables:
    target_cursor.execute("DROP TABLE IF EXISTS %s" % (t[0]))
    source_ds = etl.fromdb(source_cnx, "SELECT * FROM %s" % (t[0]))
    etl.todb(source_ds, target_cnx, t[0], create=True, sample=1000)
