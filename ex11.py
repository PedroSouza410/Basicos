nome=input("Digite seu nome: ")
ano=(int(input("Digite o ano do seu nascimento: ")))
idade=2025-ano
if idade>18:
    print(nome, "seu acesso está liberado.")
else:
    print(nome,"seu acesso está negado.")