import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
from typing import ValuesView
from numpy import lib
import view
import pandas as pd

from view import librarian_sign_in

class Library:
    def__init__(self,Name ='Byte'):
       self.Name=Name

    def connect(self):
        self.connection=sqlite3.connect('LibraryDatabase.db')
        self.cursor=self.connection.cursor()

    def create_tables(self)
    try:
        self.cursor.execute(
        '''
        create table if not exists librarian (name text,email text,password text,phone_number integer)
        
        '''
    )

    self.cursor.execute(
        '''
        create table if not exists users(name text PRIMARY KEY,email text,password text,phone_number)
        
        '''
    )

    self.cursor.execute(
        '''
        create table if not exists books(title text PRIMARY KEY, author text, publication_company text,rented_date,rented_user text, FOREIGN KEY(rented_user)REFERENCES users(name))'''
        
        )
    except Error:
        print(Error)

    def insert_librarian(self):
        try:
            self.cursor.execute(
                '''
                insert into librarian values('Neelima','se.neelima@gmail.com','password','9999999999')
                '''
            ) 
            self.connection.commit()
    except Error:
        print(Error)

    def librarian_sign_in(self,email,password):
        try:
            self.cursor.execute("select * from librarian where email=? and password=?",(email,password,))                   
            librarian=self.cursor.fetchone()
            if librarian is None:
                print("Email and password are not in the system")
            elif librarian!=None:
                print(f"Welcome {librarian[0]}")
                print(pd.DataFrame(librarian))
                return librarian[0]
            else:
                raise ValueError
        except ValueError:
            print("Email or password is wrong")
            return librarian[0]

        def librarian_register(self):
            try:
                name,email,password,ph_no=view.librarian_register_view()
                self.cursor.execute('''
                insert into librarian values(?,?,?,?)
                ''',
                (name,email,password,ph_no,))
                self.connection.commit()
            except Error:
                print Error
            
    def insert_books(self,details):#Error thrown-Need to fix
        try:
            self.cursor.execute('''
            insert into books values(?,?,?,?)
            ''',
            (details[0],details[1],details[2],details[3],details[4]))
            self.connection.commit()
        except Error:
            print(Error)
        return True















)
            

