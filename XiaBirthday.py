import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import pygame
import os


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height = 700, width =1100, bg = "#FFF5EE")
        self.logo_image = tk.PhotoImage(file = "giphy.gif")
        tk.Button(self,image = self.logo_image, command = self.main_login).place(relx=0.5, rely=0.5, anchor="center")
        
    def main_login(self):
        login = tk.Toplevel()

        login.title("Login")
        login.geometry("500x300+500+250")
        login.config(bg = "#feecef")


        def check_account():
            account = entry_account.get()
            password = entry_password.get()

            if account == "xia" and password == "0510":
                tk.messagebox.showinfo(title = "Login Successful", message = "Welcome Xia!")
                login.destroy()
                self._frame = None
                App.switch_frame(self, MainPage)
            else:
                tk.messagebox.showerror(title = "Login Denied", message = "Failed to Login!")   

        label_account = tk.Label(login, text = "Account:", bg = "#feecef", font=("Courier", 22))
        label_account.place(x = 100, y = 80)

        label_password = tk.Label(login, text = "Password:", bg = "#feecef", font=("Courier", 22))
        label_password.place(x = 87, y = 130)

        login_act = tk.StringVar()
        entry_account = tk.Entry(login, textvariable = login_act, bg = "grey")
        entry_account.place(x = 230, y = 80)

        login_psw = tk.StringVar()
        entry_password = tk.Entry(login, textvariable = login_psw, bg = "grey", show = "*")
        entry_password.place(x = 230, y = 130)

        login_button = tk.Button(login, text = "Login", bg = "white", command = check_account)
        login_button.place(x = 220, y = 200)

     
class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg = "#F5DEB3", width = 1100, height = 700)
        self.mainpageimage = tk.PhotoImage(file = "source.gif")
        self.quizimage = tk.PhotoImage(file = "quiz.gif")
        self.memoryimage = tk.PhotoImage(file = "memory.gif")
        
        tk.Button(self, image = self.mainpageimage, command = self.play_music).place(x=310 ,y = 50)
        tk.Button(self, image = self.quizimage, command = self.switch_Quiz).place(x = 200, y = 450)
        tk.Button(self, image = self.memoryimage, command = self.switch_Memory).place(x = 620, y = 450)

        tk.Label(self, text = "Credit: Wei", font = ("Zapfino", 10), fg = "darkgray", bg = "#F5DEB3").place(x = 1090, y = 710, anchor = "se")


    def play_music(self):
        pygame.mixer.music.load("halo.wav")
        pygame.mixer.music.play()

    
    def switch_Quiz(self):
        self._frame = None
        App.switch_frame(self, QuizPage)
    
    def switch_Memory(self):
        answer = tk.Toplevel()

        answer.title("Passcode")
        answer.geometry("800x500+350+120")
        answer.config(bg = "#F5DEB3")

        def check_ans():
            ans_in = answer_entry.get()

            if ans_in == "HappyBirthdayFlower":
                os.system('open XiaBirthday.m4v')
                answer.destroy()
                
            else:
                tk.messagebox.showerror(title = "Wrong!!!!", message = "You are not qualified!!!")
        
        answer_label = tk.Label(answer, text = "Enter Your Keyword", font = ("Courier", 20))
        answer_label.place(x = 300, y = 150)

        ans = tk.StringVar()
        answer_entry = tk.Entry(answer, textvariable = ans, bg = "grey")
        answer_entry.place(x = 280, y = 300)

        confirm_button = tk.Button(answer, text = "Confirm", bg = "white", command = check_ans)
        confirm_button.place(x = 480, y = 300)
       

class QuizPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg = "#D8BFD8", width = 1100, height = 700)
        self.quizpageimage = tk.PhotoImage(file = "quizpage.gif")
        
        self.quiz1 = Image.open("1.gif")
        self.quiz2 = Image.open("2.gif")
        self.quiz3 = Image.open("3.gif")
        self.return1 = Image.open("return.gif")

        self.img1 = self.quiz1.resize((80, 100), Image.ANTIALIAS)
        self.img2 = self.quiz2.resize((80, 100), Image.ANTIALIAS)
        self.img3 = self.quiz3.resize((80, 100), Image.ANTIALIAS)
        self.r1 = self.return1.resize((130,160), Image.ANTIALIAS)
        
        self.q1 = ImageTk.PhotoImage(self.img1)
        self.q2 = ImageTk.PhotoImage(self.img2)
        self.q3 = ImageTk.PhotoImage(self.img3)
        self.r = ImageTk.PhotoImage(self.r1)
    
        tk.Label(self, image = self.quizpageimage).place(x = 310 , y = 20)
        tk.Button(self, image = self.q1, height = 90, width = 110, command = self.question1).place(x = 110, y = 470)
        tk.Button(self, image = self.q2, height = 90, width = 110, command = self.question2).place(x = 370, y = 470)
        tk.Button(self, image = self.q3, height = 90, width = 110, command = self.question3).place(x = 630, y = 470)
        tk.Button(self, image = self.r, height = 160, width = 130, command = self.returning).place(x = 900, y = 500)

    def returning(self):
        self._frame = None
        App.switch_frame(self, MainPage)

    def question1(self):
        q1 = tk.Toplevel()

        q1.title("Qustion1 ( Level: Easy )")
        q1.geometry("800x500+350+120")
        q1.config(bg = "#FFE4CA")

        def correct():
            tk.messagebox.showinfo(title = "Correct!!!!", message = "Not bad. Keep Going!!!\nKeyword:『Happy』")
            q1.destroy()

        def wrong():
            tk.messagebox.showerror(title = "Wrong!!!!", message = "You're So Dumb !!!!! Try Harder ....")

        self.questionimage = Image.open("howmany3.jpg")
        self.q = self.questionimage.resize((230,400), Image.ANTIALIAS)
        self.q_image = ImageTk.PhotoImage(self.q) 

        tk.Label(q1, image = self.q_image).place(x = 50, y = 35)
        tk.Label(q1, text = "How many 3 are in the picture ?", bg = "#C7C7E2", font = ("Courier", 20)).place(x = 370, y = 80)

        tk.Button(q1, text = "A. 15", font=("Courier", 20), command = wrong).place(x = 515, y = 180)
        tk.Button(q1, text = "B. 18", font=("Courier", 20), command = wrong).place(x = 515, y = 250)
        tk.Button(q1, text = "C. 19", font=("Courier", 20), command = correct).place(x = 515, y = 320)
        tk.Button(q1, text = "D. 21", font=("Courier", 20), command = wrong).place(x = 515, y = 390)
    def question2(self):
        q2 = tk.Toplevel()

        q2.title("Question 2 ( Level : Medium )")
        q2.geometry("800x500+350+120")
        q2.config(bg = "#FFE4CA")

        def correct():
            tk.messagebox.showinfo(title = "Correct!!!!", message = "Great!! One More Left!!!\nKeyword:『Birthday』")
            q2.destroy()

        def wrong():
            tk.messagebox.showerror(title = "Wrong!!!!", message = "Are You Joking ????? ")

        tk.Label(q2, text = "Who is more HANDSOME ??????????", bg = "#C7C7E2", font = ("Courier", 30)).place(x = 140, y = 80)


        tk.Button(q2, text = "A. 陳德維", font=("Courier", 20), command = correct).place(x = 350, y = 180)
        tk.Button(q2, text = "B. 王俊凱", font=("Courier", 20), command = wrong).place(x = 350, y = 250)
        tk.Button(q2, text = "C. 王源", font=("Courier", 20), command = wrong).place(x = 350, y = 320)
        tk.Button(q2, text = "D. 易烊千璽", font=("Courier", 20), command = wrong).place(x = 350, y = 390)
    def question3(self):
        q3 = tk.Toplevel()

        q3.title("Question 3 ( Level : Extreme )")
        q3.geometry("800x500+350+120")
        q3.config(bg = "#FFE4CA")
        
        def check_ans():
            answer = q3_entry.get()
            if answer == "1006":
                tk.messagebox.showinfo(title = "Correct!!!!", message = "Congrtulations!!! You've finished the quiz !!!\nKeyword:『Flower』")
                q3.destroy()
            else:
                tk.messagebox.showerror(title = "Wrong!!!!", message = "You must be sleeping in math class !!! \nTry Harder ....")
        
        self.q3image = Image.open("q3.gif")
        self.q3resized = self.q3image.resize((300,30), Image.ANTIALIAS)
        self.q3i = ImageTk.PhotoImage(self.q3resized) 


        tk.Label(q3, text = "Calculate        ", bg = "#C7C7E2", font = ("Courier", 28)).place(x = 150, y = 80)
        tk.Label(q3, image = self.q3i, bg = "#C7C7E2").place(x = 360 , y = 80)


        q3_ans = tk.StringVar()
        q3_entry = tk.Entry(q3, textvariable = q3_ans, bg = "grey")
        q3_entry.place(x = 280, y = 350)

        confirm_button = tk.Button(q3, text = "Confirm", bg = "white", command = check_ans)
        confirm_button.place(x = 480, y = 350)


if __name__ == "__main__":

    pygame.mixer.init()
    main_win = App()
    main_win.title("Happy Birthday!!!")
    main_win.geometry("1100x700+170+50")
    main_win.resizable(False,False)

    main_win.mainloop()