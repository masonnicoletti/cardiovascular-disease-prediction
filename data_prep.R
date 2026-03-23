# Load data
framingham <- read_csv("./framingham.csv")

# Add primary key patientID
framingham <- framingham %>%
  mutate(patientID = 1000:(1000 + n() - 1))

# Create subset dataframes
patients_cvd <- framingham %>% select(patientID, TenYearCHD)
lifestyle <- framingham %>% select(patientID, male, age, education, currentSmoker, cigsPerDay)
clinical <- framingham %>% select(patientID, totChol, sysBP, diaBP, BMI, heartRate, glucose)
history <- framingham %>% select(patientID, BPMeds, prevalentStroke, prevalentHyp, diabetes)

# Save files to csv
write_csv(patients_cvd, "./patients_cvd.csv")
write_csv(lifestyle, "./lifestyle.csv")
write_csv(clinical, "./clinical.csv")
write_csv(history, "./medical_history.csv")