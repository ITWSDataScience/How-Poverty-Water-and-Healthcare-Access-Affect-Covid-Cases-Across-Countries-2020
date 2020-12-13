#Clear working space
rm(list = ls())
#Set working directory
setwd(choose.dir())

#Read in datasets
covid <- read.csv("owid-covid-data.csv", header=TRUE) 
exp_health <- read.csv("ExpenditureonHealth.csv", header=TRUE, skip=1)

summary(covid)
summary(exp_health)
colnames(exp_health)[2] <- "Country"

#Jan23 Data
#Used for checking status before COVID
jan23covid <- covid[covid$date == "2020-01-23",]
summary(jan23covid)

#Dec9 Data
#Used for checking number of cases
dec9covid <-covid[covid$date == "2020-12-09",]
summary(dec9covid)

#Most recent data for expenditure on health
exp2017_health <- exp_health[exp_health$Year == "2017",]
summary(exp2017_health)

#current_exp = Current health expenditure (% of GDP)
#dom_gen_exp = Domestic general government health expenditure (% of total government expenditure)
table(exp2017_health$Series)
current_exp <- exp2017_health[exp2017_health$Series == "Current health expenditure (% of GDP)",]
dom_gen_exp <- exp2017_health[exp2017_health$Series == "Domestic general government health expenditure (% of total government expenditure)",]


#extreme_poverty
summary(jan23covid$extreme_poverty)
hist(jan23covid$extreme_poverty)

#handwashing_facilities
summary(jan23covid$handwashing_facilities)
hist(jan23covid$handwashing_facilities)

#population_density
summary(jan23covid$population_density)
hist(jan23covid$population_density)

#current_exp
summary(current_exp$Value)
hist(current_exp$Value)

#dom_gen_exp
summary(dom_gen_exp$Value)
hist(dom_gen_exp$Value)

# ========================Poverty and Covid============================
# Scattered graphs
# Total cases
plot(jan23covid$extreme_poverty, dec9covid$total_cases)
# Total cases per million
plot(jan23covid$extreme_poverty, dec9covid$total_cases_per_million)
# Death rate
plot(jan23covid$extreme_poverty, dec9covid$total_deaths/dec9covid$total_cases)
# Tests per case
plot(jan23covid$extreme_poverty, dec9covid$tests_per_case)
# Tests per thousand
plot(jan23covid$extreme_poverty, dec9covid$total_tests_per_thousand)
# Positive rate
plot(jan23covid$extreme_poverty, dec9covid$positive_rate)

