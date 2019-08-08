'''
The purpose of this project is to save the title of movies that I have wached into a database.
Create a main page
On the main page there will be a add movie button and an exit button that will exit the program
To add movie user should click the add movie button, this should open a new window
In the new window user can enter a title and have it saved to the databse
The program will save the title, year, runtime, actors, plot
The program will also display those information on window
'''



from tkinter import *
from tkinter import ttk
import urllib.request
import json
import sqlite3

conn = sqlite3.connect('mydatabase.db')   # Connects with databse
c = conn.cursor()

class Mymedia():             # This class opens the main window
    def __init__(self,master):

        self.master=master
        self.master.geometry('250x200')
        self.master.title('My Media')
        self.master.configure(background='red4')

        
        self.label1=Label(self.master,text='My Media Directory',bg='red4',fg='white').pack()
        self.button1=Button(self.master,text="Add Movie",fg='red',command=self.movie).pack()
        self.button3=Button(self.master,text="Exit",fg='blue',command=self.exit).pack()

    def exit(self):
        self.master.destroy()

    def movie(self):
        root2=Toplevel(self.master)
        myGUI=getmovie(root2)

class getmovie():
    def __init__ (self,master):

        c.execute("CREATE TABLE IF NOT EXISTS movieInfo(Title TEXT,Year DATE, Runtime TEXT,Actors TEXT, Plot TEXT)")

        self.master=master
        self.master.geometry('9500x400')
        self.master.title('Enter Movies')

        self.label2=Label(self.master,text="Name").pack()
        self.name=Entry(self.master) # The movie title is entered
        self.name.pack()

        self.button1=Button(self.master,text="Add title",fg='red')
        self.button1.pack()
        self.button1["command"]=self.getinfo # by clicking button, it conducts the action of get info

    def getinfo(self):
        query=(self.name.get())        # gets the title from previous entry   
        url=("http://www.omdbapi.com/?t=")
        movie=query.replace(" ", "%20")
        final_url= url+movie
        json_obj=urllib.request.urlopen(final_url)
        fullinfo=json.load(json_obj)
        print(fullinfo)                 #Using this to test if info is coming from api
        print (final_url)

        c.execute("CREATE TABLE IF NOT EXISTS movieInfo(Title TEXT,Year DATE, Runtime TEXT,Actors TEXT, Plot TEXT)") # Creates table if it does not exist
        title = fullinfo["Title"]
        year = fullinfo["Year"]
        runtime = fullinfo["Runtime"]
        actor = fullinfo["Actors"]
        plot =fullinfo["Plot"]
        
        titlelable=Label(self.master,text=('Title: {}').format(title),fg='red').pack()
        titlelable=Label(self.master,text=('Year: {}').format(year),fg='orange').pack()
        titlelable=Label(self.master,text=('Runtime: {}').format(runtime),fg='black').pack()
        titlelable=Label(self.master,text=('Actors: {}').format(actor),fg='green').pack()
        titlelable=Label(self.master,text=('Plot: {}').format(plot),fg='blue').pack()

        c.execute ("INSERT INTO movieInfo (Title, Year, Runtime, Actors, Plot) VALUES (?,?,?,?,?)",(title,year,runtime,actor,plot))
       
        conn.commit()
                
            

        
 
    
def main():
     root=Tk()
     myGUI=Mymedia(root)
     

if __name__ == '__main__':
     main()
    

 
