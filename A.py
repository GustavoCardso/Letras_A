print('----- VOU CONTAR QUANTAS LETRAS "A" APARECEM NO SEU TEXTO -----'  )
texto = input("Digite o que você deseja: ")

quantidade_a = 0

for caractere in texto:
    
    if caractere == 'a' or caractere == 'A':
        quantidade_a += 1

print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
