import MySQLdb
import simplejson as json

def main():
  db=MySQLdb.connect("localhost","root","","MACHINELEARNING")
  cur=db.cursor()
  cur.execute("SELECT * FROM USERSHORTINF")
  f1=open('titles.csv','r')
  f=open('userinfo.csv','w')
  line=f1.readline()
  titles=line.split(",")
  #print len(titles)
  for row in cur.fetchall():
    f.write(row[1]+","+row[2]+",")
    features=row[4][1:-1]
    for t in titles:
      index=features.find(t)
      if index!=-1:
        s1=features[index:]
        s1=s1.split(",")
        s1=s1[0].split(":")
        if len(s1)>1:
          s1=s1[1]
          #print s1
          f.write(s1+",")
        else:
          f.write(" ,")
      else:
        f.write(" ,")  
    #print row[3]
    #break
    f.write(row[3]+"\n")
  db.close()

main()
