# Postgres ODBC

Connecting to a postgres database and making/editing tables etc using the ODBC package in Python. Designed to pull in inventory from QuickBooks and push it to a remote server to help get away from reliance on QuickBooks for inventory management. Will ideally be run once a day to get the inventory log from that day and be pushed to a csv file or put straight into Excel and then saved to have a comprehensive list of inventory for different dates.

I have currently added a gui version of it that is able to push, pull, edit and import data into the database. The testing branch has a smoother experience and will probably make that the main branch but have yet to do so. Everything should be working without bugs or glitches.

## Current issues:
 - The placement of the dropdown menu is pretty garbage.
----
## Resolved issues and how:
 - Fixed having more than one item opened from dropdown menu by adding `conn.commit()` which I totally spaced out on adding in.