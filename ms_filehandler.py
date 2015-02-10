import os;
import os.path;

# Simple file-saving for debug output...  Not used for anything critical.
def save_todays_downloads(list_of_downloads):
    saveFile = open('SeriesDB\\series.log', 'w');

    for name in list_of_downloads:
        name += '\n';
        saveFile.write(name);
    saveFile.close();