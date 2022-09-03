from importlib.resources import contents
from tkinter import *
import webbrowser
from PIL import ImageTk,Image
import requests
import json
root = Tk()
root.title("my_user")

#changing tkinter window icon 
root.wm_iconbitmap("icon.ico")

#function for cityinfo
def city():
    cinfo = Label(root , text = "About the city")
    cinfo.grid(row=4, column=6)

#function for diseases 
def disease():
    dinfo = Label(root, text = "maut, mrityu")
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
    webbrowser.open_new(r"https://app.powerbi.com/Redirect?action=OpenApp&appId=1bc2ed57-92c5-4fa1-8a6a-d72a2f8b1a7f&ctid=09bd1956-edda-4e9a-9543-7c7aa2cf4e81")
link = Button(root, text="Demo Power Bi", command=callback)
    
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
    apirequests = requests.get("http://history.openweathermap.org/data/2.5/history/city?q=London,UK&appid=4e52a4e14e70c053e0456f61e068d8ad")
    #this api is paid api felling sad
    myapi = json.loads(apirequests.content)

    #using dictionary to obtain values by get method
    #datasorttemp = myapi.get('current')
    #temp = datasorttemp.get('temp_c')


    print(myapi)
    apilabel = Label(root, text= myapi)
    apilabel.grid(row=100,column=4)

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