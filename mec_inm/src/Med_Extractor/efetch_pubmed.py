from dataclasses import Field
from Bio import Entrez
from Bio import Medline
from loguru import logger
import sys
import datetime
import json
import pandas as pd 

import src.constants as ct

ct.input_credentials()


def efetch_all_datas_from_ids(all_ids):
    handle = Entrez.efetch(db=ct.DB, id=all_ids, rettype="Medline", retmode="text", retmax=len(all_ids))
    records = Medline.parse(handle)
    datas = list(records)
    
    return pd.DataFrame(datas)
    
def info_fetch_datas(df):
    lignes = df.shape[0]
    champs = df.shape[1]
    liste_cols = df.columns
    nulles  = df.isna().sum()
    logger.info(f"Nombres de publications: {lignes}")
    logger.info(f"Nombre de Champs: {champs}")
    for _, row in df.iterrows():
        na_values = row.isna().sum()
        logger.info(f"colonne : {row.name} | valeurs non nulles de chaque colonne : {na_values}")
    logger.info(f"liste des champs :{liste_cols}")
    
    
