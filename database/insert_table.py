from connection import get_connection

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

# import datetime
# current = datetime.datetime.now() 

# insert_climates("Clouds")
# insert_users("Anna", "aliciamilani92@gmail.com", "123456")
# insert_historics("Relay", "On", current.date(), current.time(), 
#                     94, 26, 1, 1)


# conn.commit()
# cursor.close()
# conn.close()