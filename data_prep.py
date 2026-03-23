import numpy as np
import pandas as pd

# Load Data
framingham = pd.read_csv("./data/framingham.csv")

# Add primary key patientID
framingham['patientID'] = range(1000, 1000 + len(framingham))

# Create subset dataframes
patients_cvd = framingham[['patientID', 'TenYearCHD']].copy()
lifestyle = framingham[['patientID', 'male', 'age', 'education', 'currentSmoker', 'cigsPerDay']].copy()
clinical = framingham[['patientID', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']].copy()
history = framingham[['patientID', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes']].copy()

# Add primary key to clinical measurements dataframe
clinical['appointmentID'] = range(10000, 10000 + len(framingham))

# Save files to csv
patients_cvd.to_csv("./data/patient_outcomes.csv", index=False)
lifestyle.to_csv("./data/lifestyle.csv", index=False)
clinical.to_csv("./data/clinical.csv", index=False)
history.to_csv("./data/medical_history.csv", index=False)