from flask import Flask, render_template, request, redirect, url_for
# You will likely need a database e.g. DynamoDB so you might either boto3 or pynamodb
# Additional installs here:
import pynamodb
import pytest

app = Flask(__name__)

## Instantiate your database here:
#
#
#


@app.route("/")
def home():
    # Complete the code below
    # The todo_list variable should be returned by running a scan on your DDB table,
    # which is then converted to a list
    from pynamodb.models import Model
    from pynamodb.attributes import UnicodeAttribute, BooleanAttribute

    class TodoItem(Model):
        class Meta:
            table_name = "accad6-assessment-db"  
            region = "ap-southeast-1"  

        id = UnicodeAttribute(hash_key=True)
        title = UnicodeAttribute()
        completed = BooleanAttribute(default=False)

    
    try:
        todo_list = list(TodoItem.scan())
    except:
        todo_list = []  

    # can leave this line as is to use the template that's provided
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    pass
    # title = request.form.get("title")
    # Complete code below to create a new item in your todo list


    # return redirect(url_for("home"))



@app.route("/update/<todo_id>")
def update(todo_id):
    pass
    # Complete the code below to update an existing item
    # For this particular app, updating just toggles the completion between True / False


    # return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    pass
    # Complete the code below to delete an item from the to-do list


    # return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)