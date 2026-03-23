import numpy as np
import pandas as pd

# Load Data
framingham = pd.read_csv("./framingham.csv")

# Add primary key patientID
framingham['patientID'] = range(1000, 1000 + len(framingham))

# Create subset dataframes
patients_cvd = framingham[['patientID', 'TenYearCHD']].copy()
lifestyle = framingham[['patientID', 'male', 'age', 'education', 'currentSmoker', 'cigsPerDay']].copy()
clinical = framingham[['patientID', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']].copy()
history = framingham[['patientID', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes']].copy()

# Save files to csv
patients_cvd.to_csv("./patients_cvd.csv", index=False)
lifestyle.to_csv("./lifestyle.csv", index=False)
clinical.to_csv("./clinical.csv", index=False)
history.to_csv("./medical_history.csv", index=False)