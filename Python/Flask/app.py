from flask import Flask,request,redirect,url_for,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome page"

@app.route('/login',methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        username=request.form['uname']
        password=request.form['pass']
    
    return render_template('login.html',username=username)
    # return f'welcome {username}'

@app.route('/admin/<name>')
def admin(name):
    return render_template('index.html',name=name)

@app.route('/librarion')
def librarion():
    return "Librarion section"

@app.route('/student')
def student():
    return "Student Section"

# @app.route('/user/<name>')
# def user(name):
#     if(name=='admin'):
#         return redirect(url_for('admin'))
#     if(name=='librarion'):
#         return redirect(url_for('librarion'))

#     if(name=='student'):
#         return redirect(url_for('student'))


# @app.route('/demo/<name>')
# def demo(name):
#     return "Demo "+name

if __name__ =="__main__":
    app.run(debug=True)
