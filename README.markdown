# mcnotify : Minecraft Status Notifier

## What is this
mcnotify checks the status of a Minecraft server,
and post it to IFTTT if some changes is detected.

## Requirements
* Python >=3.5.1
	* pyvenv
* pip >= 7.1.2
* systemd
* Python libraries
	* mcstatus

## Install
The following script is the custom installation instructions for systemd in userspace .
It would be helpful if you have any advice about the installation.
(I am not familiar with Python package installation. 🙃)

``` sh
### create a virtual environment
$ pyvenv venv

### install requirements
$ venv/bin/python setup.py install

### install systemd services
$ python copy_systemd_services.py

### enable systemd.
$ systemctl --user enable mcnotify.timer
```

## Setup IFTTT Recipe
1. [Create a account of IFTTT](https://ifttt.com/join).
2. [Create a recipe](https://ifttt.com/myrecipes/personal/new) for mcnotify.
	1. Choose "Maker" as Trigger Channel.
	2. Choose "Receive a web request" as Trigger.
	3. Specify unique "Event Name" for mcnotify updates such as `server_status_changed`.
	4. Choose "Action Channel" which you like.
		* Twitter, Slack, IF Notification, SMS, Yo etc.
	5. Choose "Action" which you like.
	6. Complete Action settings.

## Settings
You have to create settings as `config.json` before using this application.
See below and <config.example.json>.

* host : host name of your Minecraft server. IP address or domain.
* port : port number of your Minecraft server. this must be a integer.
* ifttt\_uri : endpoint of [IFTTT Maker](https://ifttt.com/maker).
* recover\_msg : message when server recovers from dead status.
* dead\_msg : message when server dies.
* join\_msg : message when somebody joins.
* leave\_msg : message when somebody leaves.
* online\_msg : template text which 
* time\_format : template text for the time representation.
* savefile : file that the last status is saved to.

## Start a daemon
```sh
$ systemctl --user start mcnotify.timer
```

If settings is wrong, mcnotify.timer will stop and save occuerd errors.

## Uninstall

```sh
$ systemctl --user stop mcnotify.timer
$ systemctl --user disable mcnotify.timer
$ rm SYSTEMD_DIR/mcnotify.{timer,service}
$ rm PATH_TO_MCNOTIFY
```

