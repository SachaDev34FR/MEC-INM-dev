from dataclasses import Field
from Bio import Entrez
from Bio import Medline
from attr import field
from loguru import logger
import sys

import src.constants as ct

Entrez.api_key = ct.ENTREZ_API_KEY
Entrez.email = ct.ENTREZ_EMAIL
Entrez.tool = ct.ENTREZ_TOOL

def esearch_dataset(db, terms, **keywds):
    handle = Entrez.esearch(db=ct.DB, term=terms, retype="medline", retmax=10)
    record = Entrez.read(handle)
    handle.close()
    if int(record["Count"]) < 1:
        print("No results") # type: ignore
    else:
        print("Results found") # type: ignore
        print(record["IdList"]) # type: ignore
        