import json

class Africell:
    def get_retrait_options(self):
        options = {
            "function called": "get_retrait_options",
            "ussd_code_to_invoke": "*1020#",
            "option1": "devise",
            "option2": "3",
            "option3": "numero",
            "option4": "montant",
            "option5": "password"
        }
        return json.dumps(options)

    def get_envoi_options(self):
        options = {
            "function called": "get_envoi_options",
            "ussd_code_to_invoke": "*1020#",
            "option1": "devise",
            "option2": "1",
            "option3": "numero",
            "option4": "montant",
            "option5": "password"
        }
        return json.dumps(options)

    # def get_bureau_options(self):
    #     options = {
    #         "function called": "get_bureau_options",
    #         "ussd_code_to_invoke": "*1020#",
    #         "option1": "devise",
    #         "option2": "1",
    #         "option3": "1",
    #         "option4": "numero",
    #         "option5": "montant",
    #         "option6": "password"
    #     }
    #     return json.dumps(options)

    def get_verificationTauxEtExecution_options(self):
        options = {
            "function called": "get_verificationTauxEtExecution_options",
            "ussd_code_to_invoke": "1020",
            "option1": "devise",
            "option2": "7",
            "option3": "1",
            "option4": "montant",
            "option5": "password"
        }
        return json.dumps(options)

    def get_achat_credit_options(self):
        options = {
            "function called": "get_achat_credit_options",
            "ussd_code_to_invoke": "*1020#",
            "option1": "devise",
            "option2": "2",
            "option3": "1",
            "option4.1": "1",
            "option4.2": "montant",
            "option4.3": "1",
            "option4.4": "password",
            "option5.1": "2",
            "option5.2": "numero",
            "option5.3": "montant",
            "option5.4": "1",
            "option5.5": "password"
        }
        return json.dumps(options)

    def get_soldes_options(self):
        options = {
            "function called": "get_soldes_options",
            "option1": ""
        }
        return json.dumps(options)

    def get_soldeMoney_options(self):
        options = {
            "function called": "get_soldeMoney_options",
            "phone_number": "Afrimoney",
            "regex_usd": "solde(.*?)USD",
            "regex_cdf": "solde(.*?)(CDF|Fc)",
            "usd_id": "USD",
            "cdf_id": "CDF"
        }
        return json.dumps(options)

    def get_cleanSoldeStr_options(self):
        options = {
            "function called": "get_cleanSoldeStr_options",
            "clean_regex": "[0-9](.*?)"
        }
        return json.dumps(options)

    def get_forcer_demande_solde_options(self):
        options = {
            "function called": "get_forcer_demande_solde_options",
            "ussd_code_to_invoke": "*1020#",
            "option1": "1",
            "option2": "5",
            "option3": "1",
            "option4": "1",
            "option5": "password"
        }
        return json.dumps(options)

    def get_forcer_demande_solde_cdf_options(self):
        options = {
            "function called": "get_forcer_demande_solde_cdf_options",
            "ussd_code_to_invoke": "*1020#",
            "option1": "2",
            "option2": "5",
            "option3": "1",
            "option4": "1",
            "option5": "password"
        }
        return json.dumps(options)

    def get_achat_forfait_appel_options(self):
        options = {
            "function called": "get_achat_forfait_appel_options",
            "ussd_code_to_invoke_1": "*111#",
            "ussd_code_to_invoke_2": "*1020#",
            "option1.1": "1",
            "option1.2": "2",
            "option1.3": "1",
            "option2.1": "devise",
            "option2.2": "2",
            "option2.3": "2",
            "option2.4": "7",
            "option2.5": "",
            "option2.6": ""
        }
        return json.dumps(options)

    def get_achat_forfait_internet_options(self):
        options = {
            "function called": "get_achat_forfait_appel_options",
            "ussd_code_to_invoke_1": "*111#",
            "ussd_code_to_invoke_2": "*1020#",
            "option1": "1",
            "option2": "1",
            "option3.1": "0",
            "option3.2": "numero",
            "option3.3": "",
            "option4.1": "devise",
            "option4.2": "2",
            "option4.3": "2",
            "option4.4": "1"
        }
        return json.dumps(options)

    def get_partager_vos_megas_options(self):
        options = {
            "function called": "get_partager_vos_megas_options",
            "ussd_code_to_invoke": "",
            "option1": ""
        }
        return json.dumps(options)

    def get_partager_vos_minutes_options(self):
        options = {
            "function called": "get_partager_vos_minutes_options",
            "ussd_code_to_invoke": "",
            "option1": ""
        }
        return json.dumps(options)

    def get_envoyer_des_unites_options(self):
        options = {
            "function called": "get_envoyer_des_unites_options",
            "ussd_code_to_invoke": "*111#",
            "option1": "7",
            "option2": "numero",
            "option3": "montant",
            "option4": "password"
        }
        return json.dumps(options)

    def get_solde_unites_options(self):
        options = {
            "function called": "get_solde_unites_options",
            "ussd_code_to_invoke": "*1000#"
        }
        return json.dumps(options)

    def get_solde_minutes_options(self):
        options = {
            "function called": "get_solde_minutes_options",
            "ussd_code_to_invoke": "*111*20#",
            "option1": "1"
        }
        return json.dumps(options)

    def get_solde_internet_options(self):
        options = {
            "function called": "get_solde_internet_options",
            "ussd_code_to_invoke": "*111*20#",
            "option1": "2"
        }
        return json.dumps(options)

    def get_historique_options(self):
        options = {
            "function called": "get_historique_options",
            "phone_number": "Afrimoney",
            "regex_recu": "recu(.*?)(USD|CDF)(.*?)[.]",
            "regex_envoi": "envoye(.*?)(USD|CDF)(.*?)[.]",
            "regex_retire": "retire(.*?)(USD|CDF)(.*?)[.]"
        }
        return json.dumps(options)

    def get_getFrais_options(self):
        options = {
            "function called": "get_getFrais_options",
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
        return json.dumps(options)

    def get_payerFrais_options(self):
        options = {
            "function called": "get_payerFrais_options",
            "ussd_code_to_invoke": "*1020#",
            "option1": "devise",
            "option2": "1",
            "option3": "0902201442",
            "option4": "montant",
            "option5": "password"
        }
        return json.dumps(options)

# NAY