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

        ok = db.child('sdsb4dday').get()
        print(ok.val())
        db.child('sdsb4dday').update({"prize1":"3669"})
        print(ok.val())


def akulaku():
        firebaseConfig={"apiKey": "AIzaSyBt7SLd-WLlPpHQcIBlzOhhIbwIjH5Du6g",
                "authDomain": "akulaku-web-1a00b.firebaseapp.com",
                "databaseURL": "https://akulaku-web-1a00b.firebaseio.com",
                "projectId": "akulaku-web-1a00b",
                "storageBucket": "akulaku-web-1a00b.appspot.com",
                "messagingSenderId": "778102340676",
                "appId": "1:778102340676:web:1144ee501f24a8ca81d011"}

        firebase=pyrebase.initialize_app(firebaseConfig)

        db=firebase.database()

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

