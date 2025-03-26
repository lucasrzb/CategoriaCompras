#ESSE CONTEUDO E DE TESTES FEITOS POR MIN / SENDO TOTALMENTE ALEATORIO / Aprendendo IF ELSE E ELIF / while


tipodecarne = str
tipodesalgado = str
tipodesanduiche = str
adicionais = str
saldo = 100
batatavalor = str
compra = str
sair = str
comida = str
macarraovalor = str
compramaccarao = str

while True: #lopp inicio
    print('Cardapio Menu: batata , macarrao, queijo, bolo, brocolis, feijoada, hellow world, carne, sanduiche, pizza, salgado')
    print('Para sair digite: sair')
    print(f'Saldo atual de R${saldo}')
    comida = input(f'Digite uma comida do cardápio ou outro comando: ')

    if comida == 'saldo':
        print(f'Seu Saldo atual e de {saldo}')

    if comida == 'sair':
        print('Voce saiu')
        break #saida de loop

    if comida == 'batata':
        print('Mrs Potato Head')
        batatavalor = input('Deseja comprar Sim ou Não? ')
        if batatavalor == 'Sim':
            print(f'Saldo atual = R${saldo}')
            valor_item = 4.50
            compra = input(f'Deseja comprar {comida} por {valor_item}, Sim ou Não? ') #compra var = if abaixo / input pra prox if
        if compra == 'Sim':
                valor_item = 3.5
                saldo  -= valor_item #calculo pra item - carteira
                print(f'Voce comprou {comida}')
                print(f'Saldo restante {saldo}')
        elif compra == 'Não':
            print('Você retornou ao menu')
        elif batatavalor == 'Não':
            print('Você retornou ao menu')
    elif comida == 'macarrao':
        print('Voce e um italiano mamamia')
        macarraovalor = input(f'Quer Comprar {comida}?. Sim ou Não? : por R$10.00? ')
        if macarraovalor == 'Sim':
            valor_item = 10.00
            saldo -= valor_item
            print(f'Voce comprou macarrão por {valor_item} ')
        elif macarraovalor == 'Não':
            print('Voce retornou ao Menu')
    elif comida == 'queijo':
        print('Um verdadeiro apreciador de degustação')
        queijo = input(f'Deseja comprar queijo? Sim ou Não. Por R$15.00: ')
        if queijo == 'Sim':
                valor_item = 20.00
                saldo -= valor_item
                print(f'Voce comprou {comida} por {valor_item} ')
        elif queijo == 'Não':
            print('Você retornou ao menu')
    elif comida == 'bolo':
        print('Um verdadeiro jogador de minecraft')
        bolo = input(f'Deseja comprar {comida}?. Sim ou Não. Por R$5.00: ')
        if bolo == 'Sim':
            valor_item = 5.00
            saldo -= valor_item
            print(f"Você comprou {comida} por R${valor_item}")
        elif bolo == 'Não':
            print("Você voltou para o menu")
    elif comida == 'brocolis':
        print('Ninguem gosta')
        brocolis = input(f'Deseja comprar {comida}. Sim ou Não. Por R$3.00: ')
        if brocolis == 'Sim':
            valor_item = 3.00
            saldo -= valor_item
            print(f'Você comprou {comida} por R${valor_item}')
        elif brocolis == 'Não':
            print('Você voltou ao menu')
    elif comida == 'feijoada':
        print('Um brasileiro perdido que ama ser brasileiro')
        feijoada = input('Deseja comprar feijoada. Sim ou Não?. Por R$8.90: ')
        if feijoada == 'Sim':
            valor_item = 8.90
            saldo -= valor_item
            print(f'Você comprou {comida} por {valor_item}')
        elif feijoada == 'Não':
            print('Você voltou ao menu')
    elif comida == 'pizza':
        print('Pac Man faltava uma parte será que não era essa?')
        pizza = input(f'Deseja comprar {comida}. Sim ou Não?. Por R$22.00: ')
        if pizza == 'Sim':
            valor_item = 22.00
            saldo -= valor_item
            print(f'Voce comprou {comida} por {valor_item}')
        elif pizza == 'Não':
            print('Você voltou ao menu')
    elif comida == 'sanduiche':
        print('sanduiche iche iche meme maldito')
        print('Cardarpio Sanduiche: X-Salada, X-Bacon, X-Especial, X-Tudo, X-Mirage')
        tipodesanduiche = input('Digite um tipo de sanduiche: ')
    if tipodesanduiche == 'X-Salada':
        print('Alface, Pão de hambuguer, tomate, alface')
        xsalada = input('Deseja comprar X-Salada?. Sim ou Não?. Por R$14.00: ')
        if xsalada == 'Sim':
            valor_item = 14.00
            saldo -= valor_item
            print(f'Você comprou {tipodesanduiche} por R${valor_item} ')
        elif xsalada == 'Não':
            print('Você voltou ao menu')
    elif tipodesanduiche == 'X-Bacon':
        print('Pão de Hambuguer, tomate, bacon, mussarela, presunto')
        xbacon = input(f'Deseja comprar {tipodesanduiche}?. Sim ou Não?. por R$23.00: ')
        if xbacon == 'Sim':
            valor_item = 23.00
            saldo -= valor_item
            print(f'Você comprou {tipodesanduiche} por R${valor_item}')
        elif xbacon == 'Não':
            print('Você retornou ao menu')
    elif tipodesanduiche == 'X-Especial':
        print('Pão de Hambuguer, tomate, carne de hambuguer, ovo')
        xespecial = input(f'Você deseja comprar {tipodesanduiche} por R$21.00: ')
        if xespecial == 'Sim':
            valor_item = 21.00
            saldo -= valor_item
            print(f'Você comprou {tipodesanduiche} por R${valor_item}')
        elif xespecial == 'Não':
            print('Você voltou ao menu')
    elif tipodesanduiche == 'X-Tudo':
        print("Pão de Hambuguer, tomate, carne de hambuguer, ovo, alface, presunto, mussarela, bacon")
        xtudo = input(f'Deseja comprar {tipodesanduiche}?. Sim ou Não?. Por R$32.00: ')
        if xtudo == 'Sim':
            valor_item = 32.00
            saldo -= valor_item
            print(f'Você comprou {tipodesanduiche} por R${valor_item}')
        elif xtudo == 'Não':
            print('Você voltou ao menu')
    elif tipodesanduiche == 'X-Mirage':
        print('Pão de Hambuguer, tomate, salcicha, presunto, mussarela')
        xmirage = input(f'Deseja comprar {tipodesanduiche}?. Sim ou Não?. Por R$19.00: ')
        if xmirage == 'Sim':
            valor_item = 19.00
            saldo -= valor_item
            print(f'Você comprou {tipodesanduiche} por {valor_item}')
        elif xmirage == 'Não':
            print('Você voltou ao menu')
    elif comida == 'salgado':
        print('Cardapio Salgados: americano, pastel, coxinha, bolinha de queijo, empada, esfiha, enroladinho')
        tipodesalgado = input('Digite o seu salgado preferido: ')
        if tipodesalgado == 'americano':
            print('Queijo e persunto sempre será a melhor combinação')
            americano = input(f'Deseja comprar {tipodesalgado} por R$3.5.? Sim ou Não?: ')
            if americano == 'Sim':
                valor_item = 3.5
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif americano == 'Não':
                print('Você voltou ao menu')
        elif tipodesalgado == 'enroladinho':
            print('Uma delicia porem demora pra digerir')
            enroladinho = input(f'Deseja comprar {tipodesalgado} por R$2.50. Sim ou Não?.')
            if enroladinho == 'Sim':
                valor_item = 2.5
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif enroladinho == 'Não':
                print('Você voltou ao menu')

        elif tipodesalgado == 'pastel':
            print('Ir a feira as 6:00am e comprar pastel e tão satisfatorio')
            pastel = input(f'Deseja comprar {tipodesalgado} por R$8.0. Sim ou Não?.')
            if pastel == 'Sim':
                valor_item = 8.0
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif pastel == 'Não':
                print('Você voltou ao menu')

        elif tipodesalgado == 'coxinha':
            print('Comedor de coxas de galinha so que em forma de massa')
            coxinha = input(f'Deseja comprar {tipodesalgado}. Sim ou Não?. Por R$4.5: ')
            if coxinha == 'Sim':
                valor_item = 4.5
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif coxinha == 'Não':
                print('Você voltou ao menu')
        elif tipodesalgado == 'bolinha de queijo':
            print('So a bolinha e 3,50 cada imagina com queijo')
            bolinha = input(f'Deseja comprar {tipodesalgado} por R$2.5: ')
            if bolinha == 'Sim':
                valor_item = 2.5
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif bolinha == 'Não':
                print('Você voltou ao menu')
        elif tipodesalgado == 'empada':
            print('Massa podre não coma isso')
            empada = input(f'Deseja comprar {tipodesalgado}. Sim ou Não?. Por R$5.0')
            if empada == 'Sim':
                valor_item = 5.0
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif empada == 'Não':
                print('Você voltou ao menu')
        elif tipodesalgado == 'esfiha':
            print('Pizza pequena so que com outro nome')
            esfiha = input(f'Deseja comprar {tipodesalgado} por R$6.0?. Sim ou Não?.')
            if esfiha == 'Sim':
                valor_item = 6.0
                saldo -= valor_item
                print(f'Você comprou {tipodesalgado} por R${valor_item}')
            elif esfiha == 'Não':
                print('Você voltou ao menu')

    elif comida == 'hellow world':
        print('certeza que e um verdadeiro programador cuidado com o café')
    elif comida == 'carne':
        print('Adora um churrasco ne?')
        escolha = input('Sim ou Não? ')
        if escolha == 'Sim':
            print('Cardapio de carnes: picanha, alcatra, cupim, fraldinha, ácem, maminha, contrafilé')
        elif escolha == 'Não':
            print('Você voltou ao menu')
        tipodecarne = input('Qual o seu tipo de carne para churrasco? ')
        if tipodecarne == 'picanha':
            print('Faz o l, picanha mais cara do planeta')
            print('Pense no lula')
            print('Se ta caro não compra')
            picanha = input(f'Deseja comprar {tipodecarne} por R$70.00. Sim ou Não?: ')
            if picanha == 'Sim':
                valor_item = 70.00
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por R${valor_item}')
            elif picanha == 'Não':
                print('Você voltou ao menu')
        elif tipodecarne == 'alcatra':
            print('Ja fez o l hoje?')
            alcatra = input(f'Deseja comprar {tipodecarne} por R$34.00?. Sim ou Não?: ')
            if alcatra == 'Sim':
                valor_item = 34.00
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por R${valor_item}')
            elif alcatra == 'Não':
                print('Você voltou ao menu')
        elif tipodecarne == 'cupim':
            print('Gosta de uma gordura né?')
            cupim = input(f'Deseja comprar {tipodecarne} por R$41.99?. Sim ou Não?: ')
            if cupim == 'Sim':
                valor_item = 41.99
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por R${valor_item}')
            elif cupim == 'Não':
                print('Você voltou ao menu')
        elif tipodecarne == 'fraldinha':
            print('E um bebe ou um churrasqueiro?')
            fraldainha = input(f'Deseja comprar {tipodecarne} por R$37.99. Sim ou Não?: ')
            if fraldainha == 'Sim':
                valor_item = 37.99
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por {valor_item}')
            elif fraldainha == 'Não':
                print('Você voltou ao menu')
        elif tipodecarne == 'ácem':
            print('Gosta de carne magra certeza')
            acem = input(f'Deseja comprar {tipodecarne} por R$32.99. Sim ou Não?: ')
            if acem == 'Sim':
                valor_item = 32.99
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por R${valor_item}')
            elif acem == 'Não':
                print('Você voltou ao menu')
        elif tipodecarne == 'maminha':
            print('Comedor de bundas')
            maminha = input(f'Deseja comprar {tipodecarne} por R$52.99. Sim ou Não?: ')
            if maminha == 'Sim':
                valor_item = 52.99
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por R${valor_item}')
            elif maminha == 'Não':
                print('Você voltou ao menu')
        elif tipodecarne == 'contrafilé':
            print('So gosta de coisas macia')
            contrafile = input(f'Deseja comprar {tipodecarne} por R$49.99?. Sim ou Não?: ')
            if contrafile == 'Sim':
                valor_item = 49.99
                saldo -= valor_item
                print(f'Você comprou {tipodecarne} por R${valor_item}')
            elif contrafile == 'Não':
                print('Você voltou ao menu')

    else:
        print(f'Não existe essa {comida} em nosso sistema pipipi')
