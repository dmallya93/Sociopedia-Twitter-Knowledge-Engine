import re, urllib

textfile = open("list_of_urls.txt","w")
textfile.close()
textfile = open("list_of_urls.txt","a")
def crawl(wish_url):
 
 #print "Enter the URL you wish to crawl.."
 #print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
 try :
  for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(wish_url).read(), re.I):
        print i 
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                if re.search("*\.html$",ee):
                 print ee
                 textfile.write(ee+'\n')
 except Exception,e:
  print str(e)

