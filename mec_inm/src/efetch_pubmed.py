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

ct.input_credentials()


def efetch_all_datas_from_ids():
    pass
