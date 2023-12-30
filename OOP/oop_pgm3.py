class Date:
    def setDate(self,d,m,y):
        self.day,self.month,self.year = d,m,y
    def getDay(self):return self.day
    def getMonth(self):return self.month
    def getYear(self):return self.year
    def print(self):
        print("{}-{}-{}".format(self.getDay(),self.getMonth(),self.getYear()))
    


d=Date()
d.setDate(1,12,2023)
d.print()
