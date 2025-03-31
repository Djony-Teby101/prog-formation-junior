<?php


class CompteBancaire{
    private $solde; //=> solde du compte.


    // Constructeur valeur initial du compte.
    public function __construct($montantInitial=0)
    {
        $this->solde=$montantInitial;
    }

    // Methode de depot d'argent.
    public function depot($montant){
        if($montant>0){
            $this->solde += $montant;
            return "Depot effectuée avec succes.".$this->solde."Fcfa";
        }else{
            return "Erreur lors de la transaction.";
        }
    }

    // Methode Afficher solde du compte.
    public function afficheSolde(){
        return "Solde de compte :{$this->solde } Fcfa.";
    }

    // Mehode de retrait de compte.
    public function retrait($montant){
        if($montant>0 && $montant <=$this->solde){
            $this->solde-=$montant;
            return "Retrait reussi. nouveau solde:{$this->solde} Fcfa";
        }elseif($montant <=0){
            return "Erreur, le montant doit etre positif.";
        }else{
            return "Operation echec ! solde du compte est insuffissant.";
        }
    }
}




// Lancer l'application.
$compte = new CompteBancaire(100);

echo $compte->depot(120) ."<br />";
echo $compte->afficheSolde() ."<br />";

echo $compte->retrait(300) ."<br />";
echo $compte->afficheSolde() ."<br />";

?>