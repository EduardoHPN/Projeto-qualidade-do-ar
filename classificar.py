def classificar():
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
    print('Classificar amostra'.center(60))
    print('*'*60)
    consulta = 'select avg(MP10) from amostra'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        mp10 = float(linha[0])

    consulta = 'select avg(MP25) from amostra'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        mp25 = float(linha[0])

    consulta = 'select avg(O3) from amostra'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        O3 = float(linha[0])

    consulta = 'select avg(CO) from amostra'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        CO = float(linha[0])

    consulta = 'select avg(NO2) from amostra'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        NO2 = float(linha[0])

    consulta = 'select avg(SO2) from amostra'
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        SO2 = float(linha[0])

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

    print('A media dos ares digitados é: ')
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

