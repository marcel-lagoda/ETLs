import psycopg2
from secrets import get_secrets


def connect():
    cnx = psycopg2.connect(
        user=get_secrets("postgres_username"),
        password=get_secrets("postgres_db_pwd"),
        host="localhost",
        database="testing",
    )

    cnx.set_session(autocommit=True)
    return cnx


create_customers_query = \
    """
    create table customers (
    customer_id serial,
    first_name varchar(45) NOT NULL,
    last_name varchar(45) NOT NULL,
    last_update timestamp default now() not null,
    constraint customer_pkey primary key(customer_id)
    );
    """

create_orders_query = \
    """CREATE TABLE orders (
    order_id smallint,
    customer_id smallint not null,
    order_date timestamp default now() not null,
    description text NOT NULL,
    constraint order_pkey primary key (order_id),
    constraint customer_fkey foreign key(customer_id) references customers(customer_id)
    );"""

create_order_details_query = \
    """create table orderDetails (
    order_id serial,
    product_id int not null,
    unit_price decimal(5, 2) not null,
    quantity int,
    discount decimal(3,2),
    constraint product_order_pkey primary key(product_id, order_id),
    constraint product_order_order_id_fkey foreign key(order_id) references products(product_id)
    match simple on update cascade on delete restrict,
    constraint order_product_order_id_fkey foreign key(product_id) references orders(order_id)
    match simple on update cascade on delete restrict 
    );
    """

create_products_query = \
    """
    create table products (
    product_id serial,
    product_name varchar(44) not null,
    supplier_id int not null,
    unit_price decimal(4,2) not null,
    constraint product_pkey primary key(product_id)
    );
    """


def execute(cursor, sql):
    try:
        cursor.execute(sql)
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as e:
        print(e)


if __name__ == "__main__":
    cnx = connect()
    cursor = cnx.cursor()
    try:
        cursor.execute(create_customers_query)
        cursor.execute(create_orders_query)
        cursor.execute(create_products_query)
        cursor.execute(create_order_details_query)
        print('ok')
    except(psycopg2.OperationalError, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()
