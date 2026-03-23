library(readr)
library(dplyr)
library(ggplot2)

# Load data
framingham <- read_csv("./data/framingham.csv")

# Add primary key patientID
framingham <- framingham %>%
  mutate(patientID = 1000:(1000 + n() - 1))

# Create subset dataframes
patients_cvd <- framingham %>% select(patientID, TenYearCHD)
lifestyle <- framingham %>% select(patientID, male, age, education, currentSmoker, cigsPerDay)
clinical <- framingham %>% select(patientID, totChol, sysBP, diaBP, BMI, heartRate, glucose)
history <- framingham %>% select(patientID, BPMeds, prevalentStroke, prevalentHyp, diabetes)

# Add primary key to clinical measurements table
clinical <- clinical %>%
  mutate(appointmentID = 10000:(10000 + n() - 1)) %>% 
  relocate(appointmentID)

# Save files to csv
write_csv(patients_cvd, "./data/patient_outcomes.csv")
write_csv(lifestyle, "./data/lifestyle.csv")
write_csv(clinical, "./data/clinical.csv")
write_csv(history, "./data/medical_history.csv")