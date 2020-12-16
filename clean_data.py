import pandas as pd
import matplotlib.pyplot as plt

covid_data = pd.read_csv("owid-covid-data.csv")
health_data = pd.read_csv("ExpenditureonHealth.csv")

##PREPPING COVID DATA##
useful_covid_data = covid_data[["location", "date", "total_cases", "total_cases_per_million", "total_deaths_per_million", "extreme_poverty", "handwashing_facilities"]]

cleaned1 = useful_covid_data[useful_covid_data["total_cases"].notna()]

cleaned2 = cleaned1[cleaned1["handwashing_facilities"].notna()]

cleaned_covid_data = cleaned2[cleaned2["extreme_poverty"].notna()]

remove_world_data = cleaned_covid_data[cleaned_covid_data["location"] != "World"]

prepped_covid_data = remove_world_data[remove_world_data["date"] == "2020-12-09"]

##PREPPING HEALTH DATA##
useful_health_data = health_data[["Region/Country/Area", "Year", "Series", "Value"]]

remove_health_data = useful_health_data[useful_health_data["Series"] == "Current health expenditure (% of GDP)"]

prepped_health_data = remove_health_data[remove_health_data["Year"] == 2017]

##JOINING DATA FOR ANALYSIS##
all_data = pd.concat([prepped_covid_data.set_index('location'), prepped_health_data.set_index('Region/Country/Area')], axis=1, join='inner')

##PLOT CASES PER MILLION##
plt.plot(prepped_covid_data["extreme_poverty"], prepped_covid_data["total_cases_per_million"], "ro")
plt.xlabel("Extreme Poverty in Countries")
plt.ylabel("Total Cases per Million in Countries")
plt.title("Extreme Poverty vs. Total Cases per Million")
plt.show()

plt.plot(prepped_covid_data["handwashing_facilities"], prepped_covid_data["total_cases_per_million"], "ro")
plt.xlabel("Handwashing Facilities in Countries")
plt.ylabel("Total Cases per Million in Countries")
plt.title("Handwashing Facilities vs. Total Cases per Million")
plt.show()

plt.plot(all_data["Value"], all_data["total_cases_per_million"], "ro")
plt.xlabel("Health Expenditure (% of GDP) in Countries")
plt.ylabel("Total Cases per Million in Countries")
plt.title("Health Expenditure vs. Total Cases per Million")
plt.show()

##PLOT DEATHS PER MILLION##
plt.plot(prepped_covid_data["extreme_poverty"], prepped_covid_data["total_deaths_per_million"], "ro")
plt.xlabel("Extreme Poverty in Countries")
plt.ylabel("Total Deaths per Million in Countries")
plt.title("Extreme Poverty vs. Total Deaths per Million")
plt.show()

plt.plot(prepped_covid_data["handwashing_facilities"], prepped_covid_data["total_deaths_per_million"], "ro")
plt.xlabel("Handwashing Facilities in Countries")
plt.ylabel("Total Deaths per Million in Countries")
plt.title("Handwashing Facilities vs. Total Deaths per Million")
plt.show()

plt.plot(all_data["Value"], all_data["total_deaths_per_million"], "ro")
plt.xlabel("Health Expenditure (% of GDP) in Countries")
plt.ylabel("Total Deaths per Million in Countries")
plt.title("Health Expenditure vs. Total Deaths per Million")
plt.show()

