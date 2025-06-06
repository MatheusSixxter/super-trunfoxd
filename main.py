# Desafio Super Trunfo - Versão simples
# Feito para a disciplina de ADS - 1º período

cartas = [
    {"nome": "Carta A", "ataque": 80, "defesa": 60, "magia": 40},
    {"nome": "Carta B", "ataque": 70, "defesa": 90, "magia": 50},
    {"nome": "Carta C", "ataque": 60, "defesa": 40, "magia": 95}
]

print("Bem-vindo ao Super Trunfo!")
print("Escolha sua carta:")
for i, carta in enumerate(cartas):
    print(f"{i}: {carta['nome']}")

escolha_jogador = int(input("Digite o número da sua carta: "))
carta_jogador = cartas[escolha_jogador]

import random
carta_cpu = random.choice(cartas)

print("\nSua carta:")
print(carta_jogador)
print("\nCarta do oponente:")
print(carta_cpu)

atributo = input("\nEscolha um atributo para competir (ataque, defesa ou magia): ")

valor_jogador = carta_jogador[atributo]
valor_cpu = carta_cpu[atributo]

print(f"\nSeu {atributo}: {valor_jogador} vs {valor_cpu} do oponente")

if valor_jogador > valor_cpu:
    print("Você venceu!")
elif valor_jogador < valor_cpu:
    print("Você perdeu!")
else:
    print("Empate!")
