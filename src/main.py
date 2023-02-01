from allegro_data_analysis.csv_file_data_analysis import generate_plots
from gui.allegro_tech_gui import create_gui
import sys
import os


def main():
    if os.path.isfile("resources/plots/dochodDom.png") is False:
        generate_plots()
    create_gui()

    print("test")


if __name__ == "__main__":
    main()
