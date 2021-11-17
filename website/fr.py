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

        ok = db.child('sdsb4dnight').get()
        print(ok.val())
        db.child('sdsb4dnight').update({"prize1":"2544"})
        print(ok.val())


def akulaku():
        firebaseConfig={"apiKey": "AIzaSyDoiC-LuZbjxszNjC0I6_3tfIywmMpVrkc",
                "authDomain": "awesome-terra-87705.firebaseapp.com",
                "databaseURL": "https://awesome-terra-87705.firebaseio.com",
                "projectId": "awesome-terra-87705",
                "storageBucket": "awesome-terra-87705.appspot.com",
                "messagingSenderId": "480338185245"}

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

