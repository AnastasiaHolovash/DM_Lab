from tkinter import *
import random
import original_expression as s_culc
import simplified_expression as simpl_exp
import second_expression as exp_2

def variant(g, n):
    return (n+g % 60) % 30+1


def from_string_to_set(x):
    x = x.replace(',', ' ')
    x = x.replace(';', ' ')
    x = x.replace(':', ' ')
    x = x.replace('.', ' ')
    x = list(x.split(' '))
    for i in range(x.count('')):
        x.remove('')
    x = {int(i) for i in x}
    return x


def gener_vyp_set(l):
    if entU_do.get() == '':
        do = 0
    else:
        do = int(entU_do.get())
    if entU_vid.get() == '':
        vid = 0
    else:
        vid = int(entU_vid.get())
    s = set()
    for i in range(l):
        s.add(random.randint(vid, do))
    while len(s) < l:
        s.add(random.randint(vid, do))
    return s


def generABC():
    global A, B, C, U
    v = var.get()
    # if manual input is selected
    if v == 0:
        if entA.get() == '':
            A = set()
        else:
            A = from_string_to_set(entA.get())

        if entB.get() == '':
            B = set()
        else:
            B = from_string_to_set(entB.get())

        if entC.get() == '':
            C = set()
        else:
            C = from_string_to_set(entC.get())
    # if random generation selected
    if v == 1:
        if lenA.get() == '':
            A = set()
        else:
            A = gener_vyp_set(int(lenA.get()))

        if lenB.get() == '':
            B = set()
        else:
            B = gener_vyp_set(int(lenB.get()))

        if lenC.get() == '':
            C = set()
        else:
            C = gener_vyp_set(int(lenC.get()))

    if entU_do.get() == '':
        do = 0
    else:
        do = int(entU_do.get())+1

    if entU_vid.get() == '':
        vid = 0
    else:
        vid = int(entU_vid.get())

    U = set(range(vid, do))
    label_vyvid.configure(text='A = {}\n'
                          'B = {}\n'
                          'C = {}\n'
                          .format(A, B, C))


def gener_f(x):
    le = len(x)
    s = set()
    s.add(min(x))
    s.add(max(x))

    for i in range(le-2):
        s.add(random.randint(min(x), max(x)))
    while len(s) < le:
        s.add(random.randint(min(x), max(x)))
    return s


def manual_input():
    global A, B, C
    entA['state'] = NORMAL
    entB['state'] = NORMAL
    entC['state'] = NORMAL
    lenA['state'] = DISABLED
    lenB['state'] = DISABLED
    lenC['state'] = DISABLED


def random_generation():
    global A, B, C
    entA['state'] = DISABLED
    entB['state'] = DISABLED
    entC['state'] = DISABLED
    lenA['state'] = NORMAL
    lenB['state'] = NORMAL
    lenC['state'] = NORMAL


def save_to_file(event):
    with open("Результат.txt", 'w') as f:
        f.write(str(event))


def save_to_file_2(event):
    with open("Результат_2.txt", 'w') as f:
        f.write(str(event))


def save_to_file_3(event):
    with open("Результат_3.txt", 'w') as f:
        f.write(str(event))


def window2():
    slave = Toplevel(root)
    slave.title('Обчислення заданого виразу')
    slave.grab_set()
    slave.focus_set()

    def show():
        lf = LabelFrame(slave, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=6, columnspan=4, sticky=W)
        Label(lf, text='1) (A & ¬B) = {f1}\n'
                       '2) (¬A & B) = {f2}\n'
                       '3) ((A & ¬B) | (¬A & B)) = {f3}\n'
                       '4) (¬C | B)  = {f4}\n'
                       '5) (¬C & (¬C | B)) = {f5}\n'
                       '6) ((A & ¬B) & (¬A & B)) & (¬C & (¬C | B)) = {f6}\n'
                       'Відповідь: {rez}'
              .format(
                      f1=A & (U - B),
                      f2=(U - A) & B,
                      f3=(A & (U - B)) | ((U - A) & B),
                      f4=(U - C) | B,
                      f5=(U - C) & ((U - C) | B),
                      f6=((A & (U - B)) | ((U - A) & B)) & ((U - C) & ((U - C) | B)),
                      rez=s_culc.origin_exp(A, B, C, U)),
              font='Arial 14', justify=LEFT).grid(column=0, row=5, sticky=W, columnspan=4)

    def but_disable(event):
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave, text='A = {}\n'
                      'B = {}\n'
                      'C = {}\n'.format(A, B, C),
          font="Arial 14", justify=LEFT).grid(column=0, row=4, sticky=W, columnspan=3)

    Label(slave, text='Відповідь:\n'
                      'D = {}\n'.format(s_culc.origin_exp(A, B, C, U)),
          font='Arial 14 bold').grid(column=0, row=2, sticky=W, columnspan=2)

    Button(slave, text="Показати розв'язок", font="Arial 16",
           command=show).grid(column=0, row=5, sticky=W)

    but = Button(slave, text='Зберегти в файл', font='Arial 16')
    but.grid(column=1, row=5)
    but.bind("<Button-1>", save_to_file(s_culc.origin_exp(A, B, C, U)))
    but.bind("<Button-1>", but_disable)

    Label(slave, text='Завдання:', font='Arial 14 bold').grid(column=0, row=0, sticky=W, columnspan=2)
    photo = PhotoImage(file="D_task.png")
    photo_but = Button(slave)
    photo_but.config(image=photo, width="669", height="70")
    photo_but.grid(column=0, row=1, columnspan=2)
    slave.mainloop()


def window3():
    slave = Toplevel(root)
    slave.title('Обчислення спрощеного виразу')
    slave.grab_set()
    slave.focus_set()

    def show():
        lf = LabelFrame(slave, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=6, columnspan=4, sticky=W)
        Label(lf, text='1) (A ∆ B) = {f1}\n'
                       '2) (A ∆ B) & ¬C = {f2}\n'
                       'Відповідь: {rez}'
              .format(
                      f1=(A - B) | (B - A),
                      f2=((A - B) | (B - A)) & (U - C),
                      rez=simpl_exp.simplified_exp(A, B, C, U)),
              font='Arial 14', justify=LEFT).grid(column=0, row=5, sticky=W, columnspan=4)

    def but_disable(event):
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave, text='A = {}\n'
                      'B = {}\n'
                      'C = {}\n'.format(A, B, C),
          font="Arial 14", justify=LEFT).grid(column=0, row=4, sticky=W, columnspan=3)

    Label(slave, text='Відповідь:\n'
                      'D = {}\n'.format(simpl_exp.simplified_exp(A, B, C, U)),
          font='Arial 14 bold').grid(column=0, row=2, sticky=W, columnspan=2)

    Button(slave, text="Показати розв'язок", font="Arial 16",
           command=show).grid(column=0, row=5, sticky=W)

    but = Button(slave, text='Зберегти в файл', font='Arial 16')
    but.grid(column=1, row=5)
    but.bind("<Button-1>", save_to_file_2(simpl_exp.simplified_exp(A, B, C, U)))
    but.bind("<Button-1>", but_disable)

    Label(slave, text='Завдання:', font='Arial 14 bold').grid(column=0, row=0, sticky=W, columnspan=2)
    photo = PhotoImage(file="D_simplified.png")
    photo_but = Button(slave)
    photo_but.config(image=photo, width="267", height="59")
    photo_but.grid(column=0, row=1, columnspan=2)
    slave.mainloop()


def window4():
    slave_2 = Toplevel(root)
    slave_2.title('Обчислення 2-го виразу')
    slave_2.grab_set()
    slave_2.focus_set()
    global x, y
    x = s_culc.notX(B, U)
    y = s_culc.notX(A, U)
    """
    def show():
        lf = LabelFrame(slave_2, text="Множина F", font='Arial 12')
        lf.grid(column=0, row=7, sticky=W, columnspan=4)
        Label(lf, text='F = {d}\n'.format(d=Fx),
              font='Arial 14', justify=LEFT, height=2).grid(column=0, row=1, columnspan=4)
    """
    def show_2():
        lf = LabelFrame(slave_2, text="Розв'язок", font='Arial 12')
        lf.grid(column=0, row=8, sticky=W, columnspan=4)
        Label(lf, text='Z = {z}\n'.format(z=exp_2.difference(x, y)),
              font='Arial 14', justify=LEFT, height=2).grid(column=0, row=1, sticky=W, columnspan=4)

    def but_disable(event):
        print(event)
        but['text'] = 'Збережено'
        but['state'] = DISABLED

    Label(slave_2, text='Множини:\n'
                        'X = {}\n'
                        'Y = {}'
                        .format(x, y), font='Arial 14 bold').grid(column=0, row=1, sticky=W, columnspan=4)

    # Button(slave_2, text="Генерувати F", font="Arial 18", command=show).grid(column=0, row=2)
    Button(slave_2, text="Показати розв'язок", font="Arial 18", command=show_2).grid(column=0, row=6)
    but = Button(slave_2, text='Зберегти в файл', font='Arial 18', command=save_to_file_3(s_culc.difer(x, y)))
    but.grid(column=0, row=3)
    but.bind("<Button-1>", but_disable)

    Label(slave_2, text='Завдання:', font='Arial 14 bold') \
        .grid(column=0, row=0, sticky=W, columnspan=4)
    photo = PhotoImage(file="Z_task.png")
    photo_but = Button(slave_2)
    photo_but.config(image=photo, width="190", height="52")
    photo_but.grid(column=1, row=0, columnspan=4)
    slave_2.mainloop()


def window5():
    slave = Toplevel(root)
    slave.title('Перевірка результатів')
    slave.grab_set()
    slave.focus_set()

    f2 = open('Результат.txt', 'r')
    f3 = open('Результат_2.txt', 'r')
    f4 = open('Результат_3.txt', 'r')

    d1 = f2.read()
    d2 = f3.read()
    z1 = f4.read()
    z2 = str(x - y)

    rez1 = 'Результати сходяться :)' if d1 == d2 else 'Помилка в обчисленні :('
    rez2 = 'Результати сходяться :)' if z1 == z2 else 'Помилка в обчисленні :('

    def but():
        Label(slave, text=rez1, font="Arial 12", fg='green').grid(column=0, row=3, sticky=W, columnspan=2)
        Label(slave, text=rez2, font="Arial 12", fg='green').grid(column=0, row=9, sticky=W, columnspan=2)

    lf1 = LabelFrame(slave, text='Множина D', font='Arial 12')
    lf2 = LabelFrame(slave, text='Множина Z', font='Arial 12')
    lf1.grid(column=0, row=1, sticky=W, columnspan=2, rowspan=2)
    lf2.grid(column=0, row=7, sticky=W, columnspan=2, rowspan=2)

    #Label(slave, text='Результати обчислень', font='Arial 14 bold').grid(column=0, row=0, columnspan=2)
    Label(lf1, text='За початковим виразом:\n'
                    'D = ((A & ¬B) & (¬A & B)) & (¬C & (¬C | B)) =\n\t\t= {}'.format(d1),
          font="Arial 14", justify=LEFT)\
        .grid(column=0, row=1, sticky=W, columnspan=2)
    Label(lf1, text='За спрощеним виразом:\n'
                    'D = (A ∆ B) & ¬C = {}'.format(d2), font="Arial 14", justify=LEFT)\
        .grid(column=0, row=2, sticky=W, columnspan=2)

    Label(slave, text='\t').grid(column=0, row=6, sticky=W, columnspan=2)

    Label(lf2, text='Z(власний алгоритм) = {}'.format(z1), font="Arial 14", justify=LEFT)\
        .grid(column=0, row=7, sticky=W, columnspan=2)
    Label(lf2, text='Z(алгоритм Python (X \ Y)) = {}'.format(z2), font="Arial 14", justify=LEFT)\
        .grid(column=0, row=8, sticky=W, columnspan=2)

    Label(slave, text='   ').grid(column=2, row=2, rowspan=2)
    Label(slave, text='\t').grid(column=0, row=11)

    Button(slave, text='Порівняти результати', font="Arial 18", command=but).grid(column=0, row=12)


root = Tk()
root.title('Головне вікно')
root.minsize(700, 400)

# menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Window2", command=window2)
filemenu.add_command(label="Window3", command=window3)
filemenu.add_command(label="Window4", command=window4)
filemenu.add_command(label="Window5", command=window5)

menubar.add_cascade(label="Windows", menu=filemenu)
root.config(menu=menubar)

Label(root, text="Виконала \n"
                 "Головаш Анастасія Василівна\n"
                 "Група ІВ-82\n"
                 "Номер у списку: 6\n"
                 "Варіант: {}".format(variant(82, 6)), font="Arial 14", width=35, height=5, justify=LEFT)\
    .grid(column=4, row=0, columnspan=3)

var = IntVar()
var.set(0)
rad0 = Radiobutton(root, text="Задати множину вручну", variable=var, value=0, command=manual_input)
rad1 = Radiobutton(root, text="Задати множину випадково", variable=var, value=1, command=random_generation)
rad0.grid(column=0, row=5, columnspan=3)
rad1.grid(column=3, row=5, columnspan=3)

Label(root, text='A:').grid(column=0, row=6, sticky=E)
Label(root, text='B:').grid(column=0, row=7, sticky=E)
Label(root, text='C:').grid(column=0, row=8, sticky=E)

entA = Entry(root, width=30, bd=3, state=DISABLED)
entA.grid(column=1, row=6, sticky=W)
entB = Entry(root, width=30, bd=3, state=DISABLED)
entB.grid(column=1, row=7, sticky=W)
entC = Entry(root, width=30, bd=3, state=DISABLED)
entC.grid(column=1, row=8, sticky=W)

Label(root, text='Потужність A:').grid(column=3, row=6, sticky=E)
Label(root, text='Потужність B:').grid(column=3, row=7, sticky=E)
Label(root, text='Потужність C:').grid(column=3, row=8, sticky=E)

lenA = Entry(root, width=10, bd=3, state=DISABLED)
lenA.grid(column=4, row=6, sticky=W)
lenB = Entry(root, width=10, bd=3, state=DISABLED)
lenB.grid(column=4, row=7, sticky=W)
lenC = Entry(root, width=10, bd=3, state=DISABLED)
lenC.grid(column=4, row=8, sticky=W)
Label(root, text='Задати універсальну множину', font="Arial 14", width=30, height=2, justify=LEFT)\
    .grid(column=0, row=10, columnspan=3)

Label(root, text='від').grid(column=0, row=11, sticky=E)
Label(root, text='до').grid(column=0, row=12, sticky=E)

entU_vid = Entry(root, width=10, bd=3)
entU_vid.grid(column=1, row=11, sticky=W)

entU_do = Entry(root, width=10, bd=3)
entU_do.grid(column=1, row=12, sticky=W)

A = set()
B = set()
C = set()
U = set()
but_OK = Button(root, text='Згенерувати множини', font='Arial 16', command=generABC)
but_OK.grid(column=3, row=11, columnspan=3)

open('Результат.txt', 'wb').close()

label_vyvid = Label(root, text='A = {}\n'
                               'B = {}\n'
                               'C = {}\n'.format(A, B, C),
                    font="Arial 14", justify=LEFT)
label_vyvid.grid(column=1, row=13, columnspan=100, sticky=W)

root.mainloop()
