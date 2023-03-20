from flask import Flask ,redirect,url_for,render_template,request,session,flash
import sqlalchemy



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/user',methods=["GET","POST"])
def user():
    email=None
    if "user" in session:
        user=session["user"]
        if request.method == "POST":
            email=request.POST["email"]
            session['email']=email
        else:
            if "email" in session:
                email=session["email"]
        return render_template('user.html', email=email)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out","info")  
    session.pop("user",None)
    session.pop("email",None)
    return redirect(url_for("login"))

if __name__=="main":
    app.run(debug=True)

     












