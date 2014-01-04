#!/usr/bin/python
#coding utf-8
import urllib2
import json
#dict={}
#dictsn={}

#dictst={}
def main14name(searchnum):
	dict={}
	s1=urllib2.urlopen('http://cop.chinacache.com/devman/list/%s' %searchnum).read()
	a1=json.loads(s1)
	l1=map(lambda i:str(i['name'])+" "+str(i['ip'])+":21900" ,a1['devInfo'])
#	l2=map(lambda i:str(i['ip'])+"21900" ,a1['devInfo'])
	for i in l1:
		dict[i.split(' ')[0]]=i.split(' ')[1]
	return dict
def main14sn(searchnum):
	dictsn={}
	s2=urllib2.urlopen('http://cop.chinacache.com/devman/list/%s' %searchnum).read()
        a2=json.loads(s2)
        l2=map(lambda i:str(i['name'])+" "+str(i['code']),a2['devInfo'])
	for i in l2:
		dictsn[i.split(' ')[0]]=i.split(' ')[1]
	return dictsn
def main14st(searchnum):
	dictst={}
	s1=urllib2.urlopen('http://cop.chinacache.com/devman/list/%s' %searchnum).read()
        a1=json.loads(s1)
        l1=map(lambda i:str(i['name'])+" "+str(i['st']) ,a1['devInfo'])
	for i in l1:
		dictst[i.split(' ')[0]]=i.split(' ')[1]
	return dictst
def mainip(searchnum):
	dictip={}
	s1=urllib2.urlopen('http://cop.chinacache.com/devman/list/%s' %searchnum).read()
        a1=json.loads(s1)
        l1=map(lambda i:str(i['name'])+" "+str(i['ip']) ,a1['devInfo'])
	for i in l1:
		dictip[i.split(' ')[0]]=i.split(' ')[1]
	return dictip
def mainmrtg(searchnum):
	dictmrtg={}
        s1=urllib2.urlopen('http://cop.chinacache.com/devman/list/%s' %searchnum).read()
        a1=json.loads(s1)
        l1=map(lambda i:str(i['name'])+" "+i['mrtg'] ,a1['devInfo'])
        for i in l1:
                dictmrtg[i.split(' ')[0]]=i.split(' ')[1]
        return dictmrtg
def mainnew(searchnum):
        dictnew={}
        s1=urllib2.urlopen('http://cop.chinacache.com/devman/list/%s' %searchnum).read()
        a1=json.loads(s1)
	l1=[str(i['name'])+" "+"http://"+str(i['ip'])+":21900/Rrd/"+str(i['name'])+"/.base-LOCAL_BAND_OUT-.base-LOCAL_BAND_IN/daily" for i in a1['devInfo'] if i['st']=="OPEN"]	
        for i in l1:
                dictnew[i.split(' ')[0]]=i.split(' ')[1]
        return dictnew
#d=mainnew(68939)
#print len(d.keys())
#print d
