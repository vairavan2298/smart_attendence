from openpyxl import Workbook

book = Workbook()

sheet= book.active

rows = ((111,21,31),
		(21,311,41),
		(411,51,611)
)

for row in rows:
	# sheet.append(row).max_row
	sheet.append(row) 
book.save("d.xlsx")