class Date:
    def setDate(self,d,m,y):
        self.day,self.month,self.year = d,m,y
    


d=Date()
d.setDate(1,12,2023)
print(d.day," ",d.month," ",d.year)
