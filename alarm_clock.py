from tkinter import *
import datetime
import time
import winsound

#create function for the alarm process
def alarm(set_alarm_timer):
	"""set the timer for the alarm clock"""
	#create a while loop for the timer
	while True:
		time.sleep(1) # we need to delay it for 1 second otherwise it will continuously run
		#we will need to order this because the current order will be e.g (2020, 11, 7, 13, 26, 56, 87458)
		current_date_time = datetime.datetime.now()
		# now we format it
		now_time = current_date_time.strftime("%H : %M : %S")
		now_date = current_date_time.strftime("%A : %B : %Y")

		print(f"The set date is {now_date}")
		print(now_time)

		# check if the current time matches the set alarm timer
		if now_time == set_alarm_timer:
			print('Wake up dude!')
			winsound.PlaySound("alien_siren.wav", winsound.SND_ASYNC)
			break


def actual_time():
	"""This function takes in user input to determine the alarm"""
	set_alarm_timer = f"{hour.get()} : {minute.get()} : {sec.get()}"
	alarm(set_alarm_timer)

# create the tkinter user interface for the alarm clock
root = Tk()

#create a title for the dialog box
root.title("Alarm Clock")

#create the size of the box
root.geometry('400x200')

# label at bottom of box
time_format = Label(root, text="Enter time in 24-Hour format", fg='gold2', bg='black', font=('Arial', 12, 'bold')).place(x=90, y=170)

# label at top of box
time_label = Label(root, text="Hour:    Minute:    Second:    ", font=('Helevetica', 12, 'bold')).place(x=97)

# the variables for the alarm
hour = StringVar()
minute = StringVar()
sec = StringVar()

# section to set the time in the dialog box
hour_entry = Entry(root, textvariable=hour, bg='MediumPurple1', width=7).place(x=100, y=50)
minute_entry = Entry(root, textvariable=minute, bg='RoyalBlue1', width=7).place(x=168, y=50)
sec_entry = Entry(root, textvariable=sec, bg='turquoise', width=7).place(x=240, y=50)


# create the submit button
submit_but = Button(root, text="Set Alarm", fg='black', width=10, font=('Helevetica', 10, 'bold'), command=actual_time).place(x=145, y=100)









#execute the window
root.mainloop()




