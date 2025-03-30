<?php

declare(strict_types=1);

namespace App {
    use Exception;
    use Throwable;
    use InvalidArgumentException;

    define('CURRENCY', 'F CFA');
    define('MIN_BALANCE', 0);

    interface Errors {
        const ERR_INVALID = "Opération invalide !";
        const ERR_INVALID_AMOUNT = Errors::ERR_INVALID . " Le montant doit être supérieur à zéro !";
        const ERR_INSUFFICIENT_FUNDS = "Fonds insuffisants !";
        const ERR_INIT = "Le solde de création doit être égal ou supérieur à zéro !";
    }

    trait Messages {
        public function createAccount(string $holder, int $balance): void {
            echo "Compte créé pour {$holder}, le solde est de {$balance} " . CURRENCY . "\n";
        }

        public function showBalance(string $holder, int $balance): string{
            return "Solde actuel du compte de {$holder} : {$balance} " . CURRENCY . "\n";
        }

        public function withdrawSuccess(int $amount, int $balance): string {
            return "Un retrait de {$amount} " . CURRENCY . " a été effectué. Nouveau solde : {$balance} " . CURRENCY . "\n";
        }

        public function depositSuccess(int $amount, int $balance): string {
            return "Un dépôt de {$amount} " . CURRENCY . " a été effectué. Nouveau solde : {$balance} " . CURRENCY . "\n";
        }
    }

    /**
     * BankAccount est une classe qui représente un compte bancaire simple avec des opérations de base telles que le dépôt, le retrait et l'affichage du solde.
     * 
     * #### Méthodes :
     * 
     * - `__construct(accountHolder: str, initialBalance: int = 0)` :
     * Constructeur qui initialise un compte bancaire avec le nom du titulaire et un solde initial optionnel.
     * - `getBalance()` :
     * Récupère le solde actuel du compte.
     * - `deposit(amount: int)` :
     * Ajoute un montant spécifié au solde du compte. Affiche des messages         appropriés en cas de succès ou d'entrée invalide.
     * - `withdraw(amount: int)` :
     * Retire un montant spécifié du compte si les fonds sont suffisants. Affiche des messages appropriés en cas de succès ou d'entrée invalide.
    */
    class BankAccount implements Errors {
        use Messages;
        /**
         * @var string $holder Le nom du titulaire du compte.
         * @var int $balance Le solde actuel du compte (attribut privé).
        */
        private string $holder;
        private int $balance;

        /**
         * Initialise un compte bancaire avec le nom du titulaire et un solde initial optionnel.
         *
         * @param string $accountHolder Le nom du titulaire du compte.
         * @param int $initialBalance Le solde initial du compte. La valeur par défaut est 0.
        */
        function __construct(string $accountHolder, int $initialBalance = MIN_BALANCE) {
            assert(is_int($initialBalance) && $initialBalance >= MIN_BALANCE, self::ERR_INIT);

            $this->holder = $accountHolder;
            $this->balance = $initialBalance;

            self::createAccount($this->holder, $this->balance);
        }

        /**
         * Récupère le solde actuel du compte.
         *
         * @return int Le solde actuel du compte.
         */
        protected function getBalance(): int {
            return $this->balance;
        }

        /**
         * Ajoute un montant spécifié au solde du compte.
         * 
         * @param int $amount Le montant à déposer. Doit être un entier positif.
         * @throws Exception Si le montant est invalide.
         * @throws Exception Si le montant est supérieur au solde actuel.
         * @throws Exception Si le montant est inférieur ou égal à zéro.
         * @return void
         * 
         * Comportement :
         * - Si le montant est un entier positif, il est ajouté au solde du compte.
         * - Affiche un message de confirmation avec le montant déposé et le nouveau solde.
         * 
         * Affiche :
         * - Un message de succès avec le montant déposé et le nouveau solde si l'opération réussit.
         * - Un message d'erreur si le montant est invalide.
         * - Un message d'erreur si le montant est inférieur ou égal à zéro.
        */
        protected function deposit(int $amount): string|Throwable {
            if ($amount > MIN_BALANCE) {
                $this->balance += $amount;

                return self::depositSuccess($amount, $this->balance);
            } else {
                throw new InvalidArgumentException(self::ERR_INVALID_AMOUNT);
            }
        }

        /**
         * Retire un montant spécifié du compte si les fonds sont suffisants.
         * 
         * @param int $amount Le montant à retirer. Doit être un entier positif.
         * @throws Exception Si le montant est supérieur au solde actuel ou si le montant est invalide.
         * 
         * @return void
         * 
         * Affiche :
         * - Un message de succès avec le montant retiré et le nouveau solde si l'opération réussit.
         * - Un message d'erreur si les fonds sont insuffisants.
         * - Un message d'erreur si le montant fourni n'est pas un entier positif.
         * - Un message d'erreur si le montant est supérieur au solde actuel.
         * - Un message d'erreur si le montant est invalide.
         */
        protected function withdraw(int $amount): string|Throwable {
            if (is_int($amount) && $amount > MIN_BALANCE) {
                if ($amount <= $this->balance) {
                    $this->balance -= $amount;

                    return self::withdrawSuccess($amount, $this->balance);
                } else {
                    return new Exception(self::ERR_INSUFFICIENT_FUNDS);
                }
            } else {
                return new InvalidArgumentException(self::ERR_INVALID_AMOUNT);
            }
        }
    }
}
