import sqlite3

def getCardName(rand_num):
    query = f"SELECT Card_Name FROM Tarot_Card_Prediction WHERE Card_Num ={rand_num}"
    conn = sqlite3.connect('call-astro.db')
   
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall(); 
    conn.close()
    return rows[0][0]

def getCardImage(rand_num):
    query = f"SELECT Card_Image FROM Tarot_Card_Prediction WHERE Card_Num ={rand_num}"
    conn = sqlite3.connect('call-astro.db')

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall(); 
    conn.close()
    return rows[0][0]





def getCardPrediction(rand_num, bin_num, lang):
    if bin_num == 0:
        if lang == "eng":
            Prediction_col = "Prediction_Down_eng"
        else:
            Prediction_col = "Prediction_Down_hin"
    else:
        if lang == "eng":
            Prediction_col = "Prediction_Up_eng"
        else:
            Prediction_col = "Prediction_Up_hin"
    
    query = f"SELECT {Prediction_col} FROM Tarot_Card_Prediction WHERE Card_Num ={rand_num}"
    conn = sqlite3.connect('call-astro.db')
    print("Opened database successfully")
    cur = conn.cursor()
    cur.execute(query)
    print ("Table created successfully")
    rows = cur.fetchall(); 
    conn.close()
    # print(rows)
    # print(bin_num)
    return rows[0][0]



def getProperty(rand_num):
    data1 = []
    data1.append(" ")
    eventType = "Major Events"
    if rand_num >="0" and rand_num <="21" :
        # eventType = "Major Events"
        # experienceType = "Universal Human Experiences like: "
        data1 =["Major Events","Universal Human Experiences like: ", "Challenging Authorities","Fall in love", "Unexpected bad news"]
        
    elif rand_num >="22" and rand_num <="36":
        if rand_num >="22" and rand_num <="31":
            data1 =["Minor Events","Emotions & Relationship", "Represent Water Element","90% positive"]
        elif rand_num =="33":
            data1 =["Minor Events","Emotions & Relationship", "Represent Water Element","90% positive","Immaturity","Energetic","Youth","Indecisive"]
        elif rand_num =="34":
            data1 =["Minor Events","Emotions & Relationship", "Represent Water Element","90% positive","Mmaturity","Discipline","Decision Making"]
        elif rand_num =="35":
            data1 =["Minor Events","Emotions & Relationship", "Represent Water Element","90% positive","Emotions","Indecisive","Power to Influence Decision"]
        elif rand_num =="36":
            data1 =["Minor Events","Emotions & Relationship", "Represent Water Element","90% positive","Authority","Decision Making"]


    elif rand_num >="37" and rand_num <="50":
        if rand_num >="37" and rand_num <="46":
            data1 =["Minor Events","Thoughts","Represent Air Element","90% negative"]
        elif rand_num =="47":
            data1 =["Minor Events","Thoughts","Represent Air Element","90% negative","Immaturity","Energetic","Youth","Indecisive"]
        elif rand_num =="48":
            data1 =["Minor Events","Thoughts","Represent Air Element","90% negative","Mmaturity","Discipline","Decision Making"]
        elif rand_num =="49":
            data1 =["Minor Events","Thoughts","Represent Air Element","90% negative","Emotions","Indecisive","Power to Influence Decision"]
        elif rand_num =="50":
            data1 =["Minor Events","Thoughts","Represent Air Element","90% negative","Authority","Decision Making"]

    elif rand_num >="51" and rand_num <="64":
        if rand_num >="51" and rand_num <="60":
            data1 =["Minor Events","Karma/Action", "Represent Fire Element","50% positive"]
        elif rand_num =="61":
            data1 =["Minor Events","Karma/Action", "Represent Fire Element","50% positive","Immaturity","Energetic","Youth","Indecisive"]
        elif rand_num =="62":
            data1 =["Minor Events","Karma/Action", "Represent Fire Element","50% positive","Mmaturity","Discipline","Decision Making"]
        elif rand_num =="63":
            data1 =["Minor Events","Karma/Action", "Represent Fire Element","50% positive","Emotions","Indecisive","Power to Influence Decision"]
        elif rand_num =="64":
            data1 =["Minor Events","Karma/Action", "Represent Fire Element","50% positive","Authority","Decision Making"]

    else:
        if rand_num >="65" and rand_num <="74":
            data1 =["Minor Events","Materialistic-Money", "Represent Earth Element","90% positive"]
        elif rand_num =="75":
            data1 =["Minor Events","Materialistic-Money", "Represent Earth Element","90% positive","Immaturity","Energetic","Youth","Indecisive"]
        elif rand_num =="76":
            data1 =["Minor Events","Materialistic-Money", "Represent Earth Element","90% positive","Mmaturity","Discipline","Decision Making"]
        elif rand_num =="77":
            data1 =["Minor Events","Materialistic-Money", "Represent Earth Element","90% positive","Emotions","Indecisive","Power to Influence Decision"]
        elif rand_num =="78":
            data1 =["Minor Events","Materialistic-Money", "Represent Earth Element","90% positive","Authority","Decision Making"]

    return data1
