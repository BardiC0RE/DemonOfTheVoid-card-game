from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image ,ImageTk, ImageSequence
import pygame

# sorry for shuffled codes ;)


# mixer for music and soundeffects
pygame.init()
pygame.mixer.init()

# player and vot points
playerpoint=0
botpoint=0

# finish cam for choosen cards
def finishcam():
    root444=tk.Toplevel()
    root444.geometry('500x500')
    root444.config(bg='black')
    S2=pygame.mixer.Sound('dtoothers.wav')
    S2.play()
    gif1242 = Image.open("demonfinisher.gif")
    frames1242 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif1242)]
    duration1242 = gif1242.info.get('duration', 70)

    label2112 = tk.Label(root444)
    label2112.pack()
    label2112.config(image=frames1242[0], bg='black')


    def update_frame1(frame_num=0):
        label2112.config(image=frames1242[frame_num])
        root444.after(duration1242, update_frame1, (frame_num + 1) % len(frames1242))
    update_frame1()
    label1212l=Label(root444, text='', font=('MS Serif', 20), bg='black')
    label1212l.pack()
    label1212=Label(root444, text='YOUR FiNiSH CAM', font=('MS Serif', 20), fg='green', bg='black')
    label1212.pack()
    root444.after(1500, root444.destroy)
    root444.mainloop()






# finish cam for choosen cards
def finishcam1():
    broot5=tk.Toplevel()
    broot5.geometry('500x500')
    broot5.config(bg='black')
    S1=pygame.mixer.Sound('dtoothers.wav')
    S1.play()
    bgif122 = Image.open("demonfinisher2.gif")
    bframes122 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(bgif122)]
    bduration122 = bgif122.info.get('duration', 70)

    blabel212 = tk.Label(broot5)
    blabel212.pack()
    blabel212.config(image=bframes122[0], bg='black')

    def update_frame2(frame_num=0):
        blabel212.config(image=bframes122[frame_num])
        broot5.after(bduration122, update_frame2, (frame_num + 1) % len(bframes122))
    update_frame2()
    label12121l=Label(broot5, text='', font=('MS Serif', 20), bg='black')
    label12121l.pack()
    label12121=Label(broot5, text='DEMONS FiNiSH CAM', font=('MS Serif', 20), fg='red', bg='black')
    label12121.pack()
    broot5.after(1500, broot5.destroy)
    broot5.mainloop()





# finish cam for choosen cards
def finishcam2():
    croot5=tk.Toplevel()
    croot5.geometry('500x500')
    croot5.config(bg='black')
    S3=pygame.mixer.Sound('gtoothersound.wav')
    S3.play()
    cgif122 = Image.open("ghostfinisher.gif")
    cframes122 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(cgif122)]
    cduration122 = cgif122.info.get('duration', 70)

    clabel212 = tk.Label(croot5)
    clabel212.pack()
    clabel212.config(image=cframes122[0], bg='black')

    def update_frame3(frame_num=0):
        clabel212.config(image=cframes122[frame_num])
        croot5.after(cduration122, update_frame3, (frame_num + 1) % len(cframes122))
    update_frame3()
    label121212l=Label(croot5, text='', font=('MS Serif', 20), bg='black')
    label121212l.pack()
    label121212=Label(croot5, text='DEMONS FiNiSH CAM', font=('MS Serif', 20), fg='red', bg='black')
    label121212.pack()
    croot5.after(1500, croot5.destroy)
    croot5.mainloop()





# finish cam for choosen cards
def finishcam3():
    droot5=tk.Toplevel()
    droot5.geometry('500x500')
    droot5.config(bg='black')
    S4=pygame.mixer.Sound('gtoothersound.wav')
    S4.play()
    dgif122 = Image.open("ghostfinisher2.gif")
    dframes122 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(dgif122)]
    dduration122 = dgif122.info.get('duration', 70)

    dlabel212 = tk.Label(droot5)
    dlabel212.pack()
    dlabel212.config(image=dframes122[0], bg='black')

    def update_frame4(frame_num=0):
        dlabel212.config(image=dframes122[frame_num])
        droot5.after(dduration122, update_frame4, (frame_num + 1) % len(dframes122))
    update_frame4()
    label1212121l=Label(droot5, text='', font=('MS Serif', 20), bg='black')
    label1212121l.pack()
    label1212121=Label(droot5, text='YOUR FiNiSH CAM', font=('MS Serif', 20), fg='green', bg='black')
    label1212121.pack()
    droot5.after(1500, droot5.destroy)
    droot5.mainloop()







# finish cam for choosen cards
def finishcam4():
    eroot5=tk.Toplevel()
    eroot5.geometry('500x500')
    eroot5.config(bg='black')
    S5=pygame.mixer.Sound('ktoothersound.wav')
    S5.play()
    egif122 = Image.open("knightfinisher.gif")
    eframes122 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(egif122)]
    eduration122 = egif122.info.get('duration', 70) 

    elabel212 = tk.Label(eroot5)
    elabel212.pack()
    elabel212.config(image=eframes122[0], bg='black')

    def update_frame5(frame_num=0):
        elabel212.config(image=eframes122[frame_num])
        eroot5.after(eduration122, update_frame5, (frame_num + 1) % len(eframes122))
    update_frame5()
    label12121212l=Label(eroot5, text='', font=('MS Serif', 20), bg='black')
    label12121212l.pack()
    label12121212=Label(eroot5, text='DEMONS FiNiSH CAM', font=('MS Serif', 20), fg='red', bg='black')
    label12121212.pack()
    eroot5.after(1500, eroot5.destroy)
    eroot5.mainloop()






# finish cam for choosen cards
def finishcam5():
    froot5=tk.Toplevel()
    froot5.geometry('500x500')
    froot5.config(bg='black')
    S6=pygame.mixer.Sound('ktoothersound.wav')
    S6.play()
    fgif122 = Image.open("knightfinisher2.gif")
    frames122 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(fgif122)]
    fduration122 = fgif122.info.get('duration', 70) 

    flabel212 = tk.Label(froot5)
    flabel212.pack()
    flabel212.config(image=frames122[0], bg='black')

    def update_frame6(frame_num=0):
        flabel212.config(image=frames122[frame_num])
        froot5.after(fduration122, update_frame6, (frame_num + 1) % len(frames122))
    update_frame6()
    label121212121l=Label(froot5, text='', font=('MS Serif', 20), bg='black')
    label121212121l.pack()
    label121212121=Label(froot5, text='YOUR FiNiSH CAM', font=('MS Serif', 20), fg='green', bg='black')
    label121212121.pack()
    froot5.after(1500, froot5.destroy)
    froot5.mainloop()





# finish cam for choosen cards
def finishcam6():
    aroot444=tk.Toplevel()
    aroot444.geometry('500x500')
    aroot444.config(bg='black')
    S7=pygame.mixer.Sound('dtodsound.wav')
    S7.play()
        # Load GIF and extract frames
    agif1242 = Image.open("dtod.gif")
    aframes12422 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(agif1242)]
    aduration12422 = agif1242.info.get('duration', 70)

    llabel2112 = tk.Label(aroot444)
    llabel2112.pack()
    llabel2112.config(image=aframes12422[0], bg='black')

    def update_frame1(frame_num=0):
        llabel2112.config(image=aframes12422[frame_num])
        aroot444.after(aduration12422, update_frame1, (frame_num + 1) % len(aframes12422))
    update_frame1()
    lllllabel1212=Label(aroot444, text='', font=('MS Serif', 20), bg='black')
    lllllabel1212.pack()
    llllabel1212=Label(aroot444, text='THE INFERNO', font=('MS Serif', 20), fg='dark red', bg='black')
    llllabel1212.pack()
    aroot444.after(1500, aroot444.destroy)
    aroot444.mainloop()





# finish cam for choosen cards
def finishcam7():
    aroot44423=tk.Toplevel()
    aroot44423.geometry('500x500')
    aroot44423.config(bg='black')
    S7=pygame.mixer.Sound('gtogsound.wav')
    S7.play()
    aagif1242 = Image.open("wtow.gif")
    aaframes12422 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(aagif1242)]
    aaduration12422 = aagif1242.info.get('duration', 70)

    allabel2112 = tk.Label(aroot44423)
    allabel2112.pack()
    allabel2112.config(image=aaframes12422[0], bg='black')

    def update_frame1(frame_num=0):
        allabel2112.config(image=aaframes12422[frame_num])
        aroot44423.after(aaduration12422, update_frame1, (frame_num + 1) % len(aaframes12422))
    update_frame1()
    lllllabel1212a=Label(aroot44423, text='', font=('MS Serif', 20), bg='black')
    lllllabel1212a.pack()
    ll1llabel1212=Label(aroot44423, text='THE THUNDER', font=('MS Serif', 20), fg='dark blue', bg='black')
    ll1llabel1212.pack()
    aroot44423.after(1500, aroot44423.destroy)
    aroot44423.mainloop()




# finish cam for choosen cards
def finishcam8():
    abroot44423=tk.Toplevel()
    abroot44423.geometry('500x500')
    abroot44423.config(bg='black')
    S8=pygame.mixer.Sound('ktoksound.wav')
    S8.play()
    abagif1242 = Image.open("ktok.gif")
    abaframes12422 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(abagif1242)]
    abaduration12422 = abagif1242.info.get('duration', 70)

    allabel2112122 = tk.Label(abroot44423)
    allabel2112122.pack()
    allabel2112122.config(image=abaframes12422[0], bg='black')

    def update_frame1(frame_num=0):
        allabel2112122.config(image=abaframes12422[frame_num])
        abroot44423.after(abaduration12422, update_frame1, (frame_num + 1) % len(abaframes12422))
    update_frame1()
    lllllabel1212a1=Label(abroot44423, text='', font=('MS Serif', 20), bg='black')
    lllllabel1212a1.pack()
    ll1llabel121222=Label(abroot44423, text='THE PLASMA FORCE', font=('MS Serif', 20), fg='cyan', bg='black')
    ll1llabel121222.pack()
    abroot44423.after(1500, abroot44423.destroy)
    abroot44423.mainloop()








# this is a assistant loading screen
def loading2():
    root5=tk.Toplevel()
    root5.attributes('-fullscreen', True)
    root5.config(bg='black')
    gif122 = Image.open("loadingscreenoni.gif")
    frames122 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif122)]
    duration122 = gif122.info.get('duration', 70)

    label212 = tk.Label(root5)
    label212.pack()
    label212.config(image=frames122[0], bg='black')

    def update_frame(frame_num=0):
        label212.config(image=frames122[frame_num])
        root5.after(duration122, update_frame, (frame_num + 1) % len(frames122))
    update_frame()
    label1212=Label(root5, text='', font=('MS Serif', 20), bg='black')
    label1212.pack()
    label1212=Label(root5, text='LOADING...', font=('MS Serif', 20), fg='white', bg='black')
    label1212.pack()
    root5.after(4000, root5.destroy)
    root5.mainloop()


# return back to menu after win or lose
def lose1win():

    if botpoint==5:
        rooot=tk.Toplevel()
        rooot.geometry('400x400')
        btn=Button(rooot, text='back to menu', font=('MS Serif', 13), fg='white', bg='black', cursor='hand2', command=lambda:[rooot.destroy(), exit1(), loading(), startmenu()])
        btn.pack()
    if playerpoint==5:
        rooot1=tk.Toplevel()
        rooot1.geometry('400x400')
        btn1=Button(rooot1, text='back to menu', font=('MS Serif', 13), fg='white', bg='black', cursor='hand2', command=lambda:[rooot1.destroy(), exit1(), loading(), startmenu()])
        btn1.pack()


# exiting from the main app
def exit1():
    root.destroy()

# bots paper , scissor, rock chooses with random
def thesystemwork():
    global thesystem,choice1
    thesystem=['R','P','S']
    choice1=random.choice(thesystem)

# players rock choosing conditions
def rocksystem():
    global playerpoint, botpoint
    if choice1=='R':

        
        img17=Image.open('knight.png ').resize((50, 50))
        phto17=ImageTk.PhotoImage(img17)
        labelbot.img17=phto17

        img18=Image.open('knight.png ').resize((50, 50))
        phto18=ImageTk.PhotoImage(img18)
        labelplayer.img18=phto18


        labelbot.config(text=f'computer choice: 🪨', image=phto18, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: 🪨',image=phto17, font=("MS Serif", 14), fg='white')
        label1.config(text='TIE', font=('MS Serif', 20), fg='gray')
        lose1win()
        finishcam8()
        
 
    if choice1=='P':

        
        img15=Image.open('knight.png ').resize((50, 50))
        phto15=ImageTk.PhotoImage(img15)
        labelbot.img15=phto15

        img16=Image.open('skull.png ').resize((50, 50))
        phto16=ImageTk.PhotoImage(img16)
        labelplayer.img16=phto16


        labelbot.config(text=f'computer choice: 📄', image=phto16, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: 🪨', image=phto15, font=("MS Serif", 14), fg='white')
        label1.config(text='LOST', font=('MS Serif', 20), fg='red')
        botpoint+=1
        label333.config(text=f'your score : {playerpoint}', fg='white')
        label444.config(text=f'computers score : {botpoint}', fg='white')
        lose1win()
        finishcam2()
        
        
        
    if choice1=='S':

        
        img13=Image.open('knight.png ').resize((50, 50))
        phto13=ImageTk.PhotoImage(img13)
        labelbot.img13=phto13

        img14=Image.open('devil.png ').resize((50, 50))
        phto14=ImageTk.PhotoImage(img14)
        labelplayer.img14=phto14


        labelbot.config(text=f'computer choice: ✂️', image=phto14, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: 🪨', image=phto13, font=("MS Serif", 14), fg='white')
        label1.config(text='WON', font=('MS Serif', 20), fg='green')
        playerpoint+=1
        label333.config(text=f'your score : {playerpoint}', fg='white')
        label444.config(text=f'computers score : {botpoint}', fg='white')
        lose1win()
        finishcam5()
        
        
        
    label333.config(text=f'your score : {playerpoint}', fg='white')
    label444.config(text=f'computers score : {botpoint}', fg='white')

# players paper choosing conditions
def papersystem():
    global playerpoint, botpoint
    if choice1=='R':
        
        img11=Image.open('skull.png ').resize((50, 50))
        phto11=ImageTk.PhotoImage(img11)
        labelbot.img11=phto11

        img12=Image.open('knight.png ').resize((50, 50))
        phto12=ImageTk.PhotoImage(img12)
        labelplayer.img12=phto12

        labelbot.config(text=f'computer choice: 🪨', imag=phto12, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: 📄', image=phto11, font=("MS Serif", 14), fg='white')
        label1.config(text='WON', font=('MS Serif', 20), fg='green')
        playerpoint+=1
        label333.config(text=f'your score : {playerpoint}', fg='white')
        label444.config(text=f'computers score : {botpoint}', fg='white')
        lose1win()
        finishcam3()
        
        
        
    if choice1=='P':
        
        img9=Image.open('skull.png ').resize((50, 50))
        phto9=ImageTk.PhotoImage(img9)
        labelbot.img9=phto9

        img10=Image.open('skull.png ').resize((50, 50))
        phto10=ImageTk.PhotoImage(img10)
        labelplayer.img10=phto10

        labelbot.config(text=f'computer choice: 📄', image=phto10, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: 📄', image=phto9, font=("MS Serif", 14), fg='white')
        label1.config(text='TIE', font=('MS Serif', 20), fg='gray')
        lose1win()
        finishcam7()
        

    if choice1=='S':

        
        img7=Image.open('skull.png ').resize((50, 50))
        phto7=ImageTk.PhotoImage(img7)
        labelbot.img7=phto7

        img8=Image.open('devil.png ').resize((50, 50))
        phto8=ImageTk.PhotoImage(img8)
        labelplayer.img8=phto8

        labelbot.config(text=f'computer choice: ✂️', image=phto8, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: 📄', image=phto7, font=("MS Serif", 14), fg='white')
        botpoint+=1

        label1.config(text='LOST', font=('MS Serif', 20), fg='red')
        label333.config(text=f'your score : {playerpoint}', fg='white')
        label444.config(text=f'computers score : {botpoint}', fg='white')
        lose1win()
        finishcam1()
        
    
# players scissor choosing conditions
def scissorsystem():
    global playerpoint, botpoint
    if choice1=='R':

        
        img5=Image.open('devil.png ').resize((50, 50))
        phto5=ImageTk.PhotoImage(img5)
        labelbot.img5=phto5

        img6=Image.open('knight.png ').resize((50, 50))
        phto6=ImageTk.PhotoImage(img6)
        labelplayer.img6=phto6


        labelbot.config(text=f'computer choice: 🪨', image=phto6, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: ✂️', image=phto5, font=("MS Serif", 14), fg='white')
        label1.config(text='LOST', font=('MS Serif', 20), fg='red')
        botpoint+=1

        label333.config(text=f'your score : {playerpoint}', fg='white')
        label444.config(text=f'computers score : {botpoint}', fg='white')
        lose1win()
        finishcam4()
        
        
        
    if choice1=='P':
        
        img3=Image.open('devil.png ').resize((50, 50))
        phto3=ImageTk.PhotoImage(img3)
        labelbot.img3=phto3

        img4=Image.open('skull.png ').resize((50, 50))
        phto4=ImageTk.PhotoImage(img4)
        labelplayer.img4=phto4

        labelbot.config(text=f'computer choice: 📄', image=phto4, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: ✂️', image=phto3, font=("MS Serif", 14), fg='white')
        label1.config(text='WON', font=('MS Serif', 20), fg='green')
        playerpoint+=1


        label333.config(text=f'your score : {playerpoint}', fg='white')
        label444.config(text=f'computers score : {botpoint}', fg='white')
        lose1win()
        finishcam()
        
        
        
        
        
    if choice1=='S':
        
        img1=Image.open('devil.png ').resize((50, 50))
        phto1=ImageTk.PhotoImage(img1)
        labelbot.img1=phto1

        img2=Image.open('devil.png ').resize((50, 50))
        phto2=ImageTk.PhotoImage(img2)
        labelplayer.img2=phto2

        labelbot.config(text=f'computer choice: ✂️', image=phto2, font=("MS Serif", 16), fg='white')
        labelplayer.config(text=f'your choice: ✂️', image=phto1, font=("MS Serif", 14), fg='white')

        label1.config(text='TIE', font=('MS Serif', 20), fg='gray')
        lose1win()
        finishcam6()
        
    
# reseting points feature is deleted
def resetingpoints():
    global botpoint, playerpoint
    playerpoint=0
    botpoint=0
    label333.config(text=f'your score : {playerpoint}', fg='white')
    label333.config(font=('MS Serif', 7))
    label444.config(text=f'computers score : {botpoint}', fg='white')
    label444.config(font=('MS Serif', 7))
    label1.config(text='')
    labelplayer.config(text='')
    labelbot.config(text='')

# just a sound effect
def easteregg():
    sound2=pygame.mixer.Sound('MOR.wav')
    sound2.play()


# this is the gui of the main program
def mainprogram1():
    global label1, labelbot, labelplayer, label333, label444
    global root
    root=tk.Tk()
    root.config(bg='black')
    root.iconbitmap('mainico1.ico')
    root.attributes('-fullscreen', True)
    sound1=pygame.mixer.Sound('laugh1.wav')
    sound1.play()
    gif1 = Image.open("onibossmain.gif")
    frames2 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif1)]
    duration3 = gif1.info.get('duration', 40)

    label = tk.Label(root)
    label.pack()
    label.config(image=frames2[0], bg='black')
    label.bind('<Double-Button-1>', lambda e : easteregg() ) # this plays the easter egg sound effect after double click on the demon

    def update_frame(frame_num=0):
        label.config(image=frames2[frame_num])
        root.after(duration3, update_frame, (frame_num + 1) % len(frames2))
    update_frame()

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=" Menu", menu=help_menu)
    help_menu.add_command(label="Exit", command=lambda:[exit1(), loading() , startmenu()])

    root.title('Demon Of The VOID')
    root.geometry('700x700')
    label333=Label(root, text='', font=('MS Serif', 14), bg='black')
    label333.place(relx=1.0, rely=0.0, anchor='ne', x=-5, y=5)
    labelblack=Label(root, text='', font=("Helvetica", 14), bg='black')
    labelblack.pack()
    labelblack111=Label(root, text='', font=("Helvetica", 14), bg='black')
    labelblack111.pack()
    labelblack1111=Label(root, text='', font=("Helvetica", 14), bg='black')
    labelblack1111.pack()

    labelbot=Label(root, text='', font=("Helvetica", 14), bg='black')
    labelbot.pack()

    labelplayer=Label(root, text='', font=("Helvetica", 14), bg='black')
    labelplayer.pack()

    labelblack2=Label(root, text='', font=("Helvetica", 14), bg='black')
    labelblack2.pack()
    label444=Label(root, text='', font=('MS Serif', 14), bg='black')
    label444.place(relx=0.0, rely=0.0, anchor='nw', x=5, y=5)
    label2=Label(root, text='', font=("Helvetica", 14), bg='black')
    label2.pack()
    label1=Label(root, text='', font=("Helvetica", 20), bg='black')
    label1.pack()
    label3=Label(root, text='', font=("Helvetica", 14), bg='black')
    label3.pack()

# knights button size and resizing after navigating the mouse on the button
    img=Image.open('knight.png').resize((150, 200))
    imgload=ImageTk.PhotoImage(img)
    button1=Button(root, image=imgload, padx=10, pady=10 , text='DEFFENCE', cursor='hand2', font=("MS Serif", 10),bg='black' ,fg='white',  compound=tk.TOP, command=lambda:[thesystemwork(), rocksystem()])
    button1.pack(side=tk.LEFT)

    def enter5(e):
        button1.config(padx=15, pady=15)
    def enter6(e):
        button1.config(padx=10, pady=10)

    button1.bind('<Enter>', enter5)
    button1.bind('<Leave>', enter6)

# devils button size and resizing after navigating the mouse on the button

    img2=Image.open('devil.png').resize((150, 200))
    imgload2=ImageTk.PhotoImage(img2)


    button3=Button(root, image=imgload2, padx=10, pady=10 , text='ATTACK', cursor='hand2', font=("MS Serif", 10),bg='black' ,fg='white',  compound=tk.TOP , command=lambda:[thesystemwork(), scissorsystem()])
    button3.pack(side=tk.RIGHT)

    def enter3(e):
        button3.config(padx=15, pady=15)
    def enter4(e):
        button3.config(padx=10, pady=10)

    button3.bind('<Enter>', enter3)
    button3.bind('<Leave>', enter4)

# skulls button size and resizing after navigating the mouse on the button

    img1=Image.open('skull.png').resize((150, 200))
    imgload1=ImageTk.PhotoImage(img1)


    button2=Button(root, image=imgload1, padx=10, pady=10 ,text='MAGIC', cursor='hand2', font=("MS Serif", 10), bg='black' , fg='white', compound=tk.TOP , command=lambda:[thesystemwork(), papersystem()])
    button2.pack(expand=True)

    def enter(e):
        button2.config(padx=15, pady=15)
    def enter2(e):
        button2.config(padx=10, pady=10)

    button2.bind('<Enter>', enter)
    button2.bind('<Leave>', enter2)

    root.mainloop()

# guid of the game at main menu
def guid():
    root32=tk.Tk()
    root32.geometry('400x250')
    root32.resizable(False, False)
    root32.title('GAME CARDS GUID')
    root32.iconbitmap('mainico1.ico')
    root32.config(bg='black')
    blacklabel=Label(root32, bg='black')
    blacklabel.pack()
    guidlabel=Label(root32, text=''' HOW GAME WORKS

                    
DEMON = ATTACK CARD
KNIGHT = DEFFENCE CARD
GHOST = MAGIC CARD
                    
DEMON BEATS GHOST
KNIGHT BEATS DEMON
GHOST BEATS KNIGHT''', font=('MS Serif', 11), bg='black', fg='white')
    guidlabel.pack()

# main loading screen
def loading():
    root4=tk.Tk()
    root4.attributes('-fullscreen', True)
    root4.config(bg='black')
    gif12 = Image.open("loadingscreenoni.gif")
    frames12 = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif12)]
    duration12 = gif12.info.get('duration', 70)

    label21 = tk.Label(root4)
    label21.pack()
    label21.config(image=frames12[0], bg='black')

    def update_frame(frame_num=0):
        label21.config(image=frames12[frame_num])
        root4.after(duration12, update_frame, (frame_num + 1) % len(frames12))
    update_frame()
    label1212=Label(root4, text='', font=('MS Serif', 20), bg='black')
    label1212.pack()
    label1212=Label(root4, text='LOADING...', font=('MS Serif', 20), fg='white', bg='black')
    label1212.pack()
    root4.after(6000, root4.destroy)
    root4.mainloop()





# the games main menu
def startmenu():
    global font_name
    root1 = tk.Tk()
    root1.attributes('-fullscreen', True)
    root1.title("Demon Of The VOID")
    root1.iconbitmap('mainico1.ico')
    def stop():
            pygame.mixer.music.stop()
    pygame.mixer.music.load('mainmusic1.wav')
    pygame.mixer.music.play(loops=-1)
    menu_bar1 = tk.Menu(root1)
    root1.config(menu=menu_bar1)
    help_menu = tk.Menu(menu_bar1, tearoff=0)
    menu_bar1.add_cascade(label=" MENU", menu=help_menu)
    help_menu.add_command(label="Game SYSTEM", command=lambda: guid())
    help_menu.add_command(label="creator", command= lambda:[messagebox.showinfo('Creator','This is cooked by BardiCore ;)')])
    
    help_menu.add_command(label="RAPID EXIT", command=lambda: root1.destroy() )


    try:
        font_name = ("MS Serif", 18)    
    except:
        font_name = ("Courier", 18)  

    title_label = tk.Label(
        root1,
        text='''D  E  M  O  N

OF THE
        
 V  O  I  D ''',
        font=font_name,
        fg="red",      
        bg="black",

    )
    title_label.pack(pady=20)

    root1.configure(bg="black")


    ab=tk.Button(root1, text="  START  ", padx=3, pady=7 ,font=("MS Serif", 12), cursor='hand2', bg='dark red', command=lambda:[root1.destroy(), stop(), loading(), mainprogram1()])
    ab.pack(pady=10)

    def ente(e):
        ab.config(padx=8, pady=10)
    def ent(e):
        ab.config(padx=3, pady=7)

    ab.bind('<Enter>', ente)
    ab.bind('<Leave>', ent)
   


    ab2=tk.Button(root1, text="  EXIT  ", padx=3, pady=7 ,font=("MS Serif", 12), bg='dark red', cursor='hand2', command=lambda:[root1.destroy()])
    ab2.pack(pady=10)

    def ente2(e):
        ab2.config(padx=8, pady=10)
    def ent2(e):
        ab2.config(padx=3, pady=7)

    ab2.bind('<Enter>', ente2)
    ab2.bind('<Leave>', ent2)

    labell=Label(root1, text='', bg='black')
    labell.pack()

    gif = Image.open("hellbgg.gif")
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]
    duration = gif.info.get('duration', 70)

    label = tk.Label(root1)
    label.pack()
    label.config(image=frames[0], bg='black')

    def update_frame(frame_num=0):
        label.config(image=frames[frame_num])
        root1.after(duration, update_frame, (frame_num + 1) % len(frames))
    update_frame()




    root1.mainloop()
    
startmenu()