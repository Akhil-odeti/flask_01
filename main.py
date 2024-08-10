# rander_templete is used to access or create a tamplete

from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__) # wsgi

@app.route("/")
def name():
    return render_template("index.html")
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = " PASS"
    else:
        res ="FAIL"
    return render_template("result.html",result = res)


@app.route("/fail/<int:score>")
def fail(score):
    return ("the person has failed in the subject with the marks " + str(score))

@app.route("/result/<int:marks>")
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    return (redirect(url_for(result,score = marks)))
## how to read the posted values ?? answer is request library
@app.route("/submit",methods = ["POST","GET"])
def submit():
    total_score = 0
    list = []
    if request.method == "POST": 
        python = float(request.form["python"]) # by default is it int we convert into float
        # request.form["python"] this python is in html in name 
        list.append(python)
        AI =  float(request.form["AI"])
        list.append(AI)
        powerBI = float(request.form["powerBI"])
        list.append(powerBI)
        ML = float(request.form["ML"])
        list.append(ML)
        total = sum(list)
        length = len(list)
        mini = min(list)
        if mini >= 40:
            total_score = total/length
        else:
            total_score = mini 
           
        return (redirect(url_for("success",score = total_score)))

    
    
     
if __name__ == "__main__":
    app.run(debug=True)