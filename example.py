import crawl
import post

post.install_opener()
post.login("dudups53@bol.com.br", "9d6ha5o4")	#modificar esta linha com dados corretos, da sua conta do fórum

threadids = crawl.getthreadids(57, 1)
nicks = []

for threadid in threadids:
	for page in range(0, 4):
		nicks.extend(crawl.getnicksfromthread(threadid, page+1))

nicks = list(set(nicks))

count = 0
for nick in nicks:
	post.sendpm(nick, "Estamos migrando para um novo fórum", "Iniciativa de usuários daqui.\n\n[color=black]0[/color]thers.createaforum.com\n\nLá há 
verdadeira liberdade de expressão, diferente deste fórum com sua ditadura do politicamente correto.\n\nAguardamos você lá.")
	count=count+1
	if count >= 500:
		print(count)
		break

if count < 500
	print(count)
