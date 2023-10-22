from Bio import Entrez
from Bio import Medline
from loguru import logger
import sys
import datetime
import json

import constants as ct

Entrez.api_key = ct.ENTREZ_API_KEY
Entrez.email = ct.ENTREZ_EMAIL
Entrez.tool = ct.ENTREZ_TOOL

def get_pmc_articles_ids(ids):
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
    records = Entrez.read(handle)
    for record in records: # type: ignore
        try:
            print(record['PMC'])
            liste_pmc.append(record["PMC"])
        except Exception :
            print("Pas de PMC")
            liste_no_text.append(record["PMID"])
    
    return liste_pmc, liste_no_text

def get_author_nationalities(pmid):
        # Récupération des données de l'article
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
        record = Entrez.read(handle)
    
        # Récupération des informations sur les auteurs
        authors = record[0].get("FAU", []) # type: ignore
    
        # Récupération des nationalités des auteurs
        nationalities = []
        for author in authors:
            last_name, initials = author.split(", ")
            author_summary = Entrez.esummary(db="pubmed", id=pmid)
            author_summary_record = Entrez.read(author_summary)
            for author_record in author_summary_record: # type: ignore
                if last_name in author_record["LastName"] and initials in author_record["Initials"]:
                    nationalities.append(author_record.get("FullAffiliation", ""))
                    break
    
        return nationalities
    
    
liste_pmc = []
liste_no_text = []
ids = ['30205425''34206736','33027981','27634207','30585192','32660101','36142616','28353571','35504067','32118296']
for pmid in ids:
    nationalities = get_author_nationalities(pmid)
    print(nationalities)
    liste_pmc, liste_no_text = get_pmc_articles_ids(ids)
    print(liste_pmc)
    print(liste_no_text)