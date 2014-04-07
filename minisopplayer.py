#!/usr/bin/env python

# MiniSopPlayer
# Attempt to connect to the Sopcast stream given on the command-line, open 
# the user's favourite movie player to play the stream

# 

import pexpect,time,sys,pprint,subprocess

# holds our config
from minisopconfig import MiniSopConfig

# mainly for testing
pp = pprint.PrettyPrinter()

# quit if there aren't enough arguments
if len(sys.argv) == 1:
   print "No arguments!"
   sys.exit(1)

# read and format the PID from command-line
sop = sys.argv[1]

print "Starting with PID " + sop + "..."

# try to connect to the SopCast stream
child = pexpect.spawn ('sp-sc-auth ' + sop + ' 3908 ' + str(MiniSopConfig.sopport))
child.logfile = sys.stdout
child.timeout = MiniSopConfig.sopconntimeout

# if we can't get a telnet session before the timeout just quit
conn = child.expect([pexpect.TIMEOUT, "I START.+"])
if conn == 0:
   print "Timeout connecting to Sopcast stream!"
   sys.exit(1)

# give us a bit of time to send the next command
time.sleep(5)

url = "http://" + MiniSopConfig.sophost + ":" + str(MiniSopConfig.sopport) + "/tv.asf"

# call the media player to play the URL
subprocess.call([MiniSopConfig.sopplayer, url])

# the user must have quit the media player, stop the stream too
child.kill(7)
