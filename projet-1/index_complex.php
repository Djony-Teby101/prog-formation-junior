<?php

    class CompteBancaire{
        private $solde;
        private $historique=[];
        private $fichierSauvegarde="compte_data.json";


        // => Constructeur recharge les données s'il y'en à.
        public function __construct($montantInitial=0){
            if(file_exists($this->fichierSauvegarde)){
                $data=json_decode(file_get_contents($this->fichierSauvegarde), true);
                $this->solde=$data['solde'] ?? $montantInitial;
                $this->historique=$data['historique'] ?? [];
            }
            else{
                $this->solde=$montantInitial;
                $this->ajouterHistorique("creation du compte avec".$montantInitial. "Fcfa");
            }
        }

        // Sauvegarder les donnees dans un fichier Json.
        private function sauvegarder(){
            $data =[
                'solde'=>$this->solde,
                'historique'=>$this->historique
            ];
            file_put_contents($this->fichierSauvegarde, json_encode($data));
        }

        // Methode : ajouter des historique.
        private function ajouterHistorique($message){
            $this->historique[] = date('Y-m-d H:i:s')."-".$message;
            $this->sauvegarder();
        }

        // Methode: depot d'argent.
        public function depot($montant){
            try {
                if($montant <=0){
                    throw new Exception("Le montant doit etre positif");
               }
               $this->solde += $montant;
               $this->ajouterHistorique("depot de {$montant} Fcfa ");
               return "depot reussi. Nouveau solde: {$this->solde} Fcfa";


            } catch (Exception $e) {
                return "Erreur: {$e->getMessage() }";
            }
        }

        // Methode: de retrait d'argent.
        public function retrait($montant){
            try {
                
                if($montant<0){
                    throw new Exception("le montant doit etre positif");
                }
                if($montant > $this->solde){
                    throw new Exception("solde insuffisant");
                }

                $this->solde -=$montant;
                $this->ajouterHistorique("retrait de {$montant} Fcfa");
                return "retrait reussi. Nouveau solde: {$this->solde} Fcfa";

            } catch (Exception $e) {
                return "Erreur:".$e->getMessage();
            }
        }

        // Afficher le solde
        public function getSolde(){
            return "Solde actuel: {$this->solde} Fcfa ";
        }

        // Afficher historique de transaction.
        public function getHistorique(){
            return implode("<br>", $this->historique);
        }

    }

    // Lancer de l'app.
    try {
        $compte = new CompteBancaire(1000);

        echo $compte->getSolde() ."<br />"; 
        echo $compte->depot(200) ."<br />"; 
        echo $compte->retrait(100) ."<br />";
        
        echo "<h3>Historique : </h3";
        echo $compte->getHistorique() ."<br />";

        
    } catch (Exception $e) {
        echo "Erreur csysteme {$e->getMessage()}";
    }


?>