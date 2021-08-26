import json
import csv
csv_columns = ['TimeStamp', 'userid', 'qid', 'qcount', 'q1', 'q2',
               'q3', 'q4', 'total', 'message', 'hint_no', 'topic', 'level']

csv_file = "log.csv"

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        with open('/home/ubuntu/github_repos/ITS-Math/UserLog.log', 'r') as f:
            data = f.readlines()
            for line in data:
                sep = line.split("|")
                TS = sep[0]
                json_data = json.loads(sep[1])
                json_data["TimeStamp"] = TS
                writer.writerow(json_data)
except IOError:
    print(IOError)
