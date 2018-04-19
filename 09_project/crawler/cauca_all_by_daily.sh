#!/bin/bash

start=`date +"%Y-%m-%d" -d "$1"`
end=`date +"%Y-%m-%d" -d "-1 day"`

while [ "$start" != "$end" ] ; 
do 
        echo $start
        scrapy crawl cauca_day --set FEED_URI=output_2013.json --set FEED_FORMAT=json --set START=$start -s END=$start
        start=`date +"%Y-%m-%d" -d "$start + 1 day"`; 
done;