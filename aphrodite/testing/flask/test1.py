from flask import Flask
import time

class webserver():
    def __init__(self, info):
        self.info = info
    def runserver(self):
        app = Flask(__name__)
        print(self.info)
        
        @app.route("/")
        def hello():
            print('test')
            print(self.info)
            print('starting flask')
            

            return self.info
    
        app.run(debug=True, host='0.0.0.0', use_reloader=False)

