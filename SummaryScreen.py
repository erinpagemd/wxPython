import wx
import wx.grid
import pymongo
import sys

client = pymongo.MongoClient("localhost", 27017)
db = client.PayCheck
db.HomeFinance
HomeFinance = db.HomeFinance


#sourcecode= http://www.java2s.com/Tutorial/Python/0380__wxPython/extendswxgridPyGridTableBase.htm

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.CreateGrid(9, 2)
        self.SetColLabelValue(0, "Title")
        self.SetColLabelValue(1, "Amount")
        self.SetRowLabelValue(0, "1")
        self.SetCellValue(0, 0, FirstResult['Title'])
        self.SetCellValue(0, 1, FirstResult['Amount'])
        self.SetRowLabelValue(1, "2")
        self.SetCellValue(1, 0, SecondResult['Title'])
        self.SetCellValue(1, 1, SecondResult['Amount'])
        self.SetRowLabelValue(2, "3")
        self.SetCellValue(2, 0, ThirdResult['Title'])
        self.SetCellValue(2, 1, ThirdResult['Amount'])
        self.SetRowLabelValue(3, "4")
        self.SetCellValue(3, 0, FourthResult['Title'])
        self.SetCellValue(3, 1, FourthResult['Amount'])
        self.SetRowLabelValue(4, "5")
        self.SetCellValue(4, 0, FifthResult['Title'])
        self.SetCellValue(4, 1, FifthResult['Amount'])
        self.SetRowLabelValue(5, "6")
        self.SetCellValue(5, 0, SixthResult['Title'])
        self.SetCellValue(5, 1, SixthResult['Amount'])
        self.SetRowLabelValue(6, "7")
        self.SetCellValue(6, 0, SeventhResult['Title'])
        self.SetCellValue(6, 1, SeventhResult['Amount'])
        self.SetRowLabelValue(7, "8")
        self.SetCellValue(7, 0, EighthResult['Title'])
        self.SetCellValue(7, 1, EighthResult['Amount'])
        self.SetRowLabelValue(8, "9")
        self.SetCellValue(8, 0, NinthResult['Title'])
        self.SetCellValue(8, 1, NinthResult['Amount'])

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Summary Screen",
                size=(400, 300))
        grid = SimpleGrid(self)

#Query Results:: need to turn query into a cursor??
#FirstResult = db.HomeFinance.find_one()


cursor = db.HomeFinance.find()
FirstResult = cursor.sort("Date")[1]
SecondResult = cursor.sort("Date")[2]
ThirdResult = cursor.sort("Date")[3]
FourthResult = cursor.sort("Date")[4]
FifthResult = cursor.sort("Date")[5]
SixthResult = cursor.sort("Date")[6]
SeventhResult = cursor.sort("Date")[7]
EighthResult = cursor.sort("Date")[8]
NinthResult = cursor.sort("Date")[9]

        #Chose display color of Amount based on Inc/Exp field
        #If there is not a result...print Null in the box
        #Put a box at the bottom that displays the current balance of showing entries

ColLabels = ("Title", "Amount")
RowLabels = ("1", "2", "3", "4", "5", "6", "7", "8", "9")




app = wx.PySimpleApp()
frame = TestFrame(None)
frame.Show(True)
app.MainLoop()
