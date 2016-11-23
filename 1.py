import poplib
server="pop.sina.com"
pop=poplib.POP3(server.110)
pop.user(user)
auth=pop.pass_(passwd)
if auth.split('')[0]=="+OK":
    pring user,passwd