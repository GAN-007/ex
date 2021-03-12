from flask import Flask,request,render_template,url_for,make_response,session,redirect

app=Flask(__name__)
app.secret_key='1234'

"""this is sessions"""

@app.route('/login/<guest>',methods=['GET','POST'])
def login(guest):
    session['guest'] = guest
    return redirect(url_for('welcome'))


@app.route('/welcome',methods=['GET','POST'])
def welcome():
  
    return render_template('welcome.html',guest=session['guest'])



  
"""_________________________________________"""
  



@app.route('/user',methods=['GET','POST'])
def user():
   user_name=input('name')  
   password=input('password')
   if request.form['user_name'] != user_name:
        return render_template("movie.html",msg="Check user_name and retry")
   else:
        return  render_template("movie.html",msg="Welcome %s as User")   

   if request.form['password'] != password:
         return render_template("error.html",msg="Check password and retry")
   else:
         return  render_template("movie.html",msg="Welcome %s as User")   

   return render_template("welcome.html",user_name=user_name)



"""____________________movies_______________________"""

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
       result=request.form
       return render_template('movies.html' , result=result) 
    else:
        return redirect(url_for('error.html'))   




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)