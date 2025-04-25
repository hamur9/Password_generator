import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as CTk
import pyperclip
from CTkTable import *
import requests
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x450")
        self.title("Password generator")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("img.png"), size=(460, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100,
                                          command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tk.StringVar()

        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9",
                                         variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tk.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tk.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbols_var,
                                          onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3, pady=(15, 15))


        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, "12")

        self.save_switch = CTk.CTkSwitch(master = self.settings_frame, text = "Save Password")
        self.save_switch.grid(row = 3, column = 0, columnspan = 2, pady = (5, 10))

        self.name_entry = CTk.CTkEntry(master = self.settings_frame, width=180, placeholder_text='Name')
        self.name_entry.grid(row = 3, column = 2, columnspan = 2, pady = (5, 10), padx = (0, 10))



        self.base_frame = CTk.CTkFrame(master=self)
        self.base_frame.grid(row=3, column=0, padx=(20, 20), pady=(10, 10))




        self.appearance_mode_option_menu = CTk.CTkButton(self.base_frame,
                                                             text="Add",
                                                             command=self.add_your_pass, width=100)
        self.appearance_mode_option_menu.grid(row=0, column=2, pady=(10, 10), sticky="we")
        CTk.set_appearance_mode("dark")




        self.btn_base = CTk.CTkButton(master=self.base_frame, text="Base",  command = self.check, width=100)
        self.btn_base.grid(row=0, column=3, pady=(10, 10), padx = (10, 10), sticky="we")

        self.back_main_lobby_btn = CTk.CTkButton(master=self.base_frame, text="Back", command = self.back_main_lobby_event, width=100)
        self.back_main_lobby_btn.grid(row=0,column=0,pady=(10,10), padx=(10,10), sticky="we")


    def refresh_table_event(self):
        args = {"uid": user_id, "key": key}
        cur_array = requests.get("http://127.0.0.1:5000/create_pass_mass", params=args)
        cur_array = cur_array.text.split()
        value_array = []
        global cur_key_array
        cur_key_array = []
        for j in range(1, len(cur_array) - 1, 6):
            n1 = cur_array[j]
            n2 = cur_array[j + 1]
            n3 = cur_array[j + 2]
            n4 = cur_array[j + 3]
            n5 = cur_array[j + 4]
            n6 = cur_array[j + 5]
            cur = [n2[1:-2], n3[1:-2], n4[1:-2]]
            value_array.append(cur)
            cur_key_array.append(n5[1:-1])
        self.table.grid_forget()
        self.table = CTkTable(master=self.table_frame, values=value_array, header_color="#1f6aa5",
                              command=self.press_cell_event)
        self.table.grid(sticky="nsew")


    def back_main_lobby_event(self):
        self.destroy()
        start_wind()

    def check(self):
        self.logo_label.grid_forget()
        self.base_frame.grid_forget()
        self.settings_frame.grid_forget()
        self.password_frame.grid_forget()
        self.geometry("450x400")
        self.resizable(False, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        args = {"uid": user_id, "key": key}
        cur_array = requests.get("http://127.0.0.1:5000/create_pass_mass", params=args)
        cur_array = cur_array.text.split()
        value_array = []
        global cur_key_array
        cur_key_array = []
        for j in range(1, len(cur_array)-1, 6):
            n1 = cur_array[j]
            n2 = cur_array[j+1]
            n3 = cur_array[j+2]
            n4 = cur_array[j+3]
            n5 = cur_array[j+4]
            n6 = cur_array[j+5]
            cur = [n2[1:-2], n3[1:-2], n4[1:-2]]
            value_array.append(cur)
            cur_key_array.append(n5[1:-1])



        self.table_frame = CTk.CTkScrollableFrame(master = self)
        self.table = CTkTable(master=self.table_frame, values=value_array, header_color="#1f6aa5", command=self.press_cell_event)
        self.table.grid(sticky="nsew")
        self.table_frame.grid(row=0,column=0, sticky='nsew', columnspan=2)
        self.back_button = CTk.CTkButton(master=self, text="Back", width=225, command=self.back_event)
        self.back_button.grid(row=1,column=0, sticky="we")
    def press_cell_event(self, value_first):
        global value
        value = value_first
        if value["column"] == 2:
            row = value["row"]
            details = self.table.get_row(row)
            text_lable = "EDITING | " + details[0]
            self.settings_wind = CTk.CTk()
            self.settings_wind.geometry("280x95")
            self.settings_wind.title('Settings')
            self.settings_wind.resizable(False, False)
            CTk.set_appearance_mode("dark")
            base_settings_label = CTk.CTkLabel(master = self.settings_wind, text = text_lable, font=('Century Gothic', 15))
            base_settings_label.grid(sticky="nsew", row=0, columnspan = 2, pady=20, padx=(20,20))
            settings_delete_btn = CTk.CTkButton(master = self.settings_wind, text = "DELETE", command= self.delete_cell_event)
            settings_delete_btn.grid(row=1, column = 0)
            settings_delete_btn = CTk.CTkButton(master=self.settings_wind, text="EDIT", command = self.edit_cell_event)
            settings_delete_btn.grid(row=1, column=1)
            self.settings_wind.mainloop()

        else:
            self.copy_event(value)
            self.copy_wind = CTk.CTk()  # creating cutstom tkinter window
            self.copy_wind.geometry("300x200")
            self.copy_wind.title('Copy')
            self.copy_wind.resizable(False, False)
            CTk.set_appearance_mode("dark")
            self.copy_wind.grid_columnconfigure(0, weight=1)
            self.copy_wind.grid_rowconfigure(0, weight=1)
            self.copy_wind_label = CTk.CTkLabel(master=self.copy_wind, text="COPIED!",
                                              font=('Century Gothic', 15))
            self.copy_wind_label.grid(sticky="nsew", row=0)
            self.copy_wind_button = CTk.CTkButton(master=self.copy_wind, text="Back", width=100,
                                                command=self.copy_wind.destroy)
            self.copy_wind_button.grid(row=1, sticky="ew")
            self.copy_wind.mainloop()


    def delete_cell_event(self):
        row = value["row"]
        args = {"pass_key": cur_key_array[row]}
        r = requests.get("http://127.0.0.1:5000/delete_cell", params=args)

        self.refresh_table_event()
        self.settings_wind.destroy()


    def edit_cell_event(self):
        row = value["row"]
        details = self.table.get_row(row)
        self.edit_pass_wind = CTk.CTk()
        self.edit_pass_wind.geometry("320x360")
        self.edit_pass_wind.title('Create Password')
        self.edit_pass_wind.resizable(False, False)
        CTk.set_appearance_mode("dark")
        self.edit_pass_wind.grid_columnconfigure(0, weight=1)


        self.edit_pass_wind_l1 = CTk.CTkLabel(master=self.edit_pass_wind, text="Change your Password", font=('Century Gothic', 20))
        self.edit_pass_wind_l1.place(x=70, y=45)
        self.edit_pass_wind_entry_log = CTk.CTkEntry(master=self.edit_pass_wind, width=220, placeholder_text=details[0])
        self.edit_pass_wind_entry_log.place(x=50, y=110)
        self.edit_pass_wind_entry_log.insert(0, details[0])
        self.edit_pass_wind_entry_pass = CTk.CTkEntry(master=self.edit_pass_wind, width=220, placeholder_text=details[1])
        self.edit_pass_wind_entry_pass.place(x=50, y=165)
        self.edit_pass_wind_entry_pass.insert(0, details[1])
        self.edit_pass_wind_btn = CTk.CTkButton(master=self.edit_pass_wind, width=220, text="Save", command=self.save_edited_pass,
                                     corner_radius=6)
        self.edit_pass_wind_btn.place(x=50, y=240)

        self.edit_pass_wind_back_btn = CTk.CTkButton(master=self.edit_pass_wind, text="BACK", width=220,
                                               command=self.edit_pass_wind.destroy)
        self.edit_pass_wind_back_btn.place(x=50, y=280)

        self.edit_pass_wind.mainloop()

    def save_edited_pass(self):
        row = value["row"]
        details = self.table.get_row(row)
        new_log = self.edit_pass_wind_entry_log.get()
        new_pass = self.edit_pass_wind_entry_pass.get()
        keyfern = cur_key_array[row]
        args = {"pass_key": keyfern, "new_log": new_log, "new_pass": new_pass, "key_up": key}
        r = requests.get("http://127.0.0.1:5000/update_pass_cell", params=args)
        self.refresh_table_event()

        self.save_edited_pass_wind = CTk.CTk()
        self.save_edited_pass_wind.geometry("320x360")
        self.save_edited_pass_wind.title('Create Password')
        self.save_edited_pass_wind.resizable(False, False)
        CTk.set_appearance_mode("dark")
        self.save_edited_pass_wind.grid_columnconfigure(0, weight=1)
        self.save_edited_pass_wind.grid_rowconfigure(0, weight=1)
        self.save_edited_pass_wind_lable = CTk.CTkLabel(master=self.save_edited_pass_wind, text="PASSWORD SAVED",
                                                 font=('Century Gothic', 20))
        self.save_edited_pass_wind_lable.grid(row=0, sticky="nsew")
        self.save_edited_pass_wind_back_button = CTk.CTkButton(master=self.save_edited_pass_wind, text="BACK",
                                                        command=self.wind_save_pass_destroy)
        self.save_edited_pass_wind_back_button.grid(row=1, sticky="ew")
        self.save_edited_pass_wind.mainloop()

    def wind_save_pass_destroy(self):
        self.save_edited_pass_wind.destroy()
        self.edit_pass_wind.destroy()
        self.settings_wind.destroy()

    def copy_event(self,value):
        object = value["value"]
        pyperclip.copy(object)
    def back_event(self):
        #self.passwords_frame.grid_forget()
        self.table_frame.grid_forget()
        self.back_button.grid_forget()
        #self.refresh_table_btn.grid_forget()
        self.geometry("460x450")
        self.resizable(False, False)
        self.logo_label.grid(row=0, column=0)
        self.base_frame.grid(row=3, column=0, padx=(20, 20), pady=(10, 10))#1f6aa5
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def add_your_pass(self):
        self.new_pass_wind = CTk.CTk()
        self.new_pass_wind.geometry("320x360")
        self.new_pass_wind.title('Create Password')
        self.new_pass_wind.resizable(False, False)
        CTk.set_appearance_mode("dark")
        self.new_pass_wind.grid_columnconfigure(0, weight=1)
        self.l1 = CTk.CTkLabel(master=self.new_pass_wind, text="Save your Password", font=('Century Gothic', 20))
        self.l1.place(x=70, y=45)
        self.entry_log = CTk.CTkEntry(master=self.new_pass_wind, width=220, placeholder_text='Name')
        self.entry_log.place(x=50, y=110)

        self.entry_pass = CTk.CTkEntry(master=self.new_pass_wind, width=220, placeholder_text='Password')
        self.entry_pass.place(x=50, y=165)

        self.button1 = CTk.CTkButton(master=self.new_pass_wind, width=220, text="Save", command = self.save_new_pass, corner_radius=6)
        self.button1.place(x=50, y=240)

        self.back_add_pass_btn = CTk.CTkButton(master=self.new_pass_wind, text="BACK",width=220,
                                                        command=self.new_pass_wind.destroy)
        self.back_add_pass_btn.place(x = 50, y = 280)

        self.new_pass_wind.mainloop()

    def save_new_pass(self):
        args = {"password_name": self.entry_log.get(), "new_password": self.entry_pass.get(), "user_id": user_id, "key": key}
        save_pass_event = requests.get("http://127.0.0.1:5000/save_pass_in_base", params=args)
        self.save_done_wind = CTk.CTk()
        self.save_done_wind.geometry("320x360")
        self.save_done_wind.title('Create Password')
        self.save_done_wind.resizable(False, False)
        CTk.set_appearance_mode("dark")
        self.save_done_wind.grid_columnconfigure(0, weight=1)
        self.save_done_wind.grid_rowconfigure(0, weight=1)
        self.save_done_wind_lable = CTk.CTkLabel(master=self.save_done_wind, text="PASSWORD SAVED", font=('Century Gothic', 20))
        self.save_done_wind_lable.grid(row = 0,sticky="nsew")
        self.save_done_wind_back_button = CTk.CTkButton(master=self.save_done_wind, text = "BACK", command=self.save_done_wind.destroy)
        self.save_done_wind_back_button.grid(row = 1, sticky="ew")
        self.save_done_wind.mainloop()
    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars

    def set_password(self):
        self.entry_password.delete(0, 'end')
        args = {"length": int(self.password_length_slider.get()), "characters": str(self.get_characters())}
        new_password = requests.get("http://127.0.0.1:5000/need_password", params = args)
        new_password = new_password.text
        self.entry_password.insert(0, new_password)
        save_flag = self.save_switch.get()
        password_name = self.name_entry.get()
        if save_flag == 1:
            args = {"password_name": password_name, "new_password": new_password, "user_id": user_id, "key": key}
            save_pass_event = requ  ests.get("http://127.0.0.1:5000/save_pass_in_base", params=args)


#------------------------------------------------------------------------------------------

def start_wind():
    base_login = CTk.CTk()  # creating cutstom tkinter window
    base_login.geometry("600x440")
    base_login.title('Login')
    base_login.resizable(False, False)
    CTk.set_appearance_mode("dark")

    def button_function():
        log = entry1.get()
        pwd = entry2.get()
        args = {"Login": log, "Password": pwd}
        r = requests.get("http://127.0.0.1:5000/login", params = args)
        r = r.text
        if r != "0":
            global user_id
            global key
            key = r
            user_id = log
            base_login.destroy()  # destroy current window and creating new one
            if __name__ == "__main__":
                app = App()
                app.mainloop()
        else:
            global error_wind
            error_wind = CTk.CTk()  # creating cutstom tkinter window
            error_wind.geometry("300x200")
            error_wind.title('ERROR')
            error_wind.resizable(False, False)
            CTk.set_appearance_mode("dark")
            error_wind.grid_columnconfigure(0, weight=1)
            error_wind.grid_rowconfigure(0, weight=1)
            error_label = CTk.CTkLabel(master=error_wind, text="WRONG USERNAME OR PASSWORD",
                                       font=('Century Gothic', 15))
            error_label.grid(sticky="nsew", row=0)
            error_button = CTk.CTkButton(master=error_wind, text="Back", width=100, command=back_error)
            error_button.grid(row=1, sticky="ew")
            error_wind.mainloop()

    def signup_event():
        global entry_log
        global entry_pass
        global sign_up_wind
        sign_up_wind = CTk.CTk()
        sign_up_wind.geometry("320x360")
        sign_up_wind.title('Create Account')
        sign_up_wind.resizable(False, False)
        CTk.set_appearance_mode("dark")
        l1 = CTk.CTkLabel(master=sign_up_wind, text="Create your Account", font=('Century Gothic', 20))
        l1.place(x=50, y=45)
        entry_log = CTk.CTkEntry(master=sign_up_wind, width=220, placeholder_text='Username')
        entry_log.place(x=50, y=110)

        entry_pass = CTk.CTkEntry(master=sign_up_wind, width=220, placeholder_text='Password')
        entry_pass.place(x=50, y=165)

        button1 = CTk.CTkButton(master=sign_up_wind, width=220, text="Create", command= save_account, corner_radius=6)
        button1.place(x=50, y=240)

        sign_up_wind.mainloop()

    def save_account():

        log = entry_log.get()
        pwd = entry_pass.get()
        if log == "" or pwd == "":
            global no_such_long
            no_such_long = CTk.CTk()  # creating cutstom tkinter window
            no_such_long.geometry("300x200")
            no_such_long.title('ERROR')
            no_such_long.resizable(False, False)
            CTk.set_appearance_mode("dark")
            no_such_long.grid_columnconfigure(0, weight=1)
            no_such_long.grid_rowconfigure(0, weight=1)
            no_such_long_label = CTk.CTkLabel(master=no_such_long, text="YOU CAN'T USE NOTHING HERE", font=('Century Gothic', 15))
            no_such_long_label.grid(sticky="nsew", row=0)
            no_such_long_button = CTk.CTkButton(master=no_such_long, text="Back", width=100, command=no_such_long.destroy)
            no_such_long_button.grid(row=1, sticky="ew")
            no_such_long.mainloop()
        else:
            #request!!!!!!!!
            args = {"save_login": log, "save_password": pwd}
            r = requests.get("http://127.0.0.1:5000/save_account", params=args)
            r = r.json()

            if r == 0:
                global already_has
                already_has = CTk.CTk()
                already_has.geometry("300x200")
                already_has.title('ERROR')
                already_has.resizable(False, False)
                CTk.set_appearance_mode("dark")
                already_has.grid_columnconfigure(0, weight=1)
                already_has.grid_rowconfigure(0, weight=1)
                already_has_label = CTk.CTkLabel(master=already_has, text="YOU ALREADY HAS AN ACCOUNT", font=('Century Gothic', 15))
                already_has_label.grid(sticky="nsew", row = 0)
                already_has_button = CTk.CTkButton(master=already_has, text="Back", width=100, command=back_event_has)
                already_has_button.grid(row=1, sticky="ew")
                already_has.mainloop()
            else:

                global save_wind
                save_wind = CTk.CTk()
                save_wind.geometry("320x360")
                save_wind.title('Create Account')
                save_wind.resizable(False, False)
                CTk.set_appearance_mode("dark")
                save_wind.grid_columnconfigure(0, weight=1)
                save_wind.grid_rowconfigure(0, weight=1)
                save_label = CTk.CTkLabel(master=save_wind, text="ACCOUNT CREATED", font=('Century Gothic', 15))
                save_label.grid(sticky="nsew", row = 0)

                back_button = CTk.CTkButton(master=save_wind, text="Back", width=100, command=back_event_save)
                back_button.grid(row=1, sticky="ew")
                save_wind.mainloop()

    def back_event_save():
        save_wind.destroy()
        sign_up_wind.destroy()

    def back_event_has():
        already_has.destroy()
        sign_up_wind.destroy()

    def back_error():
        error_wind.destroy()

    img_base_login = ImageTk.PhotoImage(Image.open("1618439460_32-phonoteka_org-p-chernii-fon-tekstura-49.jpg"))
    l1 = CTk.CTkLabel(master=base_login,image=img_base_login)
    l1.pack()

    # creating custom frame
    frame = CTk.CTkFrame(master=l1, width=320, height=360, corner_radius=15, fg_color="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    l2 = CTk.CTkLabel(master=frame, text="Login into your Account", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = CTk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = CTk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    # l3 = CTk.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
    # l3.place(x=155, y=195)

    # Create custom button
    button1 = CTk.CTkButton(master=frame, width=220, text="Login", command=button_function,
                            corner_radius=6)
    button1.place(x=50, y=240)

    signup_button = CTk.CTkButton(master=frame, command=signup_event, text="Sign Up", width=220, height=30,
                                  text_color="white", font=('Century Gothic', 10), corner_radius=6)
    signup_button.place(x=50, y=290)



    base_login.mainloop()


start_wind()