# from flask import Flask, render_template, redirect, url_for, session, flash, Flask, render_template, request, send_from_directory, url_for
# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField
# from wtforms.validators import DataRequired, Email, ValidationError
# import bcrypt
# from flask_mysqldb import MySQL
# import pymysql
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os

# app = Flask(__name__)

# # MySQL Configuration
# # app.config['MYSQL_HOST'] = 'localhost'
# # app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = ''
# # app.config['MYSQL_DB'] = 'mydatabase'
# app.secret_key = 'your_secret_key_here'

# # mysql = MySQL(app)

# connection=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='mydatabase'
# )



# class RegisterForm(FlaskForm):
#     name = StringField("Name",validators=[DataRequired()])
#     email = StringField("Email",validators=[DataRequired(), Email()])
#     password = PasswordField("Password",validators=[DataRequired()])
#     submit = SubmitField("Register")

#     def validate_email(self,field):
#         cur = connection.cursor()
#         cur.execute("SELECT * FROM users where email=%s",(field.data,))
#         user = cur.fetchone()
#         cur.close()
#         if user:
#             raise ValidationError('Email Already Taken')

# class LoginForm(FlaskForm):
#     email = StringField("Email",validators=[DataRequired(), Email()])
#     password = PasswordField("Password",validators=[DataRequired()])
#     submit = SubmitField("Login")


# # Loading the trained model
# model = load_model('best_model.h5')

# # Defining the class names
# class_names = ["fall armyworm", "grasshopper", "healthy", "leaf beetle", "leaf blight", "leaf spot", "streak virus"]

# # Defining class details
# # Defining class details
# class_details = {
#     "fall armyworm": {
#         "description": "The fall armyworm (Spodoptera frugiperda) is a highly destructive pest that targets various crops, with a primary focus on maize. Originating from the Americas, it has become a global threat, capable of causing significant yield losses if not adequately controlled. The adult moths lay eggs on leaves, and the larvae feed voraciously, causing damage to plant tissues. Early detection is crucial for effective management.",
#         "solution": "Integrated pest management (IPM) strategies are recommended for fall armyworm control. These include the use of biological control agents, such as parasitoid wasps and predators. Additionally, targeted application of insecticides may be necessary in severe infestations. Farmers are advised to implement cultural practices like crop rotation and maintain vigilant monitoring.",
#         "link": "https://example.com/fall-armyworm-management-guide",
#     },
#     "grasshopper": {
#         "description": "Grasshoppers are herbivorous insects known for their powerful hind legs, enabling them to jump considerable distances. They pose a threat to various crops by feeding on leaves, stems, and grains. Grasshopper infestations can lead to defoliation and yield loss if not addressed promptly. These insects are most active during warm and dry conditions.",
#         "solution": "Control measures for grasshoppers involve a combination of cultural, biological, and chemical approaches. Farmers can implement physical barriers, such as nets, to protect crops. Natural predators like birds and predatory insects can be encouraged. In cases of severe infestation, targeted application of insecticides may be necessary.",
#         "link": "https://example.com/grasshopper-control-strategies",
#     },
#     "healthy": {
#         "description": "A healthy plant is characterized by vibrant growth, lush foliage, and absence of visible pests or diseases. Optimal plant health is crucial for achieving maximum crop yield and quality. Healthy plants are more resilient to environmental stresses and can better withstand various challenges.",
#         "solution": "Maintaining plant health involves practicing good agricultural habits. This includes providing adequate water and nutrients, implementing proper crop rotation, and managing pest populations through preventive measures. Regular monitoring for early signs of stress or diseases is essential.",
#         "link": "https://example.com/plant-health-guidelines",
#     },
#     "leaf beetle": {
#         "description": "Leaf beetles, belonging to the Chrysomelidae family, are herbivorous insects that can cause significant damage to plants by feeding on leaves. These beetles come in various colors and are known for their chewing mouthparts. They can be a concern for crops such as potatoes, beans, and cruciferous vegetables.",
#         "solution": "Control of leaf beetles involves the use of insecticides, especially during the early stages of infestation. Implementing cultural practices like crop rotation and companion planting can help disrupt their life cycle. Natural enemies, such as predatory insects, may also contribute to population control.",
#         "link": "https://example.com/leaf-beetle-management-strategies",
#     },
#     "leaf blight": {
#         "description": "Leaf blight is a common fungal disease that affects a variety of plants, leading to browning and death of leaves. The disease is often characterized by dark lesions with irregular margins. Warm and humid conditions favor the development and spread of leaf blight, posing a threat to crop health.",
#         "solution": "Management of leaf blight involves implementing preventive measures and early intervention. Fungicides may be applied during the growing season to protect plants. Cultural practices, such as proper spacing and pruning, can improve air circulation and reduce disease pressure.",
#         "link": "https://example.com/leaf-blight-prevention-and-control",
#     },
#     "leaf spot": {
#         "description": "Leaf spot is a plant disease caused by various fungi or bacteria, resulting in the formation of small, dark spots on leaves. These spots may coalesce, leading to defoliation and reduced photosynthetic capacity. Leaf spot diseases can affect a wide range of crops and ornamental plants.",
#         "solution": "Effective management of leaf spot diseases includes the application of fungicides, especially during periods of high humidity. Additionally, cultural practices such as removing infected plant material, practicing crop rotation, and providing adequate spacing can help reduce disease incidence.",
#         "link": "https://example.com/leaf-spot-disease-management",
#     },
#     "streak virus": {
#         "description": "Streak viruses are plant viruses that cause streak-like symptoms on leaves, affecting crop health and productivity. These viruses are often transmitted by insect vectors, such as aphids or leafhoppers. Streak virus infections can lead to stunted growth, yellowing, and reduced yield in infected plants.",
#         "solution": "Preventing the spread of streak viruses involves managing insect vectors and implementing strict sanitation measures. Planting virus-resistant varieties can provide an additional layer of protection. Early detection and removal of infected plants help mitigate the risk of further spread.",
#         "link": "https://example.com/streak-virus-management-strategies",
#     },
# }



# # @app.route('/')
# # def index():
# #     return render_template('dashboard.html')



# @app.route('/', methods=['GET', 'POST'])
# def upload_predict():
#     if request.method == 'POST':
#         image_file = request.files['image']
#         if image_file:
#             # Ensuring 'uploads' directory exists
#             uploads_dir = os.path.join('static', 'uploads')
#             os.makedirs(uploads_dir, exist_ok=True)

#             # Saving the uploaded image
#             image_location = os.path.join(uploads_dir, image_file.filename)
#             image_file.save(image_location)

#             # Loading and preprocessing the image for prediction
#             img = image.load_img(image_location, target_size=(64, 64))
#             x = image.img_to_array(img)
#             x = np.expand_dims(x, axis=0)

#             # Making a prediction using the loaded model
#             pred = model.predict(x)
#             pred_class = np.argmax(pred, axis=-1)[0]
#             predicted_label = class_names[pred_class]
            
#             # Getting class description
#             class_description = class_details.get(predicted_label, "")
            
#             # Generating URL for the uploaded image
#             image_url = url_for('static', filename=f'uploads/{image_file.filename}')

#             # Rendering the result template with prediction and image details
#             return render_template('result.html', prediction=predicted_label, image_loc=image_url, class_description=class_description)

#     return render_template('dashboard.html', prediction="", image_loc=None)




# @app.route('/register',methods=['GET','POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         password = form.password.data

#         hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

#         # store data into database 
#         cur = connection.cursor()
#         cur.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,hashed_password))
#         connection.commit()
#         cur.close()

#         return redirect(url_for('login'))

#     return render_template('register.html',form=form)

# @app.route('/login',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data

#         cur = connection.cursor()
#         cur.execute("SELECT * FROM users WHERE email=%s",(email,))
#         user = cur.fetchone()
#         cur.close()
#         if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
#             session['user_id'] = user[0]
#             return redirect(url_for('dashboard'))
#         else:
#             flash("Login failed. Please check your email and password")
#             return redirect(url_for('login'))

#     return render_template('login.html',form=form)

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         user_id = session['user_id']

#         cur = connection.cursor()
#         cur.execute("SELECT * FROM users where id=%s",(user_id,))
#         user = cur.fetchone()
#         cur.close()

#         if user:
#             return render_template('dashboard.html',user=user)
            
#     return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     flash("You have been logged out successfully.")
#     return redirect(url_for('login'))




# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, session, flash, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import bcrypt
import pymysql
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# MySQL Connection Configuration
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='mydatabase'
)

# Flask-WTF Form for User Registration
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s", (field.data,))
        user = cur.fetchone()
        cur.close()
        if user:
            raise ValidationError('Email Already Taken')

# Flask-WTF Form for User Login
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Loading the trained model
model = load_model('best_model.h5')

# Defining class names and details
class_names = ["fall armyworm", "grasshopper", "healthy", "leaf beetle", "leaf blight", "leaf spot", "streak virus"]

class_details = {
    "fall armyworm": {
        "description": "The fall armyworm (Spodoptera frugiperda) is a highly destructive pest that targets various crops, with a primary focus on maize. Originating from the Americas, it has become a global threat, capable of causing significant yield losses if not adequately controlled. The adult moths lay eggs on leaves, and the larvae feed voraciously, causing damage to plant tissues. Early detection is crucial for effective management.",
        "solution": "Integrated pest management (IPM) strategies are recommended for fall armyworm control. These include the use of biological control agents, such as parasitoid wasps and predators. Additionally, targeted application of insecticides may be necessary in severe infestations. Farmers are advised to implement cultural practices like crop rotation and maintain vigilant monitoring.",
        "link": "https://example.com/fall-armyworm-management-guide",
    },
    "grasshopper": {
        "description": "Grasshoppers are herbivorous insects known for their powerful hind legs, enabling them to jump considerable distances. They pose a threat to various crops by feeding on leaves, stems, and grains. Grasshopper infestations can lead to defoliation and yield loss if not addressed promptly. These insects are most active during warm and dry conditions.",
        "solution": "Control measures for grasshoppers involve a combination of cultural, biological, and chemical approaches. Farmers can implement physical barriers, such as nets, to protect crops. Natural predators like birds and predatory insects can be encouraged. In cases of severe infestation, targeted application of insecticides may be necessary.",
        "link": "https://example.com/grasshopper-control-strategies",
    },
    "healthy": {
        "description": "A healthy plant is characterized by vibrant growth, lush foliage, and absence of visible pests or diseases. Optimal plant health is crucial for achieving maximum crop yield and quality. Healthy plants are more resilient to environmental stresses and can better withstand various challenges.",
        "solution": "Maintaining plant health involves practicing good agricultural habits. This includes providing adequate water and nutrients, implementing proper crop rotation, and managing pest populations through preventive measures. Regular monitoring for early signs of stress or diseases is essential.",
        "link": "https://example.com/plant-health-guidelines",
    },
    "leaf beetle": {
        "description": "Leaf beetles, belonging to the Chrysomelidae family, are herbivorous insects that can cause significant damage to plants by feeding on leaves. These beetles come in various colors and are known for their chewing mouthparts. They can be a concern for crops such as potatoes, beans, and cruciferous vegetables.",
        "solution": "Control of leaf beetles involves the use of insecticides, especially during the early stages of infestation. Implementing cultural practices like crop rotation and companion planting can help disrupt their life cycle. Natural enemies, such as predatory insects, may also contribute to population control.",
        "link": "https://example.com/leaf-beetle-management-strategies",
    },
    "leaf blight": {
        "description": "Leaf blight is a common fungal disease that affects a variety of plants, leading to browning and death of leaves. The disease is often characterized by dark lesions with irregular margins. Warm and humid conditions favor the development and spread of leaf blight, posing a threat to crop health.",
        "solution": "Management of leaf blight involves implementing preventive measures and early intervention. Fungicides may be applied during the growing season to protect plants. Cultural practices, such as proper spacing and pruning, can improve air circulation and reduce disease pressure.",
        "link": "https://example.com/leaf-blight-prevention-and-control",
    },
    "leaf spot": {
        "description": "Leaf spot is a plant disease caused by various fungi or bacteria, resulting in the formation of small, dark spots on leaves. These spots may coalesce, leading to defoliation and reduced photosynthetic capacity. Leaf spot diseases can affect a wide range of crops and ornamental plants.",
        "solution": "Effective management of leaf spot diseases includes the application of fungicides, especially during periods of high humidity. Additionally, cultural practices such as removing infected plant material, practicing crop rotation, and providing adequate spacing can help reduce disease incidence.",
        "link": "https://example.com/leaf-spot-disease-management",
    },
    "streak virus": {
        "description": "Streak viruses are plant viruses that cause streak-like symptoms on leaves, affecting crop health and productivity. These viruses are often transmitted by insect vectors, such as aphids or leafhoppers. Streak virus infections can lead to stunted growth, yellowing, and reduced yield in infected plants.",
        "solution": "Preventing the spread of streak viruses involves managing insect vectors and implementing strict sanitation measures. Planting virus-resistant varieties can provide an additional layer of protection. Early detection and removal of infected plants help mitigate the risk of further spread.",
        "link": "https://example.com/streak-virus-management-strategies",
    },
}



# @app.route('/', methods=['GET', 'POST'])
# def upload_predict():
#     if request.method == 'POST':
#         image_file = request.files['image']
#         if image_file:
#             # Saving the uploaded image
#             uploads_dir = os.path.join('static', 'uploads')
#             os.makedirs(uploads_dir, exist_ok=True)
#             image_location = os.path.join(uploads_dir, image_file.filename)
#             image_file.save(image_location)

#             # Loading and preprocessing the image for prediction
#             img = image.load_img(image_location, target_size=(64, 64))
#             x = image.img_to_array(img)
#             x = np.expand_dims(x, axis=0)

#             # Making a prediction using the loaded model
#             pred = model.predict(x)
#             pred_class = np.argmax(pred, axis=-1)[0]
#             predicted_label = class_names[pred_class]

#             # Getting class description
#             class_description = class_details.get(predicted_label, "")

#             # Generating URL for the uploaded image
#             image_url = url_for('static', filename=f'uploads/{image_file.filename}')

#             # Rendering the result template with prediction and image details
#             return render_template('result.html', prediction=predicted_label, image_loc=image_url, class_description=class_description)

#     return render_template('dashboard.html', prediction="", image_loc=None)

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Storing data into database
        cur = connection.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
        connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cur.fetchone()
        cur.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed. Please check your email and password")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

# User Dashboard Route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        user = cur.fetchone()
        cur.close()

        if user:
            if request.method == 'POST':
                image_file = request.files['image']
                if image_file:
                    # Saving the uploaded image
                    uploads_dir = os.path.join('static', 'uploads')
                    os.makedirs(uploads_dir, exist_ok=True)
                    image_location = os.path.join(uploads_dir, image_file.filename)
                    image_file.save(image_location)

                    # Loading and preprocessing the image for prediction
                    img = image.load_img(image_location, target_size=(64, 64))
                    x = image.img_to_array(img)
                    x = np.expand_dims(x, axis=0)

                    # Making a prediction using the loaded model
                    pred = model.predict(x)
                    pred_class = np.argmax(pred, axis=-1)[0]
                    predicted_label = class_names[pred_class]

                    # Getting class description
                    class_description = class_details.get(predicted_label, "")

                    # Generating URL for the uploaded image
                    image_url = url_for('static', filename=f'uploads/{image_file.filename}')

                    # Rendering the result template with prediction and image details
                    return render_template('result.html', prediction=predicted_label, image_loc=image_url, class_description=class_description)

            return render_template('dashboard.html', user=user)

    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.html')

# User Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out successfully.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)