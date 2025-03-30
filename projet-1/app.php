<?php

namespace Usages {
    require_once 'src/init.php';

    use App\BankAccount;

    /**
     * Interface Params
     * 
     * Cette interface définit des paramètres constants utilisés pour les opérations de BankAccount.
     * 
     * @constant string holder Le nom du titulaire du compte.
     * @constant int default Le solde par défaut du compte.
     * @constant int get Le montant à retirer du compte.
     * @constant int deposit Le montant à déposer sur le compte.
     */
    interface Params {
        const holder = 'John Smith';
        const default = 1000;
        const get = 350;
        const deposit = 5000;
    }

    /**
     * Classe Finale Example
     * 
     * Cette classe étend la classe BankAccount et implémente l'interface Params.
     * Elle démontre l'utilisation de la classe BankAccount en effectuant des opérations
     * telles que le retrait, le dépôt et l'affichage du solde.
     * 
     * @extends App\BankAccount
     * @implements Params
     */
    final class Example extends BankAccount implements Params {
        /**
         * Constructeur
         * 
         * Initialise une nouvelle instance de la classe Example. Elle crée un objet BankAccount
         * avec le nom du titulaire et le solde par défaut spécifiés, et effectue les opérations suivantes :
         * - Affiche un aperçu de l'objet BankAccount.
         * - Retire un montant spécifié du compte et affiche le résultat.
         * - Dépose un montant spécifié sur le compte et affiche le résultat.
         * - Affiche le solde du compte et imprime le résultat.
         * 
         * @return void
         */
        public function __construct() {
            $bank = new parent(self::holder, self::default);

            # Aperçu de l'objet BankAccount
            print_r($bank);

            // Retire un montant spécifié et affiche le résultat
            print($bank->withdraw(self::get));

            // Dépose un montant spécifié et affiche le résultat
            print($bank->deposit(self::deposit));

            // Affiche le solde du compte et imprime le résultat
            print($bank->showBalance(self::holder, $bank->getBalance()));
        }
    }

    /**
     * Instancie la classe Example pour démontrer sa fonctionnalité.
     */
    new Example;
}

?>
