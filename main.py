from random import randint
from tkinter import Tk,Canvas,Frame,Button,Label
import time

class App(Tk):
	
	couleurs = {1:'red',2:'orange',3:'yellow',4:'green',5:'blue',6:'purple'}
	barre_largeur = 10
	
	
	def __init__(self):
		super(App,self).__init__()
		
		self.geometry("800x600")
		self.title('Test')
		
		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=1)
		
		self.canvas = Canvas(self,height='800',width='600',bg='white')

		self.canvas.grid(padx=10,pady=10,sticky='nsew')
		self.box = Frame(self,bd=10,width=10)
		self.box.grid(row=1,ipady=5,sticky='nsew')
		self.generate = Button(self.box,text='Generate',command=self.generate_chart)
		self.generate.grid(column=0,row=0,sticky='nsew')
		self.sort = Button(self.box,text='Sort',command=self.sort_chart,state='disabled')
		self.sort.grid(column=1,row=0,sticky='nsew')
		self.largeur = Label(self.box,text=" Largeur : ")
		self.largeur.grid(column=2,row=0)
		self.value = Label(self.box,text=str(self.barre_largeur),width=5)
		self.value.grid(column=4,row=0)
		self.plus = Button(self.box,text='+',command=self.plus_barre)
		self.plus.grid(column=3,row=0)
		self.moins = Button(self.box,text='-',command=self.moins_barre)
		self.moins.grid(column=5,row=0)
		
		self.update()
		self.c_wd = self.canvas.winfo_width()
		self.c_he = self.canvas.winfo_height()
		self.liste_barres = []
	
	def plus_barre(self):
		if self.barre_largeur < 50:
			self.barre_largeur +=1
			self.value.config(text=str(self.barre_largeur))
			
	def moins_barre(self):
		if self.barre_largeur > 3:
			self.barre_largeur -=1
			self.value.config(text=str(self.barre_largeur))
			
		
	def disable_buttons(self):
		self.generate.config(state='disabled')
		self.sort.config(state='disabled')
		self.plus.config(state='disabled')
		self.moins.config(state='disabled')
	
	def enable_buttons(self):
		self.generate.config(state='normal')
		self.sort.config(state='normal')
		self.plus.config(state='normal')
		self.moins.config(state='normal')
	
		
	def generate_chart(self):
		self.disable_buttons()
		self.canvas.delete('all')
		self.liste_barres.clear()

		for it in range(int(self.c_wd / self.barre_largeur)):
			x0 = it*self.barre_largeur
			x1 = x0 + self.barre_largeur-1
			y0 = randint(100,self.c_he-10)
			y1 = self.c_he
			
			taille = y1-y0
			coef = int(self.c_he/6)
			
			if taille <= coef:
				couleur = self.couleurs[1]
			elif taille <= coef*2:
				couleur = self.couleurs[2]
			elif taille <= coef*3:
				couleur = self.couleurs[3]
			elif taille <= coef*4:
				couleur = self.couleurs[4]
			elif taille <= coef*5:
				couleur = self.couleurs[5]
			elif taille <= coef*6:
				couleur = self.couleurs[6]
			
			barre = self.canvas.create_rectangle(x0,y0,x1,y1,fill=couleur)
			self.liste_barres.append(barre)
			time.sleep(0.001)
			self.update()
		
		self.enable_buttons()
#-----------------
	def sort_chart(self):
		self.disable_buttons() 
		leng = len(self.liste_barres)
		for index in range(leng):
			already_sorted = True
			for idex in range(leng-index-1):
				idx = int(self.liste_barres[idex])
				
				temp_color = self.canvas.itemcget(idx,'fill')
				self.canvas.itemconfig(idx,fill='white')

				
				idx2 = int(self.liste_barres[idex+1])
				coord1 = self.canvas.coords(idx)
				coord2 = self.canvas.coords(idx2)
				posx01 = coord1[0]
				taille1 = coord1[3]-coord1[1]
				posx02 = coord2[0]
				taille2 = coord2[3]-coord2[1]
				deltax = posx02-posx01
				if taille1 > taille2:
					self.canvas.move(idx,deltax,0)
					self.canvas.move(idx2,-deltax,0)
					self.liste_barres[idex] = idx2
					self.liste_barres[idex+1] = idx
					already_sorted=False
					self.update()
				self.canvas.itemconfig(idx,fill=temp_color)
					
			if already_sorted:
				break
		self.enable_buttons()
		
if __name__ =='__main__':
	app = App()
	app.mainloop()
	
