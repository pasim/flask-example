import urllib.request
import json
import urllib.parse
from models.constants import URL_ROOT, OUT_CODES_ROOT
from app.app import DATA_DIR


class Utility:

    @staticmethod
    def load_postcode_data_single(postcode=""):

        """
            @see http://postcodes.io/docs
        """
        code = urllib.parse.quote(postcode)
        try:
            with urllib.request.urlopen(URL_ROOT + code) as url:
                data = json.loads(url.read().decode())
                if data['status'] == 200:
                    return data
        except:
            pass

        return None

    @staticmethod
    def load_postcode_data_multiple(postcodes=None):
        """
         @see http://postcodes.io/docs
        """
        data = {"postcodes" : postcodes}
        req = urllib.request.Request(URL_ROOT)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        json_data = json.dumps(data)
        json_data_as_bytes = json_data.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(json_data_as_bytes))
        with urllib.request.urlopen(req, json_data_as_bytes) as url:
            data = json.loads(url.read().decode())
            if data['status'] == 200:
                return data

        return None

    """
    Builds the functionality that allows you to return a list of stores in a given radius of a given postcode in the UK. 
    The list is ordered from north to south.
    """
    @staticmethod
    def nearest_outcodes(postcode="", radius=5000, sort=True):
        data = Utility.load_postcode_data_single(postcode)
        if data['status'] == 200:
            longitude = data['result']['longitude']
            latitude = data['result']['latitude']
            param = (('lon', longitude), ('lat', latitude), ('radius', radius))
            params = urllib.parse.urlencode(param)
            try:
                with urllib.request.urlopen(OUT_CODES_ROOT + '?' + params) as url:
                    data = json.loads(url.read().decode())
                    if data['status'] == 200:
                        with open(DATA_DIR + '/stores.json') as file:
                            js = json.load(file)
                            resulting = []
                            for item in data['result']:
                                for store in js:
                                    ps = store['postcode'].split()
                                    if ps[0] == item['outcode']:
                                        new = {'northings': item['northings'], 'outcode': item['outcode']}
                                        new['name'] = store['name']
                                        new['postcode'] = store['postcode']
                                        resulting.append(new)
                                        continue

                            # Adding extra argument
                            if sort:
                                return sorted(resulting, key=lambda i: i['northings'], reverse=True)
                            return resulting

            except:
                pass

            return None
