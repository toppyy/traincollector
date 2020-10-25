# Train location collector

The program collects the current location of trains in Finland (from [Digitraffic API](https://www.digitraffic.fi/en/railway-traffic/) with a given time interval.

## Installation

Assuming you have pip and python installed, call `pip install -r ./packages.txt`
after cloning the project.

## Collect train data

Calling `python3 collect.py 10` will store the location of trains into *./data/data.csv* every 10 seconds (the default is 5).

## Structure of the data

The output file is a CSV with ";" as a separator.

The columns are the following:
- Train number
- Departure date
- Timestamp
- Coordinate (lat)
- Coordinate (lon)
- Speed (km/h)



