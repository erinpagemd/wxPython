#Make each field a string
Date = str(self.EditDate.GetValue())
Title = str(self.EditTitle.GetValue())
Amount = str(self.EditAmount.GetValue())

#Save to Database
Entry = db.HomeFinance.save({
    "Date": Date,
    "Title": Title,
    "Amount": Amount
    }
    )

client = pymongo.MongoClient("localhost", 27017)
db = client.PayCheck
db.HomeFinance
HomeFinance = db.HomeFinance    
