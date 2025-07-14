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

        #호감도
        self.point = 0

        self.rootlb_start = tk.Label(root, text = "레이게임", font = ("Times New Roman", 20, "bold"), fg="purple")
        self.rootlb_start.pack(padx=10)

        self.rootbt_start = tk.Button(root, text = "시작", command = start_game)
        self.rootbt_start.pack(padx=2)

    def start_game(self):
        self.rootlb_start.destroy()
        self.rootbt_start.destroy()

        #첫 스테이지
        story_stage1 = self.stages[0]

        img_first_stage = story_stage1[3]
        img = Image.open(img_first_stage)
        img = img.resize(200, 200)
        self.photo = ImageTK.PhotoImage(img)

        self.img_label1 = tk.Label(self.root, image=self.photo)
        self.img_label1.pack(pady=10)

        self.status_lb1 = tk.Label(self.root, text = story_stage1[0])
        self.status_lb1.pack()

        self.radio_var_stage1 = tk.StringVar(value = story_stage1[1])
        self.radio_1_choice1 = tk.Radiobutton(self.root, text = story_stage1[1], variable= self.radio_var_stage1, value = story_stage1[1])
        self.radio_1_choice1.pack()
        self.radio_2_choice1 = tk.Radiobutton(self.root, text = story_stage1[2], variable=self.radio_var_stage1, value=story_stage1[2])
        self.radio_2_choice1.pack()

        def next_stage(self):
            if self.radio_var_stage1 == story_stage1[1]:
                self.point += 1

            self.img_label1.destroy()
            self.status_lb1.destroy()
            self.radio_1_choice1.destroy()
            self.radio_2_choice1.destroy()

            #두 번째 스테이지
            self.rootlb_second = tk.Label(self.root, text = self.stages[1][0])
            self.rootlb_second.pack()

            img2 = Image.open(self.stages[1][3])
            img2 = img2.resize(200, 200)
            self.photo2 = ImageTK.PhotoImage(img2)
            
            self.imagelb2 = tk.Label(self.root, image=self.photo2)
            self.imagelb2.pack()

            self.radiovar2 = tk.StringVar(value = self.stages[1][1])
            self.radio_1_choice2 = tk.Radiobutton(self.root, text = self.stages[1][1], value = self.stages[1][1], variable= self.radiovar2)
            self.radio_1_choice2.pack()
            self.radio_2_choice2 = tk.Radiobutton(self.root, text = self.stages[1][2], value= self.stages[1][2], variable=self.radiovar2)
            self.radio_2_choice2.pack()

            def thirdstage(self):
                self.rootlb_second.destroy()
                self.imagelb2.destroy()
                self.radio_1_choice2.destroy()
                self.radio_2_choice2.destroy()

                #세 번째 스테이지
                self.rootlb_third = tk.Label(self.root, text = self.stages[2][0])
                self.rootlb_third.pack()
                
                img = Image.open(self.stages[2][3])
                img = img.resize(200, 200)
                self.photo3 = ImageTK.PhotoImage(img)
                
                self.imagelb3 = tk.Label(self.root, image=self.photo3)
                self.imagelb3.pack()
                
                self.radiovar3 = tk.StringVar(value= self.stages[2][1])
                self.radiobutton3 = tk.Radiobutton(self.root, text = self.stages[2][1], value = self.stages[2][1], variable= self.radiovar3)
                self.radiobutton3.pack()
                self.radiobutton3_1 = tk.Radiobutton(self.root, text = self.stages[2][2], value = self.stages[2][2], variable= self.radiovar3)
                self.radiobutton3_1.pack()
                
                def finalstage(self):
                    

                self.finalstage = tk.Button(self.root, text = "선택", command = finalstage)
                self.finalstage.pack()
            
            self.bt_next = tk.Button(self.root, text = "선택", command = thirdstage)
            self.bt_next.pack()

        self.button_choice1 = tk.Button(self.root, text = "선택", command=next_stage)
        self.button_choice1.pack()

        

            
                
                


                
                

        

    
        
        

        



        



        

        
