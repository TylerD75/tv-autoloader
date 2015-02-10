This is my first Python project ever, so please be gentle in your critique. 
Some things are bound to be more complicated than it has to be.  And error handeling
is completely missing, so feel free to adapt and improve, and please contact me
if you do so, and I'll give access for further development if anyone is interested.

As you might have guessed, this is not my main application, but it's used by another Java
application that uses the data retrieved by this python code (the magnet:URIs).

This can easily be adapted to download torrent files if needed, but that's beyond my own needs.

To use these scripts, you have to adapt them to your own needs, but that should not be too hard,
as python is surprisingly readable (don't understand why I haven't had a look at it before now).

The inner workings:
  1. The TV-Downloader.py script checks a given folder structure, like:
    <Main Series Folder>
	  |-> Series 1 (i.e. The Big Bang Theory)
	  |-> Series 2 (i.e. 12_Monkeys_(2015) )
	  |-> Series 3 etc...
	  
	Each series should follow, what might be called the XBMC standard, i.e. "Series_name_(YEAR)".
	The script will handle both " ", and "_" as word separators, but I've focused on "_", as
	this is what I've used.
	
  2. Then we check airdates.tv, and filter out all but the shows that aired yesterday.
    This list is then compared to the folder list we got in step 1.
	What we're left with is a list of shows in the folder structure, that were aired yesterday.
	The reason I've chosen to focus on yesterdays shows, is that if a show haven't been uploaded
	yet, you'll end up with last weeks episode, as this script is a hard-worker, but not a very
	intelligent one ;)
	
  3. This might be a murky step, as we download magnet uri's from kickass.to (the URL changes
	 from time to time, which breaks the script, but it's easy to change URL).
	 The list from step 2 is sent to the kickass.py script, which then builds kickass search
	 urls.  Each of these are used to filter against series title, season number and episode
	 number, in addition to encoding quality (720p in my case), and ordered by upload date
	 (as ordering based on number of seeds will probably fail).
	 
	 What we're left with is the magnet:uri for each episode we're interested in.
	 Now, what YOU do with this, is up to you?
	 
	 Some suggestions:
	   1. Start Vuze with the magnet:uri as argument, this will add the download to the download queue.
	   2. Store the magnet:URI in a file, for later...
	   3. Send the magnet:URI to another i.e. Java application (as I have done in this script).
	      This step is something you have to change if you intend to use this script, as it's specialized
		  towards my needs.
		  
File and folder descriptions:
	README.txt			-> This file.
	TVDownloader.py 	-> Main executable that binds it all together.
	common_web.py		-> Common web functionality.
	ms_filehandler.py	-> Filehandler for finding folder structure (Windows folder structure used here).
	airdates.py			-> Functions for checking airdates.tv, and filtering output.
	kickass.py			-> Functions for searching kickass.to, and filtering responses.
	Series_DB			-> Temp folder for storing logs.  Mainly used for debug.
	TVShows.py			-> One monolithic script which includes all above functionality.  
							This made debugging my third party application a lot easier.
							
Disclaimer:
  I know this could be used to start illegal downloads of TV-Series, but please only download episodes of series you own.
  I hold no responsibility to what others might do with these scripts, as all it does is downloading Magnet:URIs which in
  itself contains no copyrighted materials.