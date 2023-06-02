import mysql.connector
def deletar():

    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "edu28102005",
    database = "projeto1"
    )
    cursor = mydb.cursor()
    print('\n')
    print('*'*60)
    print('Deletar Amostra'.center(60))
    print('*'*60)
    
    exibir = ' select * from amostra '
    cursor.execute(exibir)
    linha = cursor.fetchall()
    for i in linha:
        print("cod:" ,i[0], ",MP10:",i[1],",MP25:",i[2],",O3:",i[3],",CO:",i[4],",NO2:",i[5],",SO2:",i[6],",qualidade:",i[7])
    print('\n')
    ex = input('Qual o codigo da amostra que deseja excluir: ')
    consulta = 'select * from amostra where cod = ' +ex
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        print('cod =' ,linha[0])
        print('MP10 =' ,linha[1])
        print('MP25 =' ,linha[2])
        print('O3 =' ,linha[3])
        print('CO =' ,linha[4])
        print('NO2 =' ,linha[5])
        print('SO2 =' ,linha[6])
        print('qualidade =' ,linha[7])
        
    while True:
        print('\n')
        resp = input('deseja realmente excluir esse registro? (S) ou (N): ').upper()
        if resp in ['S','N']:
            break
        else:
            print('Digite apenas (S) ou (N), Tente novamente!: ')
    if resp == 'S':
        sql = 'DELETE FROM AMOSTRA WHERE cod = ' +ex
        try:
            cursor.execute(sql)
            mydb.commit()
            cursor.close()
        except:
            print('Não foi possivel excluir esse registro')
        else:
            print('\n')
            print('sucesso!!')
            return
    else:
        print('\n')
        print('então não iremos excluir!')
        return
