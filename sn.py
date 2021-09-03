import socket
import os
import re
from struct import pack, unpack
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from snback import *
import tkinter as tk


def update():

        #update toner levels from snback.py
        label_xerox_3.config(text=xerox())
        label_xerox_3.after(upd(),update)

        label_kyocera_3.config(text=kyocera_black())
        label_kyocera_3.after(upd(),update)
        label_kyocera_4.config(text=kyocera_cyan())
        label_kyocera_4.after(upd(),update)
        label_kyocera_5.config(text=kyocera_mageneta())
        label_kyocera_5.after(upd(),update)
        label_kyocera_6.config(text=kyocera_yellow())
        label_kyocera_6.after(upd(),update)

        label_hp_buh_3.config(text=hp_buh())
        label_hp_buh_3.after(upd(),update)

        label_hp_svc_3.config(text=hp_svc())
        label_hp_svc_3.after(upd(),update)


        #clock widget data from snback.py
        clock.config(text=upd_time())
        clock.after(upd(),update)

#close main window
def exit():
    root.destroy()

#settings window
class settings(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("360x100")
        self.title('Частота обновления')
        self.iconbitmap('cog.ico')
        # initialize data
        self.languages = ('5 мин.', '10 мин.', '30 мин.',
                        '60 мин.', '120 мин.', '180 мин.',
                        '240 мин.', '300 мин')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='Выберите время обновления')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        self.output_label2 = ttk.Label(self, foreground='red')
        self.output_label2.grid(column=0, row=2, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        #display choosen option_var
        self.output_label['text'] = f'Выбрана частота: {self.option_var.get()}'
        self.output_label2['text'] = f'Чтобы изменения вступили в силу, перезапустите программу.'
        #saving option_var and convert in number
        save = (self.option_var.get())
        save = re.findall("\d+", save)[0]
        save = int(save)
        #convert minutes in miliseconds
        save = (save * 60000)
        save = str(save)
        #save in file
        file = open("set","w")
        file.write(save)
        file.close()


#main window
root = Tk()
root.iconbitmap('icon.ico')
root.title("Мониторинг картриджей")
root.geometry ('800x400')
root.minsize(800, 400)
root.maxsize(800, 400)

#paddings for labels
paddings = {'padx': 1, 'pady': 1}
paddings_col = {'padx': 2, 'pady': 0}

#header labels
label_1 = Label(root,  text='Принтер', font=("Arial",16,"bold"))
label_1.grid(column=0, row=0, sticky=tk.N+S, **paddings)
label_2 = Label(root,  text='Расположение', font=("Arial",16,"bold"))
label_2.grid(column=1, row=0, sticky=tk.N+S, **paddings)
label_3 = Label(root,  text='B, %', font=("Arial",16,"bold"),bg="#A9A9A9")
label_3.grid(column=2, row=0, sticky=tk.W, **paddings)
label_4 = Label(root,  text='C, %', font=("Arial",16,"bold"),bg="#00FFFF")
label_4.grid(column=3, row=0, sticky=tk.W, **paddings_col)
label_5 = Label(root,  text='M, %', font=("Arial",16,"bold"),bg="#BA55D3")
label_5.grid(column=4, row=0, sticky=tk.W, **paddings_col)
label_6 = Label(root,  text='Y, %', font=("Arial",16,"bold"),bg="#FFD700")
label_6.grid(column=5, row=0, sticky=tk.W, **paddings_col)
label_7 = Label(root,  text='ip', font=("Arial",16,"bold"))
label_7.grid(column=6, row=0, sticky=tk.N+S, **paddings_col)

#separotor label
label_sep = Label(root,  text='', font=("Arial",2,"bold"))
label_sep.grid(column=0, row=1, sticky=tk.N+S+W+E, **paddings)


#toner status labels

label_xerox_1 = Label(root,  text='Xerox VersaLink B7030 MFP', font=("Arial",13))
label_xerox_1.grid(column=0, row=2, sticky=tk.W, **paddings)
label_xerox_2 = Label(root,  text='Конструкторский отдел', font=("Arial",13))
label_xerox_2.grid(column=1, row=2, sticky=tk.W, **paddings)
label_xerox_3 = Label(root,  text='', font=("Arial",13,"bold"),bg="#A9A9A9")
label_xerox_3.grid(column=2, row=2, sticky=tk.N+S+W+E, **paddings_col)
label_xerox_4 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#00FFFF")
label_xerox_4.grid(column=3, row=2, sticky=tk.N+S+W+E, **paddings_col)
label_xerox_5 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#BA55D3")
label_xerox_5.grid(column=4, row=2, sticky=tk.N+S+W+E, **paddings_col)
label_xerox_6 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#FFD700")
label_xerox_6.grid(column=5, row=2, sticky=tk.N+S+W+E, **paddings_col)
label_xerox_7 = Label(root,  text='192.138.1.159', font=("Arial",13))
label_xerox_7.grid(column=6, row=2, sticky=tk.W, **paddings)

label_kyocera_1 = Label(root,  text='Kyocera ECOSYS P5021cdn', font=("Arial",13))
label_kyocera_1.grid(column=0, row=3, sticky=tk.W, **paddings)
label_kyocera_2 = Label(root,  text='Конструкторский отдел', font=("Arial",13))
label_kyocera_2.grid(column=1, row=3, sticky=tk.W, **paddings)
label_kyocera_3 = Label(root,  text='', font=("Arial",13,"bold"),bg="#A9A9A9")
label_kyocera_3.grid(column=2, row=3, sticky=tk.N+S+W+E, **paddings_col)
label_kyocera_4 = Label(root,  text='', font=("Arial",13,"bold"),bg="#00FFFF")
label_kyocera_4.grid(column=3, row=3, sticky=tk.N+S+W+E, **paddings_col)
label_kyocera_5 = Label(root,  text='', font=("Arial",13,"bold"),bg="#BA55D3")
label_kyocera_5.grid(column=4, row=3, sticky=tk.N+S+W+E, **paddings_col)
label_kyocera_6 = Label(root,  text='', font=("Arial",13,"bold"),bg="#FFD700")
label_kyocera_6.grid(column=5, row=3, sticky=tk.N+S+W+E, **paddings_col)
label_kyocera_7 = Label(root,  text='192.138.1.160', font=("Arial",13))
label_kyocera_7.grid(column=6, row=3, sticky=tk.W, **paddings)

label_hp_buh_1 = Label(root,  text='HP MFP M428fdn', font=("Arial",13))
label_hp_buh_1.grid(column=0, row=4, sticky=tk.W, **paddings)
label_hp_buh_2 = Label(root,  text='Бухгалтерский отдел', font=("Arial",13))
label_hp_buh_2.grid(column=1, row=4, sticky=tk.W, **paddings)
label_hp_buh_3 = Label(root,  text='', font=("Arial",13,"bold"),bg="#A9A9A9")
label_hp_buh_3.grid(column=2, row=4, sticky=tk.N+S+W+E, **paddings_col)
label_hp_buh_4 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#00FFFF")
label_hp_buh_4.grid(column=3, row=4, sticky=tk.N+S+W+E, **paddings_col)
label_hp_buh_5 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#BA55D3")
label_hp_buh_5.grid(column=4, row=4, sticky=tk.N+S+W+E, **paddings_col)
label_hp_buh_6 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#FFD700")
label_hp_buh_6.grid(column=5, row=4, sticky=tk.N+S+W+E, **paddings_col)
label_hp_buh_7 = Label(root,  text='192.138.10.162', font=("Arial",13))
label_hp_buh_7.grid(column=6, row=4, sticky=tk.W, **paddings)

label_hp_svc_1 = Label(root,  text='HP M1536dnf', font=("Arial",13))
label_hp_svc_1.grid(column=0, row=5, sticky=tk.W, **paddings)
label_hp_svc_2 = Label(root,  text='СВЧ отдел', font=("Arial",13))
label_hp_svc_2.grid(column=1, row=5, sticky=tk.W, **paddings)
label_hp_svc_3 = Label(root,  text='', font=("Arial",13,"bold"),bg="#A9A9A9")
label_hp_svc_3.grid(column=2, row=5, sticky=tk.N+S+W+E, **paddings_col)
label_hp_svc_4 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#00FFFF")
label_hp_svc_4.grid(column=3, row=5, sticky=tk.N+S+W+E, **paddings_col)
label_hp_svc_5 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#BA55D3")
label_hp_svc_5.grid(column=4, row=5, sticky=tk.N+S+W+E, **paddings_col)
label_hp_svc_6 = Label(root,  text='-', font=("Arial",13,"bold"),bg="#FFD700")
label_hp_svc_6.grid(column=5, row=5, sticky=tk.N+S+W+E, **paddings_col)
label_hp_svc_7 = Label(root,  text='192.138.10.173', font=("Arial",13))
label_hp_svc_7.grid(column=6, row=5, sticky=tk.W, **paddings)


#time of last update
clock=Label(root,font=("Arial",20,"bold"),bg="#A9A9A9")

update()





#options menu
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Частота обновления", command = settings)
filemenu.add_separator()
filemenu.add_command(label="Выход", command = exit)

mainmenu.add_cascade(label="Меню",
                     menu=filemenu)


root.mainloop()
