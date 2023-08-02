import cx_Oracle
def sql_query(sql):
    # create the connection
    dsn     = cx_Oracle.makedsn('localhost', 
                                1521, 
                                service_name = 'XEPDB1')

    conn    = cx_Oracle.connect(user     = 'system', 
                                password = 'kauan',  
                                dsn      = dsn)

    cursor  = conn.cursor()
    cursor.execute(sql)
    result  = cursor.fetchall()
    
    # Close the connection
    cursor.close()
    conn.close()

        
    return result

def sql_inserir(sql):
    # create the connection
    dsn     = cx_Oracle.makedsn('localhost', 
                                1521, 
                                service_name = 'XEPDB1')

    conn    = cx_Oracle.connect(user     = 'system', 
                                password = 'kauan',  
                                dsn      = dsn)

    cursor  = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    
    # Close the connection
    cursor.close()
    conn.close()