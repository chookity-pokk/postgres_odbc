# Postgres ODBC

Connecting to a postgres database and making/editing tables etc using the ODBC package in Python. Designed to pull in inventory from QuickBooks and push it to a remote server to help get away from reliance on QuickBooks for inventory management. Will ideally be run once a day to get the inventory log from that day and be pushed to a csv file or put straight into Excel (with minimal adjustments) and then saved to have a comprehensive list of inventory for different dates.

I have currently added a gui version of it that is a work in progress as it is just showing 'first name', 'last name' and 'Id number'. That is there for testing reasons as I don't want to make a bunch of unnecessary columns while try to test because it'll just drag it out. As of 8/7/2020 the GUI is able to add stuff to the database, delete stuff from the database(only while using the ID number), push to a csv that you name(that was annoying to get working), see the records on the page(still haven't figured out the scrollbar though) and I believe edit entries. This is all still a work in progress though and isn't quite done.
