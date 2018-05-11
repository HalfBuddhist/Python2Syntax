__author__ = 'Qingwei'

import urllib
import webbrowser

url = "http://www.163.com"

content = urllib.urlopen(url).read()

print(content)

open("163.com.html", "w").write(content)


#webbrowser.open_new_tab("163.com.html")

#ebbrowser.open_new_tab("www.163.com")