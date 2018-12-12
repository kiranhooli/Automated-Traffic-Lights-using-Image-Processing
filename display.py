from tkinter import *
import time

def disp(r1,r2,r3,r4):
	r1g=r1
	r2g=r2
	r3g=r3
	r4g=r4

	r1r=0
	r2r=r1g
	r3r=r1g+r2g
	r4r=r1g+r2g+r3g

	root =Tk()	
	
	l1 = Label(text="ROAD 1",bg='white', relief=RIDGE,width=10,font=("Helvetica", 20)).grid(row=0,column=0)
	l2 = Label(text="ROAD 2",bg='white', relief=RIDGE,width=10,font=("Helvetica", 20)).grid(row=0,column=1)
	l3 = Label(text="ROAD 3",bg='white', relief=RIDGE,width=10,font=("Helvetica", 20)).grid(row=0,column=2)
	l4 = Label(text="ROAD 4",bg='white', relief=RIDGE,width=10,font=("Helvetica", 20)).grid(row=0,column=3)

	l5 = Label(text=r1r,bg='red',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l5.grid(row=1,column=0)
	l6 = Label(text=r2r,bg='red',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l6.grid(row=1,column=1)
	l7 = Label(text=r3r,bg='red',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l7.grid(row=1,column=2)
	l8 = Label(text=r4r,bg='red',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l8.grid(row=1,column=3)

	l9 = Label(text=r1g,bg='green',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l9.grid(row=2,column=0)
	l10 = Label(text=r2g,bg='green',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l10.grid(row=2,column=1)
	l11 = Label(text=r3g,bg='green',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l11.grid(row=2,column=2)
	l12 = Label(text=r4g,bg='green',fg='white', relief=RIDGE,width=10,font=("Helvetica", 20))
	l12.grid(row=2,column=3)

	l13 = Label(text="GO",bg='white',fg='green', relief=RIDGE,width=10,font=("Helvetica", 20))
	l13.grid(row=3,column=0)
	l14 = Label(text="STOP",bg='white',fg='red', relief=RIDGE,width=10,font=("Helvetica", 20))
	l14.grid(row=3,column=1)
	l15 = Label(text="STOP",bg='white',fg='red', relief=RIDGE,width=10,font=("Helvetica", 20))
	l15.grid(row=3,column=2)
	l16 = Label(text="STOP",bg='white',fg='red', relief=RIDGE,width=10,font=("Helvetica", 20))
	l16.grid(row=3,column=3)


	def upd():
		l5[ "text" ] = r1r
		l6[ "text" ] = r2r
		l7[ "text" ] = r3r
		l8[ "text" ] = r4r
		l9[ "text" ] = r1g
		l10[ "text" ] = r2g
		l11[ "text" ] = r3g
		l12[ "text" ] = r4g

		if r1r==0:
			l13[ "text" ] = "GO"
			l13[ "fg" ] = 'green'
		else:
			l13[ "text" ] = "STOP"
			l13[ "fg" ] = 'red'

		if r2r==0:
			l14[ "text" ] = "GO"
			l14[ "fg" ] = 'green'
		else:
			l14[ "text" ] = "STOP"
			l14[ "fg" ] = 'red'

		if r3r==0:
			l15[ "text" ] = "GO"
			l15[ "fg" ] = 'green'
		else:
			l15[ "text" ] = "STOP"
			l15[ "fg" ] = 'red'

		if r4r==0:
			l16[ "text" ] = "GO"
			l16[ "fg" ] = 'green'
		else:
			l16[ "text" ] = "STOP"
			l16[ "fg" ] = 'red'
		root.update()


	while(1):
		if r1r==0:
			while(r1g>0):
				r1g -= 1
				r2r -= 1
				r3r -= 1
				r4r -= 1
				upd()
				time.sleep(1)
			r1g = r1
			r1r = r4g+r4r
			upd()

		if r2r==0:
			while(r2g>0):
				r2g -= 1
				r1r -= 1
				r3r -= 1
				r4r -= 1
				upd()
				time.sleep(1)
			r2g = r2
			r2r = r1g+r1r
			upd()

		if r3r==0:
			while(r3g>0):
				r3g -= 1
				r1r -= 1
				r2r -= 1
				r4r -= 1
				upd()
				time.sleep(1)
			r3g = r3
			r3r = r2g+r2r
			upd()

		if r4r==0:
			while(r4g>0):
				r4g -= 1
				r1r -= 1
				r2r -= 1
				r3r -= 1
				upd()
				time.sleep(1)
			r4g = r4
			r4r = r3g+r3r
			upd()


	root.mainloop()
