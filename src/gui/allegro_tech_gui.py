import pandas as pd
import tabloo
import tkinter as tk
from PIL import Image
from allegro_data_analysis.product_data_analysis import get_products_data_by_name


def create_tabloo_button(text: str, relx: float, rely: float, relwidth: float, relheight: float, frame: tk.Frame, searched_product: tk.Entry):
    def display_text():
        products = get_products_data_by_name(searched_product.get())
        df_products = pd.DataFrame(products)
        tabloo.show(df_products)

    button = tk.Button(frame, text=text, command=lambda: display_text())
    button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


def create_button(text: str, image_path: str, relx: float, rely: float, relwidth: float, relheight: float, frame: tk.Frame):
    def show_plot():
        image = Image.open(image_path)
        image.show()

    button = tk.Button(frame, text=text, command=lambda: show_plot())
    button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


def create_gui():
    root = tk.Tk()
    root.title('Allegro Tech')
    canvas = tk.Canvas(root, height=604, width=1108)
    canvas.pack()

    background_image = tk.PhotoImage(file='resources/AllegroLogo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='#ffffff')
    frame.place(relx=0.3, rely=0.20, relwidth=0.9, relheight=0.4, anchor='n')

    searched_product_label = tk.Label(frame)
    searched_product_label.place(relx=0.2, rely=0.15, relwidth=0.18, relheight=0.1)
    searched_product_label.configure(text="Nazwa produktu")

    searched_product = tk.Entry(frame, font=40)
    searched_product.place(relx=0.40, rely=0.15, relwidth=0.2, relheight=0.1)

    create_tabloo_button("Wyświetl listę produktów", relx=0.40, rely=0.30, relwidth=0.2, relheight=0.1, frame=frame, searched_product=searched_product)
    create_button("Ilość w danym kwartale", "resources/ZamowieniaKwartal.png", relx=0.7, rely=0.15, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("Ilość w danym kwartale", "resources/zamowieniaMiesiac.png", relx=0.7, rely=0.25, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("10 Krajów o największym dochodzie", "resources/najwiekszyDochod.png", relx=0.7, rely=0.35, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("10 Krajów o najmniejszym dochodzie", "resources/najmniejszyDochod.png", relx=0.7, rely=0.45, relwidth=0.2, relheight=0.10, frame=frame)
    create_button("Kategorie prduktów", "resources/zamowieniaKategorie.png", relx=0.7, rely=0.55, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("Dochody kategoria Auto", "resources/dochodSamochod.png", relx=0.7, rely=0.65, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("Dochody kategoria Elektronika", "resources/dochodelektornika.png", relx=0.7, rely=0.75, relwidth=0.2, relheight=0.10, frame=frame)
    create_button("Dochody kategoria Moda", "resources/dochodMods.png", relx=0.7, rely=0.85, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("Dochody kategoria Dom", "resources/dochodDom.png", relx=0.4, rely=0.50, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("Miesięczna sprzedaż i dochód", "resources/sprzedazDochod.png", relx=0.4, rely=0.60, relwidth=0.2, relheight=0.10, frame=frame)
    create_button("Dochody z poszczególnych sewktorów klientów", "resources/dochodSegment.png", relx=0.4, rely=0.70, relwidth=0.2, relheight=0.1, frame=frame)
    create_button("Historgram dla dochodów z segmentów", "resources/segmentyHistohram.png", relx=0.4, rely=0.80, relwidth=0.2, relheight=0.10, frame=frame)
    create_button("Średni czas oczekiwania na wysyłkę", "resources/sredniaAgign.png", relx=0.4, rely=0.90, relwidth=0.2, relheight=0.10, frame=frame)

    imagebox = tk.Label(root)
    imagebox.pack()

    root.mainloop()
