try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


def lift_win1():
    win1.lift(aboveThis=root)

def lower_win1():
    win1.lower(belowThis=root)
root = tk.Tk()
root.title('root win')
root.geometry("200x100+30+30")
root.configure(bg='yellow')
# create a child/top window
win1 = tk.Toplevel(bg='red')
win1.title('top/child window win1')
win1.geometry("300x150+120+120")
btn_lift = tk.Button(win1, text="Lift win1", command=lift_win1)
btn_lift.pack(padx=30, pady=5)
btn_lower = tk.Button(win1, text="Lower win1", command=lower_win1)
btn_lower.pack(pady=5)
root.mainloop()