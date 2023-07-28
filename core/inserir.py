import banco


def segundo(nickname,email,log,password):
      banco.sql_inserir(f"""INSERT INTO listas_tabelas_jogos
                        (nome, 
                         email, 
                         login, 
                         senha) 
                         VALUES('{nickname}'
                                ,'{email}', 
                                {log},
                                {password} )""")

