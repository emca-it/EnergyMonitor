# Integrating Discord with Energy Monitor

Energy Monitor allows for sending for notifications from hosts and services to your Discord server. 

In order to set it up the following must be done:

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
All instructions below assume you are running Oracle Linux 8.X.
</blockquote>

## Setting up 

1. Enter "**Manage**" -> "**Configure**" -> "**Authentication Modules**"


![Integration_with_Discord](/media/05_00_28_01_Integration_with_Discord.png)

![Integration_with_Discord](/media/05_00_28_02_Integration_with_Discord.png)

![Integration_with_Discord](/media/05_00_28_03_Integration_with_Discord.png)

What we want from this section is the "**Webhook**", which is a method for sending data in real-time using HTTPS requests, with the POST method. 

-   Webhook, the URL, must be placed in the "**e-mail**"
 field of a "**Contact**".
<br></br>
-   service/host_notification_cmds field must point to a script:
<br></br>
    -   notify-host-by-discord
<br></bR>
    -   notify-service-by-discord  


![Integration_with_Discord](/media/05_00_28_04_Integration_with_Discord.png)

![Integration_with_Discord](/media/05_00_28_05_Integration_with_Discord.png)

2. Modifying files:

Adjust accordingly for your setup:

-   /opt/naemon/etc/naemon/conf.d/commands.cfg

```
#command 'notify_by_host_discord'
define command {
    command_name                  notify-by-host-discord
    command_line                  /opt/energy-monitor/notify/notify_by_host-discord.py -c  "$CONTACTEMAIL$" -t  "$NOTIFICATIONTYPE$" -o "$HOSTOUTPUT$" -d "$LONGDATETIME$" -n "$HOSTNAME$" -s "$HOSTSTATE$" -a "$HOSTADDRESS$" -l "$HOSTALIAS$" -e "$HOSTNOTES$" -u "$HOSTACTIONURL$" -r "$HOSTNOTESURL$" -m "$NOTIFICATIONCOMMENT$" --energymonitorsite "https://demo-monitor.energylogserver.pl/"  }
```

<br>

```
#!/usr/bin/env python3.6
# https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/macrolist.html
# https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
import argparse
import requests
from urllib.parse import quote

def send_discord_notification(webhook_url, embed):
    data = {
        "username": "Webhook ENERGY MONITOR",
        "embeds": [embed]
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}, Response: {response.text}")

def main():
    parser = argparse.ArgumentParser(description='Send notification to Discord.')
    parser.add_argument('-c', '--contactemail', type=str, required=True, help='Contact email (webhook URL)')
    parser.add_argument('-t', '--notificationtype', type=str, required=False, help='Notification type')
    parser.add_argument('-o', '--hostoutput', type=str, required=False, help='Host output')
    parser.add_argument('-d', '--longdatetime', type=str, required=False, help='Date and time')
    parser.add_argument('-n', '--hostname', type=str, required=False, help='Host name')
    parser.add_argument('-s', '--hoststate', type=str, required=False, help='Host state')
    parser.add_argument('-a', '--hostaddress', type=str, required=False, help='Host address')
    parser.add_argument('-l', '--hostalias', type=str, required=False, help='Host alias')
    parser.add_argument('-e', '--hostnotes', type=str, required=False, help='Host notes')
    parser.add_argument('-u', '--hostactionurl', type=str, required=False, help='Host action URL')
    parser.add_argument('-r', '--hostnotesurl', type=str, required=False, help='Host notes URL')
    parser.add_argument('-f', '--servicedesc', type=str, required=False, help='Service description')
    parser.add_argument('-g', '--servicestate', type=str, required=False, help='Service state')
    parser.add_argument('-p', '--serviceactionurl', type=str, required=False, help='Service action URL')
    parser.add_argument('-i', '--servicenotesurl', type=str, required=False, help='Service notes URL')
    parser.add_argument('-j', '--servicedowntime', type=str, required=False, help='Service downtime')
    parser.add_argument('-k', '--serviceoutput', type=str, required=False, help='Service output')
    parser.add_argument('-m', '--notificationcomment', type=str, required=False, help='Notification comment')
    parser.add_argument('--energymonitorsite', type=str, required=False, help='Energy Monitor site URL')
    args = parser.parse_args()

    webhook_url = args.contactemail  # Use contact email as the webhook URL

    # Mapping states to colors (hex) and emojis
    state_colors = {
        "OK": 0x00FF00,       # Green
        "UP": 0x00FF00,       # Green
        "DOWN": 0xFF0000,     # Red
        "CRITICAL": 0xFF0000, # Red
        "WARNING": 0xFFFF00,  # Yellow
        "UNKNOWN": 0xA9A9A9   # Dark Gray
    }

    state_emojis = {
        "OK": "✅",
        "UP": "✅",
        "DOWN": "❌",
        "CRITICAL": "❌",
        "WARNING": "⚠️",
        "UNKNOWN": "❓"
    }

    host_state_color = state_colors.get(args.hoststate, 0xA9A9A9)
    host_state_emoji = state_emojis.get(args.hoststate, "❓")

    # Create title based on host description
    title = f"{host_state_emoji} {args.hostname} is {args.hoststate}! {host_state_emoji}"

    # Create fields for embed
    fields = [
        {"name": "Notification Type", "value": args.notificationtype, "inline": True},
        {"name": "Host Output", "value": args.hostoutput, "inline": True},
        {"name": "Date and Time", "value": args.longdatetime, "inline": True},
        {"name": "Host Name", "value": args.hostname, "inline": True},
        {"name": "Host State", "value": args.hoststate, "inline": True},
        {"name": "Host Address", "value": args.hostaddress, "inline": True},
        {"name": "Host Alias", "value": args.hostalias or "N/A", "inline": True},
    ]

    embed = {
        "title": "title123",
        "color": host_state_color,
        "description": "testestest", 
        "author": {
            "name": "ENERGY MONITOR"
        }
    }

    if args.hostactionurl:
        fields.append({"name": "Host Action URL", "value": args.hostactionurl, "inline": True})

    if args.hostnotes:
        fields.append({"name": "Host Notes", "value": args.hostnotes, "inline": True})

    if args.serviceactionurl:
        fields.append({"name": "Service Action URL", "value": args.serviceactionurl, "inline": True})

    if args.hostnotesurl:
        fields.append({"name": "Host Notes URL", "value": args.hostnotesurl, "inline": True})

    if args.energymonitorsite:
        energymonitorsite = args.energymonitorsite.rstrip('/')
        host_details_url = f"{energymonitorsite}/monitor/index.php/status/service/{quote(args.hostname)}"
        fields.append({"name": "Host Details", "value": host_details_url, "inline": False})
        if args.servicedesc:
            service_details_link = f"{energymonitorsite}/monitor/index.php/extinfo/details?host={quote(args.hostname)}&service={quote(args.servicedesc)}"
            fields.append({"name": "Service Details", "value": service_details_link, "inline": False})
            embed["url"] = service_details_link
        else:
            embed["url"] = host_details_url

    if args.notificationcomment:
        fields.append({"name": "Notification Comment", "value": args.notificationcomment, "inline": True})

    send_discord_notification(webhook_url, embed)

if __name__ == "__main__":
    main()



```

<br>

- notify_by_service-discord.py  

```
#!/usr/bin/env python3.6
# https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/macrolist.html
# https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
import argparse
import requests
from urllib.parse import quote

def send_discord_notification(webhook_url, embed):
    data = {
        "username": "Webhook ENERGY MONITOR",
        "embeds": [embed]
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}, Response: {response.text}")

def main():
    parser = argparse.ArgumentParser(description='Send notification to Discord.')
    parser.add_argument('-c', '--contactemail', type=str, required=True, help='Contact email (webhook URL)')
    parser.add_argument('-t', '--notificationtype', type=str, required=False, help='Notification type')
    parser.add_argument('-d', '--longdatetime', type=str, required=False, help='Date and time')
    parser.add_argument('-n', '--hostname', type=str, required=False, help='Host name')
    parser.add_argument('-s', '--hoststate', type=str, required=False, help='Host state')
    parser.add_argument('-a', '--hostaddress', type=str, required=False, help='Host address')
    parser.add_argument('-l', '--hostalias', type=str, required=False, help='Host alias')
    parser.add_argument('-e', '--hostnotes', type=str, required=False, help='Host notes')
    parser.add_argument('-u', '--hostactionurl', type=str, required=False, help='Host action URL')
    parser.add_argument('-r', '--hostnotesurl', type=str, required=False, help='Host notes URL')
    parser.add_argument('-f', '--servicedesc', type=str, required=False, help='Service description')
    parser.add_argument('-g', '--servicestate', type=str, required=False, help='Service state')
    parser.add_argument('-p', '--serviceactionurl', type=str, required=False, help='Service action URL')
    parser.add_argument('-i', '--servicenotesurl', type=str, required=False, help='Service notes URL')
    parser.add_argument('-j', '--servicedowntime', type=str, required=False, help='Service downtime')
    parser.add_argument('-k', '--serviceoutput', type=str, required=False, help='Service output')
    parser.add_argument('-m', '--notificationcomment', type=str, required=False, help='Notification comment')
    parser.add_argument('-z', '--hostsdowntime', type=str, required=False, help='Hosts downtime')
    parser.add_argument('--energymonitorsite', type=str, required=False, help='Energy Monitor site URL')
    args = parser.parse_args()

    webhook_url = args.contactemail  # Use contact email as the webhook URL

    # Mapping states to colors (hex) and emojis
    state_colors = {
        "OK": 0x00FF00,       # Green
        "UP": 0x00FF00,       # Green
        "DOWN": 0xFF0000,     # Red
        "CRITICAL": 0xFF0000, # Red
        "WARNING": 0xFFFF00,  # Yellow
        "UNKNOWN": 0xA9A9A9   # Dark Gray
    }

    state_emojis = {
        "OK": "✅",
        "UP": "✅",
        "DOWN": "❌",
        "CRITICAL": "❌",
        "WARNING": "⚠️",
        "UNKNOWN": "❓"
    }

    service_state_color = state_colors.get(args.servicestate, 0xA9A9A9)
    service_state_emoji = state_emojis.get(args.servicestate, "❓")

    # Create title based on service state and host/service description
    title = f"{service_state_emoji} {args.servicedesc} on {args.hostname} is {args.servicestate}! {service_state_emoji}"

    # Create fields for embed
    fields = [
        {"name": "Date and Time", "value": args.longdatetime, "inline": True},
        {"name": "Host Name", "value": args.hostname, "inline": True},
        {"name": "Host State", "value": args.hoststate, "inline": True},
        {"name": "Host Address", "value": args.hostaddress, "inline": True},
        {"name": "Host Alias", "value": args.hostalias, "inline": True},
        {"name": "Service Description", "value": args.servicedesc, "inline": True},
        {"name": "Service State", "value": args.servicestate, "inline": True},
        {"name": "Service Downtime", "value": args.servicedowntime or "N/A", "inline": True},
        {"name": "Service Output", "value": args.serviceoutput, "inline": True},
        {"name": "Hosts Downtime", "value": args.hostsdowntime or "N/A", "inline": True}
    ]

    embed = {
    "title": "Test Notification",
    "description": "This is a test.",
    "color": service_state_color,  # green
    "fields": [
        {"name": "Host", "value": "ASTA-NET", "inline": True},
        {"name": "Status", "value": "UP", "inline": True}
    ],
    "author": {"name": "ENERGY MONITOR"}
}

    if args.hostactionurl:
        fields.append({"name": "Host Action URL", "value": args.hostactionurl, "inline": True})

    if args.hostnotes:
        fields.append({"name": "Host Notes", "value": args.hostnotes, "inline": True})

    if args.serviceactionurl:
        fields.append({"name": "Service Action URL", "value": args.serviceactionurl, "inline": True})

    if args.hostnotesurl:
        fields.append({"name": "Host Notes URL", "value": args.hostnotesurl, "inline": True})

    if args.servicenotesurl:
        fields.append({"name": "Service Notes URL", "value": args.servicenotesurl, "inline": True})

    if args.energymonitorsite:
        energymonitorsite = args.energymonitorsite.rstrip('/')
        host_details_url = f"{energymonitorsite}/monitor/index.php/status/service/{quote(args.hostname)}"
        fields.append({"name": "Host Details", "value": host_details_url, "inline": False})
        if args.servicedesc:
            service_details_link = f"{energymonitorsite}/monitor/index.php/extinfo/details?host={quote(args.hostname)}&service={quote(args.servicedesc)}"
            fields.append({"name": "Service Details", "value": service_details_link, "inline": False})
            embed["url"] = service_details_link
        else:
            embed["url"] = host_details_url

    if args.notificationcomment:
        fields.append({"name": "Notification Comment", "value": args.notificationcomment, "inline": True})

    send_discord_notification(webhook_url, embed)

if __name__ == "__main__":
    main()


```



### Checking if the script works properly

To check the set up, the adiministrator can do the following:

-   from /opt/energy-monitory/notify:

```
python3 /opt/energy-monitor/notify/notify_by_host-discord.py   -c "webhook_URL" -n "hostname" -s "state" -l "label/alias"
```
```
python3 /opt/energy-monitor/notify/notify_by_host-discord.py -c https://discord.com/api/webhooks/1377647158395928596/6q1SjBP6ujA7YXvpcjwa3WkEhN9uWvTqfsbsrGYnQShp07lGzwmVd2wgL4vUewIQIA4K -n "ASTA-NET" -s "UP" -l "Main Server"
```
<br>

```
python3 /opt/energy-monitor/notify/notify_by_service-discord.py   -c "webhook" -n "hostname" -s "state" -l "label/alias"
```
```
python3 /opt/energy-monitor/notify/notify_by_service-discord.py -c https://discord.com/api/webhooks/1377647158395928596/6q1SjBP6ujA7YXvpcjwa3WkEhN9uWvTqfsbsrGYnQShp07lGzwmVd2wgL4vUewIQIA4K -n "ASTA-NET" -s "UP" -l "Main Server"
```

-   This will send the most mandatory information in the payload, if everything is working properly, You should see "**Notification sent successfully**"

![Integration_with_Discord](/media/05_00_28_06_Integration_with_Discord.png)

In your Discord server, you will receive the notification. 

![Integration_with_Discord](/media/05_00_28_07_Integration_with_Discord.png)



