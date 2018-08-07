# -*- coding: utf-8 -*-

import pymysql


class Database:

    def __init__(self):
        host = "localhost"
        user = "root"
        password = ""
        database = "app_db"

        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database=database,
                                          cursorclass=pymysql.
                                          cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def user_list(self):
        self.cursor.execute(
            """SELECT *
            FROM users WHERE deleted IS false""")
        result = self.cursor.fetchall()

        return result

    def add_user(self, user_name, status):
        add_user = """INSERT INTO users(user_name,
              status)
              VALUES (%s, %s)"""
        try:
            self.cursor.execute(add_user,
                                (user_name, status))
            self.connection.commit()
        except ValueError:
            raise ValueError
            # self.connection.commit()

    def get_user(self, user_id):
        get_user = """SELECT * FROM users WHERE id = %s
        	AND deleted IS false"""

        try:
            self.cursor.execute(get_user,
                                (user_id))
            result = self.cursor.fetchall()
        except ValueError:
            raise ValueError
        return result

    def edit_user(self, user_name, status, prev_status, user_id):
        edit_user = """UPDATE users set user_name = %s,
        	status = %s, prev_status = %s WHERE id = %s"""
        try:
            self.cursor.execute(edit_user,
                                (user_name,
                                 status,
                                 prev_status,
                                 user_id))
            self.connection.commit()
        except ValueError:
            return ValueError, 500

    def delete_user(self, user_id):
        delete_user = """UPDATE users set deleted = true where id = %s"""
        try:
            self.cursor.execute(delete_user,
                                (user_id))
            self.connection.commit()
        except ValueError:
            return ValueError

    def restore_user(self, user_id):
        delete_user = """UPDATE users set deleted = false where id = %s"""
        try:
            self.cursor.execute(delete_user,
                                (user_id))
            self.connection.commit()
        except ValueError:
            return ValueError
