# API 

## Introduction to API
Energy Monitor utilizes REST-API, so the administrator can issue commands directly into the system, with HTTP requests. 

Essentially, one can operate various aspects of Energy Monitor from the level of the command line.

The following guide contains helpful tips on the methodology of formulating these requests with appropriate help pages.

```

Requests can be performed with:

-   Shell:

    -   Curl

-   Scripting Languages

    -   Python

    -   PHP
```


Expected performance for passive checks via API should be around 10 checks/minute.

A valid request must met few requirements depending how it is performed:

```
-   The URL format:

    -   /api/config/host
    -   /api/config/host/{host_name}

-   The HTTP format

    -   GET:
        -   lists object

    -   POST: 
        -   creates objects

    -   PUT:
        -   overwrites objects

    -   PATCH:
        -   update objects

    -   DELETE: 
        -   delete objects

-   HTTP header format:

    -    -H 'accept: application/json' 
    -    -H 'Content-Type: application/json' 
```

Energy Monitor has internal API query editor available at the following:

![API_Introduction](/media/07-00-01-01-Introduction.png)

![API_Introduction](/media/07-00-01-02-Introduction.png)

Every category contains interactive editor for every HTTP method.

```
The editor contains following categories:

-   Commands

-   Contacts

-   Filters

-   Hosts

-   HostGroups

-   Changes

-   Services

-   ServiceGroups

-   Status
```

Example:

![API_Introduction](/media/07-00-01-03-Introduction.png)

![API_Introduction](/media/07-00-01-04-Introduction.png)

In order to enable input for the fields, press the **"Try it out"** button.

After pressing **"Execute"** button, you will receive the following reponse:

![API_Introduction](/media/07-00-01-05-Introduction.png)

![API_Introduction](/media/07-00-01-06-Introduction.png)

The query you can utilize with the **"Curl"** command from the shell or URL you can paste into the browser. 

You can also see descriptions of errors you might encounter.
```
Examples of status codes:

-   200: Everything went fine.
-   201: Everything went fine, you wanted to create an object and it was created.
-   400: You sent a request Monitor didn't understand. Correct the input and try again.
-   401: Authentication required.
-   403: You're not authorized to do this.
-   404: The URI doesn't exist.
```

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
With methods like POST or PATCH, you will see in the curl query, a long list of options that will be passed.
<br></br>
Instead of pasting all those lines into the shell, it's more convenient to create a file, let's say <b>"host_update.json"</b>. You use the <b>"-d"</b> flag to point the command to read from the created file (remember to place the <b>"@"</b> sign prior to path):
<br></br>
Example:
<br></br>
<blockquote>curl -X 'PUT' https://192.168.3.166/api/config/host/TEST -H 'accept: application/json' -H 'Content-Type: application/json' -k -u admin:admin -d @/home/Testy_API/host_update.json</blockquote> 
Keep in mind that all the changes made to the configuration, aren't automatically saved into the database. 
</blockquote>
<br></br>

"Changes" category governs this aspect, for instance saving the changes for my installation was:

```
 curl -X 'POST''https://192.168.3.78/api/config/change' -H 'accept: application/json' -H 'Authorization: Basic YWRtaW46YWRtaW4=' -H 'X-CSRF-TOKEN: ' -d '' -k
```

in short:
```
-   GET method allows you to view changes pending

-   POST method saves them into the database

-   DELETE method deletes the changes. 
```

## SSL Certificates:

In these examples, we skipped certification check with the **"-k"** flag, however in regular production environments, certificates should be checked prior to executing the queries due to security. Alternatively, adding **"--insecure"** also does the same thing, omitting the check.

In Python You would need to add **"a verify=False**" flag.

Example:

```
requests.get('<API endpoint here>', auth=('<your username>', '<your password>'), verify=False)
```

in PHP with cURL, You would need to add a CURLOPT_SSL_VERIFYPEER flag
PHP with cURL: 

```
curl_setopt($a_handle, CURLOPT_SSL_VERIFYPEER, false);
```

## Authorization Types

You have the capacity to log either with basic login and password or LDAP. 

When you have more than one auth module, for example "Default" and "LDAP", you need to specify which to authenticate against. This is done with the dollar character ('$').

Thus, this regular call:
```
curl -u user:password https://monitor/api/config/host
```
becomes
```
curl -u 'user$LDAP:password' https://monitor/api/config/host
```
or
```
curl -u 'user$Default:password' https://monitor/api/config/host
```

LDAP:

If utilizing LDAP verification, in curl, use the **"$"** sign:
```
curl -X 'PUT' https://192.168.3.166/api/config/host/TEST -H 'accept: application/json' -H 'Content-Type: application/json' -k **-u 'admin$LDAP:admin'** -d @/home/Testy_API/host_update.json
```

**'** is dependent on the environment, in bash, it's mandatory.

### Restricting access to the API

By editing API config files you can decide whether to accept or reject connections to the API based on connection method. For now, there are two categories: basic_auth and ninja.

If you disallow basic_auth, you can no longer access the API through scripts as described in all examples in this documentation.
If you disallow ninja, you can no longer access the API through AJAX requests carried out by code in Monitor, such as the Host Wizard.

The files governing this aspect are located in:
```
/etc/energy-monitor/http_api.yml
/opt/energy-monitor/ninja/etc/http_api.yml
```

### Handling custom variables

Custom variables function as key values stored within a Nagios object, therefore API also treats them as mere objects. 

In the request, refer to them with an underscore. 

Example

-   Adding/Updating variables
```
curl -u admin:admin -k https://192.168.3.166/api/config/host/test/ -X "PATCH" -H "content-type: application/json" -d '{"_ENVIRONMENT": "production"}'
```
-   This will add a custom variable _ENVIRONMENT to the host "test".
```
curl -u admin:admin -k https://192.168.3.166/api/config/host/test/ -X "PATCH" -H "content-type: application/json" -d '{"_ENVIRONMENT": "staging"}'
```
-   This will update a custom variable _ENVIRONMENT to the host "test".

### Adding multiple variables at once
```
curl -u admin:admin -k https://192.168.3.166/api/config/host/test/ -X "PATCH" -H "content-type: application/json" -d '{"_ENVIRONMENT": "staging", "_OWNER":"ops_team"}'
```
-   This will add custom variables _ENVIRONMENT and _OWNER to the host "test".

### Removing custom variables:
```
curl -u admin:admin -k https://192.168.3.166/api/config/host/test/ -X "PATCH" -H "content-type: application/json" -d '{"_ENVIRONMENT": "null"}'
```
-   This will remove custom variables _ENVIRONMENT of the host "test".
```
curl -X 'GET' https://192.168.3.166/api/config/change -k -u admin:admin
```

### Filtering data via API 

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
jq is a tool that "prettify'ies" the output to be more convenient for reading. 
<br></br>
It isn't a part of the API. 
</blockquote>

<br>

-   an example query listing "display_name" 

```
curl -X 'GET' 'https://192.168.3.166/api/filter/query?query=%5Bhosts%5D%20state%20%3D%201&columns=display_name' -H 'accept: application/json' -H 'Authorization: Basic YWRtaW46YWRtaW4=' -H 'X-CSRF-TOKEN: ' -k -o output.json | jq
```

-   an example query listing "display_name", "alias" and "address"

```
curl -X 'GET' 'https://192.168.3.166/api/filter/query?query=%5Bhosts%5D%20state%20%3D%201&columns=display_name%2Caddress%2Calias' -H 'accept: application/json' -H 'Authorization: Basic YWRtaW46YWRtaW4=' -H 'X-CSRF-TOKEN: ' -k -o output.json | jq
```

As you can see, the columns are separated by stanard URL encoding of **"%2C"**



You can be very expressive and ask for e.g. "all hosts with a problem state that are not acknowledged and not in downtime" with a single HTTP request. Every filter that you have defined in Monitor is copy & pastable into the HTTP API, via the query GET parameter.
You can limit the data transfered by:
defining what columns you would like in the output. If you only need to display a list of problem hosts' names and if they are acknowledged or not, you can limit the result to only include those two columns.
This is done through the columns GET parameter, as in ?columns=name,state
using the limit and offset variables, as if you are paginating something. Append the GET parameters ?limit=5&offset=3 to any request to see them in action.
All tables and columns are documented in the article Listview filter columns.

-   Requests
In a REST-API, there are a couple of important things that make up for a valid request:

The URI, in the following form
/api/filter/
/api/filter/query
/api/filter/count
The HTTP method
GET: retrieve data
The format, appended to the URI
?format=xml
?format=json (default, except for requests from a browser)
?format=html (default in a browser environment)

```
 948  curl -X 'GET'  'https://192.168.3.78/api/config/command/check_nt'   -H 'accept: application/json'   -H 'Authorization: Basic YWRtaW46YWRtaW4='   -H 'X-CSRF-TOKEN: ' -k -u admin:admin | jq
```

Authorization Basic can be obtained from the Swagger UI under any type of query and any method. 

for instance commands - GET:

![07-00-01-Introduction](/media/07-00-01-07-Introduction.png)


#### Example of a filter:

```
curl -X 'GET' 'https://192.168.3.166/api/filter/query?query=%5Bhosts%5D%20state%20%3D%201&columns=name%2Caddress&limit=50&offset=1&sort=name%20DESC%2Cstate%20ASC' -H 'accept: application/json'-H 'Authorization: Basic YWRtaW46YWRtaW4=' -k -u admin:admin
```

The query looks up:

-   hostname
-   IP
-   Pagination offset of 1 (EM API expects the pagination to be > than 0.)
-   Sorting DESC ny name and ASC by state.
-   Limiting results to 50.

#### Example of a count:

```
curl -X 'GET' 'https://192.168.3.166/api/filter/count?query=%5Bhosts%5D%20state%20%3D%201' -H 'accept: application/json' -H 'Authorization: Basic YWRtaW46YWRtaW4=' -k -u admin:admin
```

The query looks up all hosts with a state of 1. 

