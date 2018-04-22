#!/bin/bash

start=`date +"%Y-%m-%d" -d "$1"`
end=`date +"%Y-%m-%d" -d "-1 day"`

while [ "$start" != "$end" ] ; 
do 
        echo $start
        scrapy crawl woori -s FEED_FORMAT=json --set START=$start
#        scrapy crawl woori --set FEED_URI=woori_2013.json --set FEED_FORMAT=json --set START=$start
        start=`date +"%Y-%m-%d" -d "$start + 1 day"`; 
done;