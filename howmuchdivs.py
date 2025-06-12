import tkinter as tk
import requests

root = tk.Tk()
root.geometry("450x550")
root.title("how much divs")

class Input_text:
    def __init__(self,ancho,top):
        self.ancho = ancho
        self.top = top

    def generate(self):
        self.objeto = tk.Entry(root, width=self.ancho)
        self.objeto.place(relx=0.5, y=self.top, anchor="center")  
    def get(self):
        return self.objeto.get()

class Button:
    def __init__(self, texto, comando, top):
        self.texto = texto
        self.comando = comando
        self.top = top
    def generate(self):
        self.objeto = tk.Button(root, text=self.texto, command=self.comando)
        self.objeto.place(relx=0.5, y=self.top, anchor="center") 

class Label:
    def __init__(self, texto, tam, top):
        self.texto = texto
        self.tam = tam
        self.top = top
    def generate(self):
        self.objeto = tk.Label(root, text=self.texto, font=("Arial", self.tam, "bold"))
        self.objeto.place(relx=0.5, y=self.top, anchor="center") 

def hey():
    print("Hey")
page_text = ""
def get_info():
    url = str(texto.get())
    try:
        r = requests.get(url)
        print(r.text)
        page_text = str(r.text)
        labeldiv = Label(f"this page contains {page_text.count('<div')} 'divs' ", 10, 350)
        labeldiv.generate()
    except:
        print("Error")
        labelerror.texto = "Error, please check the url"
        labelerror.generate()

label = Label("How much DIV does \n your page contain?", 20, 100)
label.generate()

labelerror = Label("", 10, 420)
labelerror.generate()

labeldiv = Label("", 10, 350)
labeldiv.generate()

labelmini = Label("enter here an url", 10, 180)
labelmini.generate()

texto = Input_text(30, 200)
texto.generate()



boton = Button("Search", get_info, 250)
boton.generate()


root.mainloop()
