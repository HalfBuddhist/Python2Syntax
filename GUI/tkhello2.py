#!/usr/bin/env python
# coding=utf-8
'例19.2 按钮组件演示（tkhello2.py）'

import Tkinter
top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello World!',command=top.quit)
quit.pack()
Tkinter.mainloop()