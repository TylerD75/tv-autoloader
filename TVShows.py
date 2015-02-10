import os;
import os.path;
import re;
import time;
import urllib;
import urllib.parse;
import urllib.request;
import urllib.response;
import subprocess;
from datetime import date, timedelta;

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

def get_Showlist():
    sRawList = [];
    sList = [];
    series = os.listdir('M:\\series\\all\\');
    for n in series:
        sRawList.append(n);
        sList.append(proper_name(n));
    return sList;
# ------------------------------------------------------ Beginning of Airdates
def get_date():
    #today = date.fromtimestamp(time.time());
    yesterday = date.today() - timedelta(1);
    yesterday.strftime('%Y%m%d');
    datoo = str(yesterday).split('-');
    dato = '%s%s%s' %(datoo[0], datoo[1], datoo[2]);
    return dato;

def airdates_filter_results(html):
    filt_list = [];
    today = get_date();
    filt_list.append('<div class="day" data-date="%s">(.*?)<div class="day" data-date=' %today);
    filt_list.append('<div class="title">(.*?)</div>');
    f1 = re.compile(filt_list[0]);
    f2 = re.compile(filt_list[1]);
    filter1 = re.findall(f1, html);
    filter2 = re.findall(f2, str(filter1));
    return filter2;

def get_todays_shows(complete_showlist):
    html = html_get('http://www.airdates.tv');
    # Check out: http://www.pagecolumn.com/tool/all_about_html_tags.htm
    final_list = airdates_filter_results(html);
    todays_shows = [];
    for n in final_list:
        for s in complete_showlist:
            if s in n:
                todays_shows.append(n);
    return todays_shows;
# --------------------------------------------------------- END OF Airdates
# --------------------------------------------------------- Beginning of filehandler
def save_todays_downloads(list_of_downloads):
    saveFile = open('SeriesDB\\series.log', 'w');

    for name in list_of_downloads:
        name += '\n';
        saveFile.write(name);
    saveFile.close();

# ------------------------------------------------------- Beginning of kickass:
def build_url(show_item):
    # Build show url
    show_string = '%s 720p' %show_item;
    show = urllib.parse.quote(show_string);
    #base_url = 'http://kickass.so/usearch/%s/?field=time_add&sorder=desc' %show;
    base_url = 'http://kickass.to/usearch/%s/?field=seeders&sorder=desc' %show;
    return base_url;

def filter_results(html):
    filter1 = '<a title="Torrent magnet link" href="(.*?)>';
    regx = re.compile(filter1);
    html_list = re.findall(regx, html);
    return html_list;

def start_download(magnet, client):
    if client == 'remote':
        arguments = [];
        arguments.append('java');
        arguments.append('-jar');
        arguments.append('D:\\Program Files\\MagnetClient\\MagnetClient.jar');
        arguments.append(magnet);
        result = subprocess.call(arguments);
    if client == 'local':
        arg = [];
        arg.append('/usr/bin/vuze');
        arg.append(magnet);
        result = subprocess.call(arg);

def search_for_list(todays_showlist):
    dl_list = [];
    for show in todays_showlist:
        url = build_url(show);
        html = common_web.html_get(url);
        filtered_results = filter_results(html);
        save_string = show;
        save_string += ' -> ';
        save_string += filtered_results[0].split('"')[0];
        dl_list.append(save_string);
        start_download(filtered_results[0].split('"')[0], 'remote'); # client can be local or remote
    save_todays_downloads(dl_list);


complete_show_list = get_Showlist();
todays_downloads = get_todays_shows(complete_show_list);
#save_todays_downloads(todays_downloads);
kickass.search_for_list(todays_downloads);