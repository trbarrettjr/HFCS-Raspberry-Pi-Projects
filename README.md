# HFCS-Raspberry-Pi-Projects
Raspberry Pi Code to teach to HFCS

This code was put together to teach students of HFCS some basic coding skills to get the Raspberry Pi to complete a task.

There are a couple of files to test with such as pressing a button and making an entry into a log file.
A file explaination is below!

Most of these programs utilize the [GPIOzero](https://github.com/gpiozero/gpiozero).

## button press time.py

The purpose of this little program is to show students how a computer sees a button press.

## latching relays.py

This is a touch and it will toggle a relay.  This shows the students howto make a simple on-off button.

## press to json.py

This file makes a json data and then writes it out to `log.txt`.  The idea was to show students how to collect and then store data.  The lesson explanation is related to time management and recording when you start and stop an activity.

## press to log.py

This file just writes a string to `log.txt`. Same lesson about time management.
