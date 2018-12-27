import pandas as pd
import datetime


class Conversion(object):
	"""docstring for Conversion"""
	def __init__(self):
		pass
	
	def json_to_excel(self,path,output_name):

		df = pd.read_json(path)
		df.to_excel(output_name + '.xls', index=False)

	def json_pandas_dataFrame(self,path):

		return pd.read_json(path)

path = 'C://Users/HP/Desktop/ADN/Computer-Vision-project/Data-collection/dataset/gaaraas/gaaraasDataU.json'
c = Conversion()
todayDate = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
output_name = "gaaraasData_"+todayDate
c.json_to_excel(path,output_name)