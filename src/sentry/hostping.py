import subprocess

def hostPing(hostIp):
    process = subprocess.Popen(["/usr/bin/ping", "-c 1 -Aq", hostIp], stdout=subprocess.PIPE)
    output = process.communicate()
    output = str(output[0])
    result = output.find('Unreachable')
    # print(result)

    if result == -1:
        ping = True
    else:
        ping = False

    # print(ping)
    return ping
