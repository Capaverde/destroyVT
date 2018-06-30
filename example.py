import crawl
import post

post.install_opener()
post.login("email@bol.com.br", "senha")	#modificar esta linha com dados corretos, da sua conta do fórum

threadids = crawl.getthreadids(57, 1)
nicks = []

for threadid in threadids:
	for page in range(0, 4):
		nicks.extend(crawl.getnicksfromthread(threadid, page+1))

nicks = list(set(nicks))

for nick in nicks:
	post.sendpm(nick, "0 thers.createaforum.com", "Fórum do Tidus.\n\n0 thers.createaforum.com\n\nRemova o espaço do link e cole-o na barra de endereços de seu navegador.")


