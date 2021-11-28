from time import sleep
import functions
work = 0

print("Je loopt in de stad en ziet een auto die je heel erg mooi vind, het is de Fiat multipla!")
sleep(3)
print("Je rent naar huis en zoekt op hoe duur je nieuwe droom auto is.")
sleep(3)
print("...€19.195")
sleep(1.5)
print("Dat is duurder dan verwacht, je kijkt gelijk op je bankrekening en ziet dat je €19.105 mist.")
sleep(3)
print("Hoe kan je snel geld verdienen? ")
sleep(2)
print("Werken natuurlijk maar dat zal zo lang duren")
sleep(3)
print("En dan krijg je het beste idee ooit")
sleep(3)
print("Een bank overval!")
sleep(3)

def workOrRobberyFunc():
    workOrRobbery = input("Wat wil je gaan doen? \nA=Werken \nB=Bankoverval \n").lower()
    if workOrRobbery == "a":
        work = input("Waar wil je werken? \nA=Donimos \nB=KFC \n").lower()
        sleep(1)
        if work == "a":
            print("Je gaat naar Donimos om te solliciteren")
            sleep(2)
            print("Je hebt geluk en je kan gelijk een gesprek hebben!")
            sleep(2)
            print("Ik ga je een paar reken vragen stellen")
            for a in range(3):
                functions.math()
        elif work == "b":
            print("Je gaat naar KFC om te solliciteren")
            sleep(2)
            print("Je hebt geluk en je kan gelijk een gesprek hebben!")
            sleep(2)
            print("Ik ga je een paar reken vragen stellen")
            for a in range(3):
                functions.math()
        else:
            print("Dat ging niet helemaal goed we beginnen opnieuw")
            workOrRobberyFunc()
        if functions.varA == 3:
            sleep(2)
            print("Dat ging heel erg goed! je bent aangenomen je krijgt via mail te horen wanneer je begint")
            sleep(2)
            print("2 uurtjes later kreeg je te horen dat je morgen 17:30 kon beginnen")
            sleep(2)
            print("Na een paar jaar werken en sparen heb je eindelijk het geld verzameld")
            sleep(2)
            print("Je hebt nu je droom auto gekocht, maar wat nu?")
            sleep(2)
            print("Een rijbewijs...")
        elif functions.varA != 3:
            print("Jammer het is niet gelukt je bent niet aangenomen.")
            sleep(2)
            print("Je zal nooit je droom auto krijgen ):")

    elif workOrRobbery == "b":
        print("Oke dus je wilt een bank overvallen.")
        sleep(2)
        print("Dan heb je wel een paar dingen nodig zoals:Een outfit, een wapen en een tas.")
        sleep(3)
        print("Wat heb je allemaal gevonden?\nEen zwart trainings pak met een ski masker, een grote tas en 3 mogelijke wapens")
        sleep(2)
        weapon = input("A=Een handpistool \nB=een katana \nC=een lepel\n").lower()
        sleep(2)
        print("Je doet je overval kleding aan en gaat naar de bank")
        sleep(5)
        print("Je komt aan bij de bank")
        sleep(2)
        print('Je rent naar binnen en roept"DIT IS EEN OVERVAL"')
        sleep(2)
        if weapon == "a": #Handpistool
            print("De bankmedewerkers kijken je bang aan")
            sleep(2)
            print('Je zegt"gooi al het geld in deze tas"terwijl je een tas op de tafel zet.')
            sleep(2)
            print("Al het geld is in de tas gegooid")
            sleep(2)
            functions.cops()
        elif weapon == "b": #Katana
            glass = functions.random.randint(1, 100)
            if glass < 50:
                print("De bankmedewerkers lachen naar je en bellen de politie")
                sleep(2)
                print("Je bent gepakt, sommige banken hebben dus glas tussen jou en de bankmedewerkers")
                sleep(3)
                print("Succes in de gevangenis")
            elif glass > 50:
                print("De bankmedewerkers kijken je bang aan")
                sleep(2)
                print('Je zegt"gooi al het geld in deze tas"terwijl je een tas op de tafel zet.')
                sleep(2)
                print("Al het geld is in de tas gegooid")
                sleep(2)
                functions.cops()
        elif weapon == "c": #Lepel
            spoon = functions.random.randint(1, 100)
            if spoon < 99:
                print("De bankmedewerkers lachen naar je")
                sleep(2)
                print("Tja wat had je ook verwacht van een lepel...")
                sleep(2)
                print("Mission failed")
            elif spoon > 99:
                print("Wow...")
                sleep(2)
                print("Wat heb jij een geluk")
                sleep(2)
                print("Het is je gewoon gelukt met een lepel")
                sleep(2)
                print("Je gaat naar de auto dealer en koopt je droom auto")
                sleep(3)
                print("De fiat multipla!")
        else:
            print("Dat ging niet helemaal goed probeer het nog eens")
            workOrRobberyFunc()

workOrRobberyFunc()