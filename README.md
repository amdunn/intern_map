intern_map
==========

This is the screen scraping piece of the intern map project.  It
includes:

- Chrome extension (src/where_ext)
- Script to run Chrome, get a return value out of HTML5 local storage
  (if there's a way to just get Chrome to print to a file, this is
  probably better than the hacky thing I did here)
  (src/get_where)

The other piece of the project is being kept in a separate repository
(intern_map_app) because one can use an existing repository directly
with Heroku.
