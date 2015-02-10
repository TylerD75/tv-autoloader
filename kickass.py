import urllib;
import urllib.parse;
import urllib.request;
import urllib.response;
import common_web;
import re;
import subprocess;
import ms_filehandler;

# http://kickass.to/usearch/the%20100%20720p/?field=time_add&sorder=desc  <-- Example search at kickass

def build_url(show_item):
    # Build show url
    show_string = '%s 720p' %show_item;												# Create search string
    show = urllib.parse.quote(show_string);											# Url encode the search string
    #base_url = 'http://kickass.so/usearch/%s/?field=time_add&sorder=desc' %show;
    base_url = 'http://kickass.so/usearch/%s/?field=seeders&sorder=desc' %show;		# Create the search URL
    return base_url;																# Return it

def filter_results(html):
    filter1 = '<a title="Torrent magnet link" href="(.*?)>';						# Create a regEx filter 
    regx = re.compile(filter1);														# As we have a variable in it, compile it
    html_list = re.findall(regx, html);												# Run the filter against the html code retrieved.
    return html_list;

# This code is very specialized for my own use, it will have to be changed to something useful for you:
def start_download(magnet, client):
    if client == 'remote':
        arguments = [];
        arguments.append('java');
        arguments.append('-jar');
        arguments.append('D:\\Program Files\\MagnetClient\\MagnetClient.jar');
        arguments.append(magnet);
		# The above code, created an argument list for use by the sub-process below.
		# This could be anything, like Vuze, or another torrent client, or like in my case:
		# my own application for handling magnets.
        result = subprocess.call(arguments);										# Call/Run the sub-process.
    if client == 'local':
		# This is another example of how one can use the data to start downloads in Vuze.
		# (On a linux system here).
        arg = [];
        arg.append('/usr/bin/vuze');
        arg.append(magnet);
        result = subprocess.call(arg);

def search_for_list(todays_showlist):
    dl_list = [];																	# Declare a list to contain debug output
    for show in todays_showlist:													# For each show to download...
        url = build_url(show);														# ...build url
        html = common_web.html_get(url);											# ...get html data from kickass
        filtered_results = filter_results(html);									# ...filter result
        save_string = show;															# (debug: create a show string for saving to file)
        save_string += ' -> ';														# (debug: add some stuff to save-string)
        save_string += filtered_results[0].split('"')[0];							# (debug: add the magnet:URI to save-string)
        dl_list.append(save_string);												# (debug: finish debug-save-string)
        start_download(filtered_results[0].split('"')[0], 'remote'); 				# ... do something with the magnet:URI
    ms_filehandler.save_todays_downloads(dl_list);									# (debug: save the debug data to file).