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

````
Insecure is a mode without encryption or strong authentication, therefore it's vulnerable to interception or spoofing. It is recommended to implement additional security measures in the network that protect against such threats.



````
sss

``


![NSC](/media/04_01_nsc_3.png)