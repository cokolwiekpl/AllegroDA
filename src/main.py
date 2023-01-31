from allegro_data_analysis.csv_file_data_analysis import generate_plots
from gui.allegro_tech_gui import create_gui

import os


def main():
    if os.path.isfile("resources/dochodDom.png") is False:
        generate_plots()
    create_gui()


if __name__ == "__main__":
    main()
