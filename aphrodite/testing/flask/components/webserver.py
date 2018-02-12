from flask import Flask
import time

class webserver():
    def __init__(self):
        pass
    def runserver(self):
        
        
        app = Flask(__name__)
        infile = open('messages.txt')
        info = infile.read()
        info = str(info)
        infile.close
        
        @app.route("/")
        def hello():
            print(info)
            print('starting flask')
            

            return info
    
        app.run(debug=True, host='0.0.0.0', use_reloader=False)
        
