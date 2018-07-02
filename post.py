import urllib.request
import urllib.parse
import http.cookiejar
import re

def login(email, password):
	data = urllib.parse.urlencode({"user" : email, "pass" : password, "skin" : "", "dest" : "REDIR|http://forum.jogos.uol.com.br/"})
	data = data.encode('ascii')
	r = urllib.request.urlopen("https://acesso.uol.com.br/login.html", data)
	return r

def gettoken():
	r = urllib.request.urlopen("http://forum.jogos.uol.com.br/new.jbb")
	mytext = r.read().decode('utf-8')
	mymatch = re.search(r"token\" value=\"(\d+)", mytext)
	return mymatch.group(1)

def sendpm(dest, subject, body):
	data = urllib.parse.urlencode({"token" : gettoken(), "userId" : "", "pm.text" : "", "username" : dest, "pm.topic" : subject, "message" : body});
	data = data.encode('ascii')
	try:
		r = urllib.request.urlopen("http://forum.jogos.uol.com.br/send.jbb", data)
		return r
	except:
		return 0

def gettoken2(forumid):
	r = urllib.request.urlopen("http://forum.jogos.uol.com.br/new_topic.jbb?forum.id=" + str(forumid))
	mytext = r.read().decode("utf-8")
	mymatch = re.search(r"token\" value=\"(\d+)", mytext)
	if mymatch:
		return mymatch.group(1)
	else:
		return -1

def createthread(forumid, subject, message):
	data = urllib.parse.urlencode({"token" : gettoken2(forumid), "topic.forum.id" : forumid, "subject" : subject, "message" : message})
	data = data.encode("ascii")
	r = urllib.request.urlopen("http://forum.jogos.uol.com.br/insert_topic.jbb", data)
	return r


def posttothread(threadid, message):	#incorreto, em construção
	data = urllib.parse.urlencode({"token" : 0, "topic.id" : threadid, "message" : message})
	data = data.encode("ascii")
	r = urllib.request.urlopen("http://forum.jogos.uol.com.br/insert_post.jbb", data)
	return r

def install_opener():
	cj = http.cookiejar.CookieJar()
	cp = urllib.request.HTTPCookieProcessor(cj)
	opener = urllib.request.build_opener(cp)
	urllib.request.install_opener(opener)


"""self.browser.open(&#39;http://forum.jogos.uol.com.br/dwr/call/plaincall/PostFunctions.insertPost.dwr&#39;, 
&quot;callCount=1\npage=/undervick_t_
&quot; + str(thread) + &quot;\nhttpSessionId=&quot; + str(self.httptoken) + &quot;\nscriptSessionId=
&quot; + self.get_token() + &quot;\nc0-scriptName=PostFunctions\nc0-methodName=insertPost\
nc0-id=0\nc0-param0=number:&quot; + str(thread) + &quot;\nc0-param1=string:&quot; + urllib.quot
e(message) + &quot;\nbatchId=0&quot;).read())"""
