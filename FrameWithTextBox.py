import wx

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "PayCheckPlanner", size=(300, 300))
        panel = wx.Panel(self, -1)

        #Enter Date
        wx.StaticText(panel, -1, "Date", pos=(10, 10))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(100, 10))

        #Enter Title
        wx.StaticText(panel, -1, "Title", pos=(10, 40))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(100, 40))

        #Enter Amount
        wx.StaticText(panel, -1, "Amount", pos=(10, 70))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(100, 70))

        #Expense/Income Button
        button = wx.Button(panel, id=wx.ID_ANY, label="Income", pos=(60, 90))
        button = wx.Button(panel, id=wx.ID_ANY, label="Expense", pos=(150, 90))

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show(True)
app.MainLoop()
