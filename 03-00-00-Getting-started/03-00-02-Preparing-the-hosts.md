# Preparing the hosts for monitoring

Before Energy Monitor can be utilized to monitor an endpoint, it must be pre-configured first. 

The steps differ, depending on what operating system it runs on. 

## Preparing Windows endpoints

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> Administrative priviliges on the host are required to implement the following instructions. 
</blockquote>

1. Energy Monitor utilizies NSClient++ for monitoring Windows based hosts, download it from [NSClient++](https://www.nsclient.org/download/) website and install on the host as shwon on the following screens:

- Choose "**Generic**"
<br></br>
 ![NSC](/media/04_01_nsc_1.png)

- Under "**Allowed Hosts**" you need to place the IP address of your server where Energy Monitor is installed.

![NSC](/media/04_01_nsc_2.png)

- Depending on the local security protocols in the company, Insecure, Safe or Secure can be chosen as preferred. 

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> 
Insecure is a mode without encryption or strong authentication, therefore it's vulnerable to interception or spoofing. It is recommended to implement additional security measures in the network that protect against such threats.
<br></br>
Safe Mode utilizes certificates to encrypt the communication. However, there isn't any method of authentication present in this mode. External means of authenticating traffic are advised. 
<br></br>
Secure Mode utilizes certficates for both, encryption and authentication. Therefore traffic is encrypted and connections authorized before sending data.
</blockquote>
<br></br>

![NSC](/media/04_01_nsc_3.png)


## Post-Installation steps

After the agent has been installed, default path being `C:\ProgramFiles\NSClient++`, it's configuration file, `nsclient.ini` needs to be edited.



````
# If you want to fill this file with all available options run the following command:
#   nscp settings --generate --add-defaults --load-all
# If you want to activate a module and bring in all its options use:
#   nscp settings --activate-module <MODULE NAME> --add-defaults
# For details run: nscp settings --help


; in flight - TODO
[/modules]

; Undocumented key
NSClientServer = enabled

; Undocumented key
CheckEventLog = enabled

; Undocumented key
CheckNSCP = enabled

; Undocumented key
CheckSystem = enabled

; Undocumented key
CheckDisk = enabled

; Undocumented key
NSCAClient = enabled

; Undocumented key
WEBServer = enabled

; Undocumented key
NRPEServer = enabled

; Undocumented key
CheckExternalScripts = enabled

; Undocumented key
CheckHelpers = enabled


; in flight - TODO
[/settings/NRPE/server]

; Undocumented key
verify mode = none

; Undocumented key
insecure = true

;arguments yes
allow arguments = true

; in flight - TODO
[/settings/default]

; Undocumented key
allowed hosts = 192.168.3.166

[/settings/log]
level = debug
````

**-** Change the allowed hosts section to the IP address of your mainframe (a host where your EnergyMonitor installation is located).

**-** Turning on all modules is recommended for futureproofing. 

**-** Allow arguments option is crucial, because it allows arguments to be passed in the queries to the agent, which results in specific metrics, tuned in to company needs. 


