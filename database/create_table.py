from connection import get_connection

conn, cursor = get_connection()


cursor.execute('''CREATE TABLE IF NOT EXISTS climates (
                    climate_id smallserial PRIMARY KEY,
                    climate_type VARCHAR(16) NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id smallserial PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    user_email VARCHAR(100) NOT NULL,
                    user_password VARCHAR(100) NOT NULL
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS historics (
                    history_id smallserial PRIMARY KEY,
                    history_device VARCHAR(50) NOT NULL,
                    history_action VARCHAR(3) NOT NULL,
                    history_date date NOT NULL,
                    history_time time NOT NULL,
                    history_humidity SMALLINT NOT NULL,
                    history_temperature SMALLINT NOT NULL,
                    history_climate_id SMALLINT NOT NULL,
                    history_user_id SMALLINT NOT NULL,
                    FOREIGN KEY (history_climate_id) REFERENCES climates (climate_id),
                    FOREIGN KEY (history_user_id) REFERENCES users (user_id)
                )''')

conn.commit()
cursor.close()
conn.close()