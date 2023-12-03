from dataclasses import Field
from Bio import Entrez
from Bio import Medline
from attr import field
from loguru import logger
import sys
import requests
import datetime
import json
import pandas as pd 

import src.esearch_pubmed as sch
import src.constants as ct

ct.input_credentials()


def efetch_all_datas_from_ids(terms):
    all_ids = sch.esearch_all_dataset(terms)
    handle = Entrez.efetch(db=ct.DB, id=all_ids, rettype="Medline", retmode="text", retmax=len(all_ids))
    records = Medline.parse(handle)
    datas = list(records)
    
    return pd.DataFrame(datas)
    
def info_fetch_datas(df):
    lignes = df.shape[0]
    champs = df.shape[1]
    liste_cols = df.columns
    nulles  = feature=df.isna().sum()
    logger.info(f"Nombres de publications: {lignes}")
    logger.info(f"Nombre de Champs: {champs}")
    logger.info(f"valeurs nulles ou non attribuees dqns le tableau: {nulles}")
    logger.info(f"liste des champs :{liste_cols}")
    
    
    
