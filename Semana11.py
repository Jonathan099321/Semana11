#Jonathan Roberto Acosta Lopez SMIS099321
#Mario Alexander Hernandez Quevedo SMIS075121

from PIL import Image, ImageTk, ImageFilter 
from tkinter import Place, Tk, Button, Label, filedialog,messagebox

#boton de cargar
def load():
    archivo = filedialog.askopenfilename()
    global imagen4
    imagen4 = Image.open(archivo)
    imagenresiz2 = imagen4.resize((800,600),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

#Boton para poner la imagen en blanco y negro
def white_black():
    global image2
    image2 = imagen4.convert("L")
    imagenresiz2 = image2.resize((800,600),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

#Boton para desenfocar la imagen   
def blur():
    global image2
    image2= imagen4.filter(ImageFilter.BLUR)
    imagenresiz2 = image2.resize((800,600),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

#Boton contornar la imagen
def outline():
    global image2
    image2= imagen4.filter(ImageFilter.CONTOUR)
    imagenresiz2 = image2.resize((800,600),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

#Boton para resaltar la imagen
def highlight():
    global image2
    image2= imagen4.filter(ImageFilter.DETAIL)
    imagenresiz2 = image2.resize((800,600),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

#Boton para guardar la imagen
def save():
    image2.save("edited image.jpg")
    messagebox.showinfo(title="saved image",message="the image was saved successfully")

#Aqui mandamos a llamar la importacion de arriba y damos el tamaño de la ventana
ventana = Tk()
ventana.geometry("1024x768")

#Aqui le damos las funciones a los botones
ventana.title("Filters image")
ventana.configure(bg='#d8d8ab')
Label2 =Label(ventana, image="")
btnsape=Button(ventana, bg = "#1077e5",text="Load", command=load, fg="white")
btn3=Button(ventana,bg = "#435889", text="White/Black", command=white_black, fg="white")
btn1=Button(ventana,bg = "#58dac5", text="Blur", command=blur, fg="white")
btn2=Button(ventana,bg = "#2cc9af", text="Outline", command=outline, fg="white")
btn3_1=Button(ventana,bg = "#219783", text="Highlight", command=highlight, fg="white")
btn_guardar=Button(ventana,bg = "#4a6196", text="Save Picture", command=save, fg="white")
btnsape.pack()
btn3.pack()
btn1.pack()
btn2.pack()
btn3_1.pack()
btn_guardar.pack()
Label2.pack()
ventana.mainloop()