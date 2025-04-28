import tkinter as tk
import random

def transcribe(dnk):
    rnk = ""
    for slovo in dnk:
        if slovo == "A":
            rnk += "U"
        elif slovo == "T":
            rnk += "A"
        elif slovo == "C":
            rnk += "G"
        elif slovo == "G":
            rnk += "C"
    return rnk

def novi_niz():
    niz = ""
    for i in range(9):
        niz += random.choice("ATCG")
    return niz

def provjera():
    global score
    user_input = input.get("1.0", tk.END).strip().upper()

    if user_input == current_rnk:
        result_label.config(text = "Tačno!")
        score += 1
    else:
        result_label.config(text = "Netačno!")

    score_label.config(text=f"Score: {score}")

    runda += 1
    if runda > 5:
        end_game()
    else:
        runda_label.config(text=f"Runda: {runda}/5")

def next():
    global current_dnk, current_rnk, runda
    if runda > 5:
        end_game()
        return
    
    current_dnk = novi_niz()
    current_rnk = transcribe(current_dnk)
    dnk_label.config(text=f"DNK: {current_dnk}")
    result_label.config(text="")
    input.delete("1.0", tk.END)

    runda_label.config(text=f"Runda: {runda}/5")
    runda += 1

def end_game():
    dnk_label.config(text="Kraj igre!")
    result_label.config(text=f"Ukupan score: {score}/5")

    with open("rezultati.txt", "a") as file:
        file.write(f"Score: {score}/5\n")

#ROOT
root = tk.Tk()
root.title("DNK -> RNK")

score = 0
runda = 1
current_dnk = ""
current_rnk = ""

dnk_label = tk.Label(root, text = "DNK: ", font=("Arial", 18))
dnk_label.pack()

input = tk.Text(root, height=1, width=25, font=("Courier", 16))
input.pack()

provjera_btn = tk.Button(root, text="Provjeri", command=provjera, font=("Arial", 14))
provjera_btn.pack()

next_btn = tk.Button(root, text="Sljedeća runda", command=next, font=("Arial", 14))
next_btn.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

score_label = tk.Label(root, text = "Score: 0", font = ("Arial", 14))
score_label.pack()

runda_label = tk.Label(root, text = "Runda: 1/5", font = ("Arial", 14))
runda_label.pack()

next()

root.mainloop()
