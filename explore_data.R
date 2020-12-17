#Clear working space
rm(list = ls())
#Set working directory
setwd(choose.dir())

library(ggplot2)

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
#hist(jan23covid$extreme_poverty)
ggplot() + 
  geom_histogram(aes(x=jan23covid$extreme_poverty),binwidth = 5, color="black", fill="#76D7C4", alpha = 0.5)+
  labs(title = "Extreme Poverty", x="Percentage")+
  theme_bw()

#handwashing_facilities
summary(jan23covid$handwashing_facilities)
#hist(jan23covid$handwashing_facilities)
ggplot() + 
  geom_histogram(aes(x=jan23covid$handwashing_facilities),binwidth = 5, color="black", fill="#76D7C4", alpha = 0.5)+
  labs(title = "Handwashing Facilities", x="Percentage")+
  theme_bw()

#population_density
summary(jan23covid$population_density)
#hist(jan23covid$population_density)
ggplot() + 
  geom_histogram(aes(x=jan23covid$population_density),binwidth = 1000, color="black", fill="#76D7C4", alpha = 0.5)+
  labs(title = "Population Density", x="Number of people per km^2")+
  theme_bw()

#current_exp
summary(current_exp$Value)
#hist(current_exp$Value)
ggplot() + 
  geom_histogram(aes(x=current_exp$Value),binwidth = 1, color="black", fill="#76D7C4", alpha = 0.5)+
  labs(title = "Current Health Expenditure", x="Value")+
  theme_bw()

#dom_gen_exp
summary(dom_gen_exp$Value)
#hist(dom_gen_exp$Value)
ggplot() + 
  geom_histogram(aes(x=dom_gen_exp$Value),binwidth = 1, color="black", fill="#76D7C4", alpha = 0.5)+
  labs(title = "Domestic General Government \nHealth Expenditure", x="Value")+
  theme_bw()

