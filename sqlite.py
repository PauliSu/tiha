import sqlite3

# tekee kannan jos sitä ei ole tai käyttää jos on
conn = sqlite3.connect('tiha.db')

# tekee tietokannan muistiin
#conn = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE tiha (
        appi text,
        tietovaranto text,
        email text
    )""")

#c.execute("INSERT INTO customers VALUES ('Pauli', 'Sutelainen', 'pauli.sutelainen@gmail.com')")
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

#many_customers =    [
#                        ('eka äppi','varanto1','eka.nimi@domain.com'),
#                        ('toka äppi','varanto2','toka.nimi@domain.com')
#                    ]

#c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

# Commit our command
#conn.commit()

# Close connection
conn.close()
