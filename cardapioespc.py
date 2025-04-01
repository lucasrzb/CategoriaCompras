#Espero que goste e teste / provavelmente vai encontrar bugs ou não, porem sou dev iniciante
#A ideia final foi transformar o Cardapio em varias categorias de produtos, frutas, items como se fosse você comprando no mercado
#Futuramente irei atualizar e adicionar coisas novas porem a versão 2.0 será a ultima versão desse projeto, fiz varias versões para testar o versionamento GitHub, assim agregando a minha experiencia!.




tipodesanduiche = str
vermelho = "\033[31m"
verde = "\033[32m"
azul = "\033[34m"
amarelo = "\033[33m"
resetar = "\033[0m"
item = float
banana = str
fruta = str

#DEF EM 30/03/2025
def obter_saldo_valido(): # so vai funcionar na ocasião do saldo <= 0
    while True:
        saldo = float(input(f'{azul}Digite o saldo desejado{resetar}: '))
        if saldo <= 0:
            print(f'{vermelho}Digite um saldo maior que 0{resetar}')
        else:
            return saldo #retorna quando saldo for valido
saldo = obter_saldo_valido()


while True: #lopp inicio


    print(f'{azul}Categoria Menu Inicial: frutas , liquidos, carne, sanduiche, salgado{resetar}')
    print(f'{vermelho}Para sair digite: sair{resetar}')
    print(f'{amarelo}Saldo atual de R${saldo:.2f}{resetar}')
    comida = input(f'{azul}Digite uma comida do cardápio ou outro comando:{resetar} ')


    if comida.lower() == 'saldo':
        print(f'Seu Saldo atual e de {saldo:.2f}')
        if comida == 'sair':
            print(f'{vermelho}Voce saiu{resetar}')
            break #saida de loop
#30/03/2025
    if comida.lower() == 'frutas':
        print('Você é fitness?')
        print(f'{amarelo}Confira as frutas: Abacaxi, Banana, Caju, Coco, Maça, Abacate{resetar} ')
        fruta = str(input(f'{azul}Deseja comprar qual fruta?{resetar}: '))
        if fruta.lower() == 'Abacaxi': #.lower não estava funcionando então fiz gambiarra
            abacaxix = int(input(f'{amarelo}Deseja quantas {fruta}{resetar}?: '))
            valor = 5.50
            calculo = valor * abacaxix
            abacaxi = input(f'''{amarelo}Deseja comprar {fruta} por R${valor}{resetar}
                        [0] {verde}Sim{resetar}
                        [1] {vermelho}Não{resetar}
                        ''')
            if abacaxi == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {fruta} por {calculo}{resetar}')
                elif saldo < item: #para caso não tenha dinheiro
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif abacaxi == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif fruta.lower() == 'Banana':
            quantidade = int(input(f'{amarelo}Deseja quantas bananas{resetar}?: '))
            valor = 0.99 * quantidade
            banana = input(f'''{amarelo}Deseja comprar {comida} por R${valor}{resetar}
                        [0] {verde}Sim{resetar}
                        [1] {vermelho}Não{resetar} ''')
            if banana == '0':
                preco = 0.99
                if saldo >= preco:
                    calculo = preco * quantidade
                    saldo -= calculo
                    print(f'{verde}Você comprou {fruta} por R${calculo}{resetar}')
                elif saldo < preco:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif banana == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif fruta.lower() == 'Caju':
            quantidade =  int(input(f'{amarelo}Deseja quantas {fruta}{resetar}?: '))
            preco = 0.99 * quantidade
            caju = input(f'''{amarelo}Deseja comprar {fruta} por R${preco}{resetar}
                                [0] {verde}Sim{resetar}
                                [1] {vermelho}Não{resetar}: ''')
            if caju == '0':
                if saldo >= preco:
                    calculo = preco * quantidade
                    saldo -= calculo
                    print(f'{verde}Você comprou {fruta} por R${calculo}{resetar}')
                elif saldo < preco:
                    print(f'{vermelho}Você não tem saldo suficiente{resetar}')
            elif caju == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif fruta.lower() == 'Coco':
            coco = int(input(f'Quantos {fruta} deseja?: '))
            valor = 1.99
            calculo = coco * valor
            coco = input(f'''{amarelo}Deseja comprar {fruta} por R${calculo}{resetar}
                         [0] {verde}Sim{resetar}
                         [1] {vermelho}Não{resetar}: ''')
            if coco == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {fruta} por {calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif coco == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif fruta.lower() == 'Abacate':
            abacate = int(input(f'{amarelo}Quantos abacate deseja?{resetar}: '))
            valor = 3.70
            calculo = abacate * valor
            input(f'''{verde}Deseja comprar {fruta} por R${calculo}{resetar}
                       [0] {verde}Sim{resetar}
                       [1] {vermelho}Não{resetar}: ''')
            if saldo >= calculo:
                saldo -= calculo
                print(f'{verde}Você comprou {fruta} por R${calculo}{resetar}')
            elif saldo < calculo:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif fruta.lower() == 'Maça':
            maca = int(input(f'{amarelo}Deseja quantas {fruta}{resetar}:? '))
            valor = 0.99
            calculo = maca * valor
            macax = input(f'''{amarelo}Deseja comprar {fruta} por R${calculo}{resetar}
                           [0] {verde}Sim{resetar}
                           [1] {vermelho}Não{resetar}                   
                          ''')
            if macax == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {fruta} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif macax == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')

                #NOVA CATEGORIA EM BAIXO

    elif comida.lower() == 'liquidos':
        print(f'{amarelo}Seção de líquidos: Leite, Coca-Cola, Kuat, Sprite, Pepsi, Guarana, Mineiro, Baré{resetar}')
        liquidos = str(input(f'{azul}Qual líquido deseja comprar?{resetar}: '))
        if liquidos.lower() == 'Leite':
            leite = int(input(f'Deseja quantos {liquidos}?: '))
            valor = 7.5
            calculoy = valor * leite
            leitex= input(f'''{amarelo}Deseja comprar {liquidos} por R${calculoy}{resetar}?: 
                                [0] {verde}Sim{resetar}
                                [1] {vermelho}Não{resetar}: ''')
            if leitex == '0':
                if saldo >= calculoy:
                    saldo -= calculoy
                    print(f'{verde}Você comprou {liquidos} por R${calculoy}{resetar}')
                elif saldo < calculoy:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif leitex == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif liquidos.lower() == 'coca-cola':
            print('Somente temos de 2lt')
            coca = int(input(f'{vermelho}Deseja quantas {liquidos}?{resetar}: '))
            valor = 8.99
            calculo = coca * valor
            cocax = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}{resetar}?
                                [0] {verde}Sim{resetar}            
                                [1] {vermelho}Não{resetar}:''')
            if cocax == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por {calculo}{resetar}')
            elif saldo < calculo:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif cocax == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif liquidos.lower() == 'Kuat':
            quantidade = int(input(f'{amarelo}Deseja quantas {liquidos}?{resetar}: '))
            valor = 5.99
            calculo = valor * quantidade
            kuat = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}{resetar}?  
                                       [0] {verde}Sim{resetar} 
                                       [1] {vermelho}Não{resetar}:  ''')
            if kuat == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif kuat == '1':
                print('Você voltou ao menu')
        elif liquidos.lower() == 'Sprite':
            print('Temos somente sprite de 1lt')
            quantidade = int(input(f'{amarelo}Deseja quantas {liquidos}?{resetar}: '))
            valor = 6.99
            calculo = valor * quantidade
            sprite = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}{resetar}?
                                    [0] {verde}Sim{resetar}
                                    [1] {vermelho}Não{resetar}: ''')
            if sprite == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif sprite == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif liquidos.lower() == 'Pepsi':
            quantidade = int(input(f'{amarelo}Deseja quantos {liquidos}{resetar}?: '))
            valor = 7.99
            calculo = valor * quantidade
            pepsi = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}{resetar}?
                                [0] {verde}Sim{resetar}
                                [1] {vermelho}Não{resetar}: ''')
            if pepsi == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif pepsi == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif liquidos.lower() == 'Guarana':
            quantidade = int(input(f'{amarelo}Deseja quantos {liquidos}?{resetar}: '))
            valor = 8.99
            calculo = valor * quantidade
            guarana = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}{resetar}?: 
                                [0] {verde}Sim{resetar}
                                [1] {vermelho}Não{resetar}: ''')
            if guarana == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif guarana == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif liquidos.lower() == 'Mineiro':
            quantidade = int(input(f'{amarelo}Deseja quantos {liquidos}?{resetar}: '))
            valor = 6.99
            calculo = valor * quantidade
            mineiro = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}?{resetar}: 
                                    [0] {verde}Sim{resetar}
                                    [1] {vermelho}Não{resetar}: ''')
            if mineiro == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif mineiro == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif liquidos.lower() == 'Baré':
            quantidade = int(input(f'{amarelo}Deseja quantos {liquidos}?{resetar}: '))
            valor = 5.99
            calculo = valor * quantidade
            bare = input(f'''{amarelo}Deseja comprar {liquidos} por R${calculo}{resetar}?: 
                                       [0] {verde}Sim{resetar}
                                       [1] {vermelho}Não{resetar}: ''')
            if bare == '0':
                if saldo >= calculo:
                    saldo -= calculo
                    print(f'{verde}Você comprou {liquidos} por R${calculo}{resetar}')
                elif saldo < calculo:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif bare == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')

            #NOVA CATEGORIA

    elif comida == 'sanduiche':
        print('sanduiche iche iche meme maldito')
        print('Cardarpio Sanduiche: X-Salada, X-Bacon, X-Especial, X-Tudo, X-Mirage')
        tipodesanduiche = input('Digite um tipo de sanduiche: ')
    if tipodesanduiche == 'X-Salada':
        print('Alface, Pão de hambuguer, tomate, alface')
        xsalada = input(f'''Deseja comprar X-Salada por R$14.00?.. 
                          [0] {verde}Sim{resetar}
                          [1] {vermelho}Não{resetar}: ''')
        if xsalada == '0':
            item = 14.00
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {tipodesanduiche} por R${item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif xsalada == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif tipodesanduiche == 'X-Bacon':
        print('Pão de Hambuguer, tomate, bacon, mussarela, presunto')
        xbacon = input(f'''Deseja comprar {tipodesanduiche} por R$23.00?.
                          [0] {verde}Sim{resetar} 
                          [1] {vermelho}Não{resetar}: ''')
        if xbacon == '0':
            item = 23.00
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {tipodesanduiche} por R${item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif xbacon == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif tipodesanduiche == 'X-Especial':
        print('Pão de Hambuguer, tomate, carne de hambuguer, ovo')
        xespecial = input(f'''Deseja comprar {tipodesanduiche} por R$21.00?.
                          [0] {verde}Sim{resetar} 
                          [1] {vermelho}Não{resetar}: ''')
        if xespecial == '0':
            item = 21.00
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {tipodesanduiche} por R${item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif xespecial == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif tipodesanduiche == 'X-Tudo':
        print("Pão de Hambuguer, tomate, carne de hambuguer, ovo, alface, presunto, mussarela, bacon")
        xtudo = input(f'''Deseja comprar {tipodesanduiche} por R$32.00?.
                              [0] {verde}Sim{resetar}
                              [1] {vermelho}Não{resetar}: ''')
        if xtudo == '0':
            item = 32.00
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {tipodesanduiche} por R${item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif xtudo == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif tipodesanduiche == 'X-Mirage':
        print('Pão de Hambuguer, tomate, salcicha, presunto, mussarela')
        xmirage = input(f'''Deseja comprar {tipodesanduiche} por R$19.00?. 
                              [0] {verde}Sim{resetar} 
                              [1] {vermelho}Não{resetar}: ''')
        if xmirage == '0':
            item = 19.00
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {tipodesanduiche} por {item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif xmirage == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif comida == 'salgado':
        print('Cardapio Salgados: americano, pastel, coxinha, bolinha de queijo, empada, esfiha, enroladinho')
        tipodesalgado = input('Digite o seu salgado preferido: ')
        if tipodesalgado == 'americano':
            print('Queijo e persunto sempre será a melhor combinação')
            americano = input(f'''Deseja comprar {tipodesalgado} por R$3.5?. 
                              [0] {verde}Sim{resetar}
                              [1] {vermelho}Não?{resetar}: ''')
            if americano == '0':
                item = 3.50
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif americano == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif tipodesalgado == 'enroladinho':
            print('Uma delicia porem demora pra digerir')
            enroladinho = input(f'''Deseja comprar {tipodesalgado} por R$2.50?. 
                           [0] {verde}Sim{resetar}
                           [1] {vermelho}Não{resetar}: ''')
            if enroladinho == '0':
                item = 2.50
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif enroladinho == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')

        elif tipodesalgado == 'pastel':
            print('Ir a feira as 6:00am e comprar pastel e tão satisfatorio')
            pastel = input(f'''Deseja comprar {tipodesalgado} por R$7.99?. 
                           [0] {verde}Sim{resetar}
                           [1] {vermelho}Não{resetar}: ''')
            if pastel == '0':
                item = 7.99
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif pastel == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')

        elif tipodesalgado == 'coxinha':
            print('Comedor de coxas de galinha so que em forma de massa')
            coxinha = input(f'''Deseja comprar {tipodesalgado} por R$4.5?.
                           [0] {verde}Sim{resetar} 
                           [1] {vermelho}Não:{resetar} ''')
            if coxinha == '0':
                item = 4.50
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif coxinha == '1':
                print('Você voltou ao menu')
        elif tipodesalgado == 'bolinha de queijo':
            print('So a bolinha e 3,50 cada imagina com queijo')
            bolinha = input(f'''Deseja comprar {tipodesalgado} por R$2.5?
                           [0] {verde}Sim{resetar}
                           [1] {vermelho}Não:{resetar}: ''')
            if bolinha == '0':
                item = 2.50
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif bolinha == '1':
                print('Você voltou ao menu')
        elif tipodesalgado == 'empada':
            print('Massa podre não coma isso')
            empada = input(f'''Deseja comprar {tipodesalgado} por R$5.0?.
                           [0] {verde}Sim{resetar}
                           [1] {vermelho}Não:{resetar}: ''')

            if empada == '0':
                item = 4.99
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
            elif empada == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')
        elif tipodesalgado == 'esfiha':
            print('Pizza pequena so que com outro nome')
            esfiha = input(f'''Deseja comprar {tipodesalgado} por R$6.0?.
                           [0] {verde}Sim{resetar} 
                           [1] {vermelho}Não:{resetar}: ''')
            if esfiha == '0':
                item = 5.99
                if saldo >= item:
                    saldo -= item
                    print(f'Você comprou {tipodesalgado} por R${item}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif esfiha == '1':
                print(f'{vermelho}Você voltou ao menu{resetar}')

    elif comida == 'hellow world':
        print(f'{verde}certeza que e um verdadeiro programador cuidado com o café{resetar}')
    elif comida == 'carne':
        print(f'Adora um churrasco ne?')
        print(f'{azul}Cardapio: Picanha, Alcatra, Cupim, Fraldinha, Ácem, Maminha, Contrafilé{resetar}')
        tipodecarne = input(f'{vermelho}Qual o tipo de carne deseja?:{resetar} ')
        if tipodecarne == 'picanha':
            print(f'{vermelho}Faz o l, picanha mais cara do planeta')
            print('Pense no lula')
            print(f'Se ta caro não compra{resetar}')
            kilos = float(input(f'{amarelo}Quantos quilos você quer?{resetar}: '))
            valor = 70.00 # valor p/kg
            x = valor * kilos # calculo a cada kg * pelo valor
            picanha = input(f'''{amarelo}Deseja comprar {tipodecarne} por R${x}?.{resetar} 
                            [0] {verde}Sim{resetar} 
                            [1] {vermelho}Não{resetar}: ''')
            if picanha == '0':
                item = 70.00 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por R${item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif picanha == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
        elif tipodecarne == 'alcatra':
            print('Ja fez o l hoje?')
            kilos = float(input(f'{amarelo}Quantos quilos você quer?{resetar}: '))
            valor = 34.00
            x = valor * kilos
            alcatra = input(f'''{amarelo}Deseja comprar {tipodecarne} por R${x}?.{resetar}
                            [0] {verde}Sim{resetar} 
                            [1] {vermelho}Não{resetar}: ''')
            if alcatra == '0':
                item = 34.00 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por R${item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif alcatra == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
        elif tipodecarne == 'cupim':
            print('Gosta de uma gordura né?')
            kilos = float(input(f'{amarelo}Quantos quilos você quer?{resetar}: '))
            valor = 41.99
            x = valor * kilos
            cupim = input(f'''{amarelo}Deseja comprar {tipodecarne} por R${x}?{resetar}. 
                            [0] {verde}Sim{resetar}
                            [1] {vermelho}Não{resetar}: ''')
            if cupim == '0':
                item = 41.99 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por R${item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif cupim == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
        elif tipodecarne == 'fraldinha':
            print('E um bebe ou um churrasqueiro?')
            kilos = float(input(f'{amarelo}Quantos quilos você quer?{resetar}: '))
            valor = 37.99
            x = valor * kilos
            fraldainha = input(f'''{amarelo}Deseja comprar {tipodecarne} por R${x}?.{resetar}
                            [0] {verde}Sim{resetar}
                            [1] {vermelho}Não{resetar}: ''')
            if fraldainha == '0':
                item = 37.99 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por {item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif fraldainha == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
        elif tipodecarne == 'ácem':
            print('Gosta de carne magra')
            kilos = float(input(f'{amarelo}Quantos quilos você quer?{resetar}: '))
            valor = 32.99
            x = valor * kilos
            acem = input(f'''{amarelo}Deseja comprar {tipodecarne} por R${x}?.{resetar} 
                            [0] {verde}Sim{resetar}
                            [1] {vermelho}Não{resetar}: ''')
            if acem == '0':
                item = 32.99 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por R${item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif acem == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
        elif tipodecarne == 'maminha':
            print('Comedor de bundas')
            maminha = input(f'''{amarelo}Deseja comprar {tipodecarne} por R$52.99?.{resetar} 
                            [0] {verde}Sim{resetar}
                            [1] {vermelho}Não{resetar}: ''')
            if maminha == '0':
                kilos = float(input('Quantos quilos você quer?: '))
                item = 52.99 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por R${item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif maminha == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
        elif tipodecarne == 'contrafilé':
            print('So gosta de coisas macia')
            kilos = float(input('Quantos quilos você quer?: '))
            valor = 49.99
            x = kilos * valor
            contrafile = input(f'''{amarelo}Deseja comprar {tipodecarne} por {x}?.{resetar} 
                            [0] {verde}Sim{resetar}
                            [1] {vermelho}Não{resetar}: ''')

            if contrafile == '0':
                item = 49.99 * kilos
                if saldo >= item:
                    saldo -= item
                    print(f'{vermelho}Você comprou {tipodecarne} por R${item}{resetar}')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
            elif contrafile == '1':
                print(f'{amarelo}Você voltou ao menu{resetar}')
