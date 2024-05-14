from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")



@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def file(data):
    with open("database.txt", mode = "a") as database:
        email_ = data["email"]
        subject_ = data["subject"]        
        message_ = data["message"]

        file = database.write(f"\nEmail: {email_}      ,Subject: {subject_}    ,Message: {message_}")


def filecsv(data):
    with open("database2.csv", newline='', mode = "a") as database2:
        email = data["email"]
        subject = data["subject"]        
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        filecsv(data)
        return redirect("/thankyou.html")
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('submit_form.html', error=error)   
    else:
        return "Something went wrong!" 



@app.route('/about.html')
def my_about():
    return render_template("about.html") 



@app.route('/works.html')
def my_works():
    return render_template("works.html")


@app.route('/contact.html')
def my_contact():
    return render_template("contact.html")



@app.route('/components.html')
def my_components():
    return render_template("components.html")    