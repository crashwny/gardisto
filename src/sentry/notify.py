import subprocess

subprocess.Popen(["echo 'Sentry detects a network failure! Check Sentry Logs!' > /tmp/pingmsg.txt"])
process = subprocess.Popen(["mutt -s 'Ping Check' pmcovert@buffaloist.com < /tmp/pingmsg.txt"], stdout=subprocess.PIPE)
output = process.communicate()
output = str(output[0])
return output
