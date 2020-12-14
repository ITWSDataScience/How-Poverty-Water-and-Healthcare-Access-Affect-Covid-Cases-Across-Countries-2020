library(ggcorrplot)
library(ggplot2)
library(dplyr)

# columns we want to look at to analyze
cols <- c("location", "total_cases_per_million", "total_deaths_per_million", "total_tests_per_thousand", "gdp_per_capita", "extreme_poverty", "handwashing_facilities", "human_development_index", "population_density")

# create data
data.covid <- dec9covid[,cols]
# merge covid data with health data
data.covidHealth <- merge(data.covid, exp2017_health[exp2017_health$Series == "Current health expenditure (% of GDP)",c("Country","Value")], by.x = "location", by.y="Country")
data.covidHealth <- data.covidHealth %>% rename(curr_health_exp = Value)
data.covidHealth <- merge(data.covid, exp2017_health[exp2017_health$Series == "Domestic general government health expenditure (% of total government expenditure)",c("Country","Value")], by.x = "location", by.y="Country")
data.covidHealth <- data.covidHealth %>% rename(dom_gov_health_exp = Value)

# create corrplot
plot <- ggcorrplot(cor(data.covidHealth[,-1], use="complete.obs"),type = "lower",
                   lab = TRUE,
                   ggtheme = ggplot2::theme_minimal(), tl.col="white")
print(plot)
ggsave("./plots/corrplot/plot.png", width = 5, height=5)