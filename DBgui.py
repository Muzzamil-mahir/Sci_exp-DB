#21CS3501
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import * 
import customtkinter as CTK
import sqlite3
import os

CTK.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
CTK.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
   

class App(CTK.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("A Scientfic Experiments DataBase")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


         # create sidebar frame with widgets
        self.sidebar_frame = CTK.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = CTK.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=CTK.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = CTK.CTkButton(self.sidebar_frame,text="INSERT", command=self.insert_button)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.toplevel_window = None

        self.sidebar_button_2 = CTK.CTkButton(self.sidebar_frame,text='DISPLAY', command=self.display_button)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = CTK.CTkButton(self.sidebar_frame,text='P1', command=self.PRO1)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        

        self.appearance_mode_label = CTK.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = CTK.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = CTK.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = CTK.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # create radiobutton frame
        self.radiobutton_frame = CTK.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=1, padx=(30, 0), pady=(30, 0), sticky="nsew")

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = CTK.CTkLabel(master=self.radiobutton_frame, text="TABLES IN DATABASE:")
        self.label_radio_group.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        self.radio_button_1 = CTK.CTkRadioButton(master=self.radiobutton_frame,text='researcher', variable=self.radio_var, value=1)
        self.radio_button_1.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.radio_button_2 = CTK.CTkRadioButton(master=self.radiobutton_frame,text='experiment', variable=self.radio_var, value=2)
        self.radio_button_2.grid(row=1, column=1, padx=20, pady=5, sticky="w")

        self.radio_button_3 = CTK.CTkRadioButton(master=self.radiobutton_frame, text='equipment',variable=self.radio_var, value=3)
        self.radio_button_3.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        self.radio_button_4 = CTK.CTkRadioButton(master=self.radiobutton_frame,text='institution', variable=self.radio_var, value=4)
        self.radio_button_4.grid(row=2, column=1, padx=20, pady=5, sticky="w")

        self.radio_button_5 = CTK.CTkRadioButton(master=self.radiobutton_frame,text='publication', variable=self.radio_var, value=5)
        self.radio_button_5.grid(row=3, column=0, padx=20, pady=5, sticky="w")





        


    

    def change_appearance_mode_event(self, new_appearance_mode: str):
        CTK.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        CTK.set_widget_scaling(new_scaling_float)

    def insert_button(self):
        if(self.radio_var.get() == 1):
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Function to insert data into the 'researcher' table
            def insert_researcher():
                try:
                    researcher_id = int(researcher_id_entry.get())
                    name = name_entry.get()
                    email = email_entry.get()
                    experiment_id = int(experiment_id_entry.get())
                    
                    if(name == '' or email == ''):
                        raise ValueError
                except ValueError:
                    topempty = CTK.CTk()
                    topempty.title("WARNING")
                    topempty.geometry("250x100")
                    topempty.state('zoomed')
                    CTK.CTkLabel(topempty, text="ANY ENTRY CAN NOT BE EMPTY",anchor='center').grid(row=0, column=0)
                    topempty.mainloop()


                cursor.execute('''
                    INSERT INTO researcher (researcher_ID, name, Email, experiment_ID)
                    VALUES (?, ?, ?, ?)
                ''', (researcher_id, name, email, experiment_id,))
                conn.commit()
                print("Data inserted successfully!")
                insert_window.destroy()

            insert_window = CTK.CTk()
            insert_window.title("Researcher Information")
            insert_window.geometry("300x300")

            # Labels
            CTK.CTkLabel(insert_window, text="Researcher ID",anchor='center').grid(row=0, column=0)
            CTK.CTkLabel(insert_window, text="Name",anchor='center').grid(row=1, column=0)
            CTK.CTkLabel(insert_window, text="Email",anchor='center').grid(row=2, column=0)
            CTK.CTkLabel(insert_window, text="Experiment ID",anchor='center').grid(row=3, column=0)


            # Entry fields
            researcher_id_entry = CTK.CTkEntry(insert_window)
            researcher_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

            name_entry = CTK.CTkEntry(insert_window)
            name_entry.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

            email_entry = CTK.CTkEntry(insert_window)
            email_entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

            experiment_id_entry = CTK.CTkEntry(insert_window)
            experiment_id_entry.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")

          
            # Placing entry fields
            researcher_id_entry.grid(row=0, column=1)
            name_entry.grid(row=1, column=1)
            email_entry.grid(row=2, column=1)
            experiment_id_entry.grid(row=3, column=1)
           

            # Button to save data
            save_button = CTK.CTkButton(insert_window, text="Save",anchor='center', command=insert_researcher)
            save_button.grid(row=5, columnspan=5, pady=20)

           
            insert_window.mainloop()
        elif(self.radio_var.get() == 2):
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Function to insert data into the 'researcher' table
            def insert_experiment():
                try:
                    experiment_id = int(experiment_id_entry.get())
                    exp_name = str(exp_name_entry.get())
                    description = description_entry.get()
                    start_date = str(start_date_entry.get())
                    end_date = str(end_date_entry.get())
                    equipment_ID = int(equipment_id_entry.get())

                    
                except ValueError:
                    topempty = CTK.CTk()
                    topempty.title("WARNING")
                    topempty.geometry("250x100")
                    topempty.state('zoomed')
                    CTK.CTkLabel(topempty, text="ANY ENTRY CAN NOT BE EMPTY",anchor='center').grid(row=0, column=0)
                    topempty.mainloop()


                cursor.execute('''
                    INSERT INTO experiment (experiment_ID, exp_name, description, start_date, end_date, equipment_ID)
                    VALUES (?, ?, ?, ?, ?,?)
                ''', (experiment_id, exp_name, description, start_date, end_date, equipment_ID))
                conn.commit()
                print("Data inserted successfully!")
                insert_window.destroy()

            insert_window = CTK.CTk()
            insert_window.title("EXPERIMENT INFORMATION")
            insert_window.geometry("450x400")

            # Labels
            CTK.CTkLabel(insert_window, text="experiment_id",anchor='center').grid(row=0, column=0)
            CTK.CTkLabel(insert_window, text="exp_name",anchor='center').grid(row=1, column=0)
            CTK.CTkLabel(insert_window, text="description",anchor='center').grid(row=2, column=0)
            CTK.CTkLabel(insert_window, text="start_date",anchor='center').grid(row=3, column=0)
            CTK.CTkLabel(insert_window, text="end_date",anchor='center').grid(row=4, column=0)
            CTK.CTkLabel(insert_window, text="equipment_ID",anchor='center').grid(row=5, column=0)

            # Entry fields
            experiment_id_entry = CTK.CTkEntry(insert_window)
            experiment_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

            exp_name_entry= CTK.CTkEntry(insert_window)
            exp_name_entry.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

            description_entry = CTK.CTkEntry(insert_window)
            description_entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

            start_date_entry = CTK.CTkEntry(insert_window)
            start_date_entry.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")

            end_date_entry = CTK.CTkEntry(insert_window)
            end_date_entry.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")

            equipment_id_entry = CTK.CTkEntry(insert_window)
            equipment_id_entry.grid(row=5, column=5, padx=10, pady=10, sticky="nsew")

          
            # Placing entry fields
            experiment_id_entry.grid(row=0, column=1)
            exp_name_entry.grid(row=1, column=1)
            description_entry.grid(row=2, column=1)
            start_date_entry.grid(row=3, column=1)
            end_date_entry.grid(row=4, column=1)
            equipment_id_entry.grid(row=5, column=1)

            # Button to save data
            save_button = CTK.CTkButton(insert_window, text="Save",anchor='center', command=insert_experiment)
            save_button.grid(row=6, columnspan=6, pady=20)
       
            insert_window.mainloop()
        elif(self.radio_var.get() == 3):
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Function to insert data into the 'researcher' table
            def insert_researcher():
                try:
                    equipment_id = int(equipment_id_entry.get())
                    nameofequ = nameofequ_entry.get()
                    quantity = int(quantity_entry.get())
                    institution_id = int(institution_id_entry.get())
                    
                    if(nameofequ == ''):
                        raise ValueError
                except ValueError:
                    topempty = CTK.CTk()
                    topempty.title("WARNING")
                    topempty.geometry("250x100")
                    topempty.state('zoomed')
                    CTK.CTkLabel(topempty, text="ANY ENTRY CAN NOT BE EMPTY",anchor='center').grid(row=0, column=0)
                    topempty.mainloop()


                cursor.execute('''
                    INSERT INTO equipment (equipment_ID, nameofequ, quantity, institution_ID)
                    VALUES (?, ?, ?, ?)
                ''', (equipment_id, nameofequ, quantity, institution_id))
                
                conn.commit()
                print("Data inserted successfully!")
                insert_window.destroy()

            insert_window = CTK.CTk()
            insert_window.title("eqwuipment Information")
            insert_window.geometry("300x300")

            # Labels
            CTK.CTkLabel(insert_window, text="equipment ID",anchor='center').grid(row=0, column=0)
            CTK.CTkLabel(insert_window, text="Nameofequ",anchor='center').grid(row=1, column=0)
            CTK.CTkLabel(insert_window, text="quantitty",anchor='center').grid(row=2, column=0)
            CTK.CTkLabel(insert_window, text="institution ID",anchor='center').grid(row=3, column=0)


            # Entry fields
            equipment_id_entry = CTK.CTkEntry(insert_window)
            equipment_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

            nameofequ_entry = CTK.CTkEntry(insert_window)
            nameofequ_entry.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

            quantity_entry = CTK.CTkEntry(insert_window)
            quantity_entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

            institution_id_entry = CTK.CTkEntry(insert_window)
            institution_id_entry.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")
          
            # Placing entry fields
            equipment_id_entry.grid(row=0, column=1)
            nameofequ_entry.grid(row=1, column=1)
            quantity_entry.grid(row=2, column=1)
            institution_id_entry.grid(row=3, column=1)
           

            # Button to save data
            save_button = CTK.CTkButton(insert_window, text="Save",anchor='center', command=insert_researcher)
            save_button.grid(row=5, columnspan=5, pady=20)

           
            insert_window.mainloop()
        
        elif(self.radio_var.get() == 4):
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Function to insert data into the 'researcher' table
            def insert_researcher():
                try:
                    institution_ID = int(institution_ID_entry.get())
                    inst_name = inst_name_entry.get()
                    location = location_entry.get()
             
                    if(inst_name == '' or location == ''):
                        raise ValueError
                except ValueError:
                    topempty = CTK.CTk()
                    topempty.title("WARNING")
                    topempty.geometry("250x100")
                    topempty.state('zoomed')
                    CTK.CTkLabel(topempty, text="ANY ENTRY CAN NOT BE EMPTY",anchor='center').grid(row=0, column=0)
                    topempty.mainloop()


                cursor.execute('''
                    INSERT INTO institution (institution_ID, inst_name, location)
                    VALUES (?, ?, ?)
                ''', (institution_ID, inst_name, location))
                conn.commit()
                print("Data inserted successfully!")
                insert_window.destroy()

            insert_window = CTK.CTk()
            insert_window.title("INSTITUTION INFORMATION")
            insert_window.geometry("300x300")

            # Labels
            CTK.CTkLabel(insert_window, text="institution_ID",anchor='center').grid(row=0, column=0)
            CTK.CTkLabel(insert_window, text="inst_Name",anchor='center').grid(row=1, column=0)
            CTK.CTkLabel(insert_window, text="location",anchor='center').grid(row=2, column=0)
        


            # Entry fields
            institution_ID_entry = CTK.CTkEntry(insert_window)
            institution_ID_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

            inst_name_entry = CTK.CTkEntry(insert_window)
            inst_name_entry.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

            location_entry = CTK.CTkEntry(insert_window)
            location_entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")


            # Placing entry fields
            institution_ID_entry.grid(row=0, column=1)
            inst_name_entry.grid(row=1, column=1)
            location_entry.grid(row=2, column=1)
           
            # Button to save data
            save_button = CTK.CTkButton(insert_window, text="Save",anchor='center', command=insert_researcher)
            save_button.grid(row=5, columnspan=5, pady=20)
            insert_window.mainloop()
        
        elif(self.radio_var.get() == 5):
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Function to insert data into the 'researcher' table
            def insert_researcher():
                try:
                    publication_ID = int(publication_ID_entry.get())
                    title = title_entry.get()
                    authors = authors_entry.get()
                    publication_date = publication_date_entry.get()
                    experiment_ID = int(experiment_ID_entry.get())
                    institution_ID = int (institution_ID_entry.get())
                    
                    if(title == '' or authors == '' or publication_date == ''):
                        raise ValueError
                except ValueError:
                    topempty = CTK.CTk()
                    topempty.title("WARNING")
                    topempty.geometry("250x100")
                    topempty.state('zoomed')
                    CTK.CTkLabel(topempty, text="ANY ENTRY CAN NOT BE EMPTY",anchor='center').grid(row=0, column=0)
                    topempty.mainloop()


                cursor.execute('''
                    INSERT INTO publication (publication_ID,title,authors,publication_date,experiment_ID,institution_ID)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (publication_ID,title,authors,publication_date,experiment_ID,institution_ID))
                conn.commit()
                print("Data inserted successfully!")
                insert_window.destroy()

            insert_window = CTK.CTk()
            insert_window.title("PUBLICATION  INOFRMATION")
            insert_window.geometry("400x470")

            # Labels
            CTK.CTkLabel(insert_window, text="publication_ID",anchor='center').grid(row=0, column=0)
            CTK.CTkLabel(insert_window, text="title",anchor='center').grid(row=1, column=0)
            CTK.CTkLabel(insert_window, text="authors",anchor='center').grid(row=2, column=0)
            CTK.CTkLabel(insert_window, text="publication_date",anchor='center').grid(row=3, column=0)
            CTK.CTkLabel(insert_window, text="Experiment ID",anchor='center').grid(row=4, column=0)
            CTK.CTkLabel(insert_window, text="institution_ID",anchor='center').grid(row=5, column=0)


            # Entry fields
            publication_ID_entry = CTK.CTkEntry(insert_window)
            publication_ID_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

            title_entry = CTK.CTkEntry(insert_window)
            title_entry.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

            authors_entry = CTK.CTkEntry(insert_window)
            authors_entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

            publication_date_entry = CTK.CTkEntry(insert_window)
            publication_date_entry.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")

            experiment_ID_entry = CTK.CTkEntry(insert_window)
            experiment_ID_entry.grid(row=5, column=5, padx=10, pady=10, sticky="nsew")

            institution_ID_entry = CTK.CTkEntry(insert_window)
            institution_ID_entry.grid(row=6, column=6, padx=10, pady=10, sticky="nsew")

            


          
            # Placing entry fields
            publication_ID_entry.grid(row=0, column=1)
            title_entry.grid(row=1, column=1)
            authors_entry.grid(row=2, column=1)
            publication_date_entry.grid(row=3, column=1)
            experiment_ID_entry.grid(row=4, column=1)
            institution_ID_entry.grid(row=5, column=1)
           

            # Button to save data
            save_button = CTK.CTkButton(insert_window, text="Save",anchor='center', command=insert_researcher)
            save_button.grid(row=6, columnspan=6, pady=20)

           
            insert_window.mainloop()

    def display_button(self):
        
        if(self.radio_var.get() == 1):
            
            r = tk.Tk()

            r.title("RESEARCHER TABLE") 
            r.geometry("600x600")

            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM researcher;")
            data = cursor.fetchall()  


            tree = ttk.Treeview (r)
            tree['show'] = 'headings'

            s = ttk.Style(r)
            s.theme_use('classic')

            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))

            #Define number of columns 
            tree["columns"]= ('researcher_ID', 'name', 'Email', 'experiment_ID')

            #Assign the width, minwidth and anchor to the respective columns 
            tree.column("researcher_ID", width=50, minwidth=50,anchor=tk.CENTER)
            tree.column("name", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("Email", width=50, minwidth=50,anchor=tk.CENTER)
            tree.column("experiment_ID", width=50, minwidth=50,anchor=tk.CENTER)

            tree.heading("researcher_ID", text='researcher_ID',anchor=tk.CENTER)
            tree.heading("name", text='name',anchor=tk.CENTER)
            tree.heading("Email", text='Email',anchor=tk.CENTER)
            tree.heading("experiment_ID", text='experiment_ID',anchor=tk.CENTER)

            # data will be a list of tuples, where each tuple represents a row from the 'researcher' table
            i = 0
            for row in data:
                tree.insert('', i,text='',values=(row[0],row[1],row[2],row[3]) )
                i = i + 1

            hsb = ttk.Scrollbar(r, orient="horizontal")

            hsb.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb.set)
            hsb.pack(fill=X, side = BOTTOM) 

            # Adding vertical scrollbar
            vsb = ttk.Scrollbar(r, orient="vertical")
            vsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=vsb.set)
            vsb.pack(fill=Y, side=RIGHT)
            # Packing the treeview
            tree.pack(fill=BOTH, expand=True)
            r.mainloop()

        elif(self.radio_var.get() == 2):
            r = tk.Tk()
            r.title("EXPERIMENT TABLE") 
            r.geometry("600x600")
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM experiment;")
            data = cursor.fetchall()  


            tree = ttk.Treeview (r)
            tree['show'] = 'headings'

            s = ttk.Style(r)
            s.theme_use('classic')

            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))

            #Define number of columns 
            tree["columns"]= ('experiment_ID', 'exp_name', 'description', 'start_date', 'end_date','equipment_ID' )

            #Assign the width, minwidth and anchor to the respective columns 
            tree.column("experiment_ID", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("exp_name", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("description", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("start_date", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("end_date", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("equipment_ID", width=100, minwidth=100,anchor=tk.CENTER)

            tree.heading("experiment_ID", text='experiment_ID',anchor=tk.CENTER)
            tree.heading("exp_name", text='exp_nam',anchor=tk.CENTER)
            tree.heading("description", text='description',anchor=tk.CENTER)
            tree.heading("start_date", text='start_date',anchor=tk.CENTER)
            tree.heading("end_date", text='end_date',anchor=tk.CENTER)
            tree.heading("equipment_ID", text='equipment_ID',anchor=tk.CENTER)

            # data will be a list of tuples, where each tuple represents a row from the 'researcher' table
            i = 0
            for row in data:
                tree.insert('', i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5]) )
                i = i + 1

            hsb = ttk.Scrollbar(r, orient="horizontal")

            hsb.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb.set)
            hsb.pack(fill=X, side = BOTTOM) 

            # Adding vertical scrollbar
            vsb = ttk.Scrollbar(r, orient="vertical")
            vsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=vsb.set)
            vsb.pack(fill=Y, side=RIGHT)


            # Packing the treeview
            tree.pack(fill=BOTH, expand=True)

            r.mainloop()
        elif(self.radio_var.get() == 3):
            r = tk.Tk()
            r.title("EQUIPMENT TABLE") 
            r.geometry("600x600")

            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM equipment;")
            data = cursor.fetchall()  


            tree = ttk.Treeview (r)
            tree['show'] = 'headings'

            s = ttk.Style(r)
            s.theme_use('classic')

            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))

            #Define number of columns 
            tree["columns"]= ('equipment_ID', 'nameofequ', 'quantity', 'institution_ID')

            #Assign the width, minwidth and anchor to the respective columns 
            tree.column("equipment_ID", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("nameofequ", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("quantity", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("institution_ID", width=100, minwidth=100,anchor=tk.CENTER)


            tree.heading("equipment_ID", text='equipment_ID',anchor=tk.CENTER)
            tree.heading("nameofequ", text='nameofequ',anchor=tk.CENTER)
            tree.heading("quantity", text='quantity',anchor=tk.CENTER)
            tree.heading("institution_ID", text='institution_ID',anchor=tk.CENTER)


            # data will be a list of tuples, where each tuple represents a row from the 'researcher' table
            i = 0
            for row in data:
                tree.insert('', i,text='',values=(row[0],row[1],row[2],row[3]) )
                i = i + 1

            hsb = ttk.Scrollbar(r, orient="horizontal")

            hsb.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb.set)
            hsb.pack(fill=X, side = BOTTOM) 

            # Adding vertical scrollbar
            vsb = ttk.Scrollbar(r, orient="vertical")
            vsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=vsb.set)
            vsb.pack(fill=Y, side=RIGHT)


            # Packing the treeview
            tree.pack(fill=BOTH, expand=True)

            r.mainloop()

        elif(self.radio_var.get() == 4):
            r = tk.Tk()
            r.title("INSTITUTION TABLE") 
            r.geometry("600x600")
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM institution;")
            data = cursor.fetchall()  


            tree = ttk.Treeview (r)
            tree['show'] = 'headings'

            s = ttk.Style(r)
            s.theme_use('classic')

            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))

            #Define number of columns 
            tree["columns"]= ('institution_ID', 'inst_name', 'location')

            #Assign the width, minwidth and anchor to the respective columns 
            tree.column("institution_ID", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("inst_name", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("location", width=100, minwidth=100,anchor=tk.CENTER)



            tree.heading("institution_ID", text='institution_ID',anchor=tk.CENTER)
            tree.heading("inst_name", text='inst_name',anchor=tk.CENTER)
            tree.heading("location", text='location',anchor=tk.CENTER)



            # data will be a list of tuples, where each tuple represents a row from the 'researcher' table
            i = 0
            for row in data:
                tree.insert('', i,text='',values=(row[0],row[1],row[2]) )
                i = i + 1

            hsb = ttk.Scrollbar(r, orient="horizontal")

            hsb.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb.set)
            hsb.pack(fill=X, side = BOTTOM) 

            # Adding vertical scrollbar
            vsb = ttk.Scrollbar(r, orient="vertical")
            vsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=vsb.set)
            vsb.pack(fill=Y, side=RIGHT)


            # Packing the treeview
            tree.pack(fill=BOTH, expand=True)

            r.mainloop()
        
        elif(self.radio_var.get() == 5):
            r = tk.Tk()

            r.title("PUBLICATION TABLE") 
            r.geometry("600x600")
            script_dir = os.path.dirname(__file__)  # Directory of the script
            db_path = os.path.join(script_dir, 'sci_data.db')
            # Establish connection to the SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM publication;")
            data = cursor.fetchall()  


            tree = ttk.Treeview (r)
            tree['show'] = 'headings'

            s = ttk.Style(r)
            s.theme_use('classic')

            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))

            #Define number of columns 
            tree["columns"]= ('publication_ID', 'title', 'authors', 'publication_date', 'experiment_ID', 'institution_ID')

            #Assign the width, minwidth and anchor to the respective columns 
            tree.column("publication_ID", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("title", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("authors", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("publication_date", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("experiment_ID", width=100, minwidth=100,anchor=tk.CENTER)
            tree.column("institution_ID", width=100, minwidth=100,anchor=tk.CENTER)



            tree.heading("publication_ID", text='publication_ID',anchor=tk.CENTER)
            tree.heading("title", text='title',anchor=tk.CENTER)
            tree.heading("authors", text='authors',anchor=tk.CENTER)
            tree.heading("publication_date", text='authors ',anchor=tk.CENTER)
            tree.heading("experiment_ID", text='experiment_ID',anchor=tk.CENTER)
            tree.heading("institution_ID", text='institution_ID',anchor=tk.CENTER)




            # data will be a list of tuples, where each tuple represents a row from the 'researcher' table
            i = 0
            for row in data:
                tree.insert('', i,text='',values=(row[0],row[1],row[2],row[3], row[4], row[5]) )
                i = i + 1

            hsb = ttk.Scrollbar(r, orient="horizontal")

            hsb.configure(command=tree.xview)
            tree.configure(xscrollcommand=hsb.set)
            hsb.pack(fill=X, side = BOTTOM) 

            # Adding vertical scrollbar
            vsb = ttk.Scrollbar(r, orient="vertical")
            vsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=vsb.set)
            vsb.pack(fill=Y, side=RIGHT)


            # Packing the treeview
            tree.pack(fill=BOTH, expand=True)

            r.mainloop()
    
    def open_input_dialog_event(self):
        dialog = CTK.CTkInputDialog(text="Enter Publication ID: ", title="PROCEDURE 1")
        ID = dialog.get_input()
        return ID
    
    def PRO1 (self):
        try:
            ET = int(self.open_input_dialog_event())
            print(ET)
            if(ET):
                r = tk.Tk()
                r.title("student details") 
                r.geometry("700x150")
                script_dir = os.path.dirname(__file__)  # Directory of the script
                db_path = os.path.join(script_dir, 'sci_data.db')
                # Establish connection to the SQLite database
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM publication WHERE publication_ID = ?;", (ET,))
                data = cursor.fetchall()
                if not data:
                    r.destroy()
                    raise ValueError  
                tree = ttk.Treeview (r)
                tree['show'] = 'headings'

                s = ttk.Style(r)
                s.theme_use('classic')

                s.configure(".", font=('Helvetica', 11))
                s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))

                #Define number of columns 
                tree["columns"]= ('publication_ID', 'title', 'authors', 'publication_date', 'experiment_ID', 'institution_ID')

                #Assign the width, minwidth and anchor to the respective columns 
                tree.column("publication_ID", width=100, minwidth=100,anchor=tk.CENTER)
                tree.column("title", width=100, minwidth=100,anchor=tk.CENTER)
                tree.column("authors", width=100, minwidth=100,anchor=tk.CENTER)
                tree.column("publication_date", width=100, minwidth=100,anchor=tk.CENTER)
                tree.column("experiment_ID", width=100, minwidth=100,anchor=tk.CENTER)
                tree.column("institution_ID", width=100, minwidth=100,anchor=tk.CENTER)



                tree.heading("publication_ID", text='publication_ID',anchor=tk.CENTER)
                tree.heading("title", text='title',anchor=tk.CENTER)
                tree.heading("authors", text='authors',anchor=tk.CENTER)
                tree.heading("publication_date", text='authors ',anchor=tk.CENTER)
                tree.heading("experiment_ID", text='experiment_ID',anchor=tk.CENTER)
                tree.heading("institution_ID", text='institution_ID',anchor=tk.CENTER)




                # data will be a list of tuples, where each tuple represents a row from the 'researcher' table
                i = 0
                for row in data:
                    tree.insert('', i,text='',values=(row[0],row[1],row[2],row[3], row[4], row[5]) )
                    i = i + 1

                hsb = ttk.Scrollbar(r, orient="horizontal")

                hsb.configure(command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X, side = BOTTOM) 

                # Adding vertical scrollbar
                vsb = ttk.Scrollbar(r, orient="vertical")
                vsb.configure(command=tree.yview)
                tree.configure(yscrollcommand=vsb.set)
                vsb.pack(fill=Y, side=RIGHT)
                # Packing the treeview
                tree.pack(fill=BOTH, expand=True)
                r.mainloop()
        except:
            topempty = CTK.CTk()
            topempty.title("WARNING")
            topempty.geometry("250x100")
            topempty.state('zoomed')
            CTK.CTkLabel(topempty, text="NO SUCH PUBLICATION_ID EXIST \nPLEASE TRY AGAIN WITH VALID ID",anchor=CTK.CENTER).grid(row=0, column=0)
            topempty.mainloop()



        


if __name__ == "__main__":
    app = App()
    app.mainloop()
