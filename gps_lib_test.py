from gps import *
import time

running = True

def getPositionData(gps):
	nx = gpsd.next()
	# For a list of all supported classes and fields refer to:
	# https://gpsd.gitlab.io/gpsd/gpsd_json.html
	if nx['class'] == 'TPV':
		latitude = getattr(nx,'lat', "Unknown")
		longitude = getattr(nx,'lon', "Unknown")
		altitude = getattr(nx,'alt', "Unknown") 
		velocity = getattr(nx,'speed', "Unknown")
		heading = getattr(nx,'track', "Unknown")
		#hdop  = getattr(nx,'hdop', "Unknown")
		#status = getattr(nx,'status ', "Unknown")
		#magnetic_declanatioin = getattr(nx,'magvar', "Unknown")
		print (" longitude = " + str(longitude) + ", latitude = " + str(latitude)+ ", altitude = " + str(altitude) + " m , vel  = " + str(velocity) + " m/s , GPS Heading = " + str(heading) + " degrees")
		#print("hdop  : " + str(hdop) + "," "Status : " + str(status) + "," "Magnetic Declanatioin: " + str(magnetic_declanatioin) )
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
	print ("Application started!")
	while running:
		getPositionData(gpsd)
		time.sleep(1.0)

except (KeyboardInterrupt):
	running = False
	print ("Applications closed!")
