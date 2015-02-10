import urllib;
import urllib.parse;
import urllib.request;
import urllib.response;

def html_get(url):
    headers = {};
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36';

    request = urllib.request.Request(url, headers=headers);
    response = urllib.request.urlopen(request);
    retVal = str(response.read());
    return retVal;

def proper_name(rawName):
    if rawName.find('_') != -1:                        # If '_' exists (index is something other than -1)
        nameList = rawName.split('_');
        str = " ";
        retVal = str.join(nameList);
    else:
        # Assuming " " to be separator, or there's no sep available (i.e. "24")
        retVal = rawName;
    return retVal;