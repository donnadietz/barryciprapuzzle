import os

def makeapage(n):
    fyle=open('page'+str(n+1)+'.html','w')
    headerblurb='''<!doctype html public "-//W3C//DTD HTML 4.0 Transitional//EN">\n<html><head>\n<title> Barry Cipra's Puzzle: 7040 Magic Tori </title>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">\n</head>\n<body>\nMagic Tori PAGE '''
    fyle.write(headerblurb)
    fyle.write(str(n+1)+"<br>\n")
    navigation='<a href="page'+str(n)+'.html">previous page</a> <a href="page'+str(n+2)+'.html">next page</a><br>\n'
    fyle.write(navigation)
    for i in range(n*600+1, n*600+601):
        lyne='<a href="magic'+str(i)+'.jpg"> <img src="magic'+str(i)+'.jpg" width=200></a>\n'
        fyle.write(lyne)
    fyle.write('</body></html>')
        
