from Bio import Entrez
from Bio import Medline
from loguru import logger
import sys
import datetime
import json

import mec_inm.src.constants as ct

Entrez.api_key = ct.ENTREZ_API_KEY
Entrez.email = ct.ENTREZ_EMAIL
Entrez.tool = ct.ENTREZ_TOOL

def get_pmc_articles_ids(ids):
    liste_pmc = []
    liste_no_text = []
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline")
    records = Entrez.read(handle)
    print(records)
    
    for record in records: # type: ignore
        if 'PMC' in record:
            print(record['PMC'])
            liste_pmc.append(record['PMC'])
        else:
            print("Pas de PMC")
            liste_no_text.append(record['PMID'])
    
    return liste_pmc, liste_no_text

def get_author_nationalities(pmid):
    hendle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
    result = Entrez.read(hendle)
    authors = result[0].get("FAU", []) # type: ignore
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

ids = ['30205425', '34206736', '33027981', '27634207', '30585192', '32660101', '36142616', '28353571', '35504067', '32118296']
# liste_pmc, liste_no_text = get_pmc_articles_ids(ids)
# print(liste_pmc)
# print(liste_no_text)
for pmid in ids:
    nationalities = get_author_nationalities(pmid)
    print(nationalities)
    