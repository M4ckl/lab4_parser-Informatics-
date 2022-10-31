import pandas as pd


def jsoncsvparser(json_file):
    json_file = pd.read_json('json_file.json', orient='index')
    csv_file = json_file.to_csv(index=False)
    print(csv_file)


jsoncsvparser(json_file='json_file.json')