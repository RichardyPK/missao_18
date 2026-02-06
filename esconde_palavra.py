frase1 = "Esse sistema é muito ruim"
frase2 = "Eu odeio me exercitar"
frase3 = "Estou péssimo hoje!"

palavras_ruins = ["ruim", "odeio", "péssimo"]

for palavra in palavras_ruins:
    frase1 = frase1.replace(palavra, "***")
    frase2 = frase2.replace(palavra, "***")
    frase3 = frase3.replace(palavra, "***")

print(frase1)
print(frase2)
print(frase3)