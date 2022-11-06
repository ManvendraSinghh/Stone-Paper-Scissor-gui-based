from tkinter import *
from PIL import Image, ImageTk
from random import randint
import pygame
import time


# main window

root = Tk() # initialising the tkinter instance
root.title("Rock Paper Scissor") #us window ka title
root.configure(background="#800080") #us window ka background color

#rule
condition = Label(root, font=50, text="First one to have 5 Points Wins !!",
                       bg="#800080", fg="white") #used to label something
condition.grid(row=0, column=2) #positioning it on the root windows



# Background Theme Music
pygame.mixer.init()
pygame.mixer.music.load("SuperMarioBros.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


# Sound Effects
def playwin():
    win = pygame.mixer.Sound("Stone_Paper_Scissor/mario_coin.wav")
    win.play()

def playlose():
    lose = pygame.mixer.Sound("Stone_Paper_Scissor/lose.mp3")
    lose.play()

def playtie():
    tie = pygame.mixer.Sound("Stone_Paper_Scissor/axedraw.mp3")
    tie.play()

def playwon():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("Stone_Paper_Scissor/mario_stage_clear.wav")
    pygame.mixer.music.play()
    root.update()
    time.sleep(5.2)
    
def playlost():
    pygame.mixer.music.load("Stone_Paper_Scissor/mario_die.wav")
    pygame.mixer.music.play()
    root.update()
    time.sleep(2.5)


# picture

rock_img = ImageTk.PhotoImage(Image.open("Stone_Paper_Scissor/rock_user.png"))
paper_img = ImageTk.PhotoImage(Image.open("Stone_Paper_Scissor/paper_user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Stone_Paper_Scissor/scissors_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Stone_Paper_Scissor/rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Stone_Paper_Scissor/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Stone_Paper_Scissor/scissors.png"))


# insert picture

user_label = Label(root, image=scissor_img, bg="#800080")
comp_label = Label(root, image=scissor_img_comp, bg="#800080")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


# scores

playerScore = Label(root, text=0, font=100, bg="#800080", fg="white")
computerScore = Label(root, text=0, font=100, bg="#800080", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


# indicators

user_indicator = Label(root, font=50, text="USER", bg="#800080", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#800080", fg="white")
user_indicator.grid(row=0, column=4)
comp_indicator.grid(row=0, column=0)


# messages

msg = Label(root, font=50, bg="#800080", fg="white")
msg.grid(row=3, column=2)



# update message

def updateMessage(x):
    msg['text'] = x

updateMessage("!! Welcome to Rock Paper Scissor !!")

# update user score

def updateUserScore():
    
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
    if(score<5):
        playwin()

    if score == 5:
        updateMessage("!! You Won the Game !!")
        playwon()
        restart()
        
        
# update computer score

def updateCompScore():
    
    score = int(computerScore["text"])
    score += 1
    if(score<5):
        playlose()
    computerScore["text"] = str(score)
    
    if score == 5:
        updateMessage("!! You Lost the Game !!")
        playlost()
        restart()
        

# check winner

def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
        playtie()
        
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

# restart

def restart():
    
    playerScore["text"] = '0'
    computerScore["text"] = '0'
    pygame.mixer.music.load("SuperMarioBros.ogg") # to restart music
    pygame.mixer.music.set_volume(0.3) 
    pygame.mixer.music.play(-1) # to play it on loop we use '-1'
    updateMessage("!! New Game started !!") 


# buttons

rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
