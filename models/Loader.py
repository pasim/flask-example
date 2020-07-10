import json
from models.Utility import Utility


class DataLoader:

    def __init__(self, dataFile=None):
        self.dataFile = dataFile

    def load_data(self):
        with open(self.dataFile) as f:
            data = json.load(f)
            sort = sorted(data, key=lambda i: i['name'])
            postcodes = [p['postcode'] for p in sort]
            try:
                results = Utility.load_postcode_data_multiple(postcodes)
                if results['status'] == 200:
                    arr = []
                    for f, b in zip(sort, results['result']):
                        if f['postcode'] == b['query']:
                            item = {'name': f['name'], 'postcode': f['postcode']}
                            if b['result'] is not None:
                                item['longitude'] = b['result']['longitude']
                                item['latitude'] = b['result']['latitude']
                            arr.append(item)
                    return arr
            except:
                pass

            return sort
