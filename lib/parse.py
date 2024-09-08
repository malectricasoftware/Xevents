import argparse
def parser():
	parser = argparse.ArgumentParser(description="xevents args")
	parser.add_argument("-H","--host",default="0.0.0.0",help="ip, default 0.0.0.0")
	parser.add_argument("-p","--port",default=5000,help="port, default 5000")
	parser.add_argument("-t","--tags",nargs="+",help="tag list separated by spaces")
	parser.add_argument("-a","--actions",nargs="+",help="event list separated by spaces")
	parser.add_argument("-c","--config",default="xevents.json",help="json config file (ignored if tags and events specified)")
	parser.add_argument("-tu","--tunnel",help="url of tunnel")
	args = parser.parse_args()
	args.url = args.tunnel or f"http://{args.host}:{args.port}"
	return args