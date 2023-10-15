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


def connect_pubmed_database():
    """
    Connects to the Pubmed database and retrieves information about it.

    Returns:
        None
    """
    handle = Entrez.einfo(db=ct.DB)
    result = Entrez.read(handle)
    
    logger.add(sys.stderr, level='INFO', format= "{time} {level} {message}")   
    logger.add("mec-inm_logs.log", level='INFO', format= "{time} {level} {message}")
    logger.info("===================================START===================================")
    logger.info("Description: {}".format(result['DbInfo']['Description'], feature={result['DbInfo']['Description']}))
    logger.info("Nombres de documents en base :{}".format(result['DbInfo']['Count']), feature={result['DbInfo']['Count']})
    logger.info("Date de la dernière mise à jour Pubmed: {}".format(result['DbInfo']['LastUpdate']), feature={result['DbInfo']['LastUpdate']})
        
    with open('pubmed_fields_datas.txt', 'w') as file:
            handle = Entrez.einfo(db=ct.DB)
            result = Entrez.read(handle)
    
            file.write(result['DbInfo']['Description'] + '\n')
            file.write("nombres de documents en base : " + str(result['DbInfo']['Count']) + '\n')
            file.write("derniere mise a jour Pubmed: " + result['DbInfo']['LastUpdate'] + '\n')
            for field in result["DbInfo"]["FieldList"]:
                file.write(f"{field['Name']} | {field['FullName']} | {field['Description']}, Type Datas : Date-> {field['IsDate']}, Nombre-> {field['IsNumerical']}\n")