from flask import Flask,jsonify, render_template, request, redirect, url_for, session, abort
import os
import sqlite3
import tarotHelper as th
import numerology as nl
import chaldeanNumerology as cn
import pythagorianNumerology as pn
import balanceNumber as bn
import maturityNumber as mn
import challengeNumber as chln
# import flask_login
app = Flask(__name__)
app.config['SECRET_KEY'] = "_user_id"
app.secret_key ='login'
# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)
# Our mock database.

# class User(flask_login.UserMixin):
    # pass
SITE_KEY ='6LfLq-InAAAAAHQXfK76bJtAoBGRKTZaZdpsPCaR'
SECRET_KEY = '6LfLq-InAAAAAN03gq3fYT-eWBSNoGrpFkHcNmI2'

@app.route('/')
def home():
    return render_template('login.html')


# @app.route('/')
# def home():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#         return "Helllo"
#     else:
#         return render_template('index.html')


# @login_manager.user_loader
# def user_loader(email):
#     equery = f"SELECT email from Login_Authentication WHERE email == '{email}' "
#     con = sqlite3.connect('call-astro.db')
#     cur = con.cursor()
#     cur.execute(equery)
#     db_email = cur.fetchall()
#     db_email = db_email[0][0]
#     if email != db_email :
#         return "Invalid Email"

#     user = User()
#     # user.id = email
#     return user


# @login_manager.request_loader   
# def request_loader(request):
#     email = request.form.get('email')
#     email = 'edukate151@gmail.com'
#     return user_loader(email)



# @app.route('/login', methods=['GET', 'POST'])
# def login5():
#     if request.method == 'GET':
#         return render_template('login.html')
#     email = request.form['email']
#     password = request.form['password']
#     equery = f"SELECT password from Login_Authentication WHERE email == '{email}' "
#     con = sqlite3.connect('call-astro.db')
#     cur = con.cursor()
#     cur.execute(equery)
#     db_password = cur.fetchall()
#     if len(db_password)==0:
#         return "Bad Login"
#     db_password = db_password[0][0]
#     print(db_password)

#     if db_password == password:
#         # print("Success")
#     # if email in users and request.form['password'] == users[email]['password']:
#         user = User()
#         user.id = email
#         flask_login.login_user(user)
#         return redirect(url_for('protected'))

#     return 'Bad login'

# @app.route('/logout')
# def logout():
#     # flask_login.logout_user()
#     session.pop('email',None)
#     return 'Logged out'

# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401

@app.route('/protected')
# @flask_login.login_required
def protected():
    #return 'Logged in as: ' + flask_login.current_user.id
    return render_template('index.html')

@app.route('/tarot')
def tarot():
    return render_template('tarot.html')

@app.route('/tarot-predict')
def tarot_predict():
    return render_template('tarot_predict.html')

    
@app.route('/tarot/<tarot_num>/<bin_num>')
def getTarotCard(tarot_num, bin_num):
    prediction_eng = th.getCardPrediction(tarot_num, bin_num,"eng")
    prediction_hin = th.getCardPrediction(tarot_num, bin_num,"hin")
    card_name = th.getCardName(tarot_num)
    card_image = th.getCardImage(tarot_num)
    property = th.getProperty(tarot_num)
    data ={
        'card_name': card_name,
        'card_image' : card_image,
        'property': property,
        'prediction_eng' : prediction_eng,
        'prediction_hin' : prediction_hin,
    }

    return jsonify(data)

@app.route('/numerology')
def numerology():
    return render_template('numerology.html')

@app.route('/numerology_prediction')
def numerology_prediction():
    return render_template('numerology_prediction.html')

# NumerologyPredictions


@app.route('/PredictionHistory/<userId>')
def get_Prediction_History(userId):
    query = f"SELECT * FROM Numerology_History where User_Id == '{userId}' "
    con = sqlite3.connect('call-astro.db')
    cur = con.cursor()
    cur.execute(query)
    data =cur.fetchall()
    print(data)
    return jsonify(data)

@app.route('/testNumerology', methods=['GET', 'POST'])
def testNumerology():
    if request.method == 'GET':
        return render_template('/numerology')
    name   = request.form['name']
    gender = request.form['gender']
    date = request.form['dob']
    time = request.form['tob']
    place = request.form['pob']
    userid = request.form['userid']

    valquery = f"SELECT * FROM Numerology_History WHERE User_Id == '{userid}' AND Name =='{name}' AND Gender == '{gender}' AND DOB== '{date}' AND TOB == '{time}' AND POB=='{place}'"
    con = sqlite3.connect('call-astro.db')
    cur= con.cursor()
    cur.execute(valquery)
    data = cur.fetchall()
    if(len(data)!=0):
        return redirect(url_for('numerology_prediction'))
    query = f"INSERT INTO Numerology_History (User_Id,Name,Gender,DOB, TOB, POB) VALUES ('{userid}','{name}','{gender}','{date}','{time}','{place}')"
    # print(query)
    cur.execute(query)
    con.commit()
    return redirect(url_for('numerology_prediction'))


@app.route('/numerology_prediction/<date_str>')
def calculate_moolank(date_str):
    # Function to calculate the sum of digits until a single-digit number is obtained
    def calculate_single_digit(num):
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num

    try:
        year, month, day= map(int, date_str.split('-'))
        # Check if the input date is valid
        if day <= 0 or month <= 0 or month > 12 or year <= 0:
            raise ValueError("Invalid date format")

        if day != 11 and day !=22 :
            # Calculate the Moolank for the day, month, and year
            moolank = calculate_single_digit(day)
            
        else:
            moolank = day

        moolank_month = calculate_single_digit(month)
        moolank_year = calculate_single_digit(year)
        if day==11 or day==22:
            moolank_t = calculate_single_digit(day)
        else:
            moolank_t = moolank
            
        total = moolank_t + moolank_month + moolank_year
        if total == 11 or total == 22 or total == 33: 
            bhagyank = total
        else:
            bhagyank = calculate_single_digit(moolank + moolank_month + moolank_year)
        
        Moolank_Prediction_eng = nl.getMoolankPrediction(moolank,"eng")
        Moolank_Prediction_hin = nl.getMoolankPrediction(moolank,"hin")

        Bhagyank_Prediction_eng = nl.getBhagyankPrediction(bhagyank,"eng")
        Bhagyank_Prediction_hin = nl.getBhagyankPrediction(bhagyank,"hin")

        data = [
            {
                'Moolank' : moolank ,
                'Moolank_Prediction_eng' : Moolank_Prediction_eng,
                'Moolank_Prediction_hin' : Moolank_Prediction_hin
            },

            {
                'Bhagyank' : bhagyank ,
                'Bhagyank_Prediction_eng' : Bhagyank_Prediction_eng,
                'Bhagyank_Prediction_hin' : Bhagyank_Prediction_hin
            },
        ]
        # print(data)
        return jsonify(data)

    except ValueError as e:
        return str(e)
    except Exception as e:
        return "Error: " + str(e)


# chladean Numebers
@app.route('/chaldean_numerology/<name>')
def find_chaldean_numerology(name):
    
    name = name.upper()
    name=name.replace(" ","")
    nameList =[x for x in name]
    # print(nameList)
    destiny_number = cn.getDestinyNumber(nameList)
    soul_number = cn.getSoulNumber(nameList)
    dream_number = cn.getDreamNumber(nameList)
    
    # print("Namank Chaldean Numbers: ")
    # print(destiny_number," ", soul_number," ",dream_number)

    data ={
        "destiny_number": destiny_number,
        "soul_number":    soul_number,
        "dream_number": dream_number
    }
    return jsonify(data)

# pythagorean numeology
@app.route('/pythagorean_numerology/<name>')
def find_pythagorean_numerology(name):
    name = name.upper()
    name = name.replace(" ","")
    nameList =[x for x in name]
    destiny_number = pn.getDestinyNumber(nameList)
    soul_number = pn.getSoulNumber(nameList)
    dream_number = pn.getDreamNumber(nameList)

    print("Namank Pyhagorean Numbers: ")
    print(destiny_number," ", soul_number," ",dream_number)
    
    data ={
        "destiny_number": destiny_number,
        "soul_number":    soul_number,
        "dream_number": dream_number
    }
    return jsonify(data)


# LoshuGrid_numeology
@app.route('/loshugrid_numerology/<date>')
def find_loshugrid(date):
    day, month, year= map(int, date.split('-'))
    # day1 = list(day).split('')

    # print(type(day))

    num =[]
    dayList = list(map(int, str(day)))
    monthList = list(map(int, str(month)))
    yearList  = list(map(int ,str(year)))

    num.extend(dayList)
    num.extend(monthList)
    num.extend(yearList)    
    # print(num)

    freq = {}
    for item in num:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    # for key, value in freq.items():
        # print("% d : % d" % (key, value))


    for f in range (10):
        if f in freq:
            # print(f, "is present")
            print("")
        else:
            freq[f] = "0"

    del freq[0]
    return jsonify(freq)


# pinnacle_number
@app.route('/pinnacle_number/<datestr>')
def pinnacle_number(date_str):
    def calculate_single_digit(num):
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num

    year, month, day= map(int, date_str.split('-'))
    # Check if the input date is valid
    if day <= 0 or month <= 0 or month > 12 or year <= 0:
        print("Invalid Date")
    
    first_pinnacle  = calculate_single_digit(day + month)
    second_pinnacle = calculate_single_digit(day + year)
    third_pinnacle =  calculate_single_digit(first_pinnacle + second_pinnacle)
    fourth_pinnacle = calculate_single_digit(month + year)

    data = {
        "first_pinnacle": first_pinnacle,
        "second_pinnacle": second_pinnacle,
        "third_pinnacle": third_pinnacle,
        "fourth_pinnacle": fourth_pinnacle,
    }
    return jsonify(data)


# balance_number
@app.route('/balance_number/<name>')
def balance_number(name):
    name = name.upper()
    numberList=[]

    nameList = name.split()
    for name in nameList:
        partName = name
        numberList.append(bn.calculate_balance_number(partName[0]))
    
    balance_number = sum(numberList)
    if balance_number>9:
        first_digit = balance_number%10
        second_digit = int(balance_number/10)
        balance_number = first_digit + second_digit
    # return "balance_number"
    return jsonify({"balance_number":f"{balance_number}"})

# karmic_number
@app.route('/karmic_number/<date_str>')
def karmic_number(date_str):
    def calculate_single_digit(num):
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num

    year, month, day= map(int, date_str.split('-'))
    # Check if the input date is valid
    if day <= 0 or month <= 0 or month > 12 or year <= 0:
        print("Invalid Date")
    
    karmic_number  = calculate_single_digit(day + month + year)
    if karmic_number == 4 or karmic_number == 5 or karmic_number == 7 or karmic_number ==1:
        return jsonify({"karmic_number": f"{karmic_number}"})
    
    return jsonify({"karmic_number": "NULL"})

# maturity_number
@app.route('/maturty_number/<name>/<dob>')
def calculate_maturity_number(name,dob):
    dob_parts = dob.split('-')
    day, month, year = int(dob_parts[2]), int(dob_parts[1]), int(dob_parts[0])
    life_path_number = sum(int(digit) for digit in str(day + month + year))

    while life_path_number > 9:
        life_path_number = sum(int(digit) for digit in str(life_path_number))

    name=name.replace(" ","")
    expression_number = mn.get_numerology_number(name)

    maturity_number = life_path_number + expression_number

    while maturity_number > 9:
        maturity_number = sum(int(digit) for digit in str(maturity_number))

    print(f"Your maturity number is: {maturity_number}")
    return jsonify({'maturity_number': maturity_number})

# challenge Number
@app.route('/challenge_number/<birth_date>')
def calculate_challenge_number(birth_date):
    birth_date = birth_date.replace("-", "")  # Removing hyphens from the date
    birth_date_digits = [int(digit) for digit in birth_date]
    life_path_number = chln.reduce_to_single_digit(sum(birth_date_digits))

    first_challenge = chln.reduce_to_single_digit(life_path_number + 1)
    second_challenge = chln.reduce_to_single_digit(life_path_number + 2)
    third_challenge = chln.reduce_to_single_digit(life_path_number + 3)
    fourth_challenge = chln.reduce_to_single_digit(life_path_number + 4)

    data={
        "first_challenge": first_challenge,
        "second_challenge": second_challenge,
        "third_challenge": third_challenge,
        "fourth_challenge": fourth_challenge,
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=8080,ssl_context=("cert.pem","key.pem"))
# if __name__ == "__main__":
# 	app.run(ssl_context='adhoc')
