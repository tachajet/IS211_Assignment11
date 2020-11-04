from flask import Flask, request, redirect, render_template
app = Flask(__name__)
email_adds=[]
@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)
@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_adds.append(email)
    print(email_adds)
    return redirect('/')
@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_adds=email_adds)


if __name__ == "__main__":
    app.run()
