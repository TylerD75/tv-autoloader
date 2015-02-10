import urllib;
import urllib.parse;
import urllib.request;
import urllib.response;
import common_web;
import re;
import time;

from datetime import date, timedelta;

# http://www.airdates.tv/

def get_date():
    #today = date.fromtimestamp(time.time());			# If we were interested in shows aired today...
    yesterday = date.today() - timedelta(1);			# Only interested in show aired yesterday.
    yesterday.strftime('%Y%m%d');						# Airdate.tv uses a date format like "20150230"
    datoo = str(yesterday).split('-');					# so we need a bit of variable munching
    dato = '%s%s%s' %(datoo[0], datoo[1], datoo[2]);	# Producing the actual date here
    return dato;										# ...and returning it to sender

def filter_results(html):
    filt_list = [];
    today = get_date();
    filt_list.append('<div class="day" data-date="%s">(.*?)<div class="day" data-date=' %today);
    filt_list.append('<div class="title">(.*?)</div>');
    f1 = re.compile(filt_list[0]);						# Compiling a couple of regEx filters, to filter airdate results.
    f2 = re.compile(filt_list[1]);
    filter1 = re.findall(f1, html);						# First filtering: finds all episodes from yesterday to the next date
    filter2 = re.findall(f2, str(filter1));				# Second filtering: filter out each episode title.
    return filter2;										# Return a html-blob of all aired episodes of yesterday.

def get_todays_shows(complete_showlist):
    html = common_web.html_get('http://www.airdates.tv');
    # Check out: http://www.pagecolumn.com/tool/all_about_html_tags.htm
    final_list = filter_results(html);
    todays_shows = [];									# Let's prepare a list to contain all episodes we want.
    for n in final_list:								# For each episode aired yesterday, do:
        for s in complete_showlist:						# ... for each episode we have, do: (could most definitely be improved)
            if s in n:									# IF (my_show_name) is in (aired_show_name):
                todays_shows.append(n);					#  ...then it's a show I'm interested in, so add it to download_list
    return todays_shows;								# Return the list of shows we're interested in.