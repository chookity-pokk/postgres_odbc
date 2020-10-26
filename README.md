# Postgres ODBC

Connecting to a postgres database and making/editing tables etc using the ODBC package in Python. Designed to pull in inventory from QuickBooks and push it to a remote server to help get away from reliance on QuickBooks for inventory management. Will ideally be run once a day to get the inventory log from that day and be pushed to a csv file or put straight into Excel and then saved to have a comprehensive list of inventory for different dates.

I have currently added a gui version of it that is able to push, pull, edit and import data into the database. The testing branch has a smoother experience and will probably make that the main branch but have yet to do so. Everything should be working without bugs or glitches.

All the code that is currently not being used but were just test scripts to see if/how certain function work are in the `Archive` folder and I moved all the different databases inside of the `Parts` folders to make the main script much smaller and cleaner. 

## Work in progress:
- Working on a way to view the data with `ttk.Treeview`. I need to figure out the scrollbar and how to change the box sizes within that becuase as of right now you can't really scroll over and view data past the first set because I haven't been able to get the scrollbar to work so once that is done and I figure out the box size and then it should be good to go. Also need to rename these to something like `view_db.py`

## Current issues:
- The placement of the dropdown menu is pretty garbage.
- Scrollbar not working for `view2.py`
- Box sizes too large on `view2.py`

## Resolved issues and how:
 - Fixed having more than one item opened from dropdown menu by adding `conn.commit()` which I totally spaced out on adding in and adding in `root.quit()` and `root.destroy()` where `root` is changed to the name of the tkinter window.
 - Fixed the auto complete for the edit menu with the error `name 'dimensions' is not defined in line 335` by changing the names to `name_editor` which is what it is called earlier. Not sure how that slipped through the cracks because I feel like I have tested that before.
 - Scrollbar not working for `view2.py`, fixed by getting rid of the `frame` which for some reason would make the bar super small and make it so you realistically couldn't scroll over within a reasonable amount of time because it look like 10 seconds to go over one column and there are 33 of them so it would take like 5 minutes just to get to the end.
 - Box sizes too large on `view2.py`, fixed by setting a `width`.
