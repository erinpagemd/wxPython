#!/usr/bin/env python
import wx
class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,700))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()



        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'Paycheck Planner')
app.MainLoop()
