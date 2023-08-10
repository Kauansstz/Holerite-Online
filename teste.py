import banco

resultado = banco.sql_query(f"""SELECT * FROM tb_login""")

print(resultado)