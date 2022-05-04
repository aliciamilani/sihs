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



