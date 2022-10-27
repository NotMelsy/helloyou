print (" Dirk wilt graag pro gamer worden en wilt een PLaystation of Computer kopen ")
print(" a - PS5 ")
print(" b - Computer ")

antwoord = input(' wat kies jij? ')
if antwoord == "a" or antwoord == "playstation":
    print(" Dirk is erg blij met zijn PS5, hij wilt Fortnite of Brawlhalla spelen. ")
    print(" a - Fortnite ")
    print(" b - Brawlhalla ")

    antwoord1 = input("wat kies jij? ")
    if antwoord1 == "a" or antwoord1 == "Fortnite":
        print("Hij word erg goed in Fortnite en begint ook bekend te worden ")
        print(" Dirk word uitgenodigt om op een LAN toernooi te spelen ")
        print(" a - Meedoen ")
        print(" b - Niet meedoen ")

        antwoord3 = input("wat kies jij?")
        if antwoord3 == "a" or antwoord3 == "meedoen":
            print(" Dirk speelt fantastisch en wint het toernooi. ")
            print(" Hij wint de komende 2 jaar 2.5 miljoen aan prijzengeld ")
            print(" Later word Fortnite minder populair en word hij 1 van de meest bekeken streamers van de wereld ")

            exit()

        if antwoord3 == "b" or antwoord3 == "niet meedoen":
            print(" Dirk verliest zelfvertrouwen en gaat erg slecht spelen. ")
            print(" Daardoor stopt dirk met gamen. ")

            exit()

        else:
            print("voer a of b in!")

    elif antwoord1 == "b" or antwoord1 == "Brawlhalla":
        print(" Dirk is veel brawlhalla gaan spelen en word erg goed, \n hij probeert mee te doen aan een in game toernooi ")
        print(" Hij speelt er goed en doet mee aan meerdere toernooien. ")

        exit()

    else:
        print("voer a of b in!")

        
elif antwoord == "b" or antwoord == "Computer":
    print(" Dirk heeft een computer en een heel erg mooie setup. \n Dirk wilt Valorant of CS:GO spelen ")
    print(" a - Valorant ")
    print(" b - CS:GO ")
    antwoord4 = input(' wat kies jij? ')

    if antwoord4 == "a" or antwoord4 == "Valorant":
        print(" Dirk wordt erg goed in Valorant en is een van de beste aimers samen met ScreaM. \n Hij is de IGL van zijn team geworden en zijn team presteert erg goed. \n Dirk word uitgenodigt tot een echt team dat veel eerste is geworden. ")
        print(" a - Accepteren ")
        print(" b - Afwijzen ")

        antwoord5 = input("wat kies jij? ")
        if antwoord5 == "a" or antwoord5 == "Accpeteren":
            print(" Dirk moet wennen aan het niveau ")
            print(" Dirk denkt erover na om in plaats van support een duelist te spelen zodat hij met zijn aim gevechten kan openen. ")
            print(" a - Duelist ")
            print(" b - Support ")

            antwoord6 = input("wat kies jij?")
            if antwoord6 == "a" or antwoord6 == "duelist":
                print(" Dirk speelt alsogf hij al jaren het spel speelt en wint met zijn team elk toernooi dat er is ")
                print(" Hij wint de komende 2 jaar 2.5 miljoen aan prijzengeld en wint zo'n 22 toernooien back-to-back. ")

                exit()

            if antwoord6 == "b" or antwoord6 == "support":
                print(" Dirk is nogsteeds een erg goede speler maar is niet de beste van de wereld. \n Dirk en zijn team winnen maar 1 toernooi in 2 jaar tijd ")
                print(" Daardoor stopt dirk met gamen. Maar hij heeft wel een mooie carriere. ")

        if antwoord5 == "b" or antwoord5 == "Afwijzen":
            print(" Dirk speelt met zijn eigen team maar ze kunnen maar niet doorbreken ")
            print(" Dirk is niet bekend of pro geworden dus stopt hij. ")

            exit()

        else:
            print("voer a of b in!")

    elif antwoord4 == "b" or antwoord4 == "CS:GO":
        print(" CS:GO was een slechte keuze voor Dirk. er was geen plek voor nieuwe teams en hij kon ook geen team joinen. ")
        print(" Dirk is gestopt met gamen ")

        exit()

    else:
        print("voer a of b in!")

    exit()

else: print("voer a of b in!")