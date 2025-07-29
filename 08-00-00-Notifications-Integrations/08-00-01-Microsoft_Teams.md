# Integrating Microsoft Teams with Energy Monitor

Energy Monitor allows for sending for notifications from hosts and services to your Microsoft Teams server. 

In order to set it up the following must be done:

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
You must have access to Power Automate, therefore you must have acquired Office365 license. 
</blockquote>

## Setting up 

1. Enter "**M365 Copilot**" -> "**Apps**" -> "**Power Automate**"


![Integration_with_MSTeams](/media/08_00_00_01_Integration_with_MSTeams.png)

2. Enter "**Templates**" -> "**Search Webhook**" -> "**Post to a chat when a webhook request is received**"

<blockquote style="border-left: 8px solid red; padding: 15px;"> <b>Note</b>: 
Energy Monitor accepts only webflows with ID 94557.
</blockquote>
<br>

3. "**Create**" -> "**Edit**" -> "**When a Teams webhook request is received**"

![Integration_with_MSTeams](/media/08_00_00_02_Integration_with_MSTeams.png)

4. "**Copy the url under "HTTP URL field"**" and "**Save**"

<br>

![Integration_with_MSTeams](/media/08_00_00_04_Integration_with_MSTeams.png)

5. In Energy Monitor "**create a contact**":

![Integration_with_MSTeams](/media/08_00_00_05_Integration_with_MSTeams.png)


What we want from this section is the "**Webhook**", which is a method for sending data in real-time using HTTPS requests, with the POST method. 

-   Webhook, the URL, must be placed as the value of a custom variable named "**_WEBHOOK**" 

![Integration_with_MSTeams](/media/08_00_00_06_Integration_with_MSTeams.png)

6.  In Microsoft Teams, in Workflows sub-app, You need to add the Webhook onto a team and channel, chosen for receiving notifications. 

    -   On the screenshot, the chosen option states to send an email when an event created by the workflow, occurs.

![Integration_with_MSTeams](/media/08_00_00_07_Integration_with_MSTeams.png)

7. If done correctly, the chat in the channel will be able to receive notifications from Energy Monitor. 

![Integration_with_MSTeams](/media/08_00_00_08_Integration_with_MSTeams.png)
![Integration_with_MSTeams](/media/08_00_00_09_Integration_with_MSTeams.png)

<blockquote style="border-left: 8px solid red; padding: 15px;"> <b>Note</b>: 
Please be mindful to pick the option with the ID of 94557. 
</blockquote>
<br>




