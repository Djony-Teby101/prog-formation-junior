from io import StringIO
import sys
import unittest
from app_poo import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_show_balance(self):
        # Redirige stdout pour capturer la sortie du print
        captured_output = StringIO()
        sys.stdout = captured_output

        # Crée une instance de BankAccount et appelle show_balance
        account = BankAccount("John Doe", 1500)
        account.show_balance()

        # Réinitialise stdout
        sys.stdout = sys.__stdout__

        # Vérifie si la sortie correspond à la chaîne attendue
        expected_output = "Solde actuel du compte de Mr John Doe : 1500 F CFA\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

class TestBankAccountInit(unittest.TestCase):
    # TestBankAccountInit est une classe de test pour vérifier l'initialisation de la classe BankAccount.
    # Méthodes :
    #     - test_initialization_with_default_balance():
    #         Vérifie qu'un objet BankAccount est correctement initialisé avec le solde par défaut de 0.
    #     - test_initialization_with_custom_balance():
    #         Vérifie qu'un objet BankAccount est correctement initialisé avec un solde initial personnalisé.
    #     - test_initialization_with_negative_balance():
    #         Vérifie qu'un objet BankAccount est correctement initialisé avec un solde négatif.
    
    def test_initialization_with_default_balance(self):
        """
        Vérifie que le compte est bien initialisé avec le solde par défaut.
        """
        account = BankAccount("Djony")
        self.assertEqual(account.account_holder, "Djony")
        self.assertEqual(account.balance, 0)

    def test_initialization_with_custom_balance(self):
        """
        Vérifie que le compte est bien initialisé avec un solde initial personnalisé.
        """
        account = BankAccount("Teby", 500)
        self.assertEqual(account.account_holder, "Teby")
        self.assertEqual(account.balance, 500)

    def test_initialization_with_negative_balance(self):
        """
        Vérifie que l'initialisation avec un solde négatif est correctement gérée.
        """
        account = BankAccount("Pearce", -100)
        self.assertEqual(account.account_holder, "Pearce")
        self.assertEqual(account.balance, -100)

class TestBankAccountWithdraw(unittest.TestCase):
    def setUp(self):
        """Initialise une instance de BankAccount pour les tests."""
        self.account = BankAccount("Joseph Howard", 1000)

    def test_withdraw_success(self):
        """Teste le retrait d'un montant valide dans la limite du solde."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.withdraw(500)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.account.balance, 500)
        self.assertIn("Un retrait de 500 F CFA a été effectué. Nouveau solde : 500 F CFA", captured_output.getvalue())

    def test_withdraw_insufficient_funds(self):
        """Teste le retrait d'un montant supérieur au solde disponible."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.withdraw(1500)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.account.balance, 1000)
        self.assertIn("Fonds insuffisants !", captured_output.getvalue())

    def test_withdraw_invalid_amount_negative(self):
        """Teste le retrait d'un montant négatif."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.withdraw(-100)
        sys.stdout = sys.__stdout__
        self.assertEqual(self.account.balance, 1000)
        self.assertIn("Opération invalide ! Le montant doit être un entier positif.", captured_output.getvalue())

    def test_withdraw_invalid_amount_non_integer(self):
        """Teste le retrait d'un montant non entier."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.withdraw("100")
        sys.stdout = sys.__stdout__
        self.assertEqual(self.account.balance, 1000)
        self.assertIn("Opération invalide ! Le montant doit être un entier positif.", captured_output.getvalue())

class TestBankAccountDeposit(unittest.TestCase):
    def setUp(self):
        """Initialise une instance de BankAccount pour les tests."""
        self.account = BankAccount("Joseph Howard", 1000)

    def test_deposit_positive_amount(self):
        """Teste le dépôt d'un montant positif."""
        initial_balance = self.account.balance
        deposit_amount = 500
        expected_balance = initial_balance + deposit_amount

        # Capture la sortie
        captured_output = StringIO()
        sys.stdout = captured_output

        self.account.deposit(deposit_amount)

        # Réinitialise stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(self.account.balance, expected_balance)
        self.assertIn(f"Un dépôt de {deposit_amount} F CFA a été effectué. Nouveau solde : {expected_balance} F CFA", captured_output.getvalue())

    def test_deposit_zero_amount(self):
        """Teste le dépôt de zéro (opération invalide)."""
        initial_balance = self.account.balance
        deposit_amount = 0

        # Capture la sortie
        captured_output = StringIO()
        sys.stdout = captured_output

        self.account.deposit(deposit_amount)

        # Réinitialise stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(self.account.balance, initial_balance)
        self.assertIn("Opération invalide ! Le montant doit être un entier positif.", captured_output.getvalue())

    def test_deposit_negative_amount(self):
        """Teste le dépôt d'un montant négatif (opération invalide)."""
        initial_balance = self.account.balance
        deposit_amount = -100

        # Capture la sortie
        captured_output = StringIO()
        sys.stdout = captured_output

        self.account.deposit(deposit_amount)

        # Réinitialise stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(self.account.balance, initial_balance)
        self.assertIn("Opération invalide ! Le montant doit être un entier positif.", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
