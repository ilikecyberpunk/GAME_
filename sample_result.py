import tkinter as tk
from PIL import Image, ImageTk
import random

class Game():
    def __init__(self, root):
        self.root = root
        self.root.title("행복하게 만들어주기")
        self.root.geometry("600x650")

        self.current_stage = 0
        self.stages = [
            ["배고파 보인다", "함께 식사한다", "식비를 건네준다", "배고픈레이.jpg"],
            ["심심해 보인다", "함께 영화를 시청한다", "함께 독서한다", "심심한레이.jpg"],
            ["우울해 보인다", "조심스레 말을 건넨다", "혼자만의 시간을 준다", "우울한레이.jpg"],
            ["화가 나 보인다", "사과한다", "사죄의 선물을 건넨다", "화난레이.jpg"]
        ]
        self.outcomes = [
            ["레이는 당신과 함께합니다", "19x.jpg"],
            ["레이는 당신을 떠납니다", "24.jpg"]
        ]
        self.point = 0

        self.rootlb_start = tk.Label(root, text="레이게임", font=("Times New Roman", 20, "bold"), fg="purple")
        self.rootlb_start.pack(padx=10)

        self.rootbt_start = tk.Button(root, text="시작", command=self.start_game)
        self.rootbt_start.pack(padx=2)

    def start_game(self):
        self.rootlb_start.destroy()
        self.rootbt_start.destroy()
        self.current_stage = 0
        self.show_stage()

    def show_stage(self):
        stage = self.stages[self.current_stage]
        img = Image.open(stage[3])
        img = img.resize((200, 200))
        self.photo = ImageTk.PhotoImage(img)

        self.img_label = tk.Label(self.root, image=self.photo)
        self.img_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text=stage[0])
        self.status_label.pack()

        self.radio_var = tk.StringVar(value=stage[1])
        self.radio_1 = tk.Radiobutton(self.root, text=stage[1], variable=self.radio_var, value=stage[1])
        self.radio_1.pack()
        self.radio_2 = tk.Radiobutton(self.root, text=stage[2], variable=self.radio_var, value=stage[2])
        self.radio_2.pack()

        self.next_btn = tk.Button(self.root, text="선택", command=self.next_stage)
        self.next_btn.pack()

    def next_stage(self):
        
        stage = self.stages[self.current_stage]
        if self.radio_var.get() == stage[1]:
            self.point += 1

        
        self.img_label.destroy()
        self.status_label.destroy()
        self.radio_1.destroy()
        self.radio_2.destroy()
        self.next_btn.destroy()

        self.current_stage += 1
        if self.current_stage < len(self.stages):
            self.show_stage()
        else:
            self.show_ending()

    def show_ending(self):
        
        if self.point >= 2:
            outcome = self.outcomes[0]
        else:
            outcome = self.outcomes[1]

        img = Image.open(outcome[1])
        img = img.resize((200, 200))
        self.photo_end = ImageTk.PhotoImage(img)

        self.img_label_end = tk.Label(self.root, image=self.photo_end)
        self.img_label_end.pack(pady=10)

        self.result_label = tk.Label(self.root, text=outcome[0], font=("Times New Roman", 18, "bold"))
        self.result_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
    
