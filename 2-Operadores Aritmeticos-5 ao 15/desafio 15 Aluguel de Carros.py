#Ler KM percorrido  e por quantos dias foi alugado. Calcular preço a pagar // R$60,00 por dia e R$0,15
#por km rodado
km = float(input("Quantos KM percorrido? --> "))
dias = int(input("Por quantos dias ele foi alugado? --> "))
resul = (60*dias) + (km*0.15)
print(f'O valor a pagar é de R${resul:.2f}')