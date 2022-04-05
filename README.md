# find_missing_trailers
Python script to iterate through multiple csv files to determine which trailers have not returned. A csv of missing trailers and their current location is created.

Trailer locations pulled from Orbcomm. Cleaned by an excel spreadsheet.
Last 48 hours departs pulled from GLS shipping reports. Cleaned by an excel spreadsheet.
Python script returns a csv of trailers that are not on the yard, and have not departed in the last 48 hours.

These spreadsheets and script have turned a 1-2 hour task into a 15 minute task.
