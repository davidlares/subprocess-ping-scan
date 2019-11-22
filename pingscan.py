# subprocess (OS processes API)
from subprocess import Popen, PIPE
# looping range
for segment in range(1,255):
    address = '192.168.1.' + str(segment)
    # creating the PING command - output as PIPE
    subprocess = Popen(['/sbin/ping','-c 1', address], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    # capturing output or errors
    stdout, stderr = subprocess.communicate(input=None)
    # evaluating a possible ECHO_REPLY evaluating "bytes from" string existance
    if "bytes from " in stdout:
        # printing the active IP addreses
        print("Active IP: %s" %(address))
