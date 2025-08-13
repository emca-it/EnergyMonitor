# Integrating with Active Directory

Energy Monitor allows for logging in with the Active Directory user database, by utilizing LDAP protocol. 

## Preparing Active Directory domain

While Energy Monitor assigns chosen group permissions, it integrates with an Active Directory account to obtain data regarding available users and groups.

Energy Monitor binds with a service account in the Active Directory to get access to user information and group memberships. Therefore you need to create a service account for the Energy Monitor in your domain.

-   Create the Account/s
<br></br>
-   User "**EM**" has been created in Active Directory and has been assigned to the newly created group "**EM_Admins**". 
<br></br>
-   "**EM_admins**" group is located in @corp.EM.com/Users
<br></br>
-   Group names in Energy Monitor must be the same as in Active Directory.
<br></br>
-   The administrator can create as many groups as he/she deems necessary.
<br></br>

![ActiveDirectory](/media/05_00_28_01_Active_Directory.png)

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
Heed that "<b>User logon name</b>" is a fragment of a "<b>User Principal Name</b>"
</blockquote>

## Preparing Energy Monitor

-  Enter "**Manage**" -> "**Group Rights**"

![ActiveDirectory](/media/05_00_28_04_Active_Directory.png)

-   We insert an Energy Monitor group, with the same name as our Active Directory group, to which our user belongs to, "**EM_Admins**".
<br></br>
-   Define the access rights as you prefer. 

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> <b>Note</b>: You can use <b>lookup</b> and <b>filter</b> fields</b> to check for user membership or group presence. </blockquote>


<br>

![ActiveDirectory](/media/05_00_28_02_Active_Directory.png)

![ActiveDirectory](/media/05_00_28_03_Active_Directory.png)

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> <b>Note</b>: 
<br></br>
Heed the 3 colors of the square, green, red or gray under LDAP.
<br></br>
-   Green means the authentication module found the group successfully.
<br></br>
-   Red means that the authentication module didn't find the group.
<br></br>
-   Grey means that the authentication nmodule cannot determine if the group is available.  

</blockquote>

### preparing LDAP module

-   Enter "**Manage**" -> "**Configure**" -> "**Authorization Modules**"
<br></br>
-   Click "**Add New Module**"
<br></br>
    - Specify LDAP under "**DriverType**" and Name the module as you please.

![ActiveDirectory](/media/05_00_28_05_Active_Directory.png)
![ActiveDirectory](/media/05_00_28_06_Active_Directory.png)
![ActiveDirectory](/media/05_00_28_07_Active_Directory.png)

- You will need 1 more information, DN or "**Distinguished Name**".
<br></br>

-   Click the right mouse button on your Domain name in "**Active Directory Users and Computers**" -> "**Advanced Features**" -> Under "**Attribute Editor**" you will find an attribute called "**Distinguished Name**"

![ActiveDirectory](/media/05_00_28_08_Active_Directory.png)
![ActiveDirectory](/media/05_00_28_09_Active_Directory.png)

-   With this information in hand, you can proceed to configure your LDAP connection.
<br></br>
    -   The fields are explained as follows:

```
-   Server

    -   This is the IP address of your LDAP server, in our example it's the same as the host where Active Directory resides.    

    -   If there more than 1 LDAP server, separate IP's with spaces. Then, if 1st fails, the 2nd one will be utilized and so forth.

-   Port

    -   Input 3268 as the port. The reason isdue to how Active Directory handles referrals to pass users between servers. With 3268, we utilize the Global Catalog, interface, so the client ust only have the access to the 1st LDAP server, regardless how many domains and trusts are in your forest.

-   Encryption

    -   We use "none". You can utilize the Certificate Authority, to make it available for the ldap-interface which uses OpenLdap. However this is beyond the scope of this tutorial. 

-   Bind DN

    -   This is the login name of the service account. Due to LDAP's specification, a user should bind with their entire DN as a login. 

-   Bind Secret

    -   It's the password for the account in Active Directory.

-   Base DN

    -   This is the root of the domain. 

-   User Base DN

    -   This is where to find user objects within the domain, in our example this is equal to Base DN. 

-   User Filter

    -   ldap objects are always defined by a class, this fields describes which class to use. Users in Active Directory always utilize "user" class, so this field will always have a value of: (objectClass=user). 

-   Group Filter

    -   Like user filter, just for groups. Groups in Active Directory always utilize "group" class, so this field will always have a value of: (objectClass=group). 

-   Group Key

    -   Group key is the name of the attribute that defines the name of a group. In Active Directory, uses "Common Name" field, "cn" for short.

-   Group Recursive

    -  Active Directory by definition, sipports groups as members of groups. 
    This isn't always the case, depending on the directory server. This field if checked, makes EM resolve not only group membership of the user but the group membership in the groups found. We leave this unchecked for this tutorial.

-   UPN Suffix

    -  Like in "Bind DN" field, which utililized the full "User Principal Name", this one utilizes only the suffix, in our example "corp.EM.com"

    -   When binding a regular user, Active Directory refers to UPN, instead of DN. Username is combined with @ and this value "username@" is combined with the UPN suffix to make a full UPN. This all occurs when option "bind with upn" is enabled, which it is, in our example.

-   Userkey

    -  It's the attribute nae of the login. Active Directory takes the login name and the domain name, combines them together, to form "UserPrincipalName" field. We set "UserPrincipalName" as a value for this field.

-   Userkey is UPN

    -  This option causes EM to cut the username after the @ sign, when using UPN as a userkey. This is a native behaviour of Active Directory, so we check this option ON. 

-   Userkey realname

    -  This is the key used to retrieve the real name of the user. The real name is used to display the full name of the user instead of username. Active Directory handles this in "Common Name" field, "cn" for short.

    -   Use "cn" as a value for this field.

-   Userkey email

    -  This key is used to retrieve the email address. Active Directory uses a key "mail" for this. 

    -   Use "mail" as a value for this field.

-   Memberkey

    -  This is the attribute in a group that defines it's members. Members are described either just the username or the distinguished name. Active Directory refes to this attibute as "member"

    -   Since you can have users and groups as members of other groups, this nesting, creates a possibility for the memberkey to use DN of a different group as a value. Active Directory can resolve those nested connections in the following syntax form:

    -   member:oid -> member:1.2.840.113556.1.4.1941: 

    - The value for htis field is "member:1.2.840.113556.1.4.1941:" in our example.

-   Memberkey is DN

    -  This is the group membership attribute, this option determines if DN, with the entire path in the domain is used or just the username.

    -   This option should be enabled.

-   Bind with UPN

    -  This enables Active Directory to bind using UPN instead of DN, which is what we want to do. 

    -   This option should be enabled.

-   Bind with UPN

    -  This enables Active Directory to bind using UPN instead of DN, which is what we want to do. 

    -   This option should be enabled.

-   LDAP options

    -  We set the protocol version (/LDAP_OPT_PROTOCOL_VERSION) to 3. 

    -   This option should be enabled.

```

### Testing the connection

-   As mentioned in the previous sections, you can utilize "**lookup**" field in the "**Group Rights**" menu to search for a specified user. 
<br></br>
-   If that user will be found in Active Directory, you will see a white "X" mark next to the group it is a member of. 
<br></br>

![ActiveDirectory](/media/05_00_28_10_Active_Directory.png)

<blockquote style="border-left: 8px solid cyan; padding: 15px;"> <b>Note</b>: 
<br></br>
Heed the 3 colors of the square, green, red or gray under LDAP.
<br></br>
-   Green means the authentication module found the group successfully.
<br></br>
-   Red means that the authentication module didn't find the group.
<br></br>
-   Grey means that the authentication module cannot determine if the group is available.  

</blockquote>

You can very precisely set the permissions of a user in Energy Monitor, using the checkboxes. 

If all is configured properly, you will be able to log into Energy Monitor with your Active Directory user.