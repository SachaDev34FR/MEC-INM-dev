from click import File
from loguru import logger
import sys

import src.constants as ct


def create_text_reports(a, b, c):

 with open('pubmed_fields_datas.txt', 'w') as file:
     file.write("Liste des PMIDs: " + str(a) + '\n')
     file.write("Liste des journaux: " + str(b) + '\n')
     file.write("Liste des dates: " + str(c) + '\n')