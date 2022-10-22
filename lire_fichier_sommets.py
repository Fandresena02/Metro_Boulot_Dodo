def fichier_sommet(nom_fichier):
    lst_f = []
    for ligne in nom_fichier:
        lst = ligne.split(";")
        dico = {"numero_sommet" : int(lst[1]), "nom_sommet" : lst[2], "ligne" : lst[3], "terminus" : lst[4], "branchement" : int(lst[5])}
        lst_f.append(dico)
    return lst_f


f = open("sommets.txt", 'r')
print(fichier_sommet(f))
f.close()
