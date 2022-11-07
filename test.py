import speedtest

st1 = speedtest.Speedtest() #Create a speedtest object. More info on line 1077

print("Starting Speed test... \n")

#Test Download
print("Retrieving download speed...")
download_speed = st1.download() #Get download speed function. More info on line 1507
print(f"Download speed: {download_speed} \n")

#Test Upload
print("Retrieving upload speed...")
upload_speed = st1.upload() #Get download speed function. More info on line 1582
print(f"Upload speed: {upload_speed}\n")

#Test Ping
print("Retrieving ping(latency)...") #Test Latency from nearest server by default. More info on line 1411
ping = st1.results.ping
print(f"Ping(Latency) {ping}")