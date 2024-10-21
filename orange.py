version = "1.0.0"

class Orange:
    def get_retrait_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_retrait_options",
            "ussd_code_to_invoke": "*144#",
            "option1": "devise",
            "option2": "3",
            "option3": "1",
            "option4": "numero",
            "option5": "montant",
            "option6": "password"
        }
        return options

    def get_envoi_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_envoi_options",
            "ussd_code_to_invoke": "*144#",
            "option1": "devise",
            "option2": "1",
            "option3": "1",
            "option4": "numero",
            "option5": "montant",
            "option6": "password"
        }
        return options

    def get_verificationTauxEtExecution_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_verificationTauxEtExecution_options",
            "ussd_code_to_invoke": "#",
            "option1": ""
        }
        return options

    def get_achat_credit_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_achat_credit_options",
            "ussd_code_to_invoke": "*144#",
            "option1": "devise",
            "option2": "4",
            "option3.1": "1",
            "option3.2": "montant",
            "option3.3": "password",
            "option4.1": "2",
            "option4.2": "numero",
            "option4.3": "montant",
            "option4.4": "password"
        }
        return options

    def get_soldes_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_soldes_options",
            "option1": ""
        }
        return options

    def get_soldeMoney_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_soldeMoney_options",
            "phone_number": "OrangeMoney",
            "regex_usd": "solde(.*?)USD",
            "regex_cdf": "solde(.*?)(CDF|Fc)",
            "usd_id": "USD",
            "cdf_id": "CDF"
        }
        return options

    def get_cleanSoldeStr_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_cleanSoldeStr_options",
            "clean_regex": "[0-9](.*?)"
        }
        return options

    def get_forcer_demande_solde_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_forcer_demande_solde_options",
            "ussd_code_to_invoke": "*144#",
            "option1": "1",
            "option2": "7",
            "option3": "1",
            "option4": "password"
        }
        return options

    def get_forcer_demande_solde_cdf_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_forcer_demande_solde_cdf_options",
            "ussd_code_to_invoke": "*144#",
            "option1": "2",
            "option2": "7",
            "option3": "1",
            "option4": "password"
        }
        return options

    def get_achat_forfait_appel_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_achat_forfait_appel_options",
            "ussd_code_to_invoke": "*101#",
            "option1.1": "1",
            "option1.2": "",
            "option1.3": "",
            "option2.1": "5",
            "option2.2": "numero",
            "option2.3": "",
            "option2.4": "",
            "option2.5": ""
        }
        return options

    def get_achat_forfait_internet_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_achat_forfait_internet_options",
            "ussd_code_to_invoke": "*101#",
            "option1.1": "2",
            "option1.2": "",
            "option1.3": "",
            "option2.1": "5",
            "option2.2": "numero",
            "option2.3": "2",
            "option2.4": "",
            "option2.5": ""
        }
        return options

    def get_partager_vos_megas_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_partager_vos_megas_options",
            "ussd_code_to_invoke": "*101#",
            "option1": "6",
            "option2": "4",
            "option3": "2"
        }
        return options

    def get_partager_vos_minutes_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_partager_vos_minutes_options",
            "ussd_code_to_invoke": "",
            "option1": ""
        }
        return options

    def get_envoyer_des_unites_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_envoyer_des_unites_options",
            "ussd_code_to_invoke": "*101#",
            "option1": "6",
            "option2": "4",
            "option3": "1",
            "option4": "password",
            "option5": "numero",
            "option6": "montant"
        }
        return options

    def get_solde_unites_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_solde_unites_options",
            "ussd_code_to_invoke": "*840#"
        }
        return options

    def get_solde_minutes_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_solde_minutes_options",
            "ussd_code_to_invoke": "*124#"
        }
        return options

    def get_solde_internet_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_solde_internet_options",
            "ussd_code_to_invoke": "*124#",
            "option1": "8"
        }
        return options

    def get_historique_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_historique_options",
            "phone_number": "OrangeMoney",
            "regex_recu": "depot(.*?)(USD|CDF)(.*?)[.]",
            "regex_envoi": "transfert est effectue(.*?)(USD|CDF)(.*?)[.]",
            "regex_retire": "retrait(.*?)(USD|CDF)(.*?)[.]"
        }
        return options

    def get_getFrais_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_getFrais_options",
            "ecart_usd1": "9",
            "ecart_usd2": "19",
            "ecart_usd3": "29",
            "ecart_usd4": "49",
            "ecart_usd5": "99",
            "ecart_usd6": "499",
            "ecart_usd7": "999",
            "default_usd_frais": ".4",
            "usd_frais1": "0.1",
            "usd_frais2": "0.2",
            "usd_frais3": "0.3",
            "usd_frais4": "0.4",
            "usd_frais5": "0.5",
            "usd_frais6": "0.6",
            "usd_frais7": "0.8",
            "usd_frais8": "1",
            "ecart_cdf1": "10000",
            "ecart_cdf2": "19999",
            "ecart_cdf3": "29999",
            "ecart_cdf4": "49999",
            "ecart_cdf5": "99999",
            "ecart_cdf6": "499999",
            "ecart_cdf7": "999999",
            "default_cdf_frais": "1000",
            "cdf_frais1": "100",
            "cdf_frais2": "150",
            "cdf_frais3": "250",
            "cdf_frais4": "350",
            "cdf_frais5": "500",
            "cdf_frais6": "1000",
            "cdf_frais7": "1500",
            "cdf_frais8": "2500"
        }
        return options

    def get_payerFrais_options(self):
        options = {
            "version": self.get_version_options(),
            "function_called": "get_payerFrais_options",
            "ussd_code_to_invoke": "*144#",
            "option1": "devise",
            "option2": "1",
            "option3": "1",
            "option4": "0895881926",
            "option5": "montant",
            "option6": "password"
        }
        return options

    def get_version_options(self):
        global version
        return version

    def get_all_options(self):
        global version
        all_options = {
            "version": self.get_version_options(),
            "get_retrait_options": self.get_retrait_options(),
            "get_envoi_options": self.get_envoi_options(),
            "get_verificationTauxEtExecution_options": self.get_verificationTauxEtExecution_options(),
            "get_achat_credit_options": self.get_achat_credit_options(),
            "get_soldes_options": self.get_soldes_options(),
            "get_soldeMoney_options": self.get_soldeMoney_options(),
            "get_cleanSoldeStr_options": self.get_cleanSoldeStr_options(),
            "get_forcer_demande_solde_options": self.get_forcer_demande_solde_options(),
            "get_forcer_demande_solde_cdf_options": self.get_forcer_demande_solde_cdf_options(),
            "get_achat_forfait_appel_options": self.get_achat_forfait_appel_options(),
            "get_achat_forfait_internet_options": self.get_achat_forfait_internet_options(),
            "get_partager_vos_megas_options": self.get_partager_vos_megas_options(),
            "get_partager_vos_minutes_options": self.get_partager_vos_minutes_options(),
            "get_envoyer_des_unites_options": self.get_envoyer_des_unites_options(),
            "get_solde_unites_options": self.get_solde_unites_options(),
            "get_solde_minutes_options": self.get_solde_minutes_options(),
            "get_solde_internet_options": self.get_solde_internet_options(),
            "get_historique_options": self.get_historique_options(),
            "get_getFrais_options": self.get_getFrais_options(),
            "get_payerFrais_options": self.get_payerFrais_options()
        }
        return all_options

# NAY