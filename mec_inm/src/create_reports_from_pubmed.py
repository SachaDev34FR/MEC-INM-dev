from click import File
from loguru import logger
import sys

import src.constants as ct


def create_text_esearch_reports(a, b, c):

 with open('report_pubmed_datas.txt', 'w') as file:
  file.write(f"Liste des PMIDs: {str(a)}" + '\n')
  file.write(f"Liste des pmids dans les dates: {str(b)}" + '\n')
  file.write(f"Liste pmid durant la periode: {str(c)}" + '\n')