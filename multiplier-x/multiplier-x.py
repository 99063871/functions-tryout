tafel = input("Van welk getal wilt u de tafel zien? ")
anwser=0
def tafelFunctie(tafel):
    for i in range(1,11):
        anwser = int(tafel) * i
        print(anwser)

tafelFunctie(tafel)