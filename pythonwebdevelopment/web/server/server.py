from flask import Flask,render_template,request
app = Flask(__name__)
import csv


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/<string:page_name>')
def index(page_name=None):
    return render_template(page_name)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
  if request.method=='POST':
    data=request.form.to_dict()
    print(data)
    write_to_file(data)
    write_to_csv(data)
    return render_template("thankyou.html")


#write file into flat datafile.
def write_to_file(data):
    with open('./static/document/database.txt',mode='a',newline='') as file:
        email,subject,message=data['email'],data['subject'],data['message']
        file.write(f'\n{email} | {subject} |{message}')

#write fiel into CSV
def write_to_csv(data):
     with open('./static/document/database.csv',mode='a',) as csvfile:
        email,subject,message=data['email'],data['subject'],data['message']
        csv_writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

