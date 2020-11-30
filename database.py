#  Get database package
import sqlite3

# SQL code create table
CREATE_CARD_TABLE = "CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);"

# SQL code insetrt new card
INSERT_CARD = "INSERT INTO card (number, pin, balance) VALUES(?, ?, ?);"

# SQL code get all new cards for display
GET_ALL_CARDS = "SELECT * FROM card;"

# SQL code get new card by number for display
GET_CARDS_BY_NUMBER = "SELECT * FROM card WHERE number = ?;"

# Make the database file
def connect():
    return sqlite3.connect("card.s3db")

# Make database tables
def create_tables(connection):
    with connection:
        connection.execute(CREATE_CARD_TABLE)

#  Add new cards to database tables
def add_card(connection, number, pin, balance):
    with connection:
        connection.execute(INSERT_CARD, (number, pin, balance))

# Retrive all cards for display
def get_all_cards(connection):
    with connection:
        return connection.execute(GET_ALL_CARDS).fetchall()

#  Retrieve one card for display
def get_card_by_number(connection, number):
    with connection:
        return connection.execute(GET_CARDS_BY_NUMBER, (number,)).fetchall()




