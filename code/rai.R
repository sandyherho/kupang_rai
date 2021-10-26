"
rai.R

RAI calculation
Sandy Herho <herho@umd.edu>
2021/10/25
"

rm(list = ls())

library(precintcon)
library(readr)
library(tidyverse)

df <- read.data("../data/raiInput.csv")
rai_kupang <- rai(df, granularity = "m")
pplot.rai(df, granularity = "m")

rai_kupang <- na.omit(as.data.frame(rai_kupang$rai))
dates <- seq.Date(from = as.Date("1978-01-31"),
                  to = as.Date("2020-12-31"),
                  by = "month")
rai_kupang <- tibble(cbind.data.frame(dates, rai_kupang), 
                .name_repair = ~ c("time", "rai"))
write_csv(rai_kupang, "../data/rai_kupang.csv")
