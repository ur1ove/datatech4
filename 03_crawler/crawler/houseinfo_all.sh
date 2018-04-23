#!/bin/bash

scrapy crawl houseinfo -s FLUME_URL=http://dn01:50001 -s FEED_FORMAT=json -s START=$1 -s END=$2 --logfile /home/log/data3/houseinfo.log &




