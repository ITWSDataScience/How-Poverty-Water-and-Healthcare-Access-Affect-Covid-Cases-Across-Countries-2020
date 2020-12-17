import pandas as pd
import matplotlib.pyplot as plt

covid_data = pd.read_csv("owid-covid-data.csv")
health_data = pd.read_csv("ExpenditureonHealth.csv")

##PREPPING COVID DATA##
useful_covid_data = covid_data[["location", "date", "total_cases", "total_cases_per_million",
                                "total_deaths_per_million", "total_tests_per_thousand",
                                "extreme_poverty", "handwashing_facilities"]]

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
all_data = pd.concat([prepped_covid_data.set_index('location'),
                      prepped_health_data.set_index('Region/Country/Area')], 
                      axis=1, join='inner')


### REGRESSION ###
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def createPlot(x_val, y_val, title, xlab, ylab):
    plt.plot(x_val, y_val, "ro")
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.savefig("./plots/scatter/noRegression/%s.png" % title)
    plt.clf()

def createRegressionPlot(x_val, y_val, title, xlab, ylab):
    x_val_reg_sample = x_val[:-10]
    x_val_pred_sample = x_val[-10:]
    y_val_reg_sample = y_val[:-10]
    y_val_pred_sample = y_val[-10:]

    ### CREATE LINEAR MODEL ###
    model = linear_model.LinearRegression().fit(np.array(x_val_reg_sample).reshape((-1, 1)), y_val_reg_sample)
    ### PREDICT YVALS ###
    model_preds = model.predict(np.array(x_val_pred_sample).reshape((-1, 1)))

    ### CREATE PLOT ###
    plt.plot(x_val, y_val, "ro")
    plt.plot(x_val,model_preds, color='blue', linewidth=2)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title("%s\n r2 = %.2f" % (title, r2_score(y_val_pred_sample, model_preds)))
    plt.savefig("./plots/scatter/regression/%s.png" % title)
    plt.clf()



##PLOT CASES PER MILLION##
createPlot(prepped_covid_data["extreme_poverty"], prepped_covid_data["total_cases_per_million"], "Extreme Poverty vs. Total Cases per Million", "Extreme Poverty in Countries", "Extreme Poverty vs. Total Cases per Million")
createRegPlot(prepped_covid_data["extreme_poverty"], prepped_covid_data["total_cases_per_million"], "Extreme Poverty vs. Total Cases per Million", "Extreme Poverty in Countries", "Extreme Poverty vs. Total Cases per Million")

createPlot(prepped_covid_data["handwashing_facilities"], prepped_covid_data["total_cases_per_million"], "Handwashing Facilities vs. Total Cases per Million", "Handwashing Facilities in Countries", "Total Cases per Million in Countries")
createRegPlot(prepped_covid_data["handwashing_facilities"], prepped_covid_data["total_cases_per_million"], "Handwashing Facilities vs. Total Cases per Million", "Handwashing Facilities in Countries", "Total Cases per Million in Countries")

createRegPlot(all_data["Value"], all_data["total_cases_per_million"], "Health Expenditure vs. Total Cases per Million", "Health Expenditure (% of GDP) in Countries", "Total Cases per Million in Countries")
createRegPlot(all_data["Value"], all_data["total_cases_per_million"], "Health Expenditure vs. Total Cases per Million", "Health Expenditure (% of GDP) in Countries", "Total Cases per Million in Countries")

##PLOT DEATHS PER MILLION##
createPlot(prepped_covid_data["extreme_poverty"], prepped_covid_data["total_deaths_per_million"], "Extreme Poverty vs. Total Deaths per Million", "Extreme Poverty in Countries", "Total Deaths per Million in Countries")
createRegPlot(prepped_covid_data["extreme_poverty"], prepped_covid_data["total_deaths_per_million"], "Extreme Poverty vs. Total Deaths per Million", "Extreme Poverty in Countries", "Total Deaths per Million in Countries")

createPlot(prepped_covid_data["handwashing_facilities"], prepped_covid_data["total_deaths_per_million"], "Handwashing Facilities vs. Total Deaths per Million", "Handwashing Facilities in Countries", "Total Deaths per Million in Countries")
createRegPlot(prepped_covid_data["handwashing_facilities"], prepped_covid_data["total_deaths_per_million"], "Handwashing Facilities vs. Total Deaths per Million", "Handwashing Facilities in Countries", "Total Deaths per Million in Countries")

createPlot(all_data["Value"], all_data["total_deaths_per_million"], "Health Expenditure vs. Total Deaths per Million", "Health Expenditure (% of GDP) in Countries", "Total Deaths per Million in Countries")
createRegPlot(all_data["Value"], all_data["total_deaths_per_million"], "Health Expenditure vs. Total Deaths per Million", "Health Expenditure (% of GDP) in Countries", "Total Deaths per Million in Countries")

createPlot(prepped_covid_data["total_tests_per_thousand"], prepped_covid_data["total_cases_per_million"], "Total Test per Thousand vs. Total Cases per Million", "Total Tests per Thousand in Countries", "Total Cases per Million in Countries")
dropTests = prepped_covid_data[prepped_covid_data["total_tests_per_thousand"].notna()]
createRegPlot(dropTests["total_tests_per_thousand"], dropTests["total_cases_per_million"], "Total Test per Thousand vs. Total Cases per Million", "Total Tests per Thousand in Countries", "Total Cases per Million in Countries")
