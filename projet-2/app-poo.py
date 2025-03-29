class Etudiant:
    def __init__(self, nom: str, prenom: str, age: int):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.notes = []
    
    def ajouter_note(self, *notes: int):
        """Ajouter plusieurs notes pour l'étudiant."""
        for note in notes:
            if isinstance(note, int) and 0 <= note <= 20:
                self.notes.append(note)
            else:
                print(f"Note invalide: {note}. Les notes doivent être entre 0 et 20.")
    
    def calculer_moyenne(self) -> float:
        """Calculer la moyenne des notes de l'étudiant."""
        return sum(self.notes) / len(self.notes) if self.notes else 0.0
    
    def afficher_infos(self):
        """Afficher les informations de l'étudiant."""
        print(f"Étudiant: {self.nom} {self.prenom}")
        print(f"Âge: {self.age} ans")
        print(f"Notes: {self.notes}")
        print(f"Moyenne: {self.calculer_moyenne():.2f}")
        print('-' * 30)

class GestionEtudiants:
    def __init__(self):
        self.etudiants = []
    
    def ajouter_etudiant(self, etudiant: Etudiant):
        """Ajouter un étudiant à la liste."""
        if isinstance(etudiant, Etudiant):
            self.etudiants.append(etudiant)
        else:
            print("L'objet ajouté n'est pas un étudiant valide.")
    
    def meilleur_etudiant(self) -> Etudiant:
        """Retourne l'étudiant ayant la meilleure moyenne."""
        return max(self.etudiants, key=lambda e: e.calculer_moyenne(), default=None)
    
    def afficher_tous(self):
        """Afficher tous les étudiants enregistrés."""
        if not self.etudiants:
            print("Aucun étudiant enregistré.")
        for etudiant in self.etudiants:
            etudiant.afficher_infos()

# Lancer l'application
if __name__ == "__main__":
    gestion = GestionEtudiants()
    
    # Initialiser les étudiants
    etudiant1 = Etudiant("Teby", "Lorince", 28)
    etudiant1.ajouter_note(12, 15, 7)
    
    etudiant2 = Etudiant("Moughola", "Day", 26)
    etudiant2.ajouter_note(16, 18, 12)
    
    # Ajouter les étudiants à la gestion
    gestion.ajouter_etudiant(etudiant1)
    gestion.ajouter_etudiant(etudiant2)
    
    # Afficher les étudiants
    gestion.afficher_tous()
    
    # Trouver et afficher le meilleur étudiant
    meilleur = gestion.meilleur_etudiant()
    if meilleur:
        print(f"Meilleur étudiant: {meilleur.prenom} {meilleur.nom} avec une moyenne de {meilleur.calculer_moyenne():.2f}")
