lst_f = []
with open("sommets.txt", "r") as filin :
    for ligne in filin:
        lst = ligne.split(";")
        dico = {"numero_sommet" : lst[0], "nom_sommet" : lst[1], "ligne" : lst[2], "terminus" : lst[3], "branchement" : lst[4]}
        lst_f.append(dico)

print(lst_f)
filin.close()
