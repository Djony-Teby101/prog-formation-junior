class CompteBancaire:
 def __init__(self, nom_titulaire, solde_initial=0):
  self.nom_titulaire=nom_titulaire
  self.solde=solde_initial

  print(f"Compte crée pour {self.nom_titulaire}, le solde est de {self.solde} Fcfa")

  # Methode pour consulter le solde.
 def afficher_solde(self):
   print(f"Solde actuel du compte de Mr {self.nom_titulaire}: est de {self.solde} Fcfa")

 def retirer(self, montant):

  if montant>0:
   self.solde -= montant
   print(f"un retrait de {montant} à ete effectue. Nouveau solde: {self.solde} Fcfa")
  else:
   print("Operation invalide !")

 def depot(self, montant):

  if type(montant)==int and montant>0:
   self.solde += montant
   print(f"un retrait de {montant} à ete effectue. Nouveau solde: {self.solde} Fcfa")
   print(type(montant))
  else:
   print("Operation invalide !")


# instance de classe
compte1=CompteBancaire('lorinceTeby',1000)
compte1.retirer(350)
compte1.depot('5000')
# compte1.afficher_solde()
# compte2=CompteBancaire('TebyDay', 5000)