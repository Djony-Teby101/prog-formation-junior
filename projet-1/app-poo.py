class CompteBancaire:
    def __init__(self, nom_titulaire: str, solde_initial: int = 0):
        self.nom_titulaire = nom_titulaire
        self._solde = solde_initial
        print(f"Compte créé pour {self.nom_titulaire}, le solde est de {self._solde} F CFA")
    
    @property
    def solde(self):
        return self._solde
    
    def afficher_solde(self):
        print(f"Solde actuel du compte de Mr {self.nom_titulaire} : {self._solde} F CFA")
    
    def retirer(self, montant: int):
        if isinstance(montant, int) and montant > 0:
            if montant <= self._solde:
                self._solde -= montant
                print(f"Un retrait de {montant} F CFA a été effectué. Nouveau solde : {self._solde} F CFA")
            else:
                print("Fonds insuffisants !")
        else:
            print("Opération invalide ! Le montant doit être un entier positif.")
    
    def depot(self, montant: int):
        if isinstance(montant, int) and montant > 0:
            self._solde += montant
            print(f"Un dépôt de {montant} F CFA a été effectué. Nouveau solde : {self._solde} F CFA")
        else:
            print("Opération invalide ! Le montant doit être un entier positif.")

# Exemple d'utilisation
if __name__ == "__main__":
    compte1 = CompteBancaire("Lorince Teby", 1000)
    compte1.retirer(350)
    compte1.depot(5000)
    compte1.afficher_solde()
