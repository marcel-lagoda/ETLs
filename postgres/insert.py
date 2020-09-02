import psycopg2 as pg
from secrets import get_secrets


def connect():
    cnx = pg.connect(
        user=get_secrets("postgres_username"),
        password=get_secrets("postgres_db_pwd"),
        host="localhost",
        database="testing")

    cnx.set_session(autocommit=True)
    return cnx


def data():
    customers = \
        """
        insert into customers(first_name, last_name)
        values(%s, %s);   
        """
    cst1 = ("Iron", "Man")
    cst2 = ("Spider", "Man")




if __name__ == "__main__":
