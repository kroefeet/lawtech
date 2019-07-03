#!/bin/bash
#get content file name

echo What is the name of your content page? ex-'index.html'

read pagename

cat templates/top.html content/$pagename templates/bottom.html > docs/$pagename

location=docs/$pagename

echo your page is now available at $location
