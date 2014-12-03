import MySQLdb
import simplejson as json

def main():
  db=MySQLdb.connect("localhost","root","","MACHINELEARNING")
  cur=db.cursor()
  cur.execute("SELECT * FROM USERSHORTINF")
  f=open('titles.csv','w')
  f1=open('userinfo.csv','w')
  titles=dict()
  alread=dict()
  for row in cur.fetchall():
    f.write("username,userid,")
    features=row[4]
    features=features.split(',')
    for e in features:
      print "ORIGIN:"+e
      ie=e.split(':')
      if len(ie)>1:
        print ie[0]+":"+ie[1]
        if ie[0] not in alread:
          rin=raw_input("Input?\n")
          alread[ie[0]]=1
          if rin=='y':
            titles[ie[0]]=1
            f.write(ie[0]+',')
          else:
            continue  
    print row[3]
  print len(titles)
    #f.write(row[3]+"\n")
  db.close()

main()
