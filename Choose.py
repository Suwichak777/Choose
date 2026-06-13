import tkinter as tk

def num1():
    root.withdraw()

    win1 = tk.Toplevel()
    win1.title("1")
    win1.geometry("400x300")

    num1_label = tk.Label(win1, text="You choose 1", font=("Arial", 20))
    num1_label.pack(pady=30)
    nothing_label = tk.Label(win1, text="Nothing!!!", font=("Arial", 50), fg="red")
    nothing_label.pack(pady=10)

def num2():
    root.withdraw()

    win2 = tk.Toplevel()
    win2.title("2")
    win2.geometry("400x300")

    num2_label = tk.Label(win2, text="You choose 2", font=("Arial", 20))
    num2_label.pack(pady=30)
    nothing_label = tk.Label(win2, text="Nothing!!!", font=("Arial", 50), fg="red")
    nothing_label.pack(pady=10)

def num3():
    root.withdraw()

    win3 = tk.Toplevel()
    win3.title("3")
    win3.geometry("400x300")

    num3_label = tk.Label(win3, text="You choose 3", font=("Arial", 20))
    num3_label.pack(pady=30)
    nothing_label = tk.Label(win3, text="Nothing!!!", font=("Arial", 50), fg="red")
    nothing_label.pack(pady=10)

def num4():
    root.withdraw()

    win4 = tk.Toplevel()
    win4.title("4")
    win4.geometry("400x300")

    num4_label = tk.Label(win4, text="You choose 4", font=("Arial", 20))
    num4_label.pack(pady=30)
    correct_label = tk.Label(win4, text="!!!Correct!!!", font=("Arial", 50), fg="green")
    correct_label.pack(pady=10)
    arrow_label = tk.Label(win4, text=" l l l ", font=("Arial", 10), fg="red")
    arrow_label.pack(pady=1)
    arrow_label = tk.Label(win4, text=" V V V ", font=("Arial", 10), fg="red")
    arrow_label.pack(pady=1)
    but_label = tk.Label(win4, text="But, it's nothing!!!", font=("Arial", 10), fg="red")
    but_label.pack(pady=10)

def num5():
    root.withdraw()

    win5 = tk.Toplevel()
    win5.title("5")
    win5.geometry("400x300")

    num5_label = tk.Label(win5, text="You choose 5", font=("Arial", 20))
    num5_label.pack(pady=30)
    nothing_label = tk.Label(win5, text="Nothing!!!", font=("Arial", 50), fg="red")
    nothing_label.pack(pady=10)

def num6():
    root.withdraw()

    win6 = tk.Toplevel()
    win6.title("6")
    win6.geometry("400x300")

    num6_label = tk.Label(win6, text="You choose 6", font=("Arial", 20))
    num6_label.pack(pady=30)
    nothing_label = tk.Label(win6, text="Nothing!!!", font=("Arial", 50), fg="red")
    nothing_label.pack(pady=10)

root = tk.Tk()
root.title("Choose")
root.geometry("500x350")

choice = tk.Label(root, text="Choose?", font=("Arial", 30)
, fg="yellow", bg="gray",width=20, height=2, relief="ridge", bd=10)
choice.pack(pady=20)

but_frame1 = tk.Frame(root)
but_frame1.pack(pady=15)
but_frame2 = tk.Frame(root)
but_frame2.pack(pady=15)

but1 = tk.Button(but_frame1, text="1", font=("Arial", 20), bg="lightblue", activebackground="skyblue", relief="groove", bd=5, cursor="hand2", command=num1)
but2 = tk.Button(but_frame1, text="2", font=("Arial", 20), bg="lightblue", activebackground="skyblue", relief="groove", bd=5, cursor="hand2", command=num2)
but3 = tk.Button(but_frame1, text="3", font=("Arial", 20), bg="lightblue", activebackground="skyblue", relief="groove", bd=5, cursor="hand2", command=num3)
but1.pack(side=tk.LEFT, padx=20)
but2.pack(side=tk.LEFT, padx=20)
but3.pack(side=tk.LEFT, padx=20)
but4 = tk.Button(but_frame2, text="4", font=("Arial", 20), bg="lightblue", activebackground="skyblue", relief="groove", bd=5, cursor="hand2", command=num4)
but5 = tk.Button(but_frame2, text="5", font=("Arial", 20), bg="lightblue", activebackground="skyblue", relief="groove", bd=5, cursor="hand2", command=num5)
but6 = tk.Button(but_frame2, text="6", font=("Arial", 20), bg="lightblue", activebackground="skyblue", relief="groove", bd=5, cursor="hand2", command=num6)
but4.pack(side=tk.LEFT, padx=20)
but5.pack(side=tk.LEFT, padx=20)
but6.pack(side=tk.LEFT, padx=20)

root.mainloop()