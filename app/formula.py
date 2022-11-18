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

def calculate_relative(gene_percent,relative_diabetic, relative_non_diabetic):
    sum_diabetic = 0
    sum_non_diabetic = 0
    for n in range(0,len(relative_diabetic)):
        sum_diabetic += gene_percent * (88 - relative_diabetic["age"]) + 20
    for n in range(0,len(relative_non_diabetic)):
        sum_non_diabetic += gene_percent * (relative_non_diabetic["age"] - 14) + 50
    return  sum_diabetic,sum_non_diabetic

def calculate_pedigree(number_of_diabetic, number_of_non_diabetic):
    sum_diabetic = 0
    sum_non_diabetic = 0

    # Immediate Relative - eg: Parent or full sibiling
    sum_diabtetic,sum_non_diabetic = calculate_relative(0.5,number_of_diabetic,number_of_non_diabetic)
    # Relatives: Grandparents, half siblings, uncle/aunts
    sum_diabtetic,sum_non_diabetic += calculate_relative(0.25,number_of_diabetic,number_of_non_diabetic)
    # Relatives: half aunt, half uncle, first cousin 
    sum_diabtetic,sum_non_diabetic += calculate_relative(0.1,number_of_diabetic,number_of_non_diabetic)

    return (sum_diabetic/sum_non_diabetic)

def get_default_pedigree(age):
    if age >= 65:
        return 0.4
    else:
        return 0.1

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
    predigree = get_default_pedigree(age)

    prediction = model.predict([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,predigree,age]])
    
    if prediction[0] == 1:
        preditcion = 'Most Likely have Diabetes'
    else:
        preditcion = 'Most Likely NOT to have Diabetes'
    return preditcion
