from flask import Flask, request, redirect, render_template
app = Flask(__name__)
todo_list={}
i=0
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
	
		new_item=todo_item(i, email, note, priority, done)
		todo_list[new_item.num]=[new_item.email,new_item.note,new_item.priority,new_item.done]
		
		return render_template("index.html", methods=["GET","POST"],todo_list=todo_list)
	else:
		return render_template('index.html')
if __name__=="__main__":
	app.run(debug=True)


