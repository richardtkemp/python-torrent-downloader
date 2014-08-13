#!/usr/bin/python
# Script to recover my music library by RK
# Call with an m3u playlist as the argument,
# it will attempt to load torrents for the
# albums in the playlist.
#

# Two approaches: load all lines to a list, the work on.
# Else, iterate over the lines, check them as we add them to the set.

# Depends on https://github.com/mnussbaum/Quick-.Torrent-Downloader


import os	# needed to run qtd
import sys	# needed to get cli arguments
import pickle	# needed to save data structures to files simply


qtd		= "/home/rich/music recovery/qtd/git/src/qtd.py"

processedLog	= "/home/rich/music recovery/processed"
albumsLog	= "/home/rich/music recovery/albums"

playlist	= sys.argv[1]


def loadFile(file):
	print "Load lines from " + playlist + " into a set called lines.."
	lines = set(line.strip() for line in open(file))
	return lines
		
def extractPaths(input):
	print "Make set of paths from set of lines.."

	paths = []
	for line in input:
	    if "/" in line:
	        paths.append(line)
	return paths

def extractAlbums(paths):
	print "Make set of albums from set of paths.."
	albums = set()
	for path in paths:
	    print "Path " + path
	    name = path.split("/",3)
#	    print "Name " + name
	    term = name[0] + ' ' + name[1]
	    print "Term " + term
	    albums.add(term) #TODO is this correct?	        
	return albums
		
def download(searchterm):
	print "Download " + searchterm
	command = 'qtd.py -s "' + searchterm + '" -r "' + searchterm + '"'
	os.system(command)
	return
	
# can use this to do partials?
#try:
#    processedFile = open(processedLog,"r+")
#    processed = processedFile.readlines()

lines = loadFile(playlist)
paths = extractPaths(lines)
albums = extractAlbums(paths)
#pickle.dump(albums, albumsLog)

while (len(albums) != 0):
	album = albums.pop()
#	show = type(album)
#	print show
	download(album)

#OR
#for album in set albums
#	download(album)
	
	
	
	
