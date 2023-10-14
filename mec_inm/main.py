from src import pubmed_connect as pconn
from src import esearch_pubmed as Esearch

import src.constants as ct
def run():
    
    pconn.connect_pubmed_database()
    term="green tea AND neoplasms"
    Esearch.esearch_dataset(ct.DB, term)
    
    
    
    
if __name__ == "__main__" :
    
    run()