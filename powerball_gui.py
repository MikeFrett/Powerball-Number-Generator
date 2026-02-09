import tkinter as tk
import random
from collections import Counter

DATA_FILE = "lonum.txt"

def load_numbers():
    white = []
    power = []

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = list(map(int, line.strip().split()))
            if len(parts) == 6:
                white.extend(parts[:5])
                power.append(parts[5])

    return Counter(white), Counter(power)

white_freq, power_freq = load_numbers()

def weighted_choice(counter, choices, k):
    population = []
    for n in choices:
        population.extend([n] * counter.get(n, 1))
    return random.sample(population, k)

def generate_numbers():
    whites = sorted(weighted_choice(white_freq, range(1, 70), 5))
    power = weighted_choice(power_freq, range(1, 27), 1)[0]

    for i, num in enumerate(whites):
        boxes[i].config(text=str(num))

    boxes[5].config(text=str(power))

# ---------- GUI ----------
root = tk.Tk()
root.title("Powerball Generator")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

boxes = []

for i in range(6):
    lbl = tk.Label(
        frame,
        text="--",
        width=4,
        height=2,
        font=("Arial", 20, "bold"),
        relief="ridge",
        bd=3
    )
    lbl.grid(row=0, column=i, padx=6)
    boxes.append(lbl)

button = tk.Button(
    root,
    text="Generate Powerball Number",
    font=("Arial", 14),
    command=generate_numbers
)
button.pack(pady=15)

root.mainloop()

