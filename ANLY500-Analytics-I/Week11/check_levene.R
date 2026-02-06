
data <- read.csv("d:/Github/data_sciences/ANLY500-Analytics-I/Week11/data/invisible.csv")
data$Cloak <- as.factor(data$Cloak)
library(car)
leveneTest(Mischief ~ Cloak, data = data)
