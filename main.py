# работа с БД PostgreSQL
# pip install psycopg2

connection = db.connect(host='localhost',
                        port=5432,
                        user='postgres',
                        password='563dneiolubvi',
                        dbname='biblio')

# курсор
cursor = connection.cursor()

query = "SELECT * FROM genre"
cursor.execute(query)  # отпрвка запроса
result = cursor.fetchall() # result = cursor.fetchmany()

print(result[1][0])  # [0] ставим иначе выведет кортежем

# CRUD - для create, update, delete
# connection.commit


# отключаем курсор
cursor.close()

# отключаемся от БД
connection.cliose()
