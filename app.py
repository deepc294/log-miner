import os
from flask import Flask, flash, render_template, request, url_for
import pandas as pd
from flask import send_from_directory
app = Flask(__name__, static_folder="D:\Webanix\static")
app.config['UPLOAD_FOLDER'] = "D:\\Webanix\\Uploads"
app.config['EXPORT'] = "D:\\Webanix\\Export"

def csv_converter(file_name):
    Ip =[]
    Date =[]
    Time =[]
    with open ("Uploads/"+file_name) as f:
        content = f.readlines()

    for line in content:
        ip = line.split(" - - ")[0]
        date = line.split(" [")[1].split(" +0000]")[0].split(":")[0]
        time = line.split(" [")[1].split(" +0000]")[0].split("2015:")[1]
        Ip.append(ip)
        Date.append(date)
        Time.append(time)
        df = pd.DataFrame({'IP Address':Ip, 'Date':Date, 'Time':Time})
        df.to_csv('Export/final.csv', index=False, encoding='utf8')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
       file = request.files["file"]
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
       csv_converter(file.filename)
       return render_template("index.html", message = "Success",result='success',file_name=('http://localhost:5000/download/final.csv'))
    return render_template("index.html", message = "Awaiting Upload")

@app.route('/download/<file_name>')
def download_file(file_name):
    return send_from_directory(app.config["EXPORT"], file_name)


if __name__ == '__main__':
   app.run(debug=True)