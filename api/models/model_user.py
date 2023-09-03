import psycopg


class UserConnection():
    connect = None

    def __init__(self):
        try:
            self.connect = psycopg.connect(
                "dbname=database_python_fast_api user=postgres password=admin host=localhost port=5432")
        except psycopg.OperationalError as error:
            print(error)
            self.connect.close()

    def write(self, data):
        with self.connect.cursor() as cursor:
            cursor.execute("""
            INSERT INTO "users"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data)
        self.connect.commit()

    def __def__(selfs):
        selfs.connect.close()
