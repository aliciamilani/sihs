import urllib.parse as up
import psycopg2

def get_connection(): 
    up.uses_netloc.append("postgres")
    url = up.urlparse("postgres://ypaibyic:Xle0xasKnchcl2axyn2SPd_n16jAanbk@kesavan.db.elephantsql.com/ypaibyic")
    conn = psycopg2.connect(database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    cursor = conn.cursor()

    return conn, cursor

conn, cursor = get_connection()

def insert_climates(climate_type):
    cursor.execute(f''' INSERT INTO climates (
                            climate_type)
                        VALUES(
                            '{climate_type}'
                        )''')


def insert_users(user_name, user_email, user_password):
    cursor.execute(f''' INSERT INTO users (
                            user_name,
                            user_email,
                            user_password)
                        VALUES(
                            '{user_name}',
                            '{user_email}',
                            '{user_password}'
                        )''')


def insert_historics(history_device, history_action, history_date, history_time, 
                    history_humidity, history_temperature, history_climate_id, history_user_id):
    cursor.execute(f''' INSERT INTO historics (
                            history_device,
                            history_action,
                            history_date,
                            history_time,
                            history_humidity,
                            history_temperature,
                            history_climate_id,
                            history_user_id)
                        VALUES(
                            '{history_device}',
                            '{history_action}',
                            '{history_date}', 
                            '{history_time}',
                            {history_humidity},
                            {history_temperature},
                            {history_climate_id},
                            {history_user_id}
                        )''')

def search_climate (climate):
    cursor.execute(f''' SELECT climate_id FROM climates WHERE climate_type = '{climate}' ''')
    return cursor.fetchall()[0][0]

def commit_close():
    conn.commit()
    cursor.close()
    conn.close()
    

# import datetime
# current = datetime.datetime.now() 

# insert_climates("Clouds")
# insert_users("Vanessa", "vanessadcamara@gmail.com", "654321")
# insert_historics("Relay", "On", current.date(), current.time(), 94, 26, 1, 1)
# insert_climates("Thunderstorm")
# insert_climates("Drizzle")
# insert_climates("Rain")
# insert_climates("Squall")
# insert_climates("Snow")
# insert_climates("Mist")
# insert_climates("Smoke")
# insert_climates("Haze")
# insert_climates("Dust")
# insert_climates("Fog")
# insert_climates("Sand")
# insert_climates("Dust")
# insert_climates("Ash")
# insert_climates("Squall")
# insert_climates("Tornado")
# insert_climates("Clear")


