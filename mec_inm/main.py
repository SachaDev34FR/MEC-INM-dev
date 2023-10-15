from src import pubmed_connect as pconn
from src import esearch_pubmed as Esearch
from src import create_reports_from_pubmed as crp

import src.constants as ct
def run():
    
    pconn.connect_pubmed_database()
    terms="green tea AND neoplasms"
    liste_pmids = Esearch.esearch_dataset(ct.DB, terms)
    resultats_intervalle_dates = Esearch.esearch_dataset_dates(terms, "2023/01/01", "2023/10/01")
    resultats_intervalle_period = Esearch.esearch_datas_period(terms,180)
    crp.create_text_reports(liste_pmids, resultats_intervalle_dates,resultats_intervalle_period)
    
    
    
if __name__ == "__main__" :
    
    run()