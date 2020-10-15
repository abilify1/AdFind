# -*- coding: utf-8 -*-
import requests, os, sys, time
from multiprocessing.pool import ThreadPool
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
r= requests.Session()
def find(y):
    try:
     kont=requests.get(sys.argv[1]+y,timeout=10)
     if kont.status_code < 200 or kont.status_code <= 201:
      print "%s[%s!%s] %s%s ===> %sFound"%(pu,qu,pu,sys.argv[1],y,hi)
      open("hasil.txt","a+").write(sys.argv[1]+y)
     else:
      print "%s[%s!%s] %s%s ===> %sNot Found"%(pu,qu,pu,sys.argv[1],y,me)
    except:
      pass

try:
  os.system("clear")
  print """%s
     _       _ _____ _           _  
    / \   __| |  ___(_)_ __   __| | %sAuthor by abilseno11%s
   / _ \ / _` | |_  | | '_ \ / _` | %sGithub github.com/AbilSeno%s
  / ___ \ (_| |  _| | | | | | (_| | %sTeam anoncybfakeplayer%s
 /_/   \_\__,_|_|   |_|_| |_|\__,_| %sAdmin Login Finder"""%(qu,pu,qu,pu,qu,pu,qu,qu)
  sys.argv[1]
  print
  ThreadPool(30).map(find,open("list.txt").read().splitlines())
  print "\n%s[%s✓%s] %sDone, file saved in %shasil.txt"%(pu,qu,pu,pu,ku)
except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] %sCheck your internet'%(W0,R0,W0,W0))
except IndexError:
        exit('%s[%s!%s] Use : python2 %s https://domain.com'%(W0,R0,W0,sys.argv[0]))
except KeyboardInterrupt:
        exit('\n%s[%s!%s] %sClosing...'%(W0,R0,W0,W0))
