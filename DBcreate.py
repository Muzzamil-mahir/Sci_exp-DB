import sqlite3 as sq
con = sq.connect("sci_data.db")
c = con.cursor()

#Creating Tables
c.execute("""CREATE TABLE researcher (
    researcher_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    Email TEXT NOT NULL,
    experiment_ID INTEGER,
    FOREIGN KEY (experiment_ID) REFERENCES experiment(experiment_ID)
);""")

c.execute("""CREATE TABLE experiment (
    experiment_ID INTEGER PRIMARY KEY,
    exp_name TEXT NOT NULL,
    description TEXT NOT NULL,
    start_date DATE DEFAULT '0000-01-01',
    end_date DATE DEFAULT '0000-01-01',
    equipment_ID INTEGER NOT NULL,
    FOREIGN KEY (equipment_ID) REFERENCES equipment(equipment_ID)
);""")

c.execute("""CREATE TABLE equipment (
    equipment_ID INTEGER PRIMARY KEY,
    nameofequ TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    institution_ID INTEGER NOT NULL, -- Added NOT NULL constraint
    FOREIGN KEY (institution_ID) REFERENCES institution(institution_ID)
);""")

c.execute("""CREATE TABLE institution(
          institution_ID INTEGER PRIMARY KEY,
          inst_name TEXT NOT NULL,
          location TEXT NOT NULL
);""")

c.execute("""CREATE TABLE publication (
    publication_ID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    publication_date DATE NOT NULL,
    experiment_ID INTEGER NOT NULL,
    institution_ID INTEGER NOT NULL,
    FOREIGN KEY (experiment_ID) REFERENCES experiment(experiment_ID),
    FOREIGN KEY (institution_ID) REFERENCES institution(institution_ID)
);
""")



#Triggers
c.execute("""CREATE TRIGGER validate_experiment_dates
            BEFORE INSERT ON experiment
            FOR EACH ROW
            WHEN NEW.start_date > NEW.end_date
            BEGIN
                SELECT RAISE(ABORT, 'Start date cannot be later than end date');
            END;

 """)
c.execute('''CREATE TABLE IF NOT EXISTS log (
  timestamp DATETIME PRIMARY KEY DEFAULT CURRENT_TIMESTAMP,
  action TEXT NOT NULL,
  table_name TEXT NOT NULL,
  record_id INTEGER REFERENCES publication(publication_ID)
);
''')
c.execute("""CREATE TRIGGER log_publication_creation
            AFTER INSERT ON publication
            FOR EACH ROW
            BEGIN
                INSERT INTO log (timestamp, action, table_name, record_id)
                VALUES (DATETIME('now'), 'CREATE', 'publication', NEW.publication_ID);
            END;

 """)