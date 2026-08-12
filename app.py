import tkinter as tk

window= tk.Tk()
window.geometry("600x400")
window.resizable(False, False)

header_frame= tk.Frame(window)
header_frame.pack()

title= tk.Label(header_frame,text="WORD DESK", font=("Arial", 28, "bold"))
title.pack(pady=10)
title2= tk.Label(header_frame,text="Words, available offline.Right on your desk.",font=(18))
title2.pack()

#search section
search_frame= tk.Frame(window)
search_frame.pack()

search_word=tk.Label(search_frame,text="Search for a word: ",font=("Arial", 12)).grid(row=0,column=0)
search_word=tk.Entry(search_frame).grid(row=0,column=1)

search_btn=tk.Button(search_frame,text="search").grid(row=0,column=2)

info_frame= tk.Frame(window)
info_frame.pack()

#word
word_label = tk.Label(info_frame, text="Word:",font=("Arial", 20, "bold"))
word_label.pack(pady=15)


window.mainloop()
