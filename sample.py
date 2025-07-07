import tkinter as tk
from PIL import Image, ImageTK
import random

class Game():
    def __init__(self, root):
        self.root = root
        self.root.title("행복하게 만들어주기")
        self.root.geometry("600x650")

        # 현스테이지
        self.current_stage = 0

        # 스테이지에 존재하는 스토리들
        self.stages = [
            ["배고파 보인다", "함께 식사한다", "식비를 건네준다", "배고픈레이.jpg"],
            ["심심해 보인다", "함께 영화를 시청한다", "함께 독서한다", "심심한레이.jpg"],
            ["우울해 보인다", "조심스레 말을 건넨다", "혼자만의 시간을 준다", "우울한레이.jpg"],
            ["화가 나 보인다", "사과한다", "사죄의 선물을 건넨다", "화난레이.jpg"]
        ]

        #결말들
        self.outcomes = [
            ("레이는 당신과 함께합니다", "19x,jpg"),
            ("레이는 당신을 떠납니다", "24.jpg")
        ]

        self.point = 0

        self.root.lb_start = tk.Label(root, text = "레이게임", font = ("Times New Roman", 20, "bold"), fg="purple")
        self.root.lb_start.pack(padx=10)

        self.root.bt_start = tk.Button(root, text = "시작", command = start_game)
        self.root.bt_start.pack(padx=2)

    def start_game(self):
        self.root.lb_start.destroy()
        self.root.bt_start.destroy()

        



        

        
