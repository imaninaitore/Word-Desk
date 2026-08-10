import tkinter as tk
window= tk.Tk()

header_frame= tk.Frame(window)
header_frame.pack()

title= tk.Label(header_frame,text="WORD DESK",font=(26))
title.pack()
title2= tk.Label(header_frame,text="Words, available offline.Right on your desk.",font=(18))
title2.pack()

search_frame= tk.Frame(window)
search_frame.pack()

search_word=tk.Label(search_frame,text="Search for a word: ").grid(row=0,column=0)
search_word=tk.Entry(search_frame).grid(row=0,column=1)

search_btn=tk.Button(search_frame,text="search").grid(row=0,column=2)

window.mainloop()
