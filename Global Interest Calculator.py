'''
Global Interest Rate Calculator
Dependent on Official Interest Rates of Countries
'''

#Necessary libraries are imported.
import requests
import lxml
import bs4
import pandas as pd
import numpy as np

#To get official interest rates, we use web scraping from Global-Rates.com
res = requests.get("https://www.global-rates.com/en/interest-rates/central-banks/central-banks.aspx")
soup = bs4.BeautifulSoup(res.text,"lxml")

data = list()

#In html of global-rates, two classes defined for countries in tabledata1 and 2.
for item in soup.select(".tabledata1"):
    data.append(item.text)

for item in soup.select(".tabledata2"):
    data.append(item.text)
    
country_names = []
interest_rates = []

#Country names and interest rates gathered as lists.
for i in range(len(data)):
    country_names.append(data[i].split("\n")[2])
    interest_rates.append(float(data[i].split("\n")[3].replace("\xa0%","")))

#To analyse data easily, I've used pandas.    
df = pd.DataFrame(interest_rates,country_names)
df.columns = ["interest_rate"]

#Function for calculating actual interest rate after time specified.
def interest_calculator(country,bank_amount,months):
    
    years = months/12
    value_after_years = bank_amount * (1 + df["interest_rate"].loc[country]/100)**years
    
    return value_after_years.round(2)

#To get currencies, we scraped through iban.com
res2 = requests.get("https://www.iban.com/currency-codes")
soup2 = bs4.BeautifulSoup(res2.text,"lxml")

data2 = []

for item in soup2.select(".table"):
    data2.append(item.text)
    
new_data = str(data2).split("\\n\\n\\n")

clear_data = []
for i in range(len(new_data)):
    clear_data.append(new_data[i].replace("\\n"," "))

clear_data.pop(0)
clear_data.pop(0)

values = []
for i in range(267):
    values.append(clear_data[i].split()[-2])

keys = []
for i in range(267):
    keys.append(clear_data[i].split()[0])

keys[1] = "ALAND"

keys_capitalize = []
for i in range(len(keys)):
    keys_capitalize.append(keys[i].capitalize())

#All countries and currency values are gathered in a dictionary.
curr_names = dict(zip(keys_capitalize,values))

#Minor changes for full complience on dictionary.
curr_names["United States"] = curr_names.pop("American")
curr_names["Czech Republic"] = curr_names.pop("Czech")
curr_names["Europe"] = "EUR"
curr_names["Russia"] = curr_names.pop("Russian")
curr_names["South Africa"] = "ZAR"
curr_names["South Korea"] = curr_names.pop("Korea")
curr_names["Great Britain"] = "GBP"
curr_names["New Zealand"] = "NZD"
curr_names["Saudi Arabia"] = "SAR"

print("The countries you can select are: " + str(country_names))

#Basic inputs section for the results.
country = ""
while country not in country_names:
    country = input("Choose the country you want to invest: \n")
    if country not in country_names:
        print("Please choose a country from the list.\n")

print(f"You have chosen {country}, the currency of {country} is {curr_names[country]}.")

while True:
    try:
        bank_amount = float(input("Please provide the amount of money you plan to invest in local bank: \n"))
        break
    except:
        print("There's most likely an error, please try again with an integer or decimal number.\n")
        
        
while True:
    try:
        months = float(input("How many months you want to keep your money: \n"))
        break
    except:
        print("There's most likely an error, please try again with an integer or decimal number.\n")
        
total_money = interest_calculator(country,bank_amount,months)
interest_money = total_money - bank_amount

print(f"\nYou've deposit {bank_amount} {curr_names[country]}, and you've earned {interest_money.round(2)} {curr_names[country]}")
print(f"\nFinal amount is {total_money} {curr_names[country]}")