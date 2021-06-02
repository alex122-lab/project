class Date:

    def __init__(self, date_as_string):
        self.date_as_string = date_as_string


    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls, day, month, year

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2999


date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
print(date2)
print(is_date)



