import pandas as pd
import matplotlib.pyplot as plt
games=pd.read_csv('vgsales1.csv')
print(" Summary Statistics Sales for North America :\n",games['NA_Sales'].describe())
print(" Summary Statistics Sales for Europe:\n",games['EU_Sales'].describe())
print(" Summary Statistics Sales for Japan:\n",games['JP_Sales'].describe())
print(" Summary Statistics Sales for Other Sales:\n",games['Other_Sales'].describe())
print(" Summary Statistics Global Sales:\n",games['Global_Sales'].describe())