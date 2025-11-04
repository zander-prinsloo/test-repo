# Install packages
#install.packages("tidyverse")
#install.packages("pipr")

# Load libraries
library(tidyverse)
library(pipr)

# Example data frame
df_pip <- pipr::get_stats()

# dir 
data_dir <- fs::path("data")

# Save data frame as CSV
write_csv(df_pip, fs::path(data_dir, "pip.csv"))

