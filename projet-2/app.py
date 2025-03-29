class Etudiants:

    def __init__(self, nom, prenom, age):

        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.notes=[]


    def ajouter_note(self, note1=0,note2=0,note3=0):
        """recuperer les notes de l'etudiant"""
        if 0<=note1 and note2 and note3 <=20:
            self.notes.append(note1)
            self.notes.append(note2)
            self.notes.append(note3)
        else:
            print("Note invalide")

    def calculer_moyenne(self):
        """Calculer la moyenne de l'etudiant"""
        if not self.notes:
            return 0
        else:
            return sum(self.notes)/len(self.notes)



    def afficher_infos(self):
        """Afficher les infos de l'etudiant"""
        print(f"etudiant:{self.nom} {self.prenom}")
        print(f"Age: {self.age} ans.")
        print(f"Notes: {self.notes}")
        print(f"Moyenne: {self.calculer_moyenne()}")

class GestionEtudiants:

    def __init__(self):
        
        self.etudiants=[]

    def ajouter_etudiant(self, etudiant):

        self.etudiants.append(etudiant)
    
    def meilleur_etudiants(self):
        """Recuperer sur la base de la moyenne le meilleur eleve"""
        if not self.etudiants:
            return None
        else:
            return max(self.etudiants, key=lambda e: e.calculer_moyenne())
        
    def afficher_tous(self):
        """Afficher les etudiants"""
        for etudiant in self.etudiants:
            etudiant.afficher_infos()
            print('-'*30)



#  Lancer l'appli.
gestion=GestionEtudiants()
print(gestion)

# initialiser la fonction.
etudiant1=Etudiants('teby', 'lorince', 28)
etudiant1.ajouter_note(12,15,7)


# Utilisateur n°2
etudiant2=Etudiants('Moughola', 'day', 26)
etudiant2.ajouter_note(16,18,12)



gestion.ajouter_etudiant(etudiant1)
gestion.ajouter_etudiant(etudiant2)

gestion.afficher_tous()

meilleur=gestion.meilleur_etudiants()
print(f"Meilleur étudiant: {meilleur.prenom} {meilleur.nom}")