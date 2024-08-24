from flask import Flask, render_template, request
import joblib
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

filename = 'label_encoder.pkl'
loaded_encoder = joblib.load(filename)
model = joblib.load('./model/decision_tree_model.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        age = request.form['age'] 
        sex = request.form['sex'] 
        education_level = request.form['education_level']   #
        premium = request.form['premium']
        deductable = request.form['deductable']
        incident_type = request.form['incident_type']   #
        collision_type = request.form['collision_type']     #
        incident_severity = request.form['incident_severity']   #
        authorities_contacted = request.form['authorities_contacted']   #
        property_damage = request.form['property_damage']       
        vehicles_involved = request.form['vehicles_involved']
        bodily_injuries = request.form['bodily_injuries']
        witnesses = request.form['witnesses']
        injury_claim = request.form['injury_claim']
        vehicle_claim = request.form['vehicle_claim']
        
        # education_level_list = ['JD', 'High School', 'Associate', 'MD', 'Masters', 'PhD', 'College']
        # encoded_educational_level_list = encoder.transform(education_level_list)
        
        encoded_educational_level = 0
        encoded_incident_type = 0
        encoded_collision_type = 0
        encoded_incident_severity = 0
        encoded_authorities_contacted = 0
        
        unseen_data = [[age,
                        sex,
                        encoded_educational_level,
                        premium,
                        deductable,
                        encoded_incident_type,
                        encoded_collision_type,
                        encoded_incident_severity,
                        encoded_authorities_contacted,
                        property_damage,
                        vehicles_involved,
                        bodily_injuries,
                        witnesses,
                        injury_claim,
                        vehicle_claim
                        ]]
        
        prediction = model.predict(unseen_data)
        output = prediction[0]
    
        return render_template('result.html',
            output = 'Fraud' if output == 'Y' else 'Not Fraud',
            age = age,
            sex = 'Male' if 1 == sex else 'Female',
            education_level = education_level,
            premium = premium,
            deductable = deductable,
            incident_type = incident_type,
            collision_type = collision_type,
            incident_severity = incident_severity,
            authorities_contacted = authorities_contacted,
            property_damage = 'Yes' if property_damage == 1 else 'No',
            vehicles_involved = vehicles_involved,
            bodily_injuries = bodily_injuries,
            witnesses = witnesses,
            injury_claim = injury_claim,
            vehicle_claim = vehicle_claim
            )

if __name__ == "__main__":
    app.run(debug=True)