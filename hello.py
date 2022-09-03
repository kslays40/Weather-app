from importlib.resources import contents
from tkinter import *
import webbrowser
from PIL import ImageTk,Image
import requests
import json
root = Tk()

# Main window of Application
root.title("Please Login")
root.geometry("500x700")
root.config(borderwidth=5)

# Possible Login
possible_users = {'user1': 'user1pass', 'z': 'z'}  # dictionary of corresponding user name and passwords

# StringVars
the_user = StringVar()  # used to retrieve input from entry
the_pass = StringVar()

# Creating Label Widget
myLabel1 = Label(root, text="Username :")
myLabel2 = Label(root, text="Password :")
bad_pass = Label(root, text="Incorrect Username or Password")

# Entry fields
username_1 = Entry(root, textvariable=the_user)
password_1 = Entry(root, show='*', textvariable=the_pass)


# Putting labels onto screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Entry field Locations
username_1.grid(row=0, column=1)
password_1.grid(row=1, column=1)


def login(user):
    forget_login_window()
    next_window(user)


def check_login():
    requested_user = the_user.get()
    try:
        if possible_users[requested_user] == the_pass.get():
            login(requested_user)
        else:
            bad_pass.grid(row=2, column=1)
    except KeyError:
        bad_pass.grid(row=2, column=1)


#space giving technique
space1 = Label(root, text="")
loginButton1 = Button(root, text="Login", command=check_login)
cancelButton3 = Button(root, text="Cancel", command=quit)
space2 = Label(root, text="")
#space giving technique

# Putting buttons onto screen
space1.grid(row=6,column=1)
loginButton1.grid(row=7, column=1)
space2.grid(row=8,column=1)
cancelButton3.grid(row=9, column=1)


# New window

def forget_login_window():  # forget all the grid items.
    username_1.grid_forget()
    password_1.grid_forget()
    myLabel1.grid_forget()
    myLabel2.grid_forget()
    loginButton1.grid_forget()
    cancelButton3.grid_forget()
    bad_pass.grid_forget()



def next_window(my_user):
    root.title(my_user)
    #changing tkinter window icon 
    root.wm_iconbitmap("MicrosoftTeams-image.ico")

    #function for cityinfo
    def city():
        cinfo = Label(root , text = "Working on ......")
        cinfo.grid(row=4, column=6)

    #function for diseases 
    def disease():
        dinfo = Label(root, text = "Working on ......")
        dinfo.grid(row=4, column=2)
    
    prone = Button(root,text = "Prone Diseases", command = disease)
    space3 = Label(root, text="")
    space4 = Label(root, text="")
    space5 = Label(root, text="")
    about = Button(root,text = "About the city", command = city)  
    wm = Label(root, text="Weather Monitoring")
    prone.grid(row=3, column=2)
    space3.grid(row=3,column=3)
    wm.grid(row=1,column=4) 
    space4.grid(row=3,column=5)
    about.grid(row=3, column=6)

    #adding powerbi link 
    def callback():
        webbrowser.open_new(r"https://app.powerbi.com/groups/2d716903-cef9-498f-80a0-a70077dcd3d2/reports/775bafec-00df-44b8-88dc-69d5fc52988c/ReportSection36f63fd558ae565a9a98")
    link = Button(root, text="Exploratory View", command=callback)
    
    #giving space again 
    space5.grid(row=3, column=7)
    link.grid(row=3, column=4)
    #adding space
    space7 = Label(root, text="")
    space7.grid(row=5,column=4)

    #adding image
    path = "weatherlogo.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(root, image=img)
    panel.photo = img
    panel.grid(column=4,row=6)

    #weather api
    #learn to generate api
    #we are using london now coordinates are + and - rpt left hand coordinate system
    def api():
        apirequests = requests.get("https://api.weatherapi.com/v1/current.json?key=cd83e662965d47c8861103732222608&q=" + cityname.get() + "&aqi=no")
        myapi = json.loads(apirequests.content)

        #using dictionary to obtain values by get method
        datasorttemp = myapi.get('current')
        temp = datasorttemp.get('temp_c')
        datasortcondn = datasorttemp.get('condition')
        datasorttext = datasortcondn.get('text')
        datasorthumidity = datasorttemp.get('humidity')
        datasortwindkph = datasorttemp.get('wind_kph')
        datasortuv = datasorttemp.get('uv')



        print(myapi)
        apilabel = Label(root, text= "Temperature in Celsius : " + str(temp))
        apilabel.grid(row=100,column=4)
        textlabel = Label(root, text= "Current conditions : " + datasorttext)
        textlabel.grid(row=101,column=4)
        humilabel = Label(root, text= "Humidity is : " + str(datasorthumidity) + " %")
        humilabel.grid(row=102, column=4)
        windkphlabel = Label(root, text="Wind speed : " + str(datasortwindkph) + " Km/h")
        windkphlabel.grid(row=103, column=4)
        uvlabel = Label(root, text="UV Index is : " + str(datasortuv))
        uvlabel.grid(row=104, column=4)

    #name entry
    cityname = Entry(root) 
    cityname.grid(row=80,column=4)

    #adding space
    space8 = Label(root, text="")
    space8.grid(row=81,column=4)

    #submitbutton
    submit = Button(root,text="Submit",command=api)
    submit.grid(row=82,column=4)


    















    
    
    
    
    
    #adding space
    space6 = Label(root, text="")
    space6.grid(row=500,column=4)

    #adding close button
    closure = Button(root,text = "Close", command = root.destroy)
    closure.grid(row=501,column=4)

    
root.mainloop()
