# Xevents
A covert event logger for deployment via xss  

## Demonstrate Impact  
When cookies are http only and you can't perform the bog standard cookie theft to ATO,  
xevents provides an easy way to demonstrate impact by enabling an attacker to spy on user actions.  

## Victim Tracking
Targets maintain the same numeric identifier accross multiple compromised domains making them easier to profile.

## Configurable
given a set of tag names and events (user specified), Xevents generates and serves a payload that attaches the relevant listners and uses the fetch api to exfiltrate data
