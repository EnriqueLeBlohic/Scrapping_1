import requests
from bs4 import BeautifulSoup
from tkinter import *

import re

def realizar_scrapping():
         #Obtener el HTLM 
  url = entrada_url.get()
  response= requests.get(url)
  response.raise_for_status()
  html = response.content
 #Analizar el HTML utilizando BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")
 
 #Obtener el título de la página
  title = soup.title.string
  resultado_texto.insert(END, f"El título es: {title}\n" + "*" * 50 + "\n\n")

 #Obtener todos los enlaces de la página
  links = [link["href"] for link in soup.find_all("a", href=True) if "http" in link["href"]]
  resultado_texto.insert(END, "Enlaces de la página:\n")
  for link in links:
         resultado_texto.insert(END, f"{link}\n")
  resultado_texto.insert(END,"*" * 50 + "\n\n")

 #Obtener todos los encabezados en la página
  encabezados = [encabezado.text.strip() for encabezado in soup.find_all(re.compile("^h[1-6]$"))]
  resultado_texto.insert(END, "Encabezados de la pagina:\n")
  for encabezado in encabezados:
      resultado_texto.insert(END, f"{encabezado}\n")
  resultado_texto.insert(END, "*" * 50 + "\n\n")

 #Obtener la imagen principal de la página
  img = soup.find("img", {"class": "mw-logo-tagline"})
  img_url = "https:" + img["src"]
  resultado_texto.insert(END, f"La imagen principal es: {img_url}\n" + "*" * 50 + "\n\n")

 #Obtener todas las imagenes
  All_imagenes = [img["src"] for img in soup.find_all("img", src=True)]
  resultado_texto.insert(END, "URLs de las imagenes:\n")
 
  for image_url in All_imagenes:
      resultado_texto.insert(END, f"{image_url}\n")
  resultado_texto.insert(END, "*" * 50 + "\n\n")
  

#Ventanas
ventana_principal = Tk()
ventana_principal.title("Scrapping")
ventana_principal.minsize(width=400, height=400)
ventana_principal.config(padx=30, pady=30)

etiqueta1 = Label(text="Escribe la direccion de la pagina", font=("Arial", 14))
etiqueta1.grid(column=0, row=1)

entrada_url = Entry(width=40)
entrada_url.grid(column=1, row=0)

#crear un botón para realizar el scrapping
boton_scrapping = Button(text="Realizar Scrapping", command=realizar_scrapping)
boton_scrapping.grid(column=1, row=1)

#crear un area de texto para mostrar los resultados
resultado_texto = Text(width=80, height=20)
resultado_texto.grid(column=0, row=2, columnspan=2)
ventana_principal.mainloop()
