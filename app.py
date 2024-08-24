from flask import Flask, render_template, request
import joblib
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
        age = int(request.form['age']) 
        sex = int(request.form['sex']) 
        education_level = request.form['education_level']   #
        premium = int(request.form['premium'])
        deductable = int(request.form['deductable'])
        incident_type = request.form['incident_type']   #
        collision_type = request.form['collision_type']     #
        incident_severity = request.form['incident_severity']   #
        authorities_contacted = request.form['authorities_contacted']   #
        property_damage = int(request.form['property_damage'])       
        vehicles_involved = int(request.form['vehicles_involved'])
        bodily_injuries = int(request.form['bodily_injuries'])
        witnesses = int(request.form['witnesses'])
        injury_claim = int(request.form['injury_claim'])
        vehicle_claim = int(request.form['vehicle_claim'])
        
        education_level_dict = {'JD':3, 'High School':2, 'Associate':0, 'MD':4, 'Masters':5, 'PhD':6, 'College':1}
        incident_type_dict = {'Multi-vehicle Collision':0, 'Single Vehicle Collision':2, 'Vehicle Theft':3, 'Parked Car':1} 
        collision_type_dict = {'Rear Collision':1, 'Side Collision':2, 'Front Collision':0}
        incident_severity_dict = {'Minor Damage':1, 'Total Loss':2, 'Major Damage':0, 'Trivial Damage':3}
        authorities_contacted_dict = {'Police':3, 'Fire':1, 'Other':2, 'Ambulance':0}
        
        if education_level in education_level_dict:
            encoded_educational_level = education_level_dict[education_level]

        if incident_type in incident_type_dict:
            encoded_incident_type = incident_type_dict[incident_type]

        if collision_type in collision_type_dict:
            encoded_collision_type = collision_type_dict[collision_type]

        if incident_severity in incident_severity_dict:
            encoded_incident_severity = incident_severity_dict[incident_severity]
        
        if authorities_contacted in authorities_contacted_dict:
            encoded_authorities_contacted = authorities_contacted_dict[authorities_contacted]
        
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
            sex = 'Male' if sex == 1 else 'Female',
            education_level = education_level,
            premium = premium,
            deductable = deductable,
            incident_type = incident_type,
            collision_type = collision_type,
            incident_severity = incident_severity,
            authorities_contacted = authorities_contacted,
            property_damage = 'Yes' if property_damage == '1' else 'No',
            vehicles_involved = vehicles_involved,
            bodily_injuries = bodily_injuries,
            witnesses = witnesses,
            injury_claim = injury_claim,
            vehicle_claim = vehicle_claim
            )

if __name__ == "__main__":
    app.run(debug=True)