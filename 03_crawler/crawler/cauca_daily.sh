#!/bin/bash

start=`date +"%Y-%m-%d" -d "-1 day"`
echo $start
scrapy crawl cauca_day --set FEED_URI=output_2013.json --set FEED_FORMAT=json --set START=$start -s END=$start
