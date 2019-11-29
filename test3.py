
def next_line(line):
    print(line)
    resultat = []
    long = len(line) - 1
    compteur = 1
    if line == [1]:
        resultat = [1, 1]
    else:
        for i in range(long):
            c = i
            while line[c] == line[c + 1]:
                compteur = compteur + 1
                c = c + 1
            resultat.append(compteur)
            resultat.append(line[i+1])
            print(resultat)

        print(resultat)

# code global©


# next_line([1])
next_line([1, 1, 1, 2, 2, 1])