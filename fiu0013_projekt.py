from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk

data = [["csgo.png", "Counter-Strike: Global Offensive", "Akční", "PC", 2012, 7, "TOP", "Counter-Strike: Global Offensive (CS:GO) prohlubuje týmovou akční hratelnost, jejímž průkopníkem byl před více než 20 lety první díl této světoznámé série."],
        ["forza5.png", "Forza Horizon 5", "Závodní", "XBOX", 2021, 8, "NEW", "Forza Horizon 5 je závodní hra, která se odehrává v Mexiku. Hráči se mohou těšit na nové zážitky, které přináší nová lokace, nové auta a nové příběhy."],
        ["lous.png", "Last Of Us Part 1", "Příběhový", "PS4 / PS5", 2013, 10, "TOP", "The Last of Us je akční příběhová hra, která se odehrává v postapokalyptickém světě. Hráči se mohou těšit na příběh o přátelství, které překonává všechny překážky."],
        ["revillage.png", "Resident Evil Village", "Horor", "PC / PS4 / PS5 / XBOX", 2021, 9, "NEW", "Zažijte přežití hrůzy jako nikdy předtím v osmé hlavní části Resident Evil - Resident Evil Village. S detainí grafikou, intenzivní akcí z první osoby a mistrovským vyprávěním hrůzy nikdy nepůsobily realističtěji."],]

users = [["af", "h", "adam.fiury@vsb.cz", "Adam" , "Fiury", "Adresa", "PSČ", "město"],]

background = "#cceeff"

class App:
    def login(self):
        self.user = self.user_entry.get()
        self.password = self.pass_entry.get()
        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)
        if self.user == users[0][0] and self.password == users[0][1]:
            self.main_page()
        else:
            messagebox.showerror("Error", "Wrong username or password")
    
    def __init__(self, root):
        root.title("Login Window")
        root.geometry("300x200")
        root.config(bg=background)

        self.username_label = Label(root, text="Username: ", bg=background).place(x=50, y=50)
        self.pass_label = Label(root, text="Password: ", bg=background).place(x=50, y=90)

        self.user_entry = Entry(root)
        self.pass_entry = Entry(root, show="*")
        self.user_entry.place(x=120, y=50)
        self.pass_entry.place(x=120, y=90)
        
        self.login_button = Button(root, text="Login", command=self.login).place(x=120, y=130) 
        
    def main_page(self):
        self.new_window = Toplevel()
        root.withdraw()
        
        self.text_in_searchbar = StringVar()
        self.background = StringVar()
        self.all_picture = []
        
        self.font = font.Font(size=10, weight="bold")
        self.font2 = font.Font(size=15, weight="bold")
        
        self.new_window.title("Game Vault")
        self.new_window.config(bg=background)
        
        self.main_frame = Frame(self.new_window)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.pack()
        
        # self.page_label = Label(self.main_frame, text="Game Vault", font=self.font2, bg="#00aaff")
        # self.page_label.pack(side=TOP, fill=BOTH, expand=1)
        
        
        self.top_frame = Frame(self.main_frame, bg=background)
        self.top_frame.pack(side=TOP, fill=BOTH, expand=1)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        
        self.page_label = Label(self.top_frame, text="Game Vault", font=self.font2, bg=background)
        self.page_label.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=(10, 0))
        
        
        self.left_frame = Frame(self.new_window, bg=background)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=0, padx=(0, 10), pady=(10, 0))
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.columnconfigure(1, weight=1)
        
        def search_bar_delete(event):
            self.search_bar.delete(0, END)
        
        self.search_bar = Entry(self.top_frame, width=50, textvariable=self.text_in_searchbar)
        self.search_bar.insert(0, "Zadejte název hry")
        self.search_bar.grid(row=1, column=0, ipady=2)
        self.search_bar.bind("<FocusIn>", search_bar_delete)
        
        self.search_button = Button(self.top_frame, text="Vyhledat", cursor="hand2", font=self.font)
        self.search_button.grid(row=1, column=1, padx=(5, 0), sticky=W)
        self.search_button.bind("<Button-1>", self.search)
        
        self.browse_frame = Label(self.left_frame, text="Procházet", font=self.font, bg=background)
        self.browse_frame.grid(row=0, column=0, sticky=SW)
        
        self.main_page = Label(self.left_frame, text="Hlavní stránka", cursor="hand2", font=self.font, bg=background)
        self.main_page.grid(row=1, column=0, sticky=NW, pady=(2, 0), padx=(7, 0))
        
        self.new_games = Label(self.left_frame, text="Nové hry", cursor="hand2", font=self.font, bg=background)
        self.new_games.grid(row=2, column=0, sticky=W, pady=(2, 0), padx=(7, 0))
        self.new_games.bind("<Button-1>", self.new_games_page)
        
        self.top_games = Label(self.left_frame, text="Top hry", cursor="hand2", font=self.font, bg=background)
        self.top_games.grid(row=3, column=0, sticky=SW, pady=(2, 0), padx=(7, 0))
        self.top_games.bind("<Button-1>", self.top_games_page)
        
        self.all_games = Label(self.left_frame, text="Všechny hry", cursor="hand2", font=self.font, bg=background)
        self.all_games.grid(row=4, column=0, sticky=W, pady=(2, 0), padx=(7, 0))
        self.all_games.bind("<Button-1>", self.all_games_page)
        
        # self.reviews = Label(self.left_frame, text="Recenze", cursor="hand2", font=self.font, bg=background)
        # self.reviews.grid(row=5, column=0, sticky=NW, pady=(2, 0), padx=(7, 0))
        
        
        self.trends = Label(self.left_frame, text="Trendy", font=self.font2, bg=background)
        self.trends.grid(row=4, column=1, sticky=W, pady=(2, 0), padx=(50, 0), columnspan=2)
        
        self.sort_by = Label(self.left_frame, text="Seřadit podle:", font=self.font, bg=background)
        self.sort_by.grid(row=5, column=1, sticky=W, pady=(2, 0), padx=(50, 0), columnspan=2)
        
        
        self.first_option = StringVar()
        self.first_option.set("Obecné")
        self.date_sort = OptionMenu(self.left_frame, self.first_option, "Obecné", "Datum vydání", "Název", "Hodnocení")
        self.date_sort.grid(row=5, column=1, sticky=W, pady=(2, 0), padx=(150, 0))
        
        self.second_option = StringVar()
        self.second_option.set("Platforma")
        self.platform_sort = OptionMenu(self.left_frame, self.second_option,"Platforma", "PC", "PS4 / PS5", "XBOX")
        self.platform_sort.grid(row=5, column=1, sticky=W, pady=(2, 0), padx=(270, 0), columnspan=2)
        
        self.third_option = StringVar()
        self.third_option.set("Žánr")
        self.genre_sort = OptionMenu(self.left_frame, self.third_option,"Žánr", "Akční", "Strategie", "RPG", "Sportovní", "Závodní", "Přírodní", "Záhadné", "Horor", "Dobrodružný", "Příběhový")
        self.genre_sort.grid(row=5, column=1, sticky=W, pady=(2, 0), padx=(370, 0))
        
        self.sorted_search_button = Button(self.left_frame, text="Vyhledat", cursor="hand2", font=self.font)
        self.sorted_search_button.grid(row=5, column=1, sticky=W, pady=(2, 0), padx=(490, 0))
        self.sorted_search_button.bind("<Button-1>", self.search_by)
        
        self.game_frame = Frame(self.left_frame, border=1, relief="solid")
        self.game_frame.grid(row=2, column=2, sticky=W, columnspan=5, pady=(10, 0))
    
        self.menubar = Menu(self.new_window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Uživatel', menu=self.filemenu)
        self.filemenu.add_command(label='Nastavení', command=self.settings_window)
        self.filemenu.add_command(label='Odhlásit', command=root.quit)
        self.new_window.config(menu=self.menubar)
        
    def settings_window(self):
        self.new_window2 = Toplevel()
        self.new_window2.title("Nastavení")
        self.new_window2.config(bg=background)

        self.username_label2 = Label(self.new_window2, text="Uživatelské jméno:", font=self.font, bg=background)
        self.username_label2.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.username_entry2 = Entry(self.new_window2, font=self.font)
        self.username_entry2.grid(row=0, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.username_entry2.insert(0, users[0][0])
        self.username_entry2.config(state="disabled")
        
        self.change_username_label = Label(self.new_window2, text="Změnit", font=self.font, cursor="hand2", bg=background)
        self.change_username_label.grid(row=0, column=2, sticky=W, pady=(10, 0), padx=(10, 0))
        self.change_username_label.bind("<Button-1>", self.change_username)
        
        self.password_label2 = Label(self.new_window2, text="Heslo:", font=self.font, bg=background)
        self.password_label2.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.password_entry2 = Entry(self.new_window2, font=self.font, show="*")
        self.password_entry2.grid(row=1, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.password_entry2.insert(0, users[0][1])
        self.password_entry2.config(state="disabled")
        
        self.change_password_label = Label(self.new_window2, text="Změnit", font=self.font, cursor="hand2", bg=background)
        self.change_password_label.grid(row=1, column=2, sticky=W, pady=(10, 0), padx=(10, 0))
        self.change_password_label.bind("<Button-1>", self.change_password)
        
        self.email_label2 = Label(self.new_window2, text="Email:", font=self.font, bg=background)
        self.email_label2.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.email_entry2 = Entry(self.new_window2, font=self.font)
        self.email_entry2.grid(row=2, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.email_entry2.insert(0, users[0][2])
        self.email_entry2.config(state="disabled")
        
        self.change_email_label = Label(self.new_window2, text="Změnit", font=self.font, cursor="hand2", bg=background)
        self.change_email_label.grid(row=2, column=2, sticky=W, pady=(10, 0), padx=(10, 0))
        self.change_email_label.bind("<Button-1>", self.change_email)
        
    def change_email(self, event):
        self.ntb = ttk.Notebook(self.new_window2)
        self.ntb.grid(row=3, column=0, columnspan=3, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab1 = ttk.Frame(self.ntb)
        self.ntb.add(self.tab1, text="Změnit email")
        
        self.email_check = Label(self.tab1, text="Heslo: ", font=self.font, bg=background)
        self.email_check.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.email_check_entry = Entry(self.tab1, font=self.font, show="*")
        self.email_check_entry.grid(row=0, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.new_email = Label(self.tab1, text="Nový email: ", font=self.font, bg=background)
        self.new_email.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.new_email_entry = Entry(self.tab1, font=self.font)
        self.new_email_entry.grid(row=1, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.new_email2 = Label(self.tab1, text="Nový email znovu: ", font=self.font, bg=background)
        self.new_email2.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        
        self.new_email2_entry = Entry(self.tab1, font=self.font)
        self.new_email2_entry.grid(row=2, column=1, sticky=W, pady=(10, 0), padx=(10, 0))

        self.change_email_button = Button(self.tab1, text="Změnit", font=self.font)
        self.change_email_button.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.change_email_button.bind("<Button-1>", self.change_email2)
    
    def change_email2(self, event):
        if(self.new_email_entry.get() == "" or self.new_email2_entry.get() == ""):
            messagebox.showerror("Chyba", "Email nesmí být prázdný.")
        elif(self.new_email_entry.get() != self.new_email2_entry.get()):
            messagebox.showerror("Chyba", "Emaily se neshodují.")
        else:
            if(self.email_check_entry.get() == users[0][1]):
                self.email_entry2.config(state="normal")
                self.email_entry2.delete(0, END)
                self.email_entry2.insert(0, self.new_email_entry.get())
                self.email_entry2.config(state="disabled")
                users[0][2] = self.new_email_entry.get()
                self.ntb.destroy()
            else:
                messagebox.showerror("Chyba", "Špatné heslo.")
                self.ntb.destroy()
        
    def change_password(self, event):
        self.ntb = ttk.Notebook(self.new_window2)
        self.ntb.grid(row=3, column=0, columnspan=3, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab1 = ttk.Frame(self.ntb)
        self.ntb.add(self.tab1, text="Změnit heslo")
        self.password_check = Label(self.tab1, text="Staré heslo: ", font=self.font, bg=background)
        self.password_check.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.password_check_entry = Entry(self.tab1, font=self.font, show="*")
        self.password_check_entry.grid(row=0, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_label = Label(self.tab1, text="Nové heslo:", font=self.font, bg=background)
        self.tab_password_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_entry = Entry(self.tab1, font=self.font)
        self.tab_password_entry.grid(row=1, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_label2 = Label(self.tab1, text="Nové heslo znovu:", font=self.font, bg=background)
        self.tab_password_label2.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_entry2 = Entry(self.tab1, font=self.font)
        self.tab_password_entry2.grid(row=2, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_button = Button(self.tab1, text="Změnit", font=self.font, cursor="hand2")
        self.tab_password_button.grid(row=3, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_button.bind("<Button-1>", self.change_password2)
        
    def change_password2(self, event):
        if(self.password_check_entry.get() != users[0][1]):
            messagebox.showerror("Chyba", "Staré heslo je špatně.")
            self.ntb.destroy()
        else:
            if(self.tab_password_entry.get() == self.tab_password_entry2.get() and self.tab_password_entry.get() != "" and self.tab_password_entry2.get() != "" and self.tab_password_entry.get() != users[0][1] and self.tab_password_entry2.get() != users[0][1]):
                self.password_entry2.config(state="normal")
                self.password_entry2.delete(0, END)
                self.password_entry2.insert(0, self.tab_password_entry2.get()) 
                self.password_entry2.config(state="disabled")
                users[0][1] = self.tab_password_entry.get()
                self.ntb.destroy()
            else:
                messagebox.showerror("Chyba", "Hesla se neshodují nebo jsou prázdná.")
                self.ntb.destroy()
              
    def change_username(self, event):
        self.ntb = ttk.Notebook(self.new_window2)
        self.ntb.grid(row=1, column=0, columnspan=3, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab1 = ttk.Frame(self.ntb)
        self.ntb.add(self.tab1, text="Změnit uživatelské jméno")
        self.tab_username_label = Label(self.tab1, text="Nové uživatelské jméno:", font=self.font, bg=background)
        self.tab_username_label.grid(row=0, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_username_entry = Entry(self.tab1, font=self.font)
        self.tab_username_entry.grid(row=0, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_label = Label(self.tab1, text="Heslo:", font=self.font, bg=background)
        self.tab_password_label.grid(row=1, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_entry = Entry(self.tab1, font=self.font)
        self.tab_password_entry.grid(row=1, column=1, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_password_entry.config(show="*")
        self.tab_change_username_button = Button(self.tab1, text="Změnit", font=self.font, cursor="hand2")
        self.tab_change_username_button.grid(row=2, column=0, sticky=W, pady=(10, 0), padx=(10, 0))
        self.tab_change_username_button.bind("<Button-1>", self.change_username2)
        
    def change_username2(self, event):
        if(self.tab_username_entry.get() == ""):
            messagebox.showerror("Chyba", "Uživatelské jméno nesmí být prázdné.")
        elif(self.tab_password_entry.get() == ""):
            messagebox.showerror("Chyba", "Heslo nesmí být prázdné.")
        else:
            if(self.tab_password_entry.get() == users[0][1]):
                self.username_entry2.config(state="normal")
                self.username_entry2.delete(0, END)
                self.username_entry2.insert(0, self.tab_username_entry.get())
                self.username_entry2.config(state="disabled")
                users[0][0] = self.tab_username_entry.get()
                self.ntb.destroy()
            else:
                messagebox.showerror("Chyba", "Heslo je nesprávné.")
                self.ntb.destroy()
        

        
    def reset_game_frame(self):
        if(self.game_frame != None):
                self.game_frame.destroy()
        self.game_frame = Frame(self.left_frame, bg=background)
        self.game_frame.grid(row=6, column=1, sticky=W, columnspan=4, pady=(10, 0))
        
    def print_game(self, current_row, i):
        self.img_label = Label(self.game_frame, image=self.all_picture[i], bg=background)
        self.img_label.grid(row=current_row, column=1, sticky=W, padx=(50, 0), pady=(10, 0))
        
        self.game_name = Label(self.game_frame, text=data[i][1], font=self.font, bg=background)
        self.game_name.grid(row=current_row, column=2, sticky=NW, padx=(5, 0), pady=(10, 0))
        
        self.game_genre = Label(self.game_frame, text="Herní žánr: " + data[i][2], font=self.font, bg=background)
        self.game_genre.grid(row=current_row, column=2, sticky=NW, padx=(5, 0), pady=(32, 0))
        
        self.game_platform = Label(self.game_frame, text="Platforma: " + data[i][3], font=self.font, bg=background)
        self.game_platform.grid(row=current_row, column=2, sticky=NW, padx=(5, 0), pady=(54, 0))
        
        self.game_year = Label(self.game_frame, text="Datum vydání: " + str(data[i][4]), font=self.font, bg=background)
        self.game_year.grid(row=current_row, column=2, sticky=NW, padx=(5, 0), pady=(76, 0))
        
        self.game_rating = Label(self.game_frame, text="Rating: " + str(data[i][5]) + "/10", font=self.font, bg=background)
        self.game_rating.grid(row=current_row, column=2, sticky=NW, padx=(5, 0), pady=(98, 0))
        
        self.game_description = Label(self.game_frame, text=data[i][7], font=self.font, bg=background)
        self.game_description.grid(row=current_row, column=2, sticky=NW, padx=(5, 0), pady=(120, 0))
        
    def all_games_page(self, event):
            self.reset_game_frame()
            current_row = 2
            self.map_pictures()
            for i in range(len(data)):
                self.print_game(current_row, i)
                current_row += 1
            
            self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
            self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
                
    def new_games_page(self, event):
        self.status_page("NEW")
           
    def top_games_page(self, event):
        self.status_page("TOP")
        
    def status_page(self, status):
        self.reset_game_frame()
        current_row = 2
        self.map_pictures()
        for i in range(len(data)):
            if(status in data[i][6]):
                self.print_game(current_row, i)
                current_row += 1
            else:
                continue
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
        
    def error_mesaage(self):
        messagebox.showerror("Error", "Tato funkce ještě není dostupná")
    
    def search_by(self, event):
        if("Obecné" in self.first_option.get() and "Platforma" in self.second_option.get() and "Žánr" in self.third_option.get()):
            self.all_games_page(None)
        elif("Obecné" in self.first_option.get() and "Platforma" not in self.second_option.get() and "Žánr" in self.third_option.get()):
            self.platform_filter(self.second_option.get())
        elif("Obecné" in self.first_option.get() and "Platforma" in self.second_option.get() and "Žánr" not in self.third_option.get()):
            self.genre_filter(self.third_option.get())
        elif("Obecné" in self.first_option.get() and "Platforma" not in self.second_option.get() and "Žánr" not in self.third_option.get()):
            self.platform_genre_filter(self.second_option.get(), self.third_option.get())
        elif("Obecné" not in self.first_option.get() and "Platforma" in self.second_option.get() and "Žánr" in self.third_option.get()):
            self.general_filter(self.first_option.get())
        elif("Obecné" not in self.first_option.get() and "Platforma" not in self.second_option.get() and "Žánr" in self.third_option.get()):
            self.general_platform_filter(self.first_option.get(), self.second_option.get())
        elif("Obecné" not in self.first_option.get() and "Platforma" in self.second_option.get() and "Žánr" not in self.third_option.get()):
            self.general_genre_filter(self.first_option.get(), self.third_option.get())
        elif("Obecné" not in self.first_option.get() and "Platforma" not in self.second_option.get() and "Žánr" not in self.third_option.get()):
            self.general_platform_genre_filter(self.first_option.get(), self.second_option.get(), self.third_option.get())
            
    def genre_filter(self, option):
        self.reset_game_frame()
        current_row = 2
        self.map_pictures()
        for i in range(len(data)):
                if(option in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
                
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))

    def platform_filter(self, option):
        self.reset_game_frame()
        current_row = 2
        self.map_pictures()
        for i in range(len(data)):
                if(option in data[i][3]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
                
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
            
    def platform_genre_filter(self, option1, option2):
        self.reset_game_frame()
        current_row = 2
        self.map_pictures()
        for i in range(len(data)):
            if(option1 in data[i][3] and option2 in data[i][2]):
                self.print_game(current_row, i)
                current_row += 1
            else:
                continue
                
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
       
    def general_filter(self, option):
        self.reset_game_frame()
        current_row = 2
        if(option == "Název"):
            data.sort()
            self.map_pictures()
            for i in range(len(data)):
                self.print_game(current_row, i)
                current_row += 1
                
        elif(option == "Hodnocení"):
            data.sort(key=lambda x: x[5], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                self.print_game(current_row, i)
                current_row += 1
        else:
            data.sort(key=lambda x: x[4], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                self.print_game(current_row, i)
                current_row += 1
            
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
        
    def general_platform_filter(self, option1, option2):
        self.reset_game_frame()
        current_row = 2
        if(option1 == "Název"):
            data.sort()
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][3]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
                
        elif(option1 == "Hodnocení"):
            data.sort(key=lambda x: x[5], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][3]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
        else:
            data.sort(key=lambda x: x[4], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][3]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
            
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
        
    def general_genre_filter(self, option1, option2):
        self.reset_game_frame()
        current_row = 2
        if(option1 == "Název"):
            data.sort()
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
                
        elif(option1 == "Hodnocení"):
            data.sort(key=lambda x: x[5], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
        else:
            data.sort(key=lambda x: x[4], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
            
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
    
    def general_platform_genre_filter(self, option1, option2, option3):
        self.reset_game_frame()
        current_row = 2
        if(option1 == "Název"):
            data.sort()
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][3] and option3 in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
                
        elif(option1 == "Hodnocení"):
            data.sort(key=lambda x: x[5], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][3] and option3 in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
        else:
            data.sort(key=lambda x: x[4], reverse=True)
            self.map_pictures()
            for i in range(len(data)):
                if(option2 in data[i][3] and option3 in data[i][2]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
            
        self.more_button = Button(self.game_frame, text="Více", cursor="hand2", font=self.font, width=10, height=1, command=self.error_mesaage)
        self.more_button.grid(row=current_row, column=2, sticky=W, pady=(20, 0), padx=(500, 0))
        
    def map_pictures(self):
        self.all_picture.clear()
        for i in range(len(data)):
            self.img = Image.open(data[i][0])
            self.ratio = self.img.height/self.img.width
            self.img=self.img.resize((125,int(125*self.ratio)),Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(self.img)
            self.all_picture.append(self.photoimg)
                               
    def search(self, event):
        self.reset_game_frame()
        current_row = 2
        game_name = self.search_bar.get()
        if(game_name == ""):
            pass
        else:
            self.map_pictures()
            
            for i in range(len(data)):
                if(game_name in data[i][1]):
                    self.print_game(current_row, i)
                    current_row += 1
                else:
                    continue
        
        
root = Tk()
root.wm_title("Hlavní stránka")
app = App(root)
root.mainloop()