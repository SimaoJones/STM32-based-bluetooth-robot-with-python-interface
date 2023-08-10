import tkinter as tk
from tkinter import messagebox
import serial
import serial.tools.list_ports

serialPort = 0

running = False
def goUp(event):
    global runnning
    running = True
    print('up')
    serialPort.write(b'w')
  
def Stop(event):
    print('Stopped')
    serialPort.write(b' ')
    running = False
  

def goDown(event):
    global runnning
    running = True
    
    serialPort.write(b's')
    print("down")

def goLeft(event):
    global runnning
    running = True
    
    serialPort.write(b'a')
    print("left")

def goRight(event):
    global runnning
    running = True
    
    serialPort.write(b'd')
    print("Right")



def CheckBluetooth():
    
    #serialPort = serial.Serial(port='COM8', baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)
    
   
     
    if serialPort.is_open == False:
        messagebox.showwarning("showwarning","The robot is disconnected")
        
    else:
        messagebox.showinfo("showinfo","The robot is connected")    
   

def Disconnect():
    print("Disconnecting")
    serialPort.close()

    var = tk.StringVar()
    label = tk.Message( top, textvariable=var, relief='raised', bg='blue')
    var.set("Robot Disconnected")

    label.pack(side='top')
    label.place(x=500,y=400)




def HelpWindow():
   Help = tk.Toplevel(top)    

   Help.title("Robot Bluetooth Interface help ")
   Help.geometry("500x500")
   tk.Label(Help,text="Robot Bluetooth Interface help").pack()
   tk.Label(Help,text="1º) Go to the Bluetooth Settings and click 'Add Bluetooth device'").place(x=160,y=50)
   tk.Label(Help,text="2º) in the 'Add Bluetooth device' find for 'HC-05' and click on it ").place(x=160,y=70)
   tk.Label(Help,text="3º) Write the pin requested ('1234' by default) ").place(x=160,y=90)
   tk.Label(Help,text="4º) Go to the Visual Studio IDE and click to run the Interface App code ").place(x=160,y=110)
   tk.Label(Help,text="5º) Enjoy the Ride ").place(x=160,y=130)



    

serialPort = serial.Serial(port='COM8', baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, stopbits=1)

top = tk.Tk()
top.title('Robot Bluetooth Interface')
top.geometry("1000x500")
top.config(bg='skyblue')
connection_frame = tk.Frame(top,width=1000,height=5)



#verificar ligação
CheckBT = tk.Button(top,text="Check Connection",command=CheckBluetooth,height = 5, width = 30)

#ir para frente
up = tk.Button(top,text = "Up",height=5,width = 10)

#ir para trás
down = tk.Button(top,text = "Down",command = goDown,height=5,width = 10)

#ir para a esquerda
left = tk.Button(top,text = "Left",command = goLeft,height=5,width = 10)

#ir para a direita
right = tk.Button(top, text = "right",command = goRight,height=5, width = 10)

#desconectar o robô
DisconnectBT = tk.Button(top,text="Disconnect",command=Disconnect,height = 5, width = 30)

#mostrar ajuda
Help = tk.Button(top,text= "?",command = HelpWindow,height=5,width=5)



up.pack(side ="top")  
up.place(x=500,y=150)
up.bind('<ButtonPress-1>',goUp)
up.bind('<ButtonRelease-1>',Stop)

down.pack(side = "bottom")  
down.place(x=500,y=300)  
down.bind('<ButtonPress-1>',goDown)
down.bind('<ButtonRelease-1>',Stop)


left.pack(side = "left")  
left.place(x=250,y=200) 
left.bind('<ButtonPress-1>',goLeft)
left.bind('<ButtonRelease-1>',Stop)


right.pack(side = "right")  
right.place(x=750,y=200)
right.bind('<ButtonPress-1>',goRight)
right.bind('<ButtonRelease-1>',Stop)



print(serialPort)

DisconnectBT.pack(side='top')
DisconnectBT.place(x=250,y=50)

CheckBT.pack(side = 'top')
CheckBT.place(x=500,y=50)


Help.pack(side='top')
Help.place(x=0,y=0)



top.mainloop()