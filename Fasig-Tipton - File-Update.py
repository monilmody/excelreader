import os
import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd
from datetime import datetime
from datetime import date

# Author: Monil Samir Mody
# Date: September 15, 2023
# Description: This Python file updates the excel file with the following requirement for Fasig Tipton.

# Open a file dialog for the user to choose a file
file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])

# Check if the user selected a file or canceled the dialog
if file_path:

    # Read the selected Excel file into a DataFrame
    df = pd.read_csv(file_path)

    # Prompt the user to insert the salecode using a dialog
    salecode = simpledialog.askstring("Input", "Please enter the SALECODE:")

    # Check if the user provided a salecode or canceled the dialog
    if salecode is not None:

        # Now you can work with the DataFrame 'df' and 'salecode' as needed

        # For example, you can print the first few rows and the salecode:
        print(df.head())
        print(f"Salecode: {salecode}")

    else:
        print("Salecode input canceled.")
else:
    print("No file selected or dialog canceled.")



df.rename(columns={'HIP': 'HIP1'}, inplace=True)
df.rename(columns={'PRICE': 'PRICE1'}, inplace=True)
df.rename(columns={'COLOR': 'COLOR1'}, inplace=True)
df.rename(columns={'SEX': 'SEX1'}, inplace=True)
df.rename(columns={'SIRE': 'SIRE1'}, inplace=True)
df.rename(columns={'DAM': 'DAM1'}, inplace=True)
df.rename(columns={'PRIVATE SALE': 'PRIVATE SALE1'}, inplace=True)

saleyear = 2023
df['SALEYEAR'] = saleyear

saletype = 'Y'
df['SALETYPE'] = saletype

df['SALECODE'] = salecode

if 'SESSION' in df.columns:
    df['SALEDATE'] = df['SESSION']

if 'SESSION' in df.columns:
    df.drop(columns=['SESSION'], inplace=True)

book = 1
df['BOOK'] = book

day = 1
df['DAY'] = day

if 'HIP1' in df.columns:
    df['HIP'] = df['HIP1']

if 'HIP1' in df.columns:
    df['HIPNUM'] = df['HIP1']

if 'HIP1' in df.columns:
    df.drop(columns=['HIP1'], inplace=True)

# Check if 'NAME' is a column in the DataFrame
if 'NAME' in df.columns:
            # Create a new 'HORSE' column and populate it with 'NAME'
            df['HORSE'] = df['NAME']


            # Check if 'NAME' is a column in the DataFrame
if 'NAME' in df.columns:
            # Create a new 'HORSE' column and populate it with 'NAME'
            df['CHORSE'] = df['NAME']

if 'NAME' in df.columns:
            df.drop(columns=['NAME'], inplace=True)

rating = ''
df['RATING'] = rating

tattoo = ''
df['TATTOO'] = tattoo

datefoal = df['YEAR OF BIRTH']
if 'YEAR OF BIRTH' in df.columns:
    df['DATEFOAL'] = datefoal

if 'YEAR OF BIRTH' in df.columns:
    df.drop(columns=['YEAR OF BIRTH'], inplace=True)

def calculate_age(datefoal):
    today = date.today()
    born = pd.to_datetime(datefoal, errors='coerce')  # Convert to datetime, handle invalid dates
    age = today.year - born.dt.year - ((today.month * 100 + today.day) < (born.dt.month * 100 + born.dt.day))
    return age

age = calculate_age(df['DATEFOAL'])
df['AGE'] = age

if 'COLOR1' in df.columns:
    df['COLOR'] = df['COLOR1']

if 'COLOR1' in df.columns:
    df.drop(columns=['COLOR1'], inplace=True)

if 'SEX1' in df.columns:
    df['SEX'] = df['SEX1']

if 'SEX1' in df.columns:
    df.drop(columns=['SEX1'], inplace=True)

gait = ''
df['GAIT'] = gait

type = 'Y'
df['TYPE'] = type

record = ''
df['RECORD'] = record

et = ''
df['ET'] = et

if 'FOALED' in df.columns:
    df['ELIG'] = df['FOALED']

if 'SIRE1' in df.columns:
    df['SIRE'] =  df['SIRE1']

if 'SIRE1' in df.columns:
    df['CSIRE'] = df['SIRE1']

if 'SIRE1' in df.columns:
    df.drop(columns=['SIRE1'], inplace=True)

if 'DAM1' in df.columns:
    df['DAM'] = df['DAM1']

if 'DAM1' in df.columns:
    df['CDAM'] = df['DAM1']

if 'DAM1' in df.columns:
    df.drop(columns=['DAM1'], inplace=True)

if 'SIRE OF DAM' in df.columns:
    df['SIREOFDAM'] = df['SIRE OF DAM']

if 'SIRE OF DAM' in df.columns:
    df['CSIREOFDAM'] = df['SIRE OF DAM']

if 'SIRE OF DAM' in df.columns:
    df.drop(columns=['SIRE OF DAM'], inplace=True)

damofdam = ''
df['DAMOFDAM'] = damofdam

cdamofdam = ''
df['CDAMOFDAM'] = cdamofdam

damtatt = ''
df['DAMTATT'] = damtatt

damyof = ''
df['DAMYOF'] = damyof

ddamtatt = ''
df['DDAMTATT'] = ddamtatt

if 'CONSIGNOR NAME' in df.columns:
    df['BREDTO'] = df['CONSIGNOR NAME']

if 'CONSIGNOR NAME' in df.columns:
    df.drop(columns=['CONSIGNOR NAME'], inplace=True)

lastbred = ''
df['LASTBRED'] = lastbred

conlname = df['PROPERTY LINE']
df['CONLNAME'] = conlname

df.drop(columns=['PROPERTY LINE'], inplace=True)

consno = ''
df['CONSNO'] = consno

pemcode = ''
df['PEMCODE'] = pemcode

purfname = ''
df['PURFNAME'] = purfname

purlname = df['PURCHASER']
df['PURLNAME'] = purlname

df.drop(columns=['PURCHASER'], inplace=True)

sbcity = ''
df['SBCITY'] = sbcity

sbstate = ''
df['SBSTATE'] = sbstate

sbcountry = ''
df['SBCOUNTRY'] = sbcountry

price = df['PRICE1']
df['PRICE'] = price

df.drop(columns=['PRICE1'], inplace=True)
df.drop(columns=['SALE TITLE'], inplace=True)

currency = ''
df['CURRENCY'] = currency

url = df['VIRTUAL INSPECTION'] 
df['URL'] = url

df.drop(columns=['VIRTUAL INSPECTION'], inplace=True)

nffm = ''
df['NFFM'] = nffm

privatesale = df['PRIVATE SALE1']
df['PRIVATE SALE'] = privatesale

df.drop(columns=['PRIVATE SALE1'], inplace=True)

breed = 'T'
df['BREED'] = breed

datefoal_series = df['DATEFOAL']

def calculate_year(datefoal):
    current_year = datetime.now().year - 2
    return current_year

# Apply the calculate_year function to each date in the Series
yearfoal_series = datefoal_series.apply(calculate_year)

# yearfoal = calculate_year(df['DATEFOAL'])
df['YEARFOAL'] = yearfoal_series

df.drop(columns=['BARN'], inplace=True)
df.drop(columns=['COVER DATE'], inplace=True)

if 'SOLD AS CODE' in df.columns:
    df.drop(columns=['SOLD AS CODE'], inplace=True)
    
df.drop(columns=['SOLD AS DESCRIPTION'], inplace=True)
df.drop(columns=['FOALED'], inplace=True)

print(df) 

output_file_path = 'C:\\Users\\monil\\Downloads\\{}.csv'.format(salecode)

if os.path.exists(output_file_path):
    # If the file exists, remove it
    os.remove(output_file_path)


df.to_csv(output_file_path, index=False)

os.system(f'start {output_file_path}')