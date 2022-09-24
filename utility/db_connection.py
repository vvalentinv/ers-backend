from dotenv import dotenv_values
# from psycopg_pool import ConnectionPool
#
config = dotenv_values(".env")
#
# pool = ConnectionPool(
#     'postgresql://' +
#     config.get('user') + ':'
#     + config.get('password') + '@' +
#     config.get('host') + ':' +
#     config.get('port') + '/' +
#     config.get('dbname')
# )
#
# import os
import urllib.parse as up
import psycopg2
#
# up.uses_netloc.append("postgres")
url = up.urlparse(config.get("URL"))
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)