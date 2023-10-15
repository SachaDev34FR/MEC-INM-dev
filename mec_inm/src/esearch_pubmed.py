from dataclasses import Field
from Bio import Entrez
from Bio import Medline
from attr import field
from loguru import logger
import sys
import requests
import datetime
import json

import src.constants as ct

Entrez.api_key = ct.ENTREZ_API_KEY
Entrez.email = ct.ENTREZ_EMAIL
Entrez.tool = ct.ENTREZ_TOOL

def esearch_dataset(db, terms, **keywds):
    """
    Perform a search on a given database using the provided search terms and optional keyword arguments.

    Parameters:
        db (str): The name of the database to search.
        terms (str): The search terms to use.
        **keywds: Additional keyword arguments that can be passed to the Entrez.esearch function.

    Returns:
        list: A list of record IDs matching the search criteria.
    """
    handle = Entrez.esearch(db=ct.DB, term=terms, retype="medline", retmax=10)
    record = Entrez.read(handle)
    handle.close()
    if int(record["Count"]) < 1: # type: ignore
        logger.info("No results") # type: ignore
    else:
        logger.info(f"Results found : {record['Count']}", feature={record['Count']}) # type: ignore
        return record['IdList'] # type: ignore
        
# fonction a cree esearch pour un intervalle date_min et date_max
def esearch_dataset_dates(terms,date_min, date_max):
    """
    Searches a dataset within a specified date range.

    Args:
        db (str): The database to search in.
        terms (str): The search terms.
        date_min (str): The minimum date in the format "YYYY/MM/DD".
        date_max (str): The maximum date in the format "YYYY/MM/DD".

    Returns:
        list: A list of record IDs matching the search criteria, or None if the date format is invalid.
    """
    # date format is YYYY/MM/DD in PubMed
    # Validate date format
    try:
        date_min = datetime.datetime.strptime(date_min, "%Y/%m/%d")
        date_max = datetime.datetime.strptime(date_max, "%Y/%m/%d")
    except ValueError:
        logger.error("Invalid date format. Please use YYYY/MM/DD format.")
        return None
    handle = Entrez.esearch(   # type: ignore
        db=ct.DB,
        term=f"{terms}",
        mindate=date_min,
        maxdate=date_max,
        datetype="pdat",
        retype="medline",
        retmax=10,
        )
    record = Entrez.read(handle)
    handle.close()
    if int(record["Count"]) < 1: # type: ignore
        logger.warning("No results for input dates")
    else:
        logger.info(f"Results found: {record['Count']}", feature={record['Count']}) # type: ignore
        return record['IdList'] # type: ignore


def esearch_datas_period(terms, period):
    handle = Entrez.esearch(   # type: ignore
        db=ct.DB,
        term=f"{terms}",
        reldate=int(period),
        datetype="pdat",
        retype="medline",
        retmax=10,
        )
    record = Entrez.read(handle)
    handle.close()
    if int(record["Count"]) < 1: # type: ignore
        logger.warning("No results for input period")
    else:
        logger.info(f"Results found: {record['Count']}", feature={record['Count']}) # type: ignore
        return record['IdList'] # type: ignore