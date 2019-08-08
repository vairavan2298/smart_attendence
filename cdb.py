from datetime import datetime
def d():
	now = datetime.now()
 
	# print("now =", now)
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	# print("date and time =", dt_string)
	return dt_string	

def val():
	s='201610A01'
	return s
