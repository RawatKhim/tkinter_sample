#P3 tk06
import tkinter as tk

def action_btn_press():

    print ("ボタンが押されました")

root = tk. Tk()
root.title('アクション組み込む')
root.geometry('350x150')

lb = tk.Label(text = 'ラベル')
bt1　＝ tk.Button
en = tk.Entry()
bt = tk.Button(text='button', command=print_txtval)
#[widget.pack() for widget in [lb,en,bt]]
lb.pack()
en.pack()
bt.pack()
root.mainloop()