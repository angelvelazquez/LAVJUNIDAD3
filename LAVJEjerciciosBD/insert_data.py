"""Luis Angel Velazquez Jimenez"""
"""NO:1215100974"""
"""GITI9072-e"""
import psycopg2
from config import config


def insert_vendor(vendor_name):
    """Insert a new vendor into the vendors table"""
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;"""
    connection = None
    vendor_id = None
    try:
        # red database configuration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the insert statement
        cursor.execute(sql, (vendor_name,))
        # get the generated id black
        vendor_id = cursor.fetchone()[0]
        # commit the changes to the database
        connection.commit()
        cursor.close()
    except(Exception, psycopg2. DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return vendor_id


def insert_vendor_list(vendor_list):
    """insert multiples vendors into vendor table"""
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
    connection = None
    try:
        # read database configuration
        params = config()
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        cursor.executemany(sql, vendor_list)
        # execute the insert statement
        connection.commit()
        # close communication with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    # insert one vendor
    # print(insert_vendor('3M Co.'))
    insert_vendor_list([('AKM Semiconductor Inc',),
                   ('Asahi Glass Go. Ltd.',),
                   ('Aiking International Inc.',),
                   ('Dynacast International Inc.',),
                   ('Foster Electric Co. Ltd',),
                   ('Maruta Manufacturing Co. Ltd.',)])
