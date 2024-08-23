from flask import Flask, render_template, request, jsonify
import joblib

# model = joblib.load('./models/randomForest.lb')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

# @app.route("/prediction",methods=['GET','POST'])
# def prediction():
#     if request.method == "POST":
#         brand = request.form['brand']
#         category = request.form['category']
#         processor_brand = request.form['processor_brand']
#         ram = request.form['ram']
#         processor_name = request.form['processor_name']
#         operating_system = request.form['operating_system']
#         generation = request.form['processor_generation']
#         architecture = request.form['architecture']
#         ssd = request.form['ssd']
#         touch_screen = request.form['touch_screen']
        
#         category_list = ['ThinNline' , 'Gaming']
#         processor_brand_list = ['Intel', 'M1']
#         operating_system_list = [ 'Mac', 'Windows']
#         processor_name_list = ['Core i3', 'Core i5', 'Core i7', 'Core i9', 'Ryzen r3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9', 'M1', 'Pentium Quad']
#         ram_list = ['4 Gb','8 Gb','32 Gb']
#         brand_list = ['Acer', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Avita']
#         generation_list = ['12th', '11th', '9th', '8th', '7th' , '4th', 'Not Available']
#         ssd_list = ['128 GB','256 GB','512 GB','1024 GB','2048 GB','3072 GB']
        
#         brand_flag = [1 if brand == b else 0 for b in brand_list]
#         category_flag = [1 if category == c else 0 for c in category_list]
#         processor_brand_flag = [1 if processor_brand == pb else 0 for pb in processor_brand_list]
#         ram_flag = [1 if ram == r else 0 for r in ram_list]
#         processor_name_flag = [1 if processor_name == pn else 0 for pn in processor_name_list]
#         operating_system_flag = [1 if operating_system == os else 0 for os in operating_system_list]
#         generation_flag = [1 if generation == gn else 0 for gn in generation_list]
#         ssd_flag = [1 if ssd == s else 0 for s in ssd_list]
#         touchscreen_flag = 1 if touch_screen == 'Yes' else 0
#         architecture_flag = 1 if architecture == '64 Bit' else 0

#         unseen_data = [architecture_flag,touchscreen_flag] + brand_flag + category_flag + processor_brand_flag + ram_flag + processor_name_flag + operating_system_flag + generation_flag + ssd_flag
        
#         prediction = model.predict([unseen_data])
#         output = round(prediction[0],2)
    
#         return render_template('result.html',
#             output=output,
#             architecture = architecture,
#             touch_screen = touch_screen,
#             brand = brand,
#             category = category,
#             processor_brand = processor_brand,
#             ram = ram,
#             processor_name = processor_name,
#             operating_system = operating_system,
#             generation = generation,
#             ssd = ssd,
#             )

if __name__ == "__main__":
    app.run(debug=True)