"""	dqcalendar.py
	a short library for doing math on the dungeon quest calendar
"""

import re

class DQCalendar:
	MONTHS = ['Ze', 'Di', 'Jha', 'Ka', 'Pho', 'Keo', 'Bak', 'Ti', 'Gu', 'Ze-Tau', 'Ze-Di', 'Ze-Jha']
	DAYS = ['Titen', 'Cen', 'Kalmis', 'Wentos', 'Obaous', 'Divu']
	FESTIVALS = ['Heb', 'Fion', 'Dai', 'Bayur']
	YEAR_LENGTH = 364
	MONTH_LENGTH = 30
	FEST_DAYS = {'H': 91, 'F': 182, 'D': 273, 'B': 364}

	YFMT = r'(?P<year>[\de]+)/((?P<month>[0-1]?\d)/(?P<day>[0-3]?\d)|(?P<fest>[BDFH]))'

	def date_to_dse(date_string):
		year = 0
		month = 0
		day = 0
		fest = ''

		dse = 0

		res = re.match(DQCalendar.YFMT, date_string)

		if res:
			ddict = res.groupdict()

			year = ddict['year']
			year = int(year[year.find('e')+1:])

			if ddict['month']:
				month = int(ddict['month'])
				day = int(ddict['day'])

				dse = year*DQCalendar.YEAR_LENGTH + (month-1)*DQCalendar.MONTH_LENGTH + day + (month-4)//3 + 1

			else:
				fest = ddict['fest']

				dse = year*DQCalendar.YEAR_LENGTH + DQCalendar.FEST_DAYS[fest] 

		else:
			raise ValueError("Invalid date format")
		
		return dse

	def dse_to_date(dse_num):
		year = (dse_num-1)//DQCalendar.YEAR_LENGTH
		fest = ''

		rem = dse_num - year*DQCalendar.YEAR_LENGTH

		date_string = ''

		if rem in DQCalendar.FEST_DAYS.values():
			fest = list(DQCalendar.FEST_DAYS.keys())[list(DQCalendar.FEST_DAYS.values()).index(rem)]
			
			date_string = f'{year}/{fest}'
		else:
			rem = rem-((rem)//(DQCalendar.YEAR_LENGTH//4)+1)

			month = (rem)//DQCalendar.MONTH_LENGTH+1

			day = (rem)%(DQCalendar.MONTH_LENGTH)+1

			date_string = f'{year}/{str(month).zfill(2)}/{str(day).zfill(2)}'

		return date_string

	
class DQDate:
	def __init__(self, date):
		if type(date) == str:
			self.dse = DQCalendar.date_to_dse(date)
		elif type(date)  == int:
			self.dse = date
		else:
			raise TypeError("Invalid type for date")

	def days_between(self, other):
		if(type(other) == DQDate):
			raise TypeError("Date comparisons require two dates")
		return abs(self.date-other.date)


