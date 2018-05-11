#!/usr/bin/env python
# coding=utf-8
"""
wxPython GUI 程序演示（animalWx.pyw）
我们的第三个例子使用wxPython（以及wxWidgets）。注意我们把所有的组件都放在一个布局
管理器里，以及该程序中更多的面向对象本质。
"""

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title=''):
        wx.Frame.__init__(self, parent, id, title, size=(200, 140))
        top = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD)
        lb = wx.StaticText(top, -1, 'Animals (in pairs; min: pair, max: dozen)')
        sizer.Add(lb)

        c1 = wx.StaticText(top, -1, 'Number:')
        c1.SetFont(font)
        ct = wx.SpinCtrl(top, -1, '2', min=2, max=12)
        sizer.Add(c1)
        sizer.Add(ct)

        c2 = wx.StaticText(top, -1, 'Type:')
        c2.SetFont(font)
        cb = wx.ComboBox(top, -1, '',
        choices=('dog', 'cat', 'hamster','python'))
        sizer.Add(c2)
        sizer.Add(cb)

        qb = wx.Button(top, -1, "QUIT")
        qb.SetBackgroundColour('red')
        qb.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, lambda e: self.Close(True), qb)
        sizer.Add(qb)

        top.SetSizer(sizer)
        self.Layout()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(title="wxWidgets")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

def main():
    app = MyApp()
    app.MainLoop()

if __name__ == '__main__':
    main()