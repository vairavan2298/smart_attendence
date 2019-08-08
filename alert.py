# import xlsxwriter module 
from datetime import datetime
import xlsxwriter 
import cdb

def dbval(val):

		workbook = xlsxwriter.Workbook('attendence.xlsx') 

		# By default worksheet names in the spreadsheet will be 
		# Sheet1, Sheet2 etc., but we can also specify a name. 
		worksheet = workbook.add_worksheet("Sheet1") 
		# val1 = cdb.val()
		now = datetime.now()
 
	# print("now =", now)
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	# print("date and time =", dt_string)

		val2 = dt_string
		# Some data we want to write to the worksheet. 
		scores = (
			[val] 
			# [val2]
			# ['ankit', 1000], 
			# ['rahul', 100], 
			# ['priya', 300], 
			# ['harshita', 50], 
		) 

		# Start from the first cell. Rows and 
		# columns are zero indexed. 
		row = 0
		col = 0

		# Iterate over the data and write it out row by row. 
		for name in (scores): 
			worksheet.write(row, col, name,mode = 'a') 
			# worksheet.write(row, col + 1, score,mode = 'a') 


		workbook.close() 
