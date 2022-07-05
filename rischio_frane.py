RISCHIO_BASSO = 0
RISCHIO_MEDIO = 1
RISCHIO_ALTO = 2

rischio = 0
descrizione_rischio = ""

print("Inizio calcolo rischio frane")

print("""Precipitazione in corso:
        1 - Sta piovendo
        2 - Non sta piovendo        
     """)

scelta = input("Rispondi alla domanda?: ")
match scelta:
    case "1":
        rischio = rischio + RISCHIO_ALTO
    case "2":
        rischio = rischio + RISCHIO_BASSO


print("""Stagione dell'anno:
        1 - Inverno
        2 - Primavera
        3 - Estate
        4 - Autunno        
     """)

scelta = input("Rispondi alla domanda?: ")
match scelta:
    case "1":
        rischio = rischio + RISCHIO_BASSO
    case "2":
        rischio = rischio + RISCHIO_MEDIO
    case "3":
        rischio = rischio + RISCHIO_ALTO
    case "4":
        rischio = rischio + RISCHIO_MEDIO


print("""Temperatura:
        1 - inferiore allo 0 Celsius
        2 - compresa tra 0 e 10 gradi Celsius
        3 - superiore ai 10 gradi              
     """)

scelta = input("Rispondi alla domanda?: ")
match scelta:
    case "1":
        rischio = rischio + RISCHIO_BASSO
    case "2":
        rischio = rischio + RISCHIO_MEDIO
    case "3":
        rischio = rischio + RISCHIO_ALTO

print("""Orario del giorno:
        1 - dalle 24:00PM alle 07:00AM
        2 - dalle 07:00AM alle 10:00AM
        3 - dalle 10:00AM alle 16:00PM
        4 - dalle 16:00PM alle 24:00PM              
     """)

scelta = input("Rispondi alla domanda?: ")
match scelta:
    case "1":
        rischio = rischio + RISCHIO_BASSO
    case "2":
        rischio = rischio + RISCHIO_MEDIO
    case "3":
        rischio = rischio + RISCHIO_ALTO
    case "4":
        rischio = rischio + RISCHIO_MEDIO

print("""Esposizione del versante:
        1 - Nord
        2 - Sud
        3 - Est
        4 - Ovest              
     """)

scelta = input("Rispondi alla domanda?: ")
match scelta:
    case "1":
        rischio = rischio + RISCHIO_BASSO
    case "2":
        rischio = rischio + RISCHIO_ALTO
    case "3":
        rischio = rischio + RISCHIO_MEDIO
    case "4":
        rischio = rischio + RISCHIO_MEDIO

print("""Quota sul livello del mare:
        1 - Da 0 a 1000
        2 - Da 1000 a 2000
        3 - Da 2000 a 3000
        4 - Da 3000 a 4000              
     """)

scelta = input("Rispondi alla domanda?: ")
match scelta:
    case "1":
        rischio = rischio + RISCHIO_BASSO
    case "2":
        rischio = rischio + RISCHIO_BASSO
    case "3":
        rischio = rischio + RISCHIO_MEDIO
    case "4":
        rischio = rischio + RISCHIO_ALTO


print("******************************************************")
print("risultato: ", rischio)
if (rischio <= 0):
    descrizione_rischio = "debole"
elif (rischio > 0 and rischio < 5):
    descrizione_rischio = "moderato"
elif (rischio == 5):
    descrizione_rischio = "medio - marcato"
elif (rischio > 5 and rischio < 12):    
    descrizione_rischio = "forte"
else: 
    descrizione_rischio = "molto forte"

print("Il rischio di frana é: ", descrizione_rischio)