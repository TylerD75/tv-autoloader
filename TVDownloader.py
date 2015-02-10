import json;
import os;
import re;
import common_web;
import airdates;
import kickass;
import ms_filehandler;



def get_Showlist():
    sRawList = [];
    sList = [];
    series = os.listdir('D:\\media\\series\\');		# This has to be altered to your needs
    for n in series:
        sRawList.append(n);
        sList.append(common_web.proper_name(n));	# Change Series name from i.e. "Band_of_Brothers" to "Band of Brothers"
    return sList;									# Return complete list of shows.

my_shows = get_Showlist();
dl_shows = airdates.get_todays_shows(my_shows);
#ms_filehandler.save_todays_downloads(dl_shows);	# Saving todays shows to file, only a debug step
kickass.search_for_list(dl_shows);					# Start kickass search, and start downloading magnets
