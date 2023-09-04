import database.banco as banco

resultado = banco.sql_query(f"""SELECT * FROM tb_login""")

print(resultado)