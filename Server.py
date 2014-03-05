__author__ = 'OMID EBRAHIMI'

import web
import json
import urllib2

urls = (
    r'/services/stat/url=(.*)', 'get_stat',
)

app = web.application(urls, globals())


class get_stat:
    def GET(self, url):
        GPlusStat = GetGPlusStat(url)
        # return json.dumps(GPlusStat)
        return url


def GetGPlusStat(url):
    MainUrl = "https://clients6.google.com/rpc?key=AIzaSyCKSbrvQasunBoV16zDH9R33D88CeLr9gQ&quot;"
    http_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11",
        "Accept": "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Charset": "ISO-8859-1",
        "Content-type": "application/json",
    }
    data = '[{"method":"pos.plusones.get","id":"p","params":{"nolog":true,"id":"%s","source":"widget","userId":"@viewer","groupId":"@self"},"jsonrpc":"2.0","key":"p","apiVersion":"v1"}]' % url

    req = urllib2.Request(MainUrl, data, headers=http_header)
    result = urllib2.urlopen(req).read()

    return result


if __name__ == "__main__":
    app.run()