import requests
import pandas
import io

URL = 'https://download.bls.gov/pub/time.series/ap/ap.data.0.Current'
r = requests.get(url=URL)

if r.ok:
    raw_data = r.content.decode('utf8')
    raw_csv = pandas.read_csv(io.StringIO(raw_data), sep='\t')
    csv = raw_csv.drop_duplicates("series_id        ")
    print(csv)
