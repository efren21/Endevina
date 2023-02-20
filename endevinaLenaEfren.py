#EFREN LENA ROSELLO

import random

#INICIALITZADOR DELS CONTADORS
seguirJuant = True
partidesJugades = 0
voltesGuanyades = 0
totalIntents = 0
mitjaIntents = 0
intentsMenor = 0

#INICIALITZADOR DEL BUCLE
while seguirJuant:
    numAleatori = random.randint(0, 100)
    numMajor = 100
    numMenor = 0
    contador = 1
    encertat = False

    numMaxIntents = input('Introdueix un nombre máxim d\'intents: ')
    intent = input('Dis-me un numero entre 1 i 100: ')

    #ESTIMACIÓ DE RANGS
    while int(numMaxIntents) > contador:
        intent = int(intent)
        if intent > numAleatori:
            if intent < numMajor:
                numMajor = intent
            intent = input("No. Es menor. Esta entre " +
                        str(numMenor) + " i " + str(numMajor-1)+": ")
        elif intent < numAleatori:
            if intent > numMenor:
                numMenor = intent
            intent = input("No. Es major. Esta entre " +
                        str(numMenor+1) + " i " + str(numMajor) + ": ")
        else:
            encertat = True
            intents = contador
            break
        contador = contador + 1

    #MOSTRAR SI EL NÚMERO HA SEGUT ENCERTAT I EN QUANTS INTENTS
    if encertat:
        print("Molt bé! ho has encertat en " + str(intents) + " intents")
        voltesGuanyades = voltesGuanyades + 1
        totalIntents = totalIntents + intents
        if intents < intentsMenor or intentsMenor == 0:
            intentsMenor = intents
    else:
        print("Has superat els intents i no ho has endevinat. El numero era el " + str(numAleatori))
    
    partidesJugades = partidesJugades + 1 
    tornarAJuar = input('Vols jugar altra partida: ')

    #PREGUNTAR SI ES VOL TORNAR A JUGAR I MOSTRAR PARTIDES JUGADES I INTENTS
    if tornarAJuar != 's' and tornarAJuar != 'S':
        seguirJuant = False
        print("Se han juat " + str(partidesJugades) + " partides")
        for i in range(0, voltesGuanyades):
            print("PREMI")
        mitjaIntents = totalIntents/voltesGuanyades
        print("La mitja de intents entre les partides guanyades es de " + str(mitjaIntents) + " intents")  
        print("El minim d'intents en que s'ha guanyat una partida es de " + str(intentsMenor) + " intents")  