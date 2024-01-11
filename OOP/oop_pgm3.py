class Date:
    def setDate(self,d,m,y):
        self.day,self.month,self.year = d,m,y
    def getDay(self):return self.day
    def getMonth(self):return self.month
    def getYear(self):return self.year
    def print(self):
        print("{}-{}-{}".format(self.getDay(),self.getMonth(),self.getYear()))
    

from datetime import datetime

d=Date()
current_datetime = datetime.now()
current_date = current_datetime.date()
# Setting the date to current date
d.setDate(current_date.day,current_date.month,current_date.year)
d.print()
