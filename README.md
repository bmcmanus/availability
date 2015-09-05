Introduction
============
Calendaring across organizations is hard. Sharing availability is impossible. 

Questions like this are common:
> Hey Brian, shoot me over some times that work for you to talk about _'why my hair is on fire, and how you need to fix it for me.'_

Oh, great. Let me pull up my Calendar, my email client and type out a few times that I am available and email them to you. That's exactly what I have time for...!

> Dear corporate project-manager. Thanks for your note. 
>
> The following times work for me:
> 
> |        |      |                                              |
> | ------ | ---- | --------------------------------------------:|
> | T      | 9/01 | 8:00AM - 12:00PM MDT / 10:00AM - 2:00PM EDT  |
> | W      | 9/02 | 10:00AM - 11:00AM MDT / 12:00AM - 1:00PM EDT |
> | R      | 9/03 | 2:00PM - 4:00PM MDT / 4:00PM - 6:00 PM EDT   |
>
> Let me know, what works for you?
>
> Brian

To hell with that. This script loops my Calendar, generates a nice and well-formatted response like this that I can simply forward on.

Getting started
===============
```
git clone https://github.com/bmcmanus/availability.git
pyvenv-3.4 availability
cd availability
source bin/activate
pip install -r requirements.txt
   
EXCHANGE_USERNAME="uglydomain.local\\brian"
EXCHANGE_PASSWORD="secret"
EXCHANGE_URL="https://remote.corporateserver.com/EWS/Exchange.asmx"
python main.py
```

Project management
==================
COMPLETE
--------
* I wasn't too keen on the pyexchange interface, so I wrote an adapter module around pyexchange.


TODO
----
* Implement 'recursive function' (or simple list comprehension) that iterates over events building up availability time blocks.
* Implement 'doctopt' so that paramaters like calendar system (gmail or exchange), credentials, working-hours, timezone, and start/stop periods can be specified on the command line.
* Deprecate using environment variable. That was a quick hack.
