import os
import psycopg2
from flask import Flask

conn = psycopg2.connect(
    host=os.environ.get('DB_HOST', 'postgres'),
    database=os.environ.get('DB_NAME', 'postgres'),
    user=os.environ.get('DB_USER', 'postgres'),
    password=os.environ.get('DB_PASS', 'pass'),
    port=5432
)


def create_table():
    try:
        cur = conn.cursor()
        query = "CREATE TABLE information (name character varying(36) NOT NULL,id SERIAL);"
        data = ()
        cur.execute(query, data)
        conn.commit()
        cur.close()
    except Exception:
        cur.close()
        return {'resp': 'ERR_1'}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    create_table()

    @app.route("/insert/<string:name>")
    def serve_insert(name):
        try:
            cur = conn.cursor()
            query = "INSERT INTO information (name) VALUES (%s);"
            data = (name,)
            cur.execute(query, data)
            conn.commit()
            cur.close()
            return {'resp': 'OK'}
        except Exception:
            cur.close()
            return {'resp': 'ERR'}

    @app.route("/select/<string:name>")
    def serve_select(name):
        try:
            cur = conn.cursor()
            query = "SELECT id FROM information WHERE name=%s;"
            data = (name,)
            cur.execute(query, data)
            result = cur.fetchall()
            cur.close()
            return {'resp': len(result)}
        except Exception:
            cur.close()
            return {'resp': 'ERR'}

    return app
