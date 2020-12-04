#Import Modules
from tkinter import Tk    
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv
import pandas as pd


def convert_to_csv():
    """
    Function to convert .xlsx files to .csv
    """
    read_file = pd.read_excel (askopenfilename())
    export_file_path = asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = False, header=True, encoding= 'utf8')

    #return


def merge_csv():
    """
    Function to merge csv files
    """
    file_1 = pd.read_csv (askopenfilename())
    file_2 = pd.read_csv (askopenfilename())

    merge_csv = file_1.append(file_2)
    export_file_path = asksaveasfilename(defaultextension='.csv')
    merge_csv.to_csv(export_file_path, index = False, header=True, encoding= 'utf8')
    #return


def data_change():
    """
    Function to change letter grade ['A', 'B', 'C', 'D', 'F'] to numbers ['100', '85', '75', '65', '0']
    """
    r = pd.read_csv (askopenfilename())

    r['CalcBuzzGrade'].replace(['A', 'B', 'C', 'D', 'F'],['100', '85', '75', '65', '0'],inplace=True)
    r['StudentName'] = r['UserLoginName']
    r['StudentName'] = r["StudentName"].str.split("@").str[0]
    export_file_path = asksaveasfilename(defaultextension='.csv')
    r.to_csv(export_file_path, index = False, header=True, encoding= 'utf8')

for _ in range(2):
    convert_to_csv()

merge_csv()

data_change()