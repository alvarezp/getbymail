getbymail
=========

Script that check an email account for messages and can trigger actions according to instructions in these messages.

I have plenty access to mail and Google, but I can't browse Internet. I usually receive a bunch of links that I'm unable to open. I can search terms on Google, but I can't browse the Google results, this was the reason to create a script that does the following:

This script can be executed periodically in a server/PC, it will check an email account and open the older of all the unread messages, extract the commands on it and trigger an action.

Right now it can only download a file or a web page, there is a lot to do.

Even though right now this script works, it's in an early stage since I have some kind of recursive problem, I can't browse Internet to learn more python and then code this script, and I do not know enough python to code this script and then have access to Internet pages.

Working
=======

It reads the subject of the message and search for two parameters, the first is the command and the second is the URL.

Commands
--------

   downloadfile = Download the file, compress it in a zip file and send it via email.

   downloadpage = Download the page, compress it in a zip file and send it via email.

Meaning that if the subject is "downloadfile http://www.cadaver.me/presentation.svg", it will download the file, will zip it and send it to the sender.


To do
=====

-Download "full" sites recursively.

-Read body of messages so It can receive multiple instructions in the same message.

-Open all unread messages on a single execution.
