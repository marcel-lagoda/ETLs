import psycopg2
from secrets import get_secrets


def connect():
    return psycopg2.connect(
        user=get_secrets("postgres_username"),
        password=get_secrets("postgres_db_pwd"),
        host="localhost",
        database="dvdrental"
    )


if __name__ == "__main__":
    try:
        cnx = connect()
        print("\o/")
    except (psycopg2.DatabaseError, psycopg2.OperationalError) as e:
        print(e)
    finally:
        cnx.close()
