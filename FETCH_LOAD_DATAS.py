__doc__ = """Ce module contient la définition des variables de chemins de destination ainsi que l'importation des librairies nécessaires à la définition des 2 fonctions suivantes:
	- fetch_food_data() : qui sert à télécharger dans un sous-dossier du dossier de travail, 'datasets', le fichier .csv contenant 	le jeu de données complet issu de https://data.seattle.gov/dataset/2016-Building-Energy-Benchmarking/2bpz-gwpy
	- load_food_data() : qui sert à charger ce jeu de données dans un DataFrame
"""


import os
import urllib
import pandas as pd

DOWNLOAD_URL = "https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Data_Scientist_P4/2016_Building_Energy_Benchmarking.csv"
FILE_NAME = "2016_Building_Energy_Benchmarking.csv"
DATA_PATH = "datasets"
FILE_PATH = os.path.join(DATA_PATH, FILE_NAME)

def fetch_food_data(data_path=DATA_PATH, dwnld_url=DOWNLOAD_URL, file_path=FILE_PATH):

	"""fonction de téléchargement des données"""

	if not os.path.isdir(data_path):
    		os.makedirs(data_path)
	urllib.request.urlretrieve(dwnld_url, file_path)


def load_food_data(file_path=FILE_PATH):

	"""fonction de chargement des données extraites dans un dataframe"""

	return pd.read_csv(file_path)
