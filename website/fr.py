import pyrebase

def sdsb():
        firebaseConfig={"apiKey": "AIzaSyCnjwV66P7jDLx5A0Hlh7CHKoZ2tg9jmMY",
                "authDomain": "united-rope-233010.firebaseapp.com",
                "databaseURL": "https://united-rope-233010-default-rtdb.asia-southeast1.firebasedatabase.app",
                "projectId": "united-rope-233010",
                "storageBucket": "united-rope-233010.appspot.com",
                "messagingSenderId": "994050756260",
                "appId": "1:994050756260:web:4dee40c4ca0c34a1842031"}

        firebase=pyrebase.initialize_app(firebaseConfig)

        db=firebase.database()
        print(db.get())
        #ok = db.child('sdsb4dnight').get()
        #print(ok.val())
        #db.child('sdsb4dnight').update({"prize1":"2544"})
        #print(ok.val())


def akulaku():
        firebaseConfig ={"apiKey":"AIzaSyAlinPrAD7l3JS49ZqVNOebbweCyerBTWQ",
        "authDomain":"formula-1-1236.firebaseapp.com",
        "databaseURL":"https://formula-1-1236.firebaseio.com",
        "projectId":"formula-1-1236",
        "storageBucket":"formula-1-1236.appspot.com",
        "messagingSenderId":"782337978959",
        "appId":"1:782337978959:web:4a66738cc25744cabc303a",
        "measurementId":"G-D9BP6Y3R6M"}

        firebase=pyrebase.initialize_app(firebaseConfig)

        db=firebase.database()
        print(db.get())
        ok = db.get()
        print(ok.val())
        



def sdsbok():
        firebaseConfig={"apiKey": "AIzaSyCnjwV66P7jDLx5A0Hlh7CHKoZ2tg9jmMY",
                "authDomain": "united-rope-233010.firebaseapp.com",
                "databaseURL": "https://united-rope-233010-default-rtdb.asia-southeast1.firebasedatabase.app",
                "projectId": "united-rope-233010",
                "storageBucket": "united-rope-233010.appspot.com",
                "messagingSenderId": "994050756260",
                "appId": "1:994050756260:web:4dee40c4ca0c34a1842031"}

        firebase=pyrebase.initialize_app(firebaseConfig)

        db=firebase.database()

        ok = db.get()
        print(ok.val())
        
akulaku()

