import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO #used to handle the byes#

#GUI FOR WINDOW#
window = tk.Tk() #calls the tkinter library#
window.geometry("700x500") #dimensions of the widow#
window.title("Rysons Pokedex")
window.config(padx = 10, pady= 10) #paddin settings#

#GUI FOR TITLE#
titlelabel = tk.Label(window, text = "Rysons Pokedex")
titlelabel.config(font = ("Mordern Love Caps", 32))
titlelabel.pack(padx = 10 , pady = 10)

pokemonimage = tk.Label(window)
pokemonimage.pack(padx = 10, pady = 10)

pokemoninfo = tk.Label(window)
pokemoninfo.config(font = ("Mordern Love Caps", 20))
pokemoninfo.pack(padx = 10, pady = 10)

pokemontypes = tk.Label(window)
pokemontypes.config(font = ("Mordern Love Caps", 20))
pokemontypes.pack(padx = 10, pady = 10)


#CODE FOR FUNTION TO LOAD POKEMON
def loadPokemon():
    pokemon = pypokedex.get(name = TextIDname.get(1.0 , "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default')) # for the image of the pokemon#
    image = PIL.Image.open(BytesIO(response.data)) #converting the image into BYTES so that we can turn it into pillow#
    #whats happning here: We are getting the data from the response and turning it into BytesIO object and use PIL to open that image and save it into and object and import in into TKinter#

    img = PIL.ImageTk.PhotoImage(image)
    pokemonimage.config(image = img)
    pokemonimage.image = img

    pokemoninfo.config(text = f"{pokemon.dex} - {pokemon.name}".title())
    pokemontypes.config(text =" - ".join([t for t in pokemon.types]).title())


#Function Used to Load the pokemon( WINDOW VERSION)
LabelIDname = tk.Label( window, text = "ID or Name")
LabelIDname.config(font = ("Mordern Love Caps", 20))
LabelIDname.pack(padx = 10, pady = 10)

TextIDname = tk.Text (window, height = 1)
TextIDname.config(font = ("Mordern Love Caps", 20))
TextIDname.pack(padx = 10, pady = 10)

LoadBtn = tk.Button(window, text = "Load Pokemon", command = loadPokemon)
LoadBtn.config(font = ("Mordern Love Caps", 20))
LoadBtn.pack(padx = 10 , pady = 10)


window.mainloop()




