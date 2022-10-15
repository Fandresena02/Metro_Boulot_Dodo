
lst_f = []
with open("sommets.txt", "r") as filin :
    for ligne in filin:
        lst = ligne.split(";")
        dico = {"numero_sommet" : int(lst[0]), "nom_sommet" : lst[1], "ligne" : int(lst[2]), "terminus" : lst[3], "branchement" : int(lst[4])}
        lst_f.append(dico)

print(lst_f)
filin.close()

