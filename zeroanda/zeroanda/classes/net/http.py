import requests
from zeroanda import utils

class Http:
    def get_csv_file(self, url):
        utils.info("Http.url: " + url)
        with requests.Session() as s:
            download = s.get(url)

            if "Content-Type" not in download.headers or download.headers['Content-Type'] != "text/csv":
                raise Exception("content type is not text/csv.")

            return download