from datetime import date
import pickle


# Model Load
pickle_in = open("model/model.pkl","rb")
model = pickle.load(pickle_in)

# Formula functions
# Age Calculator function
def calulate_age(DOB):
    today = date.today()
    return today.year - int(str(DOB)[-4:])
# BMI Calculator function
def calculate_bmi(height,weight):
    return ((703*weight) / (height*height))




# Prediction Model 
def predict_diabetes(patient):

    blood_pressure = patient['blood_pressure']
    age = calulate_age(patient['DOB'])
    gender = patient['gender']
    glucose = patient['glucose']
    bmi = calculate_bmi(patient['height'],patient['weight'])
    insulin = patient['insulin']
    pregnancies = patient['pregnancies']
    skin_thickness = patient['skin_thickness']
    predigree = patient['pedigree']

    prediction = model.predict([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,predigree,age]])
    
    if prediction[0] == 1:
        preditcion = 'Most Likely have Diabetes'
    else:
        preditcion = 'Most Likely NOT to have Diabetes'
    return preditcion
