class time():

	def __init__(self, yy, mm, dd, hh, mn, ss):
			#yyyy-mm-dd hh-mm-ss
		
		second = 1
		minute = second * 60
		hour = minute * 60
		day = hour * 24
		month = day * 30.4167
		year = month * 12
	
		yy *= year
		mm *= month
		dd *= day
		hh *= hour
		mn *= minute
		ss *= second
		
		self.seconds = yy + mm + dd + hh + mn + ss
		
	def minutes(self):
		minutes = self.seconds/60
		return minutes
		
	def hours(self):
		hours = self.seconds/3600
		return hours

	def days(self):
		days = self.seconds/86400
		return days
		
	def months(self):
		months = self.seconds/2628002.88
		return months
		
	def years(self):
		years = self.seconds/31536034.56
		return years
		
	def total(self):
		print(self.seconds, "Segundos")
		print(self.minutes(), "Minutos")
		print(self.hours(), "Horas")
		print(self.days(), "Dias")
		print(self.months(), "Meses")
		print(self.years(), "Años")
		print()



