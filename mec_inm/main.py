from src import pubmed_connect as pconn
from src import esearch_pubmed as Esearch
from src import create_reports_from_pubmed as crp

import src.constants as ct
def run():
    
    pconn.connect_pubmed_database()
    terms="green tea AND neoplasms"
    liste_pmids = Esearch.esearch_dataset(ct.DB, terms)
    liste_journaux = Esearch.get_journal_names(terms)
    resultats_intervalle_dates = Esearch.esearch_dataset_dates(ct.DB, terms, "2020/01/01", "2023/10//01")
    crp.create_text_reports(liste_pmids, liste_journaux, resultats_intervalle_dates)
    
    
    
if __name__ == "__main__" :
    
    run()