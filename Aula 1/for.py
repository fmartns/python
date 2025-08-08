# 6. For

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

texto = "Python"

for letra in texto:
    print(letra)

for i in range(5):  # de 0 a 4
    print(i)

# range(início, fim, passo)
# início: valor inicial (inclusivo) → opcional, padrão é 0
# fim: valor final (exclusivo)
# passo: de quanto em quanto contar → opcional, padrão é 1

for i in range(1, 11, 2):
    print(i)


pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")