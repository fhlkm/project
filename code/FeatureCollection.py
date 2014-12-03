import MySQLdb
import ConfigParser
import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
import json
from networkx.algorithms import centrality
from TwitterAPI import TwitterAPI
conn = MySQLdb.connect(host="localhost",user="hanlu",passwd="root",db="MACHINELEARNING")
cursor = conn.cursor()
# sql= "INSERT INTO USERINF (Info)VALUES(\"DFSDFDSF\")"
# cursor.execute(sql)
# conn.commit()


class singleuser:
    id ="0";
    name =""
    number =0
    friends=[]
    features=[]
    def setfeatures(self, f):
        self.features =f
    def setfriends(self, fd):
        self.friends = fd
        self.number = len(fd)
    def setid(self,_id):
        self.id =_id;
    def setname(self,_name):
        self.name = _name

    def setnumber(self, nm):
        self.number=nm

username ="HanluFeng"
userpassword ="123456"
usr = singleuser()
f=[]
f.append("f1")
fr=[]
fr.append("friend")
fr.append("friend2")

usr.setname(username)
usr.setfeatures(f)
usr.setfriends(fr)
usr.setfeatures(f)
usr.setid(userpassword)
def sqlInsert(usr):
    # sql= "INSERT INTO USERINF (Info)VALUES(\"DFSDFDSF\")"
    name = usr.name.encode('utf-8').strip()
    friends=u",".join(usr.friends).encode('utf-8').strip()
    # features=u",".join(usr.features).encode('utf-8').strip()
    features= (str(usr.features)).encode('utf-8').strip()
    features = MySQLdb.escape_string(features)
    number = str(usr.number)

    sql= "INSERT INTO USERSHORTINF VALUES(\"sfsfs\","+"\""+name+"\","+"\""+str(usr.id)+"\","+"\""+number+"\","+"\""+features+"\")"
    cursor.execute(sql)
    conn.commit()

# sqlInsert(usr)
# This method is done for you.
def get_twitter(config_file):
    """ Read the config_file and construct an instance of TwitterAPI.
    Args:
      config_file ... A config file in ConfigParser format with Twitter credentials
    Returns:
      An instance of TwitterAPI.
    """
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    twitter = TwitterAPI(
                   config.get('twitter', 'consumer_key'),
                   config.get('twitter', 'consumer_secret'),
                   config.get('twitter', 'access_token'),
                   config.get('twitter', 'access_token_secret'))
    return twitter




def read_senators(filename):


    """ Read a list of usernames for U.S. senators.
    Args:
      filename: The name of the text file containing one senator username per file.
    Returns:
      A list of usernames
    """
    # Complete this method.
    arr=[]
    f = open(filename)
    line = f.readline()
    while line:
        msg = line.rstrip("\n")
        arr.append(msg)
        line = f.readline()

    return arr



def robust_request(twitter, resource, params, max_tries=5):
    """ If a Twitter request fails, sleep for 15 minutes.
    Do this at most max_tries times before quitting.
    Args:
      twitter .... A TwitterAPI object.
      resource ... A resource string to request.
      params ..... A parameter dictionary for the request.
      max_tries .. The maximum number of tries to attempt.
    Returns:
      A TwitterResponse object, or None if failed.
    """
    for i in range(max_tries):
        request = twitter.request(resource, params)
        if request.status_code == 200:
                users = request.response.text
                Gson = json.loads(users)
                # if(len(Gson['users'])==0):
                #     print >> sys.stderr, 'Got error:', request.text, '\nsleeping for 15 minutes.'
                #     sys.stderr.flush()
                #     time.sleep(60 * 15)
                #     twitter = get_twitter('twitter.cfg')
                #     return None
                return json.loads(users)
        else:
            print >> sys.stderr, 'Got error:', request.text, '\nsleeping for 15 minutes.'
            sys.stderr.flush()
            time.sleep(60 * 15)
            twitter = get_twitter('twitter.cfg')
            return None

def get_friends(screen_name, twitter,usr, list):
    """ Return Twitter screen names for all accounts followed by screen_name. Returns the first 200 users.
    See docs at: https://dev.twitter.com/docs/api/1.1/get/friends/list
    Args:
      screen_name ... The query account.
      twitter ....... The TwitterAPI object.
    Returns:
      A list of Twitter screen names.
    """
    # Complete this method.
    friendlist =[]
    cursor =-1
    while (cursor !=0):

        if(usr.id==0):
            res = robust_request(twitter,'friends/list',{'screen_name':screen_name,'cursor':cursor,'count':200})
        else:
            res = robust_request(twitter,'friends/list',{'user_id':usr.id,'cursor':cursor,'count':200})
        cursor =-1
        if(res != None):
                 if(res.has_key('users')):
                    # friendlist.extend(res['users'])
                    u = res['users']
                    for i in u:
                        friendlist.append(i["name"])
                        n_usr = singleuser()
                        n_usr.setname(i["name"])
                        n_usr.setid(str(i["id"]))
                        n_usr.setfeatures(i);
                        n_usr.setnumber(i["friends_count"])
                        list.append(n_usr)
                        sqlInsert(n_usr)

                    cursor = res['next_cursor']
                    if(len(friendlist)>=400):
                        cursor =0;
    # usr.setfriends(friendlist)
    # sqlInsert(usr)


    return friendlist

twitter = get_twitter('twitter.cfg')
print 'Established Twitter connection.'
senators = read_senators('senators.txt')
print 'Read', len(senators), 'senators:\n', '\n'.join(senators)
userslist=[]
for senator in senators:
        #senator=senators[1]
        usr = singleuser()
        usr.setname(senator)
        usr.setid(0)
        userslist.append(usr)
        # friends = get_friends(senator,twitter, usr)
def getData(list):
    for m in list:
        get_friends(m.name, twitter,m, list)
        list.remove(m)
getData(userslist)