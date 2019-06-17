import subprocess
import sys
import time

clear = "\x1b[0m"
red = "\x1b[1;31m"
green = "\x1b[1;32m"
cyan = "\x1b[1;36m"


infile = open(sys.argv[1], "r")
iplist = infile.readlines()

for ip in iplist:
 single = ip.strip()
 cmd = ["curl","-k","-b", "cookie.txt", "-x", "http://127.0.0.1:8080", single]
 proc = subprocess.Popen(cmd,stdout=subprocess.PIPE)
 time.sleep(5) #quick time hack to ensure target is not overwhelmed as it's live
 print("%s{+}Running: %s%s " % (cyan,cmd,clear))
 while True:
  output = proc.stdout.readline()
  if "Unauthorised" in output or proc.poll() is not None:
   print("%s{!} Process errored... %s%s" % (red,cmd,clear))
   print("%s{!} Moving on... %s" % (red,clear))
   break
  if output:
   print output.strip()
   print("%s{+} Next target... %s" % (cyan,clear))
   rc = proc.poll()
