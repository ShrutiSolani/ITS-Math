import json
import csv
csv_columns = ['TimeStamp', "userid", "qid", "qcount", "startTime" , "endTime" , "levelofdifficulty","chapter",
"hintCount", "h1time","h2time","diffh1","diffh2","wrongCount","wronghintcount","score"]

csv_file = "log.csv"

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        with open('UserLog.log', 'r') as f:
            data = f.readlines()
            for line in data:
                sep = line.split("|")
                print(sep)
                TS = sep[0]
                json_data = json.loads(sep[1])
                json_data["TimeStamp"] = TS
                if(len(json_data.keys())==len(csv_columns)):
                    writer.writerow(json_data)
except IOError:
    print(IOError)
