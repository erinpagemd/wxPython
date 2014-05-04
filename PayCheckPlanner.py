import wx
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.PayCheck
db.HomeFinance
HomeFinance = db.HomeFinance

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "PayCheckPlanner", size=(600, 500))
        panel = wx.Panel(self, -1)

        self.panel = wx.Panel(self)

        #Show Entry
        self.Quote = wx.StaticText(self.panel, label= "Recently Added:  ")
        self.ResultDate = wx.StaticText(self.panel, label= "")
        self.ResultDate.SetForegroundColour(wx.BLUE)
        self.ResultTitle = wx.StaticText(self.panel, label= "")
        self.ResultTitle.SetForegroundColour(wx.BLUE)
        self.ResultAmount = wx.StaticText(self.panel, label= "")
        self.ResultAmount.SetForegroundColour(wx.BLUE)
        self.ResultExpInc = wx.StaticText(self.panel, label="")
        self.ResultExpInc.SetForegroundColour(wx.BLUE)

        #Enter Date
        self.LabelDate = wx.StaticText(self.panel, label = "Date: ")
        self.EditDate = wx.TextCtrl(self.panel, size=(140, -1))

        #Enter Title
        self.LabelTitle = wx.StaticText(self.panel, label = "Title: ")
        self.EditTitle = wx.TextCtrl(self.panel, size=(140, -1))

        #Enter Amount
        self.LabelAmount= wx.StaticText(self.panel, label = "Amount: ")
        self.EditAmount= wx.TextCtrl(self.panel, size=(140, -1))

        #Enter Expense/Income (would like to make into a button)
        self.LabelExpInc = wx.StaticText(self.panel, label = "Type: ")
        self.EditExpInc = wx.TextCtrl(self.panel, size=(140, -1))

        #Save button
        self.SaveButton = wx.Button(self.panel, label="Save")


        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(50, 50)
        self.sizer.Add(self.Quote, (0, 0))
        self.sizer.Add(self.ResultDate, (0, 1))
        self.sizer.Add(self.ResultTitle, (1, 1))
        self.sizer.Add(self.ResultAmount, (2, 1))
        self.sizer.Add(self.ResultExpInc, (3, 1))
        self.sizer.Add(self.LabelDate, (4, 0))
        self.sizer.Add(self.EditDate, (4, 1))
        self.sizer.Add(self.LabelTitle, (5, 0))
        self.sizer.Add(self.EditTitle, (5, 1))
        self.sizer.Add(self.LabelAmount, (6,0))
        self.sizer.Add(self.EditAmount,(6, 1))
        self.sizer.Add(self.LabelExpInc, (7,0))
        self.sizer.Add(self.EditExpInc, (7,1))
        self.sizer.Add(self.SaveButton, (8, 0), (1, 2), flag=wx.EXPAND)


        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, wx.ALL | wx.EXPAND)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        # Set event handlers
        self.SaveButton.Bind(wx.EVT_BUTTON, self.OnSaveButton)

    #Capture Entry
    def OnSaveButton(self, e):
        self.ResultDate.SetLabel(self.EditDate.GetValue())
        self.ResultTitle.SetLabel(self.EditTitle.GetValue())
        self.ResultAmount.SetLabel(self.EditAmount.GetValue())
        self.ResultExpInc.SetLabel(self.EditExpInc.GetValue())

        #Clear the fields after entering
        #self.ResultDate.Clear()
        #self.ResultTitle.Clear()
        #self.ResultAmount.Clear()

        #Make each field a string
        Date = str(self.EditDate.GetValue())
        Title = str(self.EditTitle.GetValue())
        Amount = str(self.EditAmount.GetValue())
        ExpInc = str(self.EditExpInc.GetValue())

        #Save to Database
        Entry = db.HomeFinance.save({
            "Date": Date,
            "Title": Title,
            "Amount": Amount,
            "ExpInc": ExpInc
            }
            )


app = wx.PySimpleApp()
frame = MyFrame()
frame.Show(True)
app.MainLoop()
