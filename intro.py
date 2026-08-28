# intro.py

from datetime import datetime  #Hämtar in datetime för att veta tid och därmed svara baserat på tiden

def hälsa():
    nu = datetime.now()   #Hämtar in nuvarande tid
    timme = nu.hour   #Hämtar in timmen
    if 5 <= timme < 12:  #Om klockan är mellan 5 och 12
        print("God morgon!")
    elif 12 <= timme < 18:  #Om klockan är mellan 12 och 18
        print("God eftermiddag!")
    else: 
        print("God kväll!")  #Om klockan är mellan 18 och 5

def fråga_ålder():
    while True:  #Loop för att säkerställa att heltal matas in för ålder
        ålder = input("Hur gammal är du?\n")  #Mata in ålder som en sträng
        if ålder.isdigit():  #Kolla om åldern är ett heltal
            ålder = int(ålder)  #Konvertera strängen till ett heltal
            break  #Avsluta loopen om ett heltal matas in
        else:  #Om det inte är ett heltal, be användaren att mata in ett heltal
            print("Vänligen ange ett heltal för ålder, tack :)")

    if ålder < 22:  #Om åldern är mindre än 22
        print("Du är ung och har mycket att lära dig i IT-världen!")
    elif ålder < 40:  #Om åldern är mellan 22 och 40
        print("Du är i dina bästa år för att utvecklas inom IT och cybersäkerhet!")
    else:  #Om åldern är 40 eller äldre
        print("Du har mycket erfarenhet att dela med dig av inom IT och cybersäkerhet!")

def pyssla_med():
    aktivitet = input("Vad vill du pyssla med i Python?(spel, programmera, lära, testa etc.)\n").lower() #Fråga användaren vad de vill pyssla med & lower() för att göra inputen med små bokstäver så att det inte spelar någon roll om användaren skriver med stora eller små bokstäver

    if "spel" in aktivitet:  #Om användaren skriver spel i sin input
        print("Kul! Låt oss skapa ett spel tillsammans!")
    elif "programmera" in aktivitet:  #Om användaren skriver programmera i sin input
        print("Toppen! Låt oss programmera något spännande!")
    elif "lära" in aktivitet:  #Om användaren skriver lära i sin input
        print("Fantastiskt! Låt oss lära oss mer om Python!")
    elif "testa" in aktivitet:  #Om användaren skriver testa i sin input
        print("Spännande! Låt oss testa våra Python-kunskaper!")
    else:  #Om användaren skriver något annat än spel, programmera, lära eller testa
        print("Det låter intressant! Låt oss utforska det tillsammans!")


# Nu är funktionerna definierade och vi kan köra programmet

print("Hej ITSX26!")
print("Jag studerar IT- och cybersäkerhet")

namn = input("Vad heter du?\n")
hälsa()  #Kör funktionen för att hälsa baserat på tid
fråga_ålder()  #Kör funktionen för att fråga efter ålder och ge svar baserat på ålder
print("Välkommen, " +namn+ "! Nu sätter vi igång med Python :)")
pyssla_med()  #Kör funktionen för att fråga vad användaren vill pyssla med i Python

