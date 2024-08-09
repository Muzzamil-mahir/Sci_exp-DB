# GUI for Scientific Database
This is a simple GUI made for a Scientific Database. The GUI is built using CustomTkinter and Tkinter. At the backend, SQLite is used for its serverless capability. The project requires further development. 
You’re free to do anything with this code. Further development will be done over time.

## Usage
To use, first Execute the DBcreate.py file. there about 5 tables in this file. to create additional tables use `c.execute('''<SQL Query>''')`.
A SQLite database is created when the file is executed.
## Note: 
Adding a table should be followed by modifications to th `DBgui.py` file. Since radio buttons are used to access the tables, any new table should have a corresponding radio button added, and the logic for it should be coded.


Install CustomTkinter
```
pip install customtkinter
```
then Execute DBgui.py to get the GUI
the RadioButton play a key role in this GUI to insert in or Display a any table, RadioButton with that tabel name is to be marked

## Acknowledgements
-**[credits to TomSchimansky](https://github.com/TomSchimansky/CustomTkinter.git)**
-**[CustomTkinter](https://customtkinter.tomschimansky.com/documentation)**: A Modern python UI-library based on Tkinter.
