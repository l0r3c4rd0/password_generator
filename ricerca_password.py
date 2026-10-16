import time
import string

password=input("dammi una password: ")
caratteri=string.digits+string.ascii_letters+string.punctuation
contatore=0
tempo_inizio=time.time()
#prende il tempo dal orario del pc
while contatore!=len(password):
    for elemento in caratteri:
        if elemento==password[contatore]:
            break
    contatore+=1
tempo_finale=time.time()
durata=tempo_finale-tempo_inizio
print(f"la tua password e decifrabile in {durata} secondi")
#se printa un e-05 indica esponente -05