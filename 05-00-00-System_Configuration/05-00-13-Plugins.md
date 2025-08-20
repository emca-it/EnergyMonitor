# Plugins

Plugins are external programs that take form of either compiled executables or scripts, that perform checks on hosts or services and return results to Nagios, which Energy Monitor relies on. 

1. Enter "**Manage**" -> "**Configure**" -> "**Plugins**"

The following menu allows the administrator to see what each plugin does and what commands are available to it, platofrms it can be used on and more. 

There are few levels of support:

- <strong>Full</strong> 

    - Nagios support forums, mailing lists, offer full help with the issues and bugs or general plugin usage.
<br>
- <strong>Best Effort</strong>

    - There is no formal support policy for plugins or executables, however community and providers still offer some degree of support.
<br>
- <strong>Bug Support</strong> 

    - Plugins are improved over time by the community, to address bug reports and fix requests.
<br>
- <strong>Unsupported</strong> 

    - There is no support. 


![Plugins](/media/05_00_12_01_Plugins.png)
![Plugins](/media/05_00_12_02_Plugins.png)


## Overview of plugin functionality

As mentioned, Energy Monitor relies on external means to check the status of an endpoint.

Plugins are compiled scripts (perl scripts, shell scripts, python among others), that are run from the commandline. Those results are gathered back and send to back to Energy Monitor.

Plugins are executed as needed, as the system determines the need to check for a metric. 

Based on the received data, a particular action is taken, like running even handler or sending out a notification.

![Plugins](/media/05_00_12_03_Plugins.png)

Plugins allow for incredible flexibility in monitoring systems based on this architecture, due to the fact that you can write your own plugins in accordance to the documentation on how to develop them.

However it's not all sunshine and roses. As Energy Monitor tracks only the changes in the state of whaetever it is you are monitoring. Only the plugin the knows the details and internal works of the script, how to do checks, etc. 

By default Energy Monitor places plugins in: 

```
/opt/plugins
```

You run plugins as you would any other script in shell environment.