#!/usr/bin/env python
# coding=utf-8
'例19.1 标签组件演示（tkhello1.py）'

import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top, text='Hello World!')
label.pack()
Tkinter.mainloop()