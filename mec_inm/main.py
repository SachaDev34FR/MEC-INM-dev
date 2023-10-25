from mec_inm.src import pubmed_connect as pconn
from mec_inm.src import esearch_pubmed as Esearch
from mec_inm.src  import efetch_pubmed as Efetch 
from mec_inm.src import create_reports_from_pubmed as crp

import mec_inm.src.constants as ct
def run():
    
    pconn.connect_pubmed_database()
    terms="green tea AND neoplasms"
    liste_pmids = Esearch.esearch_dataset(ct.DB, terms)
    pmcs, no_pmcs = Efetch.get_pmc_articles_ids(liste_pmids)
    print(pmcs)
    print(no_pmcs)    

    # liste_journaux = Esearch.get_journal_names(terms)
    #resultats_intervalle_dates = Esearch.esearch_dataset_dates(ct.DB, terms, "2020/01/01", "2023/10//01")
    #crp.create_text_reports(liste_pmids, resultats_intervalle_dates)
    
    
    
if __name__ == "__main__" :
    
    run()