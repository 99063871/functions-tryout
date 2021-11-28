from time import sleep
import random

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
            sleep(3)
            escapeVar = random.randint(1, 100)
            if escapeVar < 75:
                print("Wow dat was nog makkelijker dan ontsnappen in gtaV")
                sleep(2)
                print("Je bent nu al succesvol ontsnapt")
                sleep(2)
                print("Je gaat gelijk naar de auto dealer en koopt je droom auto")
                sleep(2)
                print("De fiat multipla")
            elif escapeVar > 75:
                print("Hmm oke in gta is het makkelijker")
                sleep(2)
                print("Je bent gepakt...")
                sleep(3)
                print("Succes in de gevangenis")

        elif police == "b":
            print("Waarom zou je de politie aanvallen??")
            sleep(2)
            print("Blijkbaar is 1 tegen 26 niet helemaal eerlijk")
            sleep(2)
            print("U died.")
    elif alarm > 80:
        print("Je loopt naar buiten.")
        sleep(2)
        print("Waarom was dat zo makkelijk??")
        sleep(3)
        print("Je gaat naar de auto dealer en koopt je droom auto")
        sleep(3)
        print("De fiat multipla!")