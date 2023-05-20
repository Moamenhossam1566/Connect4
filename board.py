#Graphical user interface (GUI)
from tkinter import *
from game import the_game

root = Tk()
root.geometry("750x250")

root.title("Connect 4 AI")
root.maxsize(1800,1800)

alg_label =Label(root, text="Select Algorithm:")
alg_options = ["Minimax", "Alpha-Beta"]
selected_alg =StringVar()
selected_alg.set(alg_options[0])
alg_dropdown =OptionMenu(root,selected_alg, *alg_options)

alg_label.pack()
alg_dropdown.pack(pady=3)


diff_label =Label(root, text="Select Difficulty:")
diff_options = ["Easy", "Medium", "Hard"]
selected_diff =StringVar()
selected_diff.set(diff_options[0])
diff_dropdown =OptionMenu(root,selected_diff, *diff_options)

diff_label.pack()
diff_dropdown.pack(pady=3)



def Connect_4():
    global selected_alg,selected_diff
    selected_alg = selected_alg.get()
    selected_diff = selected_diff.get()
    Algorithm=Label(text="Selected Algorithm: "+str(selected_alg))
    Algorithm.pack()
    level=Label(text="Selected Difficulty: "+str(selected_diff))
    level.pack()

    the_game()



button_data=Button(text="let's play",command=Connect_4)
button_data.pack()

root.mainloop()

