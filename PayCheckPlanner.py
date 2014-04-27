import wx
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.PayCheck
db.HomeFinance

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "PayCheckPlanner", size=(400, 500))
        panel = wx.Panel(self, -1)

        self.panel = wx.Panel(self)

        #Show Entry
        self.quote = wx.StaticText(self.panel, label= "Recently Added:  ")
        self.resultDate = wx.StaticText(self.panel, label= "")
        self.resultDate.SetForegroundColour(wx.BLUE)
        self.resultTitle = wx.StaticText(self.panel, label= "")
        self.resultTitle.SetForegroundColour(wx.BLUE)
        self.resultAmount = wx.StaticText(self.panel, label= "")
        self.resultAmount.SetForegroundColour(wx.BLUE)

        #Enter Date
        self.lblDate = wx.StaticText(self.panel, label = "Date: ")
        self.editDate = wx.TextCtrl(self.panel, size=(140, -1))

        #Enter Title
        self.lblTitle = wx.StaticText(self.panel, label = "Title: ")
        self.editTitle = wx.TextCtrl(self.panel, size=(140, -1))

        #Enter Amount
        self.lblAmount= wx.StaticText(self.panel, label = "Amount: ")
        self.editAmount= wx.TextCtrl(self.panel, size=(140, -1))

        #Expense/Income Button
        #button = wx.Button(panel, id=wx.ID_ANY, label="Income", pos=(60, 100))
        #button = wx.Button(panel, id=wx.ID_ANY, label="Expense", pos=(150, 100))

        #Save Button
        self.button = wx.Button(self.panel, label="Save")

        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(50, 50)
        self.sizer.Add(self.quote, (0, 0))
        self.sizer.Add(self.resultDate, (0, 1))
        self.sizer.Add(self.resultTitle, (1, 1))
        self.sizer.Add(self.resultAmount, (2, 1))
        self.sizer.Add(self.lblDate, (3, 0))
        self.sizer.Add(self.editDate, (3, 1))
        self.sizer.Add(self.lblTitle, (4, 0))
        self.sizer.Add(self.editTitle, (4, 1))
        self.sizer.Add(self.lblAmount, (5,0))
        self.sizer.Add(self.editAmount,(5, 1))
        self.sizer.Add(self.button, (6, 0), (1, 2), flag=wx.EXPAND)

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, wx.ALL | wx.EXPAND)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)


        # Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

    #Capture Entry
    def OnButton(self, e):
        self.resultDate.SetLabel(self.editDate.GetValue())
        self.resultTitle.SetLabel(self.editTitle.GetValue())
        self.resultAmount.SetLabel(self.editAmount.GetValue())


        #Make each field a string
        Date = str(self.editDate.GetValue())
        Title = str(self.editTitle.GetValue())
        Amount = str(self.editAmount.GetValue())

        #Save to Database
        db.HomeFinance.save({
            "Date": Date,
            "Title": Title,
            "Amount": Amount
            }
            )


app = wx.PySimpleApp()
frame = MyFrame()
frame.Show(True)
app.MainLoop()
