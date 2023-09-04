import sqlite3


def getMoolankPrediction(moolank,lang):
    if lang == "eng":
        lang_col = "Moolank_Prediction_eng"
    else:
        lang_col = "Moolank_Prediction_hin"
    
    query = f"SELECT {lang_col} FROM Moolank_Prediction WHERE Moolank={moolank}"
    conn = sqlite3.connect('call-astro.db')
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall(); 
    conn.close()
    return rows[0][0]


def getBhagyankPrediction(bhagyank,lang):
    if lang == "eng":
        lang_col = "Bhagyank_Prediction_eng"
    else:
        lang_col = "Bhagyank_Prediction_hin"
    
    query = f"SELECT {lang_col} FROM Bhagyank_Prediction WHERE Bhagyank={bhagyank}"
    conn = sqlite3.connect('call-astro.db')
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall(); 
    conn.close()
    return rows[0][0]