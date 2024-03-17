from flask import Flask, render_template
from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():    
    return "<p>Hello world!</p>"

#LAATSTE REGELS CODE
if __name__ == '__main__':   
    app.run(port=5000,debug=True)