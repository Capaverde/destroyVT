import urllib.request
import re
from html.parser import HTMLParser


def getnicksfromthread(threadid, page):
	r = urllib.request.urlopen("http://forum.jogos.uol.com.br/_t_" + str(threadid) + "?page=" + str(page))
	mytext = r.read().decode("utf-8")
	mymatch = re.findall(r"class=\"userNickname\">\s*<a href=\"[^\"]+\">([^<]+)</a>", mytext)
	nicks = list(set(mymatch))
	return nicks

def gethtmltext(url):
	r = urllib.request.urlopen(url)
	mytext = r.read().decode("utf-8")
	return mytext

def getthreadids(forumid, page):
	r = urllib.request.urlopen("http://forum.jogos.uol.com.br/_f_" + str(forumid) + "?page=" + str(page))
	mytext = r.read().decode("utf-8")
	mymatch = re.findall(r"_t_(\d+)", mytext)
	threadlist = list(set(mymatch))
	return threadlist

#def getformsignature(url):	#todo
#	r = urllib.request.urlopen(url)
#	mytext = r.read().decode("utf-8")
#	forms = re.findall(r"<\s*form([^>]*)>(.+?)</form>", mytext)
#	for form in forms:
#		attributes = form[0]
#		body = form[1]
#		#...
