from flask import Flask
from flask import render_template
from flask import request
from device import main14name,main14sn,main14st,mainnew,mainip,mainmrtg
app=Flask(__name__)
@app.route('/')
#@app.route('/<ip>')
def all():
	k=main14name(68939)
	k46=main14name(68938)
	k69=main14name(68940)
	return render_template('hello.html',k=k,k46=k46,k69=k69)
@app.route('/all14')
def showdev14():
	devs14=main14name(68939)
	devss14=devs14.keys()[0]
	dn14=len(devs14.keys())
	devsv14=devs14.values()[0]
	del devs14[devs14.keys()[0]]
	lens14=[str(i) for i in range(1,len(devs14.keys())+1)]
	lenss14=0
	stn14=main14st(68939)
	op14=[i for i in stn14.values() if i == "OPEN"]
	sp14=[i for i in stn14.values() if i == "SUSPEND"]
	spd14=[k for k,v in stn14.items() if v == "SUSPEND"]
	cs14=[i for i in stn14.values() if i == "CLOSE"]
	csd14=[k for k,v in stn14.items() if v == "CLOSE"]
	return render_template('showdevall.html',devs14=devs14,devss14=devss14,devsv14=devsv14,sn14=main14sn(68939),lens14=lens14,lenss14=lenss14,dn14=dn14,opn14=len(op14),spn14=len(sp14),csn14=len(cs14),spd14=spd14,csd14=csd14)
@app.route('/all46')
def showdev46():
	devs46=main14name(68938)
	devss46=devs46.keys()[0]
	dn46=len(devs46.keys())
	devsv46=devs46.values()[0]
	del devs46[devs46.keys()[0]]
	lens46=[str(i) for i in range(1,len(devs46.keys())+1)]
	lenss46=0
	stn46=main14st(68938)
	op46=[i for i in stn46.values() if i == "OPEN"]
	sp46=[i for i in stn46.values() if i == "SUSPEND"]
	spd46=[k for k,v in stn46.items() if v == "SUSPEND"]
	cs46=[i for i in stn46.values() if i == "CLOSE"]
	csd46=[k for k,v in stn46.items() if v == "CLOSE"]
	return render_template('showdevall46.html',devs46=devs46,devss46=devss46,devsv46=devsv46,sn46=main14sn(68938),lens46=lens46,lenss46=lenss46,dn46=dn46,opn46=len(op46),spn46=len(sp46),csn46=len(cs46),spd46=spd46,csd46=csd46)
#46end#
@app.route('/all69')
def showdev69():
	devs69=main14name(68940)
	devss69=devs69.keys()[0]
	dn69=len(devs69.keys())
	devsv69=devs69.values()[0]
	del devs69[devs69.keys()[0]]
	lens69=[str(i) for i in range(1,len(devs69.keys())+1)]
	lenss69=0
	stn69=main14st(68940)
	op69=[i for i in stn69.values() if i == "OPEN"]
	sp69=[i for i in stn69.values() if i == "SUSPEND"]
	spd69=[k for k,v in stn69.items() if v == "SUSPEND"]
	cs69=[i for i in stn69.values() if i == "CLOSE"]
	csd69=[k for k,v in stn69.items() if v == "CLOSE"]
	return render_template('showdevall69.html',devs69=devs69,devss69=devss69,devsv69=devsv69,sn69=main14sn(68940),lens69=lens69,lenss69=lenss69,dn69=dn69,opn69=len(op69),spn69=len(sp69),csn69=len(cs69),spd69=spd69,csd69=csd69)

@app.route('/devicelist69')
def showdevlist69():
	devs69=main14name(68940)
	ips69=mainip(68940)
	mrtgs69=mainmrtg(68940)
	sts69=main14st(68940)
	return render_template('showdevlist69.html',devs69=devs69,ips69=ips69,sts69=sts69,mrtgs69=mrtgs69)

@app.route('/14/<name14>')
def showip14(name14):
	nd=main14name(68939)
	sns=main14sn(68939)
	nd46=main14name(68938)
	sns46=main14sn(68938)
	nd69=main14name(68940)
	sns69=main14sn(68940)
	ndall=dict(dict(nd,**nd46),**nd69)
	snall=dict(dict(sns,**sns46),**sns69)
#	names=namess.keys()
	return render_template('detail.html',names=name14,nda=ndall,sn=snall)
@app.route('/46/<name46>')
def showip46(name46):
	nd46=main14name(68938)
	sns46=main14sn(68938)
	print nd46,sns46
#	names=namess.keys()
	return render_template('detail46.html',names46=name46,nda46=nd46,sn46=sns46)
@app.route('/69/<name69>')
def showip69(name69):
	nd=main14name(68940)
	sns=main14sn(68940)
#	names=namess.keys()
	return render_template('detail69.html',names=name69,nda=nd,sn=sns)
@app.route('/14')
def cc14():
	error=None
	return render_template('14.html',error=error)
@app.route('/46')
def cc46():
	error=None
	return render_template('46.html',error=error)
@app.route('/69')
def cc69():
	error=None
	return render_template('69.html',error=error)
@app.route('/newimg')
def newimage():
	newall=mainnew(68939)
	newalld=newall.keys()
        stn14=main14st(68939)
        op14=[i for i in stn14.values() if i == "OPEN"]
        spd14=[k for k,v in stn14.items() if v == "SUSPEND"]
        csd14=[k for k,v in stn14.items() if v == "CLOSE"]
	return render_template('newall14.html',newall14=newall,newalld=newalld,op14=len(op14),spd14=len(spd14),csd14=len(csd14))
@app.route('/search',methods=['GET','POST'])
def search():
	error=None
	k14=mainnew(68939)
        k46=mainnew(68938)
        k69=mainnew(68940)
	da=dict(dict(k14,**k46),**k69)
	alld=da.keys()
	if request.method=='POST':
		sv=request.form['devicename']
		if sv in alld:
			svurl=da[sv]
			return render_template('search.html',error=error,sv=sv,da=da,alld=alld,svurl=svurl)
		else:
			error="Invalid Device Name"
		        return render_template('search.html',error=error,sv=sv,da=da,alld=alld)
		
if __name__=="__main__":
	app.run(debug=True,host='192.168.6.27')
