#!/usr/bin/python
#coding:utf-8

from selenium import webdriver
import os
from Tkinter import *
import tkFileDialog
import tkMessageBox
import re


def getDriver():
        chrome_options = webdriver.ChromeOptions()
        # 设置无界面化运行
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=r"./chromedriver",chrome_options=chrome_options)
        return driver


def getHtml(driver,url):
    if url == "":
   		tkMessageBox.showwarning("警告","url不能为空")
    else:
		driver.get(url)
		return driver.page_source


def getArticle(html,pre,beh):
	arti = re.findall(pre + '(.+)' + beh,html)
	return arti[0]

#点击按钮执行的动作
def test(e1,e2,e3,e4,text1):
	url = e1.get()
	pre = e2.get()
	beh = e3.get()
	path = e4.get()

	current = os.path.split(os.path.realpath(__file__))[0]

	tkMessageBox.showinfo("消息","开始抓取页面")
	driver = getDriver()
	html = getHtml(driver,url)
	arti = getArticle(html,pre,beh)
	text1.delete(0.0,END)
	text1.insert(INSERT,arti)
	

	fil = None
	if path == "":
		#fil = open("web.html","w")
		fil = open(current + "/web.html" + path,"w")
	else:
		fil = open(path,"w")
	#fil.write(arti.decode('utf-8'))
	fil.write(arti.encode('utf-8'))
	fil.close()

#选择一个保存文件的目录
def dia(e4):
	#filename = tkFileDialog.askopenfilename()
	filename = tkFileDialog.askdirectory() + "/"
	e4.delete(0,END)
	e4.insert(0,filename)


def createGUI():
	window = Tk()

	url = Label(window, text="URL：").grid(row=0)
	label1 = Label(window, text="开始：").grid(row=1)
	label2 = Label(window, text="结束：").grid(row=2)
	label3 = Label(window, text="保存：").grid(row=3)
	label4 = Label(window, text="正文：").grid(row=5,sticky=N)

	#输入框
	e1 = Entry(window,width=50)
	e2 = Entry(window,width=50)
	e3 = Entry(window,width=50)
	e4 = Entry(window,width=50)
	#添加控件
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)


	scrollbar1 = Scrollbar(window)
	scrollbar1.grid(row=5,column=2,sticky= N + S)
	text1 = Text(window,height=30,width=65,yscrollcommand=scrollbar1.set)
	#text1.grid(row=5,column=0,columnspan=2)
	text1.grid(row=5,column=1)
	scrollbar1.config(command=text1.yview)

	button1 = Button(window,text="开始抓取",command=lambda:test(e1,e2,e3,e4,text1)).grid(row=4,column=1)
	button2 = Button(window,text="选择",command=lambda:dia(e4)).grid(row=3,column=2)
	

	window.mainloop()



createGUI()
