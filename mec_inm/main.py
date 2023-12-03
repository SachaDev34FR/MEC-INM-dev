from src.Med_Extractor import pubmed_connect as pconn
from src.Med_Extractor import esearch_pubmed as Esearch
from src.Med_Extractor import efetch_pubmed as Efetch
import pandas as pd

import src.constants as ct
def run():
    
    pconn.connect_pubmed_database()
    terms="neoplasms"
    liste_pmids = Esearch.esearch_dataset(terms)
    date_min = '2018/01/01'
    date_max = '2023/10/01'
    period = '180'
    # resultats_intervalle_dates = Esearch.esearch_dataset_dates(terms, date_min, date_max)  verifier format dates medline pour date_min et date_max
    # resultats_intervalle_period = Esearch.esearch_datas_period(terms, period)
    # crp.create_text_esearch_reports(liste_pmids, resultats_intervalle_dates,resultats_intervalle_period)
    df = Efetch.efetch_all_datas_from_ids(liste_pmids)
    Efetch.info_fetch_datas(df)
    
   
if __name__ == "__main__" :
    
    run()