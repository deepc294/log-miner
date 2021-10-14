import pandas as pd

def csv_converter():
    Ip =[]
    Date =[]
    Time =[]
    with open ("access.log") as f:
        content = f.readlines()

    for line in content:
        ip = line.split(" - - ")[0]
        date = line.split(" [")[1].split(" +0000]")[0].split(":")[0]
        time = line.split(" [")[1].split(" +0000]")[0].split("2015:")[1]
        Ip.append(ip)
        Date.append(date)
        Time.append(time)
        df = pd.DataFrame({'IP Address':Ip, 'Date':Date, 'Time':Time})
        df.to_csv('final.csv', index=False, encoding='utf8')

