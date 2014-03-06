__author__ = 'OMID EBRAHIMI'

import web
import json
import urllib2

urls = (
    r'/services/stat', 'get_stat',
)

app = web.application(urls, globals())


class get_stat:
    def GET(self):
        receivedData = web.input(url='')
        url = web.websafe(receivedData.url)
        if url!='':
            GPlusStat = GetGPlusStat(url)
            PinterestStat = GetPinterestStat(url)
            FaceResult = GetFaceResult(url)
            TwitterStat = GetTwitterStat(url)
            LinkedInStat = GetLinkedInStat(url)

            TotalStat = 0
            if GPlusStat != 'Error':
                TotalStat += GPlusStat
            if PinterestStat != 'Error':
                TotalStat += PinterestStat
            if FaceResult != 'Error':
                TotalStat += FaceResult
            if TwitterStat != 'Error':
                TotalStat += TwitterStat
            if LinkedInStat != 'Error':
                TotalStat += LinkedInStat

            result = {'GPlus': GPlusStat, 'Pinterest': PinterestStat, 'Facebook': FaceResult, 'Twitter': TwitterStat,
                      'LinkedIn': LinkedInStat, 'Total': TotalStat}

            return json.dumps(result)
            # return url
        else:
            f = open('statService.wsdl', 'r')
            return f.read()


def GetGPlusStat(url):
    try:
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

        return json.loads(result)[0]['result']['metadata']['globalCounts']['count']
    except:
        return 'Error'


def GetPinterestStat(url):
    try:
        MainUrl = "http://api.pinterest.com/v1/urls/count.json?&url=" + url
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(MainUrl, headers=headers)
        result = urllib2.urlopen(req).read()

        #  ============ Pinterst return result as below  =============================
        #  receiveCount({"count": 0, "url": "http://t.co/dtEdGb7Ttq"})
        #  ============ Pinterst return result as below  =============================

        #  ============ We remove receiveCount() from the result ====================
        result = result.replace("receiveCount(", "").replace(")", "")
        #  ============ We remove receiveCount() from the result ====================

        return json.loads(result)["count"]
    except:
        return 'Error'


def GetFaceResult(url):
    try:
        MainUrl = "http://graph.facebook.com/fql?q=SELECT%20total_count%20FROM%20link_stat%20WHERE%20url=%27" + url + "%27";
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(MainUrl, headers=headers)
        result = urllib2.urlopen(req).read()

        return json.loads(result)['data'][0]['total_count']
    except:
        return 'Error'


def GetTwitterStat(url):
    try:
        MainUrl = "http://urls.api.twitter.com/1/urls/count.json?url=" + url
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(MainUrl, headers=headers)
        result = urllib2.urlopen(req).read()
        return json.loads(result)['count']
    except:
        return 'Error'


def GetLinkedInStat(url):
    try:
        MainUrl = "http://www.linkedin.com/countserv/count/share?format=json&url=" + url
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(MainUrl, headers=headers)
        result = urllib2.urlopen(req).read()
        return json.loads(result)['count']
    except:
        return 'Error'


if __name__ == "__main__":
    app.run()