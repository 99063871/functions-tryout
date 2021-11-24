import time
import random

work = 0
varA = 0
varB = 0

def varthing():
    global varA
    varA = varA + 1

def math():
    numA =  random.randint(1, 1000)
    numB =  random.randint(1, 1000)
    numAstr = str(numA)
    numBstr = str(numB)
    question = input("Wat is " + numAstr + " + " + numBstr + "? ")
    anwser = numA + numB
    anwserFrom = int(question)
    anwser = numA + numB
    if anwserFrom == anwser:
        varthing()

def cops():
    alarm = random.randint(1, 100)
    if alarm < 80:
        print("Je rent naar de deur en je ziet politie.")
        police = input("Wat doe je? ren je weg of val je de politie aan?\nA=Weg rennen\nB=politie aanvallen \n").lower()
        if police == "a":
            print("Je rent weg")
            time.sleep(3)
            escapeVar = random.randint(1, 100)
            if escapeVar < 75:
                print("Wow dat was nog makkelijker dan ontsnappen in gtaV")
                time.sleep(2)
                print("Je bent nu al succesvol ontsnapt")
                time.sleep(2)
                print("Je gaat gelijk naar de auto dealer en koopt je droom auto")
                time.sleep(2)
                print("De fiat multipla")
            elif escapeVar > 75:
                print("Hmm oke in gta is het makkelijker")
                time.sleep(2)
                print("Je bent gepakt...")
                time.sleep(3)
                print("Succes in de gevangenis")

        elif police == "b":
            print("Waarom zou je de politie aanvallen??")
            time.sleep(2)
            print("Blijkbaar is 1 tegen 26 niet helemaal eerlijk")
            time.sleep(2)
            print("U died.")
    elif alarm > 80:
        print("Je loopt naar buiten.")
        time.sleep(2)
        print("Waarom was dat zo makkelijk??")
        time.sleep(3)
        print("Je gaat naar de auto dealer en koopt je droom auto")
        time.sleep(3)
        print("De fiat multipla!")


print("Je loopt in de stad en ziet een auto die je heel erg mooi vind, het is de Fiat multipla!")
time.sleep(3)
print("Je rent naar huis en zoekt op hoe duur je nieuwe droom auto is.")
time.sleep(3)
print("...€19.195")
time.sleep(1.5)
print("Dat is duurder dan verwacht, je kijkt gelijk op je bankrekening en ziet dat je €19.105 mist.")
time.sleep(3)
print("Hoe kan je snel geld verdienen? ")
time.sleep(2)
print("Werken natuurlijk maar dat zal zo lang duren")
time.sleep(3)
print("En dan krijg je het beste idee ooit")
time.sleep(3)
print("Een bank overval!")
time.sleep(3)

def workOrRobberyFunc():
    workOrRobbery = input("Wat wil je gaan doen? \nA=Werken \nB=Bankoverval \n").lower()
    if workOrRobbery == "a":
        work = input("Waar wil je werken? \nA=Donimos \nB=KFC \n").lower()
        time.sleep(1)
        if work == "a":
            print("Je gaat naar Donimos om te solliciteren")
            time.sleep(2)
            print("Je hebt geluk en je kan gelijk een gesprek hebben!")
            time.sleep(2)
            print("Ik ga je een paar reken vragen stellen")
            math()
            math()
            math()
        elif work == "b":
            print("Je gaat naar KFC om te solliciteren")
            time.sleep(2)
            print("Je hebt geluk en je kan gelijk een gesprek hebben!")
            time.sleep(2)
            print("Ik ga je een paar reken vragen stellen")
            math()
            math()
            math()
        else:
            print("Dat ging niet helemaal goed we beginnen opnieuw")
            workOrRobberyFunc()
        if varA == 3:
            time.sleep(2)
            print("Dat ging heel erg goed! je bent aangenomen je krijgt via mail te horen wanneer je begint")
            time.sleep(2)
            print("2 uurtjes later kreeg je te horen dat je morgen 17:30 kon beginnen")
            time.sleep(2)
            print("Na een paar jaar werken en sparen heb je eindelijk het geld verzameld")
            time.sleep(2)
            print("Je hebt nu je droom auto gekocht, maar wat nu?")
            time.sleep(2)
            print("Een rijbewijs...")
        elif varA != 3:
            print("Jammer het is niet gelukt je bent niet aangenomen.")
            time.sleep(2)
            print("Je zal nooit je droom auto krijgen ):")

    elif workOrRobbery == "b":
        print("Oke dus je wilt een bank overvallen.")
        time.sleep(2)
        print("Dan heb je wel een paar dingen nodig zoals:Een outfit, een wapen en een tas.")
        time.sleep(3)
        print("Wat heb je allemaal gevonden?\nEen zwart trainings pak met een ski masker, een grote tas en 3 mogelijke wapens")
        time.sleep(2)
        weapon = input("A=Een handpistool \nB=een katana \nC=een lepel\n").lower()
        time.sleep(2)
        print("Je doet je overval kleding aan en gaat naar de bank")
        time.sleep(5)
        print("Je komt aan bij de bank")
        time.sleep(2)
        print('Je rent naar binnen en roept"DIT IS EEN OVERVAL"')
        time.sleep(2)
        if weapon == "a": #Handpistool
            print("De bankmedewerkers kijken je bang aan")
            time.sleep(2)
            print('Je zegt"gooi al het geld in deze tas"terwijl je een tas op de tafel zet.')
            time.sleep(2)
            print("Al het geld is in de tas gegooid")
            time.sleep(2)
            cops()
        elif weapon == "b": #Katana
            glass = random.randint(1, 100)
            if glass < 50:
                print("De bankmedewerkers lachen naar je en bellen de politie")
                time.sleep(2)
                print("Je bent gepakt, sommige banken hebben dus glas tussen jou en de bankmedewerkers")
                time.sleep(3)
                print("Succes in de gevangenis")
            elif glass > 50:
                print("De bankmedewerkers kijken je bang aan")
                time.sleep(2)
                print('Je zegt"gooi al het geld in deze tas"terwijl je een tas op de tafel zet.')
                time.sleep(2)
                print("Al het geld is in de tas gegooid")
                time.sleep(2)
                cops()
        elif weapon == "c": #Lepel
            spoon = random.randint(1, 100)
            if spoon < 99:
                print("De bankmedewerkers lachen naar je")
                time.sleep(2)
                print("Tja wat had je ook verwacht van een lepel...")
                time.sleep(2)
                print("Mission failed")
            elif spoon > 99:
                print("Wow...")
                time.sleep(2)
                print("Wat heb jij een geluk")
                time.sleep(2)
                print("Het is je gewoon gelukt met een lepel")
                time.sleep(2)
                print("Je gaat naar de auto dealer en koopt je droom auto")
                time.sleep(3)
                print("De fiat multipla!")
        else:
            print("Dat ging niet helemaal goed probeer het nog eens")
            workOrRobberyFunc()

workOrRobberyFunc()