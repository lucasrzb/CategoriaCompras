#ESSE CONTEUDO E DE TESTES FEITOS POR MIN / SENDO TOTALMENTE ALEATORIO / Aprendendo IF ELSE E ELIF / while


tipodesanduiche = str
vermelho = "\033[31m"
verde = "\033[32m"
azul = "\033[34m"
amarelo = "\033[33m"
resetar = "\033[0m"
item = float

saldo = int(input('Digite o saldo desejado: ')) # fora do loop while evita repetição
print(f'{amarelo}Saldo atual de R${saldo}{resetar}')
while True: #lopp inicio

    print(f'{azul}Cardapio Menu: batata , macarrao, queijo, bolo, brocolis, feijoada, hellow world, carne, sanduiche, pizza, salgado{resetar}')
    print(f'{vermelho}Para sair digite: sair{resetar}')
    print(f'{amarelo}Saldo atual de R${saldo}{resetar}')
    comida = input(f'{azul}Digite uma comida do cardápio ou outro comando:{resetar} ')


    if comida == 'saldo':
        print(f'Seu Saldo atual e de {saldo:.2f}')
        if comida == 'sair':
            print(f'{vermelho}Voce saiu{resetar}')
            break #saida de loop

    if comida == 'batata':
        print('Mrs Potato Head')
        batatavalor = input(f'''Deseja comprar {comida} por R$1.50?.
                            [0] {verde}Sim{resetar}
                            [1] {vermelho}Não{resetar}: ''')
        if batatavalor == '0':
           item = 1.50
           if saldo >= item:
            saldo -= item
            print(f'Você comprou {comida} por {item}')
           elif saldo < item: #para caso não tenha dinheiro
               print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')

        elif batatavalor == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif comida == 'macarrao':
        print('Voce e um italiano mamamia')
        macarraovalor = input(f'''Deseja comprar {comida} por R$6.50? 
                            [0] {verde}Sim{resetar} 
                            [1] {vermelho}Não{resetar}: ''')
        if macarraovalor == '0':
            item = 6.50
            if saldo >= item:
               saldo -= item
               print(f'Voce comprou {comida} por {item} ')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif macarraovalor == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif comida == 'queijo':
        print('Um verdadeiro apreciador de degustação')
        queijo = input(f'''Deseja comprar {comida} por R$15.00?.
                         [0] {verde}Sim{resetar}
                         [1] {vermelho}Não{resetar}: ''')
        if queijo == '0':
                item = 20.00
                if saldo >= item:
                    saldo -= item
                    print(f'Voce comprou {comida} por {item} ')
                elif saldo < item:
                    print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif queijo == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')

    elif comida == 'bolo':
        print('Um verdadeiro jogador de minecraft')
        bolo = input(f'''Deseja comprar {comida} por R$5.00?.
                         [0] {verde}Sim{resetar}
                         [1] {vermelho}Não{resetar}: ''')
        if bolo == '0':
            item = 5.00
            if saldo >= item:
                saldo -= item
                print(f"Você comprou {comida} por R${item}")
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif bolo == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif comida == 'brocolis':
        print('Ninguem gosta')
        brocolis = input(f'''Deseja comprar {comida} por R$3.00?
                         [0] {verde}Sim{resetar}
                         [1] {vermelho}Não{resetar}: ''')
        if brocolis == '0':
            item = 3.00
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {comida} por R${item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif brocolis == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif comida == 'feijoada':
        print('Um brasileiro perdido que ama ser brasileiro')
        feijoada = input(f'''Deseja comprar {comida} por R$8.90?. 
                         [0] {verde}Sim{resetar} 
                         [1] {vermelho}Não{resetar}: ''')
        if feijoada == '0':
            item = 8.90
            if saldo >= item:
                saldo -= item
                print(f'Você comprou {comida} por {item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif feijoada == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
    elif comida == 'pizza':
        print('Pac Man faltava uma parte será que não era essa?')
        pizza = input(f'''Deseja comprar {comida} por R$22.00?.
                          [0] {verde}Sim{resetar} 
                          [1] {vermelho}Não{resetar}: ''')
        if pizza == '0':
            item = 22.00
            if saldo >= item:
                saldo -= item
                print(f'Voce comprou {comida} por {item}')
            elif saldo < item:
                print(f'{vermelho}Você não tem dinheiro suficiente{resetar}')
        elif pizza == '1':
            print(f'{vermelho}Você voltou ao menu{resetar}')
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
