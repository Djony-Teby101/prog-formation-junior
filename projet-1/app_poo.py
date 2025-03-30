class BankAccount:
    """
    ### BankAccount

    BankAccount est une classe qui représente un compte bancaire simple avec des opérations de base telles que le dépôt, le retrait et la consultation du solde.

    #### Méthodes :
    
    - `__init__(account_holder: str, initial_balance: int = 0)`:
        Constructeur qui initialise un compte bancaire avec le nom du titulaire et un solde initial optionnel.
    - `balance()` :
        Récupère le solde actuel du compte.
    - `show_balance()` :
        Affiche le solde actuel du compte, y compris le nom du titulaire.
    - `withdraw(amount: int)` :
        Retire un montant spécifié du compte si les fonds sont suffisants. Affiche des messages appropriés
        en cas de succès, de fonds insuffisants ou d'entrée invalide.
    - `deposit(amount: int)` :
        Ajoute un montant spécifié au solde du compte. Affiche des messages appropriés en cas de succès ou d'entrée invalide.
    """
    def __init__(self, account_holder: str, initial_balance: int = 0):
        """
        Initialise un compte bancaire avec le nom du titulaire et un solde initial optionnel.

        - Args :
            account_holder (str) : Le nom du titulaire du compte.
            initial_balance (int, optionnel) : Le solde initial du compte. La valeur par défaut est 0.
        - Attributs :
            `account_holder (str)` : Le nom du titulaire du compte.
            `_balance (int)` : Le solde actuel du compte.
        """
        self.account_holder = account_holder
        self._balance = initial_balance
        
        print(f"Compte créé pour {self.account_holder}, le solde est de {self._balance} F CFA")
    
    @property
    def balance(self):
        """
        Récupère le solde actuel du compte.

        Returns :
            float : Le solde actuel du compte.
        """
        return self._balance
    
    def show_balance(self):
        """
        Affiche le solde actuel du compte.

        Cette méthode affiche le nom du titulaire du compte et le solde actuel en francs CFA.
        """
        print(f"Solde actuel du compte de Mr {self.account_holder} : {self._balance} F CFA")
    
    def withdraw(self, amount: int):
        """
        Retire un montant spécifié du compte si les fonds sont suffisants.

        Paramètres :
            amount (int) : Le montant à retirer. Doit être un entier positif.

        Retourne :
            None

        Affiche :
            - Un message de succès avec le montant retiré et le nouveau solde si l'opération réussit.
            - Un message d'erreur si les fonds sont insuffisants.
            - Un message d'erreur si le montant fourni n'est pas un entier positif.
            - Un message d'erreur si le montant est supérieur au solde actuel.
            - Un message d'erreur si le montant est invalide.
        """
        if isinstance(amount, int) and amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Un retrait de {amount} F CFA a été effectué. Nouveau solde : {self._balance} F CFA")
            else:
                raise ValueError("Montant supérieur au solde actuel !")
        else:
            if amount <= 0:
                raise ValueError("Le montant doit être supérieur à zéro !")
            else:
                raise TypeError("Opération invalide ! Le montant doit être un entier positif.")
            
        if isinstance(amount, int) and amount > 0:
            print("Opération invalide ! Le montant doit être un entier positif.")
    
    def deposit(self, amount: int):
        """
        Ajoute un montant spécifié au solde du compte.

        Paramètres :
            amount (int) : Le montant à déposer. Doit être un entier positif.

        Comportement :
            - Si le montant est un entier positif, il est ajouté au solde du compte.
            - Affiche un message de confirmation avec le montant déposé et le nouveau solde.
            - Si le montant n'est pas un entier positif, affiche un message d'erreur indiquant que l'opération est invalide.
        """
        if isinstance(amount, int) and amount > 0:
            self._balance += amount
            print(f"Un dépôt de {amount} F CFA a été effectué. Nouveau solde : {self._balance} F CFA")
        else:
            print("Opération invalide ! Le montant doit être un entier positif.")

# Exemple d'utilisation
if __name__ == "__main__":
    account = BankAccount("John Smith", 1000)
    account.withdraw(350)
    account.deposit(5000)
    account.show_balance()
