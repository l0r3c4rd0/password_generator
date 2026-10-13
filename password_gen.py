import string
import random
import customtkinter as gui

caratteri=string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits
#mette assieme una stringa di caratteri minuscoli maiuscoli punteggiatura e numeri
finestra=gui.CTk()
finestra.title("cardelli password generator")
finestra.geometry("750x500")
finestra.resizable(False,False)
#per evitare che puoi mettere la finestra ad intero
titolo_1=gui.CTkLabel(finestra,text="Password",text_color="#FFFFFF",font=("Arial",40,"bold"))
#ultima che descrive font grandezza e grassetto
titolo_2=gui.CTkLabel(finestra,text="Generator",text_color="#2DE2D0",font=("Arial",40,"bold"))
titolo_1.place(x=200,y=70)
titolo_2.place(x=410,y=70)
mostra_password=gui.CTkEntry(finestra,placeholder_text="la tua password verra generata qua",width=400,height=70)
mostra_password.place(x=200,y=150)
finestra.configure(fg_color="#062B33")
finestra.mainloop()