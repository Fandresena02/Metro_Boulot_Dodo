
class MatriceAdjacence(object):
    def __init__(self, num=0):
        """Initialise un graphe sans arêtes sur num sommets.

        >>> G = MatriceAdjacence()
        >>> G._matrice_adjacence
        []
        """
        self._matrice_adjacence = [[0] * num for _ in range(num)]

    def ajouter_arete(self, source, destination):
        """Ajoute l'arête {source, destination} au graphe, en créant les sommets manquants le cas échéant.

        >>> G = MatriceAdjacence(2)
        >>> G.ajouter_arete(0,1)
        >>> G._matrice_adjacence
        [[0, 1], [1, 0]]
        """
        a_ajouter = max(source, destination) - len(self._matrice_adjacence) +1
        if max(source, destination) >= len(self._matrice_adjacence) : 
            for i  in range(a_ajouter):
                self.ajouter_sommet()
        self._matrice_adjacence[source][destination] = 1
        self._matrice_adjacence[destination][source] = 1
        
    def ajouter_aretes(self, iterable):
        """Ajoute toutes les arêtes de l'itérable donné au graphe. N'importe quel type d'itérable est acceptable, mais il faut qu'il ne contienne que des couples de naturels.
        
        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,1), (1,1), (2,0)])
        >>> G._matrice_adjacence
        [[0, 1, 1], [1, 1, 0], [1, 0, 0]]
        """
        for i in iterable: 
            self.ajouter_arete(i[0], i[1])

    def ajouter_sommet(self):
        """Ajoute un nouveau sommet au graphe et renvoie son identifiant.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_sommet()
        0
        """
        # Pour chaque element de la liste _matrice_adjacence, on ajoute un sommet, et on ajoute a _matrice_adjacence un nouvel element de self.num element [0]
        length = len(self._matrice_adjacence)
        length += 1
        for i in self._matrice_adjacence:
            i += [0]
        self._matrice_adjacence.append([0]*length)

        return length - 1


    def aretes(self):
        """Renvoie l'ensemble des arêtes du graphe sous forme de couples (si on les stocke sous forme de paires, on ne peut pas stocker les boucles, c'est-à-dire les arêtes de la forme (u, u)).
        
        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,1), (1,2)])
        >>> G.aretes()
        [(0, 1), (1, 0), (1, 2), (2, 1)]
        """
        tmp = []
        to_parse = len(self._matrice_adjacence)
        for i in range(to_parse):
            for j in range(to_parse):
                if self._matrice_adjacence[i][j] == 1:
                    tmp.append((i,j))
                    tmp.append((j,i))
        return list(dict.fromkeys(tmp))

    def boucles(self):
        """Renvoie les boucles du graphe, c'est-à-dire les arêtes reliant un sommet à lui-même.
        
        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,0), (1,1), (2,1)])
        >>> G.boucles()
        [(0, 0), (1, 1)]
        """
        tmp = []
        for i in range(len(self._matrice_adjacence)):
            if self._matrice_adjacence[i][i]:
                tmp.append((i, i))
        return tmp

    def contient_arete(self, u, v):
        """Renvoie True si l'arête {u, v} existe, False sinon.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,0), (1,1), (2,1)])
        >>> G.contient_arete(1,1)
        True
        >>> G.contient_arete(0,2)
        False
        """
        for i in range(len(self._matrice_adjacence)):
            if self._matrice_adjacence[u][v]:
                return True
        return False

    def contient_sommet(self, u):
        """Renvoie True si le sommet u existe, False sinon.
        
        >>> G = MatriceAdjacence(2)
        >>> G.contient_sommet(0)
        True
        >>> G.contient_sommet(-1)
        False
        """
        for i in range(len(self._matrice_adjacence)): 
            if u == i:
                return True 
        return False

    def degre(self, sommet):
        """Renvoie le degré d'un sommet, c'est-à-dire le nombre de voisins qu'il possède.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,0), (1,1), (2,1)])
        >>> G.degre(1)
        2
        """
        degre = 0
        for i in self._matrice_adjacence[sommet]:
            if i == 1:
                degre += 1
        return degre 

    def nombre_aretes(self):
        """Renvoie le nombre d'arêtes du graphe.
        """
        nb_boucles = len(self.aretes())
        return nb_boucles

    def nombre_boucles(self):
        """Renvoie le nombre d'arêtes de la forme {u, u}.

        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,0), (1,0)])
        >>> G.nombre_boucles()
        1
        """
        nb_boucles = len(self.boucles())
        return nb_boucles

    def nombre_sommets(self):
        """Renvoie le nombre de sommets du graphe.

        >>> from random import randint
        >>> n = randint(0, 1000)
        >>> MatriceAdjacence(n).nombre_sommets() == n
        True
        """
        tmp = 0
        for i in self._matrice_adjacence:
            tmp += 1
        return tmp

    def retirer_arete(self, u, v):
        """Retire l'arête {u, v} si elle existe; provoque une erreur sinon.
        
        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(1,1), (0,0)])
        >>> G.retirer_arete(1,1)
        >>> G._matrice_adjacence
        [[1, 0], [0, 0]]
        >>> G.retirer_arete(1,1)
        Traceback (most recent call last):
            ...
        ValueError: Element do not exist in list
        """
        if self._matrice_adjacence[u][v]: 
            self._matrice_adjacence[u][v] = 0
        else :
            raise ValueError("Element do not exist in list")
            

    def retirer_aretes(self, iterable):
        """Retire toutes les arêtes de l'itérable donné du graphe. N'importe quel type d'itérable est acceptable, mais il faut qu'il ne contienne que des couples d'éléments (quel que soit le type du couple).
        """
        pass

    def retirer_sommet(self, sommet):
        """Déconnecte un sommet du graphe et le supprime.

        >>> G = MatriceAdjacence(4)
        >>> G.ajouter_aretes([(0,0), (1,0), (1,2), (2,1), (2,3), (3,3)])
        >>> G.retirer_sommet(1)
        >>> G._matrice_adjacence
        [[1, 0, 0], [0, 0, 1], [0, 1, 1]]
        """
        #On supprime le sommet donné en argument, et pour tous les sommets, on supprime le lien avec le sommet supprimé 
        #Ce qui réduit la taille de la liste _matrice_adjacence, car un sommet a été retiré
        length = len(self._matrice_adjacence)
        self._matrice_adjacence.pop(sommet)
        for i in self._matrice_adjacence:
            i.pop(sommet)
        length -= 1


    def retirer_sommets(self, iterable):
        """Efface les sommets de l'itérable donné du graphe, et retire toutes les arêtes incidentes à ces sommets.

        >>> G = MatriceAdjacence(4)
        >>> G.ajouter_aretes([(1,0), (1,2), (2,1), (2,3), (3,3)])
        >>> G.retirer_sommets([0, 1])
        >>> G._matrice_adjacence
        [[0, 0], [0, 1]]
        """
        for i in iterable: self.retirer_sommet(i)

    def sommets(self):
        """Renvoie l'ensemble des sommets du graphe.

        >>> G = MatriceAdjacence(2)
        >>> G.sommets()
        [0, 1]
        """
        tmp = []
        for i in range(len(self._matrice_adjacence)):
            tmp.append(i)
        return tmp
        

    def sous_graphe_induit(self, iterable):
        """Renvoie le sous-graphe induit par l'itérable de sommets donné."""
        pass  # à compléter

    def voisins(self, sommet):
        """Renvoie la liste des voisins d'un sommet.
        
        >>> G = MatriceAdjacence()
        >>> G.ajouter_aretes([(0,1), (1, 0)])
        >>> G.voisins(1)
        [0]
        """
        tmp = []
        for i in range(len(self._matrice_adjacence)):
            if self._matrice_adjacence[sommet][i] == 1:
                tmp.append(i)
        return tmp
        

# def export_dot(graphe):
#     """Renvoie une chaîne encodant le graphe au format dot."""
#     return ""  # à compléter


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
