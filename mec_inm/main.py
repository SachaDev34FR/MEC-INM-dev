from src import pubmed_connect as pconn
from src import esearch_pubmed as Esearch
from src import create_reports_from_pubmed as crp
from src import efetch_pubmed as Efetch
import pandas as pd

import src.constants as ct
def run():
    
    pconn.connect_pubmed_database()
    terms="green tea AND neoplasms"
    liste_pmids = Esearch.esearch_dataset(terms)
    date_min = '2023/01/01'
    date_max = '2023/10/01'
    period = '180'
    resultats_intervalle_dates = Esearch.esearch_dataset_dates(terms, date_min, date_max)
    resultats_intervalle_period = Esearch.esearch_datas_period(terms, period)
    crp.create_text_esearch_reports(liste_pmids, resultats_intervalle_dates,resultats_intervalle_period)
    df = Efetch.efetch_all_datas_from_ids(terms)
    Efetch.info_fetch_datas(df)
    
    
if __name__ == "__main__" :
    
    run()