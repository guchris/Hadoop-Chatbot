import requests
import json
import urllib

def getClusterInfo(server):
    url = 'http://' + server + '.uppr.com:50070/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo'
    data = requests.get(url).json()
    print(url)
