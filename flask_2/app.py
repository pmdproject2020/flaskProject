from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/answer',methods=["POST","GET"])
def Answer():
  if request.method=="POST":
    return render_template
  return render_template('index.html')
  
if __name__=="__main__":
  app.run()
