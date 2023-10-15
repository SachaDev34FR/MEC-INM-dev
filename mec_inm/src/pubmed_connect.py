from dataclasses import Field
from Bio import Entrez
from loguru import logger
import sys

import src.constants as ct

ct.input_credentials()

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
    logger.info(
        f"Nombres de documents en base :{result['DbInfo']['Count']}",
        feature={result['DbInfo']['Count']},
    )
    logger.info(
        f"Date de la dernière mise à jour Pubmed: {result['DbInfo']['LastUpdate']}",
        feature={result['DbInfo']['LastUpdate']},
    )

    with open('pubmed_fields_datas.txt', 'w') as file:
            handle = Entrez.einfo(db=ct.DB)
            result = Entrez.read(handle) 
            file.write(result['DbInfo']['Description'] + '\n') # type: ignore
            file.write("nombres de documents en base : " + str(result['DbInfo']['Count']) + '\n') # type: ignore
            file.write("derniere mise a jour Pubmed: " + result['DbInfo']['LastUpdate'] + '\n') # type: ignore
            for field in result["DbInfo"]["FieldList"]: # type: ignore
                file.write(f"{field['Name']} | {field['FullName']} | {field['Description']}, Type Datas : Date-> {field['IsDate']}, Nombre-> {field['IsNumerical']}\n")