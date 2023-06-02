def mudar():
    import mysql.connector
    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "edu28102005",
    database = "projeto1"
    )
    cursor = mydb.cursor()
    
    print('\n')
    print('*'*60)
    print('Alterar amostra'.center(60))
    print('*'*60)

    exibir = ' select * from amostra '
    cursor.execute(exibir)
    linha = cursor.fetchall()
    for i in linha:
        print("cod:" ,i[0], ",MP10:",i[1],",MP25:",i[2],",O3:",i[3],",CO:",i[4],",NO2:",i[5],",SO2:",i[6],",qualidade:",i[7])
    print('\n')
    try:
        tipo = input('digite o codigo que voce quer alterar: ')

        consulta = 'select * from amostra where cod = ' +tipo
        cursor.execute(consulta)
        linhas = cursor.fetchall()
    except:
        print('erro no codigo')
    else:
        for linha in linhas:
            print('1 - MP10 =' ,linha[1])
            print('2 - MP25 =' ,linha[2])
            print('3 - O3 =' ,linha[3])
            print('4 - CO =' ,linha[4])
            print('5 - NO2 =' ,linha[5])
            print('6 - SO2 =' ,linha[6])

        while True:
            resp = input('é essa amostra que deseja alterar? (S) ou (N): ').upper()
            if resp in ['S','N']:
                break
            else:
                print('Digite apenas (S) ou (N)')
                print('Tente novamente!!')
        if resp == 'S':
            while True:
                muda = int(input('qual desses campos deseja alterar?: '))
                if muda >=1 and muda <=6:
                    break
                else:
                    print('digite valores entre 1 e 6')
                    print('tente novamente')
            if muda == 1:
                muda = 'MP10'
            elif muda == 2:
                muda = 'MP25'
            elif muda == 3:
                muda = 'O3'
            elif muda == 4:
                muda = 'CO'
            elif muda == 5:
                muda = 'NO2'
            elif muda == 6:
                muda = 'SO2'

            consulta = 'select ' +muda+ ' from amostra where cod = ' +tipo
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            for linha in linhas:
                muda2 = str(linha[0])

            novo = input('digite o novo valor: ')
            sql = 'update amostra set '+muda + ' = '+novo+ ' where cod = ' + tipo
            cursor.execute(sql)
            mydb.commit()

            consulta = 'select * from amostra where cod = ' +tipo
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            for linha in linhas:
                mp10 = linha[1]
                mp25 = linha[2]
                O3 = linha[3]
                CO = linha[4]
                NO2 = linha[5]
                SO2 = linha[6]
            while True:
                n = []
                np = 0
            #particulas inalaveis
                if mp10 >= 0 and mp10 <= 50:
                    n.append(1)
                if mp10 > 50 and mp10 <= 100:
                    n.append(2)
                if mp10 > 100 and mp10 <= 150:
                    n.append(3)
                if mp10 > 150 and mp10 <= 250:
                    n.append(4)
                if mp10 > 250:
                    n.append(5)
                            
                #particulas inalaveis finas
                if mp25 >= 0 and mp25 <= 25:
                    n.append(1)
                if mp25 > 25 and mp25 <= 50:
                    n.append(2)
                if mp25 > 50 and mp25 <= 75:
                    n.append(3)
                if mp25 > 75 and mp25 <= 125:
                    n.append(4)
                if mp25 > 125:
                    n.append(5)

                #ozonio
                if O3 >= 0 and O3 <= 100:
                    n.append(1)
                if O3 > 100 and O3 <= 130:
                    n.append(2)
                if O3 > 130 and O3 <= 160:
                    n.append(3)
                if O3 > 160 and O3 <= 200:
                    n.append(4)
                if O3 > 200:
                    n.append(5)
                #monoxido de carbono
                if CO >= 0 and CO <= 9:
                    n.append(1)
                if CO > 9 and CO <= 11:
                    n.append(2)
                if CO > 11 and CO <= 13:
                    n.append(3)
                if CO > 13 and CO <= 15:
                    n.append(4)
                if CO > 15:
                    n.append(5)

                #dioxido de nitrogenio
                if NO2 >= 0 and NO2 <= 200:
                    n.append(1)
                if NO2 > 200 and NO2 <= 240:
                    n.append(2)
                if NO2 > 240 and NO2 <= 320:
                    n.append(3)
                if NO2 > 320 and NO2 <= 1130:
                    n.append(4)
                if NO2 > 1130:
                    n.append(5)

                #dioxido de enxofre
                if SO2 >= 0 and SO2 <= 20:
                    n.append(1)
                if SO2 > 20 and SO2 <= 40:
                    n.append(2)
                if SO2 > 40 and SO2 <= 365:
                    n.append(3)
                if SO2 > 365 and SO2 <= 800:
                    n.append(4)
                if SO2 > 800:
                    n.append(5)
                            
                for c in n:
                    if c > np:
                        np = c

                print('\n')
                if np == 1:
                    qualidade = 'bom'
                if np == 2:
                    qualidade = 'razoavel'
                if np == 3:
                    qualidade = 'ruim'
                if np == 4:
                    qualidade = 'muito ruim'
                if np == 5:
                    qualidade = 'pessima'
                break
            #mudar a qualidade se necessario
            try:
                sql2 = """update amostra set qualidade = '""" +qualidade+"""' where cod = """ + tipo
                cursor.execute(sql2)
                mydb.commit()
                cursor.close()
                mydb.close()
            except:
                print('erro a atulizar o banco')
            else:
                print('sucesso ao mudar! ')
                return
        else:
            print('então tente novamente')
            return
            



