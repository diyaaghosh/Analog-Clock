from tkinter import *
import time
import math
root=Tk()
root.title("Analog Clock")
root.geometry("470x470")


x_mid=235
y_mid=235
def live_clock():
   hour=int(time.strftime("%I"))
   minute=int(time.strftime("%M"))
   second=int(time.strftime("%S"))
   sec_x=second_hand_len*math.sin(math.radians(second*6))+x_mid
   sec_y=(-1)*second_hand_len*math.cos(math.radians(second*6))+y_mid
   canvas.coords(second_hand,x_mid,y_mid,sec_x,sec_y)
   min_x=minute_hand_len*math.sin(math.radians(minute*6))+x_mid
   min_y=(-1)*minute_hand_len*math.cos(math.radians(minute*6))+y_mid
   canvas.coords(minute_hand,x_mid,y_mid,min_x,min_y)
   hour_x=hour_hand_len*math.sin(math.radians(hour*30))+x_mid
   hour_y=(-1)*hour_hand_len*math.cos(math.radians(hour*30))+y_mid
   canvas.coords(hour_hand,x_mid,y_mid,hour_x,hour_y)
   canvas.after(1000,live_clock)

canvas=Canvas(width=470,height=470,bg="black")
canvas.pack()
root.config(bg="black")
bg=PhotoImage(file="image.png")
canvas.create_image(235,235,image=bg)
second_hand_len=160
minute_hand_len=140
hour_hand_len=100
second_hand=canvas.create_line(235,235,250+second_hand_len,250+second_hand_len,fill="red",width=2.5)
minute_hand=canvas.create_line(235,235,235+minute_hand_len,235+minute_hand_len,fill="yellow",width=3.0)
hour_hand=canvas.create_line(235,235,235+hour_hand_len,235+hour_hand_len,fill="black",width=3.5)
live_clock()
root.mainloop()