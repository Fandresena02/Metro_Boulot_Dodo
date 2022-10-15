def fichier_sommet(nom_fichier):
    lst_f = []
    for ligne in nom_fichier:
        lst = ligne.split(";")
        dico = {"numero_sommet" : int(lst[0]), "nom_sommet" : lst[1], "ligne" : lst[2], "terminus" : lst[3], "branchement" : int(lst[4])}
        lst_f.append(dico)
    return lst_f


f = open("sommets.txt", 'r')
print(fichier_sommet(f))
f.close()
