import string
import random
import customtkinter as gui

def aggiorna(valore):
    global numero
    numero.configure(text=int(valore))

def password():
    global password_generata
    lunghezza=int(lunghezza_password.get())
    password_generata=""
    for i in range(lunghezza):
        password_generata+=random.choice(caratteri)
        #scelgo randomicamente le lettere da caratteri che è la nostra stringa di elementi ascii e numerici
    mostra_password.delete(0,"end")
    #per pulire dal carattere 0 fino alla fine
    mostra_password.insert(0,password_generata)
    #inserisce password generata dalla posizione 0

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
numero=gui.CTkLabel(finestra,text="19",font=("Arial",30,"bold"))
numero.place(x=260,y=290)
mostra_password=gui.CTkEntry(finestra,placeholder_text="la tua password verra generata qua",width=400,height=70,font=("Arial",20,"bold"))
mostra_password.place(x=200,y=150)
lunghezza_password=gui.CTkSlider(finestra,from_=6,to=32,number_of_steps=26,command=aggiorna)
#no parentesi se no lo fa sempre
#number of step serve per avere tutti i numeri da 6 a 32
lunghezza_password.place(x=300,y=300)
genera_password=gui.CTkButton(finestra,command=password,fg_color="#39D6C3",hover_color="#24B8A8",text="genera password",text_color="#062D32",height=60,width=300,font=("Arial",30,"bold"))
#qua invece il valore non viene passato in automatico
genera_password.place(x=250,y=370)
finestra.configure(fg_color="#062B33")
finestra.mainloop()