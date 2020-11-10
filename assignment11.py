from flask import Flask, request, redirect, url_for, render_template
import re
app = Flask(__name__)
#Initiating the to do list dictionary and key variables
todo_list={}
i=0
#Regular expression to validate email addresses
email_reg=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

def validate_email(email):
	if re.search(email_reg,email):
		return True
	else:
		return False
class todo_item:
	def __init__(self, num, email, note, priority, done):
		self.num=num
		self.email=email
		self.note=note
		self.priority=priority
		self.done=done
@app.route('/', methods=["GET", "POST"])
def start():
	return render_template('index.html')
@app.route('/submit', methods=["GET","POST"])
def submit():
	if request.method == 'POST':
		global i
		i+=1
		email=request.form["email"]
		note=request.form["note"]
		priority=request.form["priority"]
		done=request.form["done"]
		if validate_email(email):
			new_item=todo_item(i, email, note, priority, done)
			todo_list[new_item.num]=[new_item.email,new_item.note,new_item.priority,new_item.done]
		
			return render_template("index.html", methods=["GET","POST"],todo_list=todo_list)
		else:
			email="Not a valid email address!"
			note="invalid"
			priority="invalid"
			done="invalid"
			new_item=todo_item(i, email, note, priority, done)
			todo_list[new_item.num]=[new_item.email,new_item.note,new_item.priority,new_item.done]
		
			return render_template("index.html", methods=["GET","POST"],todo_list=todo_list)
	else:
		return render_template('index.html')
@app.route('/clear', methods=["GET","POST"])
def clear():
	global todo_list
	todo_list={}
	return redirect(url_for('start'))
@app.route('/delete', methods=["GET","POST"])
def delete_item():
	"""Function to delete an individual list entry
	"""
	delete_key=request.form["delete_key"]
	del todo_list[int(delete_key)]
	return render_template("index.html",methods=["GET","POST"],todo_list=todo_list)
if __name__=="__main__":
	app.run(debug=True)


