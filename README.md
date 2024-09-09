# Xevents
A covert event logger for deployment via xss  
![image](https://github.com/user-attachments/assets/e2ffd5d4-5e0c-4995-92d0-9e8804142712)

## Demonstrate Impact  
When cookies are http only and you can't perform the bog standard cookie theft to ATO,  
xevents provides an easy way to demonstrate impact by enabling an attacker to spy on user actions.  

## Victim Tracking
Targets maintain the same numeric identifier accross multiple compromised domains making them easier to profile.

## Configurable
given a set of tag names and events (user specified), Xevents generates and serves a payload that attaches the relevant listeners and uses the fetch api to exfiltrate data

## useage
```
usage: xevents.py [-h] [-H HOST] [-p PORT] [-t TAGS [TAGS ...]] [-a ACTIONS [ACTIONS ...]] [-c CONFIG] [-tu TUNNEL]

xevents args

options:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  ip, default 0.0.0.0
  -p PORT, --port PORT  port, default 5000
  -t TAGS [TAGS ...], --tags TAGS [TAGS ...]
                        tag list separated by spaces
  -a ACTIONS [ACTIONS ...], --actions ACTIONS [ACTIONS ...]
                        event list separated by spaces
  -c CONFIG, --config CONFIG
                        json config file (ignored if tags and events specified)
  -tu TUNNEL, --tunnel TUNNEL
                        url of tunnel

```
