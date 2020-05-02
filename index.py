#!/usr/bin/python
import sys
import pandas as pandas

source_folder = '~/Downloads/'
activity = str(sys.argv[1])
source = pandas.read_csv(source_folder + 'activity_' + activity + '.csv')
to_keep = ['Split','Time','Distance','Avg Speed','Avg HR','Avg Bike Cadence',\
    'Normalized Power','Avg Power']

for column in ['Avg HR','Avg Bike Cadence','Normalized Power','Avg Power']:
   source[column] = source[column].replace('--', 0)
   source[column] = pandas.to_numeric(source[column], downcast ='integer',\
        errors='ignore')

destination = source[to_keep]
destination.to_csv(source_folder + 'converted.csv')

print('Successfully converted activity ' + activity)
