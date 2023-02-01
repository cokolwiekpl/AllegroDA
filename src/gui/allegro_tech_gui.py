import pandas as pd
import tabloo
import tkinter as tk
from PIL import Image
from allegro_data_analysis.product_data_analysis import get_products_data_by_name


def create_tabloo_button(text: str, relx: float, rely: float, relwidth: float, relheight: float, frame: tk.Frame, searched_product: tk.Entry):
    """
    Create a button widget in a tkinter frame that displays a table using the tabloo library.
    Parameters:
    text (str): The text displayed on the button.
    relx (float): The horizontal placement of the button in the frame, as a fraction of the width of the frame.
    rely (float): The vertical placement of the button in the frame, as a fraction of the height of the frame.
    relwidth (float): The width of the button, as a fraction of the width of the frame.
    relheight (float): The height of the button, as a fraction of the height of the frame.
    frame (tk.Frame): The tkinter frame in which to place the button.
    searched_product (tk.Entry): The tkinter entry widget that contains the product name to search for.
    """

    def display_text():
        """
        Display a table of products using the tabloo library.
        """
        if not searched_product.get().isspace() and searched_product.get() != '':
            print(searched_product.get().strip())
            products = get_products_data_by_name(searched_product.get().strip())
            open("resources/access_token.txt", "w").write('')
            df_products = pd.DataFrame(products)
            tabloo.show(df_products)

    button = tk.Button(frame, text=text, command=lambda: display_text())
    button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


def create_button(text: str, image_path: str, relx: float, rely: float, relwidth: float, relheight: float, frame: tk.Frame):
    """
    Create a button widget in a tkinter frame.
    Parameters:
    text (str): The text displayed on the button.
    image_path (str): The path to the image file to be displayed when the button is pressed.
    relx (float): The horizontal placement of the button in the frame, as a fraction of the width of the frame.
    rely (float): The vertical placement of the button in the frame, as a fraction of the height of the frame.
    relwidth (float): The width of the button, as a fraction of the width of the frame.
    relheight (float): The height of the button, as a fraction of the height of the frame.
    frame (tk.Frame): The tkinter frame in which to place the button.
    """

    def show_plot():
        """
        Open the specified image file in a default image viewer.
        """
        image = Image.open(image_path)
        image.show()

    button = tk.Button(frame, text=text, command=lambda: show_plot())
    button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)


def create_gui():
    """
    This function creates the GUI for the Allegro Tech application.

    This function uses the Tkinter library to create the GUI window and place various widgets on it such as buttons, labels, and an entry widget.
    The function also calls other helper functions (create_tabloo_button, create_button) to create buttons that have specific text, images and placement on the GUI window.
    The buttons perform various actions when clicked by the user.
    """
    root = tk.Tk()
    root.title('Allegro Tech')
    canvas = tk.Canvas(root, height=604, width=1108)
    canvas.pack()

    background_image = tk.PhotoImage(file='resources/AllegroLogo.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='#ffffff')
    frame.place(relx=0.3, rely=0.20, relwidth=0.9, relheight=0.6, anchor='n')

    searched_product_label = tk.Label(frame)
    searched_product_label.place(relx=0.2, rely=0.15, relwidth=0.18, relheight=0.1)
    searched_product_label.configure(text="Nazwa produktu")

    searched_product = tk.Entry(frame, font=40)
    searched_product.place(relx=0.40, rely=0.15, relwidth=0.2, relheight=0.1)

    path = "resources/plots/"

    create_tabloo_button("Wyświetl listę produktów", relx=0.35, rely=0.30, relwidth=0.3, relheight=0.06, frame=frame, searched_product=searched_product)
    create_button("Ilość w danym kwartale", f"{path}ZamowieniaKwartal.png", relx=0.75, rely=0.08, relwidth=0.2, relheight=0.06, frame=frame)
    create_button("Kategorie produktów", f"{path}zamowieniaKategorie.png", relx=0.75, rely=0.16, relwidth=0.2, relheight=0.06, frame=frame)
    create_button("Dochody kategoria Auto", f"{path}dochodSamochod.png", relx=0.75, rely=0.24, relwidth=0.2, relheight=0.06, frame=frame)
    create_button("Dochody kategoria Elektronika", f"{path}dochodelEktornika.png", relx=0.75, rely=0.32, relwidth=0.2, relheight=0.060, frame=frame)
    create_button("Dochody kategoria Moda", f"{path}dochodMods.png", relx=0.75, rely=0.40, relwidth=0.2, relheight=0.06, frame=frame)
    create_button("Dochody kategoria Dom", f"{path}dochodDom.png", relx=0.75, rely=0.48, relwidth=0.2, relheight=0.06, frame=frame)
    create_button("Miesięczna sprzedaż i dochód", f"{path}sprzedazDochod.png", relx=0.75, rely=0.56, relwidth=0.2, relheight=0.060, frame=frame)
    create_button("Korelacja między zmiennymi", f"{path}korelacja.png", relx=0.75, rely=0.64, relwidth=0.2, relheight=0.060, frame=frame)
    create_button("10 Krajów o największym dochodzie", f"{path}najwiekszyDochod.png", relx=0.35, rely=0.45, relwidth=0.3, relheight=0.06, frame=frame)
    create_button("10 Krajów o najmniejszym dochodzie", f"{path}najmniejszyDochod.png", relx=0.35, rely=0.53, relwidth=0.3, relheight=0.060, frame=frame)
    create_button("Dochody z poszczególnych sewktorów klientów", f"{path}dochodSegment.png", relx=0.35, rely=0.61, relwidth=0.3, relheight=0.06, frame=frame)
    create_button("Historgram dla dochodów z segmentów", f"{path}segmentyHistohram.png", relx=0.35, rely=0.69, relwidth=0.3, relheight=0.060, frame=frame)
    create_button("Średni czas oczekiwania na wysyłkę", f"{path}sredniaAgign.png", relx=0.35, rely=0.77, relwidth=0.3, relheight=0.060, frame=frame)
    create_button("Dochód i Koszt wysyłki, a regresja liniowa", f"{path}proftCostReg.png", relx=0.35, rely=0.85, relwidth=0.3, relheight=0.060, frame=frame)

    imagebox = tk.Label(root)
    imagebox.pack()
    root.mainloop()
