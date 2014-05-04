import wx
import wx.grid
import pymongo

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
        self.SetCellValue(0, 0, FirstResultTitle)
        self.SetCellValue(0, 1, "B")
        self.SetRowLabelValue(1, "2")
        self.SetCellValue(1, 0, "C")
        self.SetCellValue(1, 1, "D")
        self.SetRowLabelValue(2, "3")
        self.SetCellValue(2, 0, "E")
        self.SetCellValue(2, 1, "F")
        self.SetRowLabelValue(3, "G")
        self.SetCellValue(3, 0, "G")
        self.SetCellValue(3, 1, "I")
        self.SetRowLabelValue(4, "5")
        self.SetCellValue(4, 0, "J")
        self.SetCellValue(4, 1, "K")
        self.SetRowLabelValue(5, "6")
        self.SetCellValue(5, 0, "L")
        self.SetCellValue(5, 1, "M")
        self.SetRowLabelValue(6, "7")
        self.SetCellValue(6, 0, "N")
        self.SetCellValue(6, 1, "O")
        self.SetRowLabelValue(7, "8")
        self.SetCellValue(7, 0, "P")
        self.SetCellValue(7, 1, "Q")
        self.SetRowLabelValue(8, "9")
        self.SetCellValue(8, 0, "R")
        self.SetCellValue(8, 1, "S")

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Summary Screen",
                size=(300, 300))
        grid = SimpleGrid(self)

        #Title Data

#First Result
FirstResultRawTitle = db.HomeFinance.find_one(
    {},
    {"Title": 1, "_id": 0}
)
#.skip(n)
#if there is no title print "Not Specified..."

FirstResultTitle = str(FirstResultRawTitle)

#FirstResultDate =

#Second Result

#Third Result

#Fourth Result

#Fifth Result

#Sixth Result

#Seventh Result

#Eighth Result

#Ninth Result

        #Query the database....Find the Title and display
        #return one result, return one result and skip one...etc


        #Amount Data
        #Query the database...sort based on same as title data ... Find the amount and display
        #Chose display color based on Inc/Exp field

        #Put a box at the bottom that displays the current balance of showing entries

ColLabels = ("Title", "Amount")
RowLabels = ("1", "2", "3", "4", "5", "6", "7", "8", "9")




app = wx.PySimpleApp()
frame = TestFrame(None)
frame.Show(True)
app.MainLoop()
