def people():
    name = str(input("Diga seu nome! >> ")).capitalize()
    idade = int(input("Diga sua idade >> "))
    pessoa = f'Seu nome é {name}, sua idade {idade}'

    if idade > 17:
        print(f'{pessoa} >> E bem vindo a CLT.')
    else:
        print(f'{pessoa} >> E ainda não chegou a CLT.')



people()