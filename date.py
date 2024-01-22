from datetime import datetime

def days(date):
    input_date = datetime(date['year'], date['month'], date['day'])
    reference_date = datetime(2000, 1, 1)
    delta = input_date - reference_date
    return delta.days

date_struct = {'month': 12, 'day': 19, 'year': 2099}
result = days(date_struct)
print(f"Number of days from 01/01/2000 to {date_struct['month']}/{date_struct['day']}/{date_struct['year']} is {result}")
