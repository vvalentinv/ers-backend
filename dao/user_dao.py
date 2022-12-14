from model.user import User
from dotenv import dotenv_values
import psycopg2

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# config = dotenv_values(".env")
# db_name = config.get("dbname")
# db_user = config.get("user")
# db_password = config.get("password")
# port = config.get("port")
# host = config.get("host")


class UserDao:

    def get_all_users(self):
        # with psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port) as conn:
        # with psycopg2.connect(database=db_name, user=db_user, password=db_password, port=port, host=host) as conn:
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_users")
                my_list_of_user_objs = []
                for user in cur:
                    user_id = user[0]
                    username = user[1]
                    password = user[2]
                    first_name = user[3]
                    last_name = user[4]
                    email = user[5]
                    role_id = user[6]
                    my_list_of_user_objs.append(User(user_id, username, password, first_name, last_name, email,
                                                     role_id))

                return my_list_of_user_objs

    def get_user_by_username(self, username):
        # with psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname,
        #                       port=url.port) as conn:
        with conn:
        # with psycopg2.connect(database=db_name, user=db_user, password=db_password, port=port, host=host) as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_users WHERE username = %s;", (username,))
                user = cur.fetchone()
                if user:
                    return User(user[0], user[1], user[2], user[3], user[4], user[5], user[6])
                else:
                    return None
