import tkinter as tk
import random,time,tkinter.messagebox

msg=tkinter.messagebox
root = tk.Tk()
canvas = tk.Canvas(root, height=1200, width=1400)
canvas.pack()
flag1 = False #For key 'X' pressed
flag2 = False #For key 'O' pressed
flag3 = False
store = []
store_pl = []
store_comp = []
count1 = 0  # To count comp steps
count2 = 0  # To count player steps
won = 0
img = tk.PhotoImage(file=r"C:\Users\TJ\PycharmProjects\Tutorial\x2.png")
img2 = tk.PhotoImage(file=r'C:\Users\TJ\PycharmProjects\Tutorial\letter-o25.png')
img3 = tk.PhotoImage(file = r"F:\python\MiniProject\blank.png")
Img = tk.PhotoImage(file=r"F:\python\MiniProject\bg.png")
img_i1= tk.PhotoImage(file=r"F:\python\MiniProject\unnamed2.png")
img_i1=img_i1.zoom(3,3)
frame1=tk.Label(root,border=2,image=img_i1)
frame1.place(relheight=1,relwidth=1)


start1 = tk.Button(frame1,text='Start',height=2,width=10,bg="purple",command=lambda: swap(frame1,frame))
start1.place(relx=0.5,rely=0.4)
start2 = tk.Button(frame1,text='Exit',height=2,width=10,bg="red",command=lambda :root.destroy())
start2.place(relx=0.5,rely=0.5)

frame = tk.Frame(root, background='pink')
frame.place(relheight=1, relwidth=1)

file = 'iu2.png'



def match(storex,player):
    global won,count2,store,store_pl,store_comp
    s1 = {1,2,3}
    s1=frozenset(s1)
    s2 = {1,5,9}
    s3 = {1,4,7}
    s4 = {2,5,8}
    s5 = {3,5,7}
    s6 = {3,6,9}
    s7 = {4,5,6}
    s8 = {7,8,9}

    st_set = set(storex)

    i1 = st_set.intersection(s1)
    i2 = st_set.intersection(s2)
    i3 = st_set.intersection(s3)
    i4 = st_set.intersection(s4)
    i5 = st_set.intersection(s5)
    i6 = st_set.intersection(s6)
    i7 = st_set.intersection(s7)
    i8 = st_set.intersection(s8)
    if i1 == s1 or i1 == s2 or i1 == s3 or i1 == s4 or i1 == s5 or i1 == s6 or i1 == s7 or i1 == s8 :
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won +=1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i2 == s1 or i2 == s2 or i2 == s3 or i2 == s4 or i2 == s5 or i2 == s6 or i2 == s7 or i2 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i3 == s1 or i3 == s2 or i3 == s3 or i3 == s4 or i3 == s5 or i3 == s6 or i3 == s7 or i3 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i4 == s1 or i4 == s2 or i4 == s3 or i4 == s4 or i4 == s5 or i4 == s6 or i4 == s7 or i4 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i5 == s1 or i5 == s2 or i5 == s3 or i5 == s4 or i5 == s5 or i5 == s6 or i5 == s7 or i5 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i6 == s1 or i6 == s2 or i6 == s3 or i6 == s4 or i6 == s5 or i6 == s6 or i6 == s7 or i6 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')

        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i7 == s1 or i7 == s2 or i7 == s3 or i7 == s4 or i7 == s5 or i7 == s6 or i7 == s7 or i7 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []
    elif i8 == s1 or i8 == s2 or i8 == s3 or i8 == s4 or i8 == s5 or i8 == s6 or i8 == s7 or i8 == s8:
        if player == 1:
            msg.askokcancel('You win!!')
        else:
            msg.askokcancel('Comp wins!!')
        won += 1
        tag6.config(text=f'Match Won: {won}')
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []

    elif count2 == 5:
        btn_Restart()
        store = []
        store_pl = []
        store_comp = []


def swap(f1,f2):
    f2.tkraise(f1)
    msg.askokcancel(message='Select Key To Play',title='Play')


def fn(opt):
    global flag1, flag2, flag3, count2,store,store_pl,store_comp
    i=0
    print(opt)
    flag3 = False
    for element in store:
        if element == opt:
            flag3=True
            break
    if count2 <= 5 and flag3 == False:
        store.append(opt)
        store_comp.append(opt)
        count2 += 1
        while i < store_pl.__len__():

            i+=1
        if flag1 == True and flag3 == False:
            if opt == 1:
                block1.config(height=95, width=95, image=small)
            elif opt == 2:
                block2.config(height=95, width=95, image=small)
            elif opt == 3:
                block3.config(height=95, width=95, image=small)
            elif opt == 4:
                block4.config(height=95, width=95, image=small)
            elif opt == 5:
                block5.config(height=95, width=95, image=small)
            elif opt == 6:
                block6.config(height=95, width=95, image=small)
            elif opt == 7:
                block7.config(height=95, width=95, image=small)
            elif opt == 8:
                block8.config(height=95, width=95, image=small)
            elif opt == 9:
                block9.config(height=95, width=95, image=small)
            match(store_comp,1)

        elif flag2 == True and flag3 == False:
            if opt == 1:
                block1.config(height=95, width=95, image=small2)
            elif opt == 2:
                block2.config(height=95, width=95, image=small2)
            elif opt == 3:
                block3.config(height=95, width=95, image=small2)
            elif opt == 4:
                block4.config(height=95, width=95, image=small2)
            elif opt == 5:
                block5.config(height=95, width=95, image=small2)
            elif opt == 6:
                block6.config(height=95, width=95, image=small2)
            elif opt == 7:
                block7.config(height=95, width=95, image=small2)
            elif opt == 8:
                block8.config(height=95, width=95, image=small2)
            elif opt == 9:
                block9.config(height=95, width=95, image=small2)
            match(store_comp,1)
        computer()


def computer():
    flag = False
    i = 0
    global count1
    count1 += 1
    t = random.randrange(1, 10)
    if count1 < 5:
        while i < store.__len__():
            if flag:
                t = random.randrange(1, 10)
                flag = False
            if store[i] == t:
                flag = True
                i = 0
                continue
            i += 1

        if flag == False:
            store_pl.append(t)
            store.append(t)

            if flag1 == True:
                if t == 1:
                    block1.config(height=95, width=95, image=small2)
                elif t == 2:

                    block2.config(height=95, width=95, image=small2)
                elif t == 3:
                    block3.config(height=95, width=95, image=small2)
                elif t == 4:
                    block4.config(height=95, width=95, image=small2)
                elif t == 5:
                    block5.config(height=95, width=95, image=small2)
                elif t == 6:
                    block6.config(height=95, width=95, image=small2)
                elif t == 7:
                    block7.config(height=95, width=95, image=small2)
                elif t == 8:
                    block8.config(height=95, width=95, image=small2)
                elif t == 9:
                    block9.config(height=95, width=95, image=small2)
                match(store_pl,2)

            elif flag2 == True:

                if t == 1:
                    block1.config(height=95, width=95, image=small)
                elif t == 2:
                    block2.config(height=95, width=95, image=small)
                elif t == 3:
                    block3.config(height=95, width=95, image=small)
                elif t == 4:
                    block4.config(height=95, width=95, image=small)
                elif t == 5:
                    block5.config(height=95, width=95, image=small)
                elif t == 6:
                    block6.config(height=95, width=95, image=small)
                elif t == 7:
                    block7.config(height=95, width=95, image=small)
                elif t == 8:
                    block8.config(height=95, width=95, image=small)
                elif t == 9:
                    block9.config(height=95, width=95, image=small)
                match(store_pl,2)
    print("store= ",store,"\nstore_pl=",store_pl,"\nstore_comp=",store_comp)

def btnX():
    global flag1, flag2
    flag1 = True
    flag2 = False
    buttonX['state']='normal'
    buttonO.configure(state='disabled')

def btnO():
    global flag2, flag1
    flag2 = True
    flag1 = False
    buttonO['state']='normal'
    buttonX['state']='disabled'

def btn_Restart():
    global store,store_comp,store_pl,count1,count2,flag1,flag2,flag3
    block1.config(height=95, width=95, image=small3)
    block2.config(height=95, width=95, image=small3)
    block3.config(height=95, width=95, image=small3)
    block4.config(height=95, width=95, image=small3)
    block5.config(height=95, width=95, image=small3)
    block6.config(height=95, width=95, image=small3)
    block7.config(height=95, width=95, image=small3)
    block8.config(height=95, width=95, image=small3)
    block9.config(height=95, width=95, image=small3)
    buttonO['state'] = 'normal'
    buttonX.configure(state='normal')
    flag1 = False
    flag2 = False

    store = []
    store_pl = []
    store_comp = []
    count1 = 0
    count2 = 0


line1 = tk.Frame(frame, bg='red', height=310, width=5)
line1.place(x=700, y=100)
line2 = tk.Frame(frame, bg='red', height=310, width=5)
line2.place(x=805, y=100)
line3 = tk.Frame(frame, bg='red', height=5, width=310)
line3.place(x=600, y=200)
line4 = tk.Frame(frame, bg='red', height=5, width=310)
line4.place(x=600, y=305)
small = img.subsample(10, 10)
small2 = img2.subsample(10, 10)
small3 = img3.subsample(10,10)

block1 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(1))
block1.place(x=600, y=100)
block2 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(2))
block2.place(x=705, y=100)
block3 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(3))
block3.place(x=810, y=100)
block4 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(4))
block4.place(x=600, y=205)
block5 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(5))
block5.place(x=705, y=205)
block6 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(6))
block6.place(x=810, y=205)
block7 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(7))
block7.place(x=600, y=310)
block8 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(8))
block8.place(x=705, y=310)
block9 = tk.Button(frame, bg='pink', border=0, height=6, width=13, command=lambda: fn(9))
block9.place(x=810, y=310)


#secondary UI design

sub_frame = tk.Frame(frame, background='white',border=2)
sub_frame.place(x=1, y=1,relheight=0.7, relwidth=0.2 )

tag1 = tk.Label(sub_frame,height=2,width=13,text="Key 'X'",background='white')
tag1.grid(row=1,column=0,padx=50)
buttonX = tk.Button(sub_frame,height=50,width=50,image=small,command=btnX)
buttonX.grid(row=2,column=0, padx=50)

tag3 = tk.Label(sub_frame,height=2,width=13,background='white')
tag3.grid(row=3,column=0,padx=50,pady=10)

tag2 = tk.Label(sub_frame,height=2,width=13,text="Key 'O'",background='white')
tag2.grid(row=4,column=0,padx=50)
buttonO = tk.Button(sub_frame,height=50,width=50,image=small2,command=btnO)
buttonO.grid(row=5,column=0,padx=50)

tag4 = tk.Label(sub_frame,height=2,width=13,background='white')
tag4.grid(row=6,column=0,padx=50,pady=10)

button_Restart = tk.Button(sub_frame,height=2, width=13, text="Restart Game",command= lambda :btn_Restart())
button_Restart.grid(row=7, column=0, padx=50,)

tag5 = tk.Label(sub_frame,height=2,width=13,background='white')
tag5.grid(row=8,column=0,padx=50,pady=10)

tag6 = tk.Label(sub_frame,height=2,width=13,background='white',text=f'Match Won: {won}')
tag6.grid(row=9,column=0,padx=50)
btn_Restart()
frame1.tkraise(frame)
root.mainloop()
