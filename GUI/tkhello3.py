#!/usr/bin/env python
# coding=utf-8
'例19.3 标签和按钮组件演示（tkhello3.py）'

import Tkinter

top = Tkinter.Tk()
hello = Tkinter.Label(top, text='Hello World!')
hello.pack()

quit = Tkinter.Button(top, text='QUIT',command=top.quit, bg='red', fg='white')
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()