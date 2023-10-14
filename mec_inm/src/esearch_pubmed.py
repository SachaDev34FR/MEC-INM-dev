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
        logger.info("No results") # type: ignore
    else:
        logger.info("Results found : {}".format(record['Count']), feature={record['Count']}) # type: ignore") 
        logger.info("Ten first results: {}".format(record['IdList'])) # type: ignore") # type: ignore
        logger.info("====================================END--ESEARCH==================================")
        return record['IdList'] # type: ignore
        