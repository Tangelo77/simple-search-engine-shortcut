import webbrowser
from tkinter import *
root = Tk()
root.title("web")
root.geometry("100x120")
def google():
    webbrowser.open("www.google.lk")
mygoogle = Button(root, text="google", command=google).pack(pady=20)
def bing():
    webbrowser.open("www.bing.com")
mygoogle = Button(root, text="bing", command=bing).pack(pady=15)
root.mainloop()