"""Luis Angel Velazquez Jimenez"""
"""NO:1215100974"""
"""GITI9072-e"""
import psycopg2
from config import config


def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_vendors()
    (1, '3M Corp')
    (2, 'AKM Semiconductor Inc.')
    (3, 'Asahi Glass Co Ltd.')
    (4, 'Daikin Industries Ltd.')
    (5, 'Dynacast International Inc.')
    (6, 'Foster Electric Co. Ltd.')
    (7, 'Murata Manufacturing Co. Ltd.')

    get_parts()
    (4, 'Antenna')
    (5, 'Home Button')
    (6, 'LTE Modem')
    (1, 'SIM Tray')
    (2, 'Speaker')
    (3, 'Vibrator')