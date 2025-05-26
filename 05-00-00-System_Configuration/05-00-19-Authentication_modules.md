# Authentication modules

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
All instructions below assume you are running OracleLinux8.X.
</blockquote>

## Setting up an Authentication Module

1. Enter "**Manage**" -> "**Configure**" -> "**Authentication Modules**"

![Authentication_modules](/media/05_00_19_01_Authentication_modules.png)

-   Authentication can utilize following drivers:

    -   Default (local user files)

    -   LDAP

    -   Apache         

![Authentication_modules](/media/05_00_19_02_Authentication_modules.png)

![Authentication_modules](/media/05_00_19_03_Authentication_modules.png)

### Default

Default authorization uses local user files, without any external software to verify the credentials. Essentially in this method, all users made in Energy Monitor GUI, are perfectly capable of logging in by themselves as long as credentials match the database entry. 

### Apache 

Setting up the module to utilize Apache only:

<blockquote>

1. <strong>.htpasswd</strong>, this file must be present in <strong>/etc/naemon/
    htpasswd</strong>

    - Simplest way to add it is via shell:

        - <strong>htpasswd -c /etc/naemon/htpasswd username </strong>
            - replace username with a first desired user.

    - any consequent users are added with:
        - <strong> htpasswd /etc/naemon/htpasswd anotheruser </strong>

</blockquote>





2. In your apache configuration file: <strong>/etc/httpd/conf.d</strong>
   
<blockquote>

    <Location /naemon>
  
     AuthType Basic
  
    AuthName "Naemon Monitoring"
  
    AuthUserFile /etc/naemon/htpasswd
  
    Require valid-user

    \</Location>

</blockquote>

3. Restart Apache service:
<br></br>
<blockquote>
<strong>systemctl restart httpd</strong>
</blockquote>

### LDAP

LDAP authorizes via Apache server, it checks against LDAP  directory using <strong>mod_authnz_ldap</strong>. This allows for a centralized approach, centralized user management.

Setting up the module to utilize Apache only:

1. Install Apache and LDAP modules

<blockquote>
<strong>dnf install httpd mod_ldap mod_ssl</strong>
</blockquote>

2. Enable the required modules:

<blockquote>
<strong>systemctl enable --now httpd</strong>

<strong>systemctl start httpd</strong>
</blockquote>

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
in OracleLinux 8.X these modules are usually already included with httpd server.
</blockquote>
<br>
3. Configure Apache for LDAP authentication:
<br></br>
- <strong>Example of /etc/httpd/conf.d/naemon.conf</strong>

<br>
<blockquote>

    <Location /naemon>

    AuthType Basic

    AuthName "Naemon Monitoring"

    AuthBasicProvider ldap

    AuthLDAPURL "ldap://ldap.example.com/dc=example,dc=com?uid?sub"

    Require valid-user

    \</Location>

</blockquote>

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
Replace ldap:// with your server IP or hostname and Distinguished Name.
<br></br>
LDAPS, if you support SSL, can be used as well: ldaps:// and port 636. 
<br></br>
Ensure the vailidty of certificates
</blockquote>

<br>4. Restart Apache service:
</br>
<blockquote>
<strong>systemctl restart httpd</strong>
</blockquote>

### Combining both at once

The administrator can set the Apache to use both providers at the same time:

1. In your apache configuration file: <strong>/etc/httpd/conf.d</strong>

<blockquote>

<Location /naemon>

  AuthType Basic

  AuthName "Naemon Monitoring"

  AuthBasicProvider file ldap

  AuthUserFile /etc/naemon/htpasswd

  AuthLDAPURL "ldap://ldap.example.com/dc=example,dc=com?uid?sub"

  Require valid-user

\</Location>

</blockquote>

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
AuthBasicProbvider is set to file and ldap.
</blockquote>

<br>
2. Restart Apache service:
<br></br>
<blockquote>
<strong>systemctl restart httpd</strong>
</blockquote>

<br>

### 4. Optional, System-Level LDAP, to use with SSH or console, on OracleLinux8.X:

1. Install SSSD and LDAP tools:
<blockquote>
<strong> dnf install sssd authselect </strong>
</blockquote>

2. Configure authselect:

<blockquote>
<strong>authselect select sssd with-ldap --force</strong>
</blockquote>

3. Edit <strong>/etc/ssd/ssd.conf</strong> to point to your LDAP server  
<br>

4. Configure <strong>/etc/nsswitch.conf</strong> to include <strong>ldap</strong> or <strong>sss</strong> for passwd and group:

<blockquote>
passwd: files sss

group: files sss
</blockquote>

5. Restart services:

<blockquote>
<strong>systemctl restart sssd</strong>
</blockquote>
<br>

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
AuthBasicProbvider is set to file and ldap.
</blockquote>

<br>
2. Restart Apache service:
<br></br>
<blockquote>
<strong>systemctl restart httpd</strong>
</blockquote>

### Optional Improvements



![Authentication_modules](/media/05_00_19_04_Authentication_modules.png)

In case of performance problems, the administrator can install PHP extensions to help mitigate this issue:

   - **APC (Alternative PHP Cache)**

       - This extension caches compiled PHP scripts, so they don't have to be recompiled on every request. It also stores application data in memory, reducing the need for repeated queries to the database.   

   - Key settings:

       - **apc_ttl** 

           - "Time to live", determines how long the data is stored in the cache.

       - **apc_store_prefix**:

           - Defines a prefix for cached keys, preventing naming collisions between applications and modules. 
