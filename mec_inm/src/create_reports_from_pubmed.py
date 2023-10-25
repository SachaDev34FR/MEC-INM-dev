from click import File
from loguru import logger
import sys

import mec_inm.src.constants as ct


def create_text_reports(a, c):
    logger.add(sys.stderr, level='INFO', format= "{time} {level} {message}")   
    logger.add("mec-inm_logs.log", level='INFO', format= "{time} {level} {message}")
    logger.info("===================================START===================================")
    logger.info("Liste des PMIDs: {}".format(a))
    logger.info("Liste des dates: {}".format(c))

    with open('pubmed_fields_datas.txt', 'w') as file:
        file.write("Liste des PMIDs: " + str(a) + '\n')
        file.write("Liste des dates: " + str(c) + '\n')