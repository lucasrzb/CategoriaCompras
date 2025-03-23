#ESSE CONTEUDO E DE TESTES FEITOS POR MIN / SENDO TOTALMENTE ALEATORIO / Aprendendo IF ELSE E ELIF / while
escolha = str
tipodecarne = str
tipodesalgado = str
tipodesanduiche = str
adicionais = str
carteira = 100
batatavalor = str
compra = str
escolha3 = str
subtrai = float
sair = str
comida = str

while True: #lopp inicio
    print('Cardapio: batata , macarrao, queijo, bolo, brocolis, feijoada, hellow world, carne, sanduiche, pizza, salgado')
    comida = input('Digite uma comida ou para Sair digite (sair) ')

    if comida == 'sair':
        print('Voce saiu')
        break #saida de loop
    if comida == 'batata':
        print('Mrs Potato Head')
        batatavalor = input('Deseja comprar Sim ou Não? ')
        if batatavalor == 'Sim':
            print(f'Saldo atual = {carteira}')
            valor_item = 4.50
            compra = input(f'Deseja comprar {comida} por {valor_item}, Sim ou Não? ') #compra var = if abaixo / input pra prox if
        if compra == 'Sim':
            if carteira >= valor_item:
                subtrai =  carteira - 4.50 #calculo pra item - carteira
            print(f'Voce comprou {comida}')
            print(f'Saldo restante {subtrai}')
        elif carteira <= valor_item: #calculo para quando não tiver saldo
            print('Saldo insuficiente para realizar a compra.')
        elif compra == 'Não':
            print('Game over')
        elif batatavalor == 'Não':
            print('Game Over')
    elif comida == 'macarrao':
        print('Voce e um italiano mamamia')
    elif comida == 'queijo':
        print('Um verdadeiro apreciador de degustação')
    elif comida == 'bolo':
        print('Um verdadeiro jogador de minecraft')
    elif comida == 'brocolis':
        print('Ninguem gosta')
    elif comida == 'feijoada':
        print('Um brasileiro perdido que ama ser brasileiro')
    elif comida == 'pizza':
        print('Pac Man faltava uma parte será que não era essa?')
    elif comida == 'sanduiche':
        print('sanduiche iche iche meme maldito')
        print('Cardarpio Sanduiche: X-Salada, X-Bacon, X-Especial, X-Tudo, X-Mirage')
        tipodesanduiche = input('Digite um tipo de sanduiche: ')
    if tipodesanduiche == 'X-Salada':
        print('Alface, Pão de hambuguer, tomate, alface')
    elif tipodesanduiche == 'X-Bacon':
        print('Pão de Hambuguer, tomate, bacon, mussarela, presunto')
    elif tipodesanduiche == 'X-Especial':
        print('Pão de Hambuguer, tomate, carne de hambuguer, ovo')
    elif tipodesanduiche == 'X-Tuddo':
        print("Pão de Hambuguer, tomate, carne de hambuguer, ovo, alface, presunto, mussarela, bacon")
    elif tipodesanduiche == 'X-Mirage':
        print('Pão de Hambuguer, tomate, salcicha, presunto, mussarela')
    elif comida == 'salgado':
        print('Cardapio Salgados: americano, pastel, coxinha, bolinha de queijo, empada, esfiha, enroladinho')
        tipodesalgado = input('Digite o seu salgado preferido: ')
        if tipodesalgado == 'americano':
            print('Queijo e persunto sempre será a melhor combinação')
        elif tipodesalgado == 'enroladinho':
            print('Uma delicia porem demora pra digerir')
        elif tipodesalgado == 'pastel':
            print('Ir a feira as 6:00am e comprar pastel e tão satisfatorio')
        elif tipodesalgado == 'coxinha':
            print('Comedor de coxas de galinha so que em forma de massa')
        elif tipodesalgado == 'bolinha de queijo':
            print('So a bolinha e 3,50 cada imagina com queijo')
        elif tipodesalgado == 'empada':
            print('Massa podre não coma isso')
        elif tipodesalgado == 'esfiha':
            print('Pizza pequena so que com outro nome')
        else:
            print('Não existe esse salgado em nosso sistema pipipi')
    elif comida == 'hellow world':
        print('certeza que e um verdadeiro programador cuidado com o café')
    elif comida == 'carne':
        print('Adora um churrasco ne?')
        escolha = input('Sim ou Não? ')
    if escolha == 'Sim':
        print('Cardapio de carnes: picanha, alcatra, cupim, fraldinha, ácem, maminha, contrafilé')
        tipodecarne = input('Qual o seu tipo de carne para churrasco? ')
        if tipodecarne == 'picanha':
            print('Faz o l, picanha mais cara do planeta')
            print('Pense no lula')
            print('Se ta caro não compra')
        elif tipodecarne == 'alcatra':
            print('Ja fez o l hoje?')
        elif tipodecarne == 'cupim':
            print('Gosta de uma gordura né?')
        elif tipodecarne == 'fraldinha':
            print('E um bebe ou um churrasqueiro?')
        elif tipodecarne == 'ácem':
            print('Gosta de carne magra certeza')
        elif tipodecarne == 'maminha':
            print('Comedor de bundas')
        elif tipodecarne == 'contrafilé':
            print('So gosta de coisas macia')
    elif escolha == 'Não':
        print('Game Over')


