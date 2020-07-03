import os
import psycopg2

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
conn = psycopg2.connenct('DATABASE_URL', sslmode = 'require')
SQLALCHEMY_DATABASE_URI_2 = os.environ.get('HEROKU_POSTGRESQL_MAUVE_URL')
conn2 = psycopg2.connenct('HEROKU_POSTGRESQL_MAUVE_URL', sslmode = 'require')
SQLALCHEMY_DATABASE_URI_3 = os.environ.get('HEROKU_POSTGRESQL_ONYX_URL')
conn2 = psycopg2.connenct('HEROKU_POSTGRESQL_ONYX_URL', sslmode = 'require')
SQLALCHEMY_TRACK_MODIFICATIONS = False
