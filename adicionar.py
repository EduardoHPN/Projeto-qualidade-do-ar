import mysql.connector
def adicionar():
    mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "edu28102005",
    database = "projeto1"
    )
    mycursor = mydb.cursor()
    print('\n')
    print('*'*60)
    print('inserir'.center(60))
    print('*'*60)
    while True:
        try:
            ParIna = float(input('Digite a quantidade de particulas inalaveis: '))
            ParInaF = float(input('Digite a quantidade de particulas inalaveis finas: '))
            Ozonio = float(input('Digite a quantidade de ozonio: '))
            MonoCarb = float(input('Digite a quantidade de monoxio de carbono: '))
            DioNitro = float(input('Digite a quantidade de dioxido de nitrogenio: '))
            DioEnx = float(input('Digite a quantidade de dioxido de enxofre: '))
        except:
            print('Digite valores numericos! Tente novamente')
        else:
            if ParIna <0 or ParInaF <0 or Ozonio <0 or MonoCarb<0 or DioNitro<0 or DioEnx<0:
                print('São aceitos apenas valores positivos')
            else:
                n = []
                np = 0
                #particulas inalaveis
                if ParIna >= 0 and ParIna <= 50:
                    n.append(1)
                if ParIna > 50 and ParIna <= 100:
                    n.append(2)
                if ParIna > 100 and ParIna <= 150:
                    n.append(3)
                if ParIna > 150 and ParIna <= 250:
                    n.append(4)
                if ParIna > 250:
                    n.append(5)
                        
                #particulas inalaveis finas
                if ParInaF >= 0 and ParInaF <= 25:
                    n.append(1)
                if ParInaF > 25 and ParInaF <= 50:
                    n.append(2)
                if ParInaF > 50 and ParInaF <= 75:
                    n.append(3)
                if ParInaF > 75 and ParInaF <= 125:
                    n.append(4)
                if ParInaF > 125:
                    n.append(5)

                #ozonio
                if Ozonio >= 0 and Ozonio <= 100:
                    n.append(1)
                if Ozonio > 100 and Ozonio <= 130:
                    n.append(2)
                if Ozonio > 130 and Ozonio <= 160:
                    n.append(3)
                if Ozonio > 160 and Ozonio <= 200:
                    n.append(4)
                if Ozonio > 200:
                    n.append(5)

                #monoxido de carbono
                if MonoCarb >= 0 and MonoCarb <= 9:
                    n.append(1)
                if MonoCarb > 9 and MonoCarb <= 11:
                    n.append(2)
                if MonoCarb > 11 and MonoCarb <= 13:
                    n.append(3)
                if MonoCarb > 13 and MonoCarb <= 15:
                    n.append(4)
                if MonoCarb > 15:
                    n.append(5)

                #dioxido de nitrogenio
                if DioNitro >= 0 and DioNitro <= 200:
                    n.append(1)
                if DioNitro > 200 and DioNitro <= 240:
                    n.append(2)
                if DioNitro > 240 and DioNitro <= 320:
                    n.append(3)
                if DioNitro > 320 and DioNitro <= 1130:
                    n.append(4)
                if DioNitro > 1130:
                    n.append(5)

                #dioxido de enxofre
                if DioEnx >= 0 and DioEnx <= 20:
                    n.append(1)
                if DioEnx > 20 and DioEnx <= 40:
                    n.append(2)
                if DioEnx > 40 and DioEnx <= 365:
                    n.append(3)
                if DioEnx > 365 and DioEnx <= 800:
                    n.append(4)
                if DioEnx > 800:
                    n.append(5)
                        
                for c in n:
                    if c > np:
                        np = c
                print('*'*60)
                print('\n')
                if np == 1:
                    qualidade = 'bom'
                    print('bom')
                if np == 2:
                    qualidade = 'razoavel'
                    print('razoavel: Pessoas de grupos sensíveis\n(crianças, idosos e pessoas com doenças respiratórias e cardiacas)\npodem apresentar sintomas como tosse seca e cansaço.\nA população, em geral, não é afetada. ')
                if np == 3:
                    qualidade = 'ruim'
                    print('ruim: Toda a população pode apresentar sintomas como tosse seca, cansaço,\nardor nos olhos, nariz e garganta. Pessoas de grupos\nsensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)\npodem apresentar efeitos mais sérios na saúde')
                if np == 4:
                    qualidade = 'muito ruim'
                    print('muito ruim: Toda a população pode apresentar agravamento dos \nsintomas como tosse seca, cansaço, ardor nos olhos,\nnariz e garganta e ainda falta de ar e respiração\nofegante. Efeitos ainda mais graves à saúde de\ngrupos sensíveis (crianças, idosos e pessoas com\ndoenças respiratórias e cardíacas).')
                if np == 5:
                    qualidade = 'pessima'
                    print('pessimo: Toda a população pode apresentar sérios riscos de\nmanifestações de doenças respiratórias e\ncardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.')

                ParInaS = str(ParIna)
                ParInaFS = str(ParInaF)
                OzonioS = str(Ozonio)
                MonoCarbS = str(MonoCarb)
                DioNitroS = str(DioNitro)
                DioEnxS = str(DioEnx)


                dados = ParInaS + ',' + ParInaFS + ',' + OzonioS + ',' +MonoCarbS+ ','+DioNitroS+','+DioEnxS+',\''+qualidade+'\')'
                declaracao = """INSERT INTO amostra
                (cod, MP10, MP25,O3,CO,NO2,SO2,qualidade)
                VALUES (default,"""
                sql = declaracao + dados
                '''print(sql)'''
                print('\n')
                try:
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor.close()
                except:
                    print('erro ao inserir no banco de dados')
                else:
                    print('inserido com sucesso')
                return

