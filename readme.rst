This is the entire code for the SFST tour checkout system. It runs on top of Django (using the Satchmo app) and uses MySQL as the backend database.


Dev Setup
=========

Basic instructions to setup the dev environment. Assuming you're developing on Linux or *nix system (Mac etc.). Assume you have Python and pip installed. Using virutalenv is highly recommended.

To install all the app requirements do::

	pip install -r requirements.pip

To get a copy of the production database, do::
    1) make directory ../db_backups
    2) make directory /logs
    3) make file sfst.logs in /logs
    4) run: fab prod updatelocaldb


QA Environment
==============

Lives and runs at (burrito required for cookie settings/security):

	http://qa.securebookingshuttletours.com/?burrito

There is an Authorize.net sandbox environment that we use for testing/QA:

https://sandbox.authorize.net/
    username: mfarver89
    password: tivixRules!


Production Environment
======================

Lives and runs at:

	http://booking.sanfranshuttletours.com/


Mobile UI
=========

The common.minidetector app has a middleware that adds a 'mobile' boolean to requests. There is also a context_processor there so that 'is_mobile' is available in the templates.

There is a 'mobile' class appended to the body tag when in mobile mode. The only page that has different markup for mobile is the product page (around the calendar).

If you'd like to fake a mobile ui in a regular desktop browser append ?mobile=1 to any url.


Change Log
==========

May 24, 2011 - Bug relating to renaming of options within an option group. Since we don't re-generate the variations if a variations already exists for a tour on a certain day, then it can throw an exception if you try and book an option for which a corresponding variation is not found.
