import csv, sys
import pandas as pd

def organizeCompanies():
	data = pd.read_csv("/Users/EthanWilk/Downloads/options.csv")
	print(data)

organizeCompanies()
