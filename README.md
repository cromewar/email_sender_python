# Simple Gmail sender using SMTP protocol and HTML manipulation

This code it's a simple script wich allows to send emails from a **google gmail** account to any other email address, using a modificable HTML file.

## Usage 
Modify lines **9** to **11** on **main** to setup the info about the sender and the destinatary, also creating a subject.

### Example:

```python
email['from'] = 'Your Name'
email['to'] = 'destinatary_email@email.com'
email['subject'] = 'Sample Subject'
```

On line **13** you can modify all the variables you want to change in the HTML file, works as an dictionary so you can use any number of parameters.

On line **18** you must setup your gmail account, givin your username and password (Don't share it with anyone)

## HTML file

You can modify it as you want it, just remember to use **$** for each word you want to be replaced using the script.

## Note: 

In order to make the script work properly you must active an option on your gmail account.

Accont Settings > Less Secured Apps > turn it on.

Mor info on:

http://google.com - Less Secured Apps
[Google](https://support.google.com/accounts/answer/6010255)