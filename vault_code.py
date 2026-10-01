import random



# Costanti del gioco

CODICE_MIN = 1

CODICE_MAX = 50

TENTATIVI_BASE = 6

TENTATIVI_MIN = 3

MAX_LIVELLO = 3





def dai_indizio(tentativo, codice):

    """Restituisce un indizio confrontando il tentativo con il codice segreto"""

    if tentativo<codice:

        print("Più alto")

    elif codice<tentativo<=CODICE_MAX:

        print("Più basso")

    elif tentativo>CODICE_MAX:

        print("Il codice è tra 1 e 50")





def stampa_tentativi(n, usati):

    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""

    riga=''

    for i in range(usati):

        riga+='X'

    for i in range(n-usati):

        riga+='O'

    print(riga)





def gestisci_livello(livello):

    """ Gestisce un singolo livello del gioco.

    Ritorna:

    * True se il giocatore indovina il codice

    * False se il giocatore esaurisce i tentativi.



    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione

    """



    # Inizializzazioni

    n = TENTATIVI_BASE - livello

    if n < TENTATIVI_MIN:

        n = TENTATIVI_MIN



    codice = random.randint(CODICE_MIN, CODICE_MAX)

    usati = 0



    print(f"Livello {livello}) {n} tentativi")

    stampa_tentativi(n, usati)

    for i in range(n):

        tentativo=int(input("Tentativo: "))

        dai_indizio(tentativo, codice)

        if tentativo == codice:

            print("Accesso consentito!")

            return True

        else:

            usati+=1

            stampa_tentativi(n, usati)

    return False



    # TODO





def main():

    print("=== Benvenuto in Vault Code ===")

    livello = 0



    while livello <= MAX_LIVELLO:

        completato = gestisci_livello(livello)

        if completato:

            livello += 1

        else:

            break

main()