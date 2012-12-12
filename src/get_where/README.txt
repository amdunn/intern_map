The process (this could stand to be a bit more automated):

1) ./get_users.py <access token> > interns.txt

You can get an access token from the Graph API Explorer.

2) ./get_where.py interns.txt > intern_locs.txt

This relies on having Chrome terminate after each request for now, so
you'll have to quit Chrome while collecting data the way this is
currently written.  The reason is that Chrome otherwise would open up
new tabs in a current session.

You also have to install the special Chrome extension where_ext,
enable it for this part of processing, and ensure that you are logged
into Facebook throughout this time (i.e. keep yourself logged in with
cookies)

3) ./parse_where.py intern_locs.txt > intern_data.js

intern_data.js is the data used in the application.
