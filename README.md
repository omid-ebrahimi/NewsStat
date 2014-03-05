NewsStat
========

Get news stat frome these sites:

1- Facebook

2- Google+

3- Twitter

4- Linkedin

5- Pinterest


Introduction:
=============

This is a web-service for giving news popularity.

You can send url of news and receive number of shares in Facebook, Twitter, Google+, Linkedin, Pinterest
and Total-Share. by Total-Share you can estimate average popularity
of a news and compare to other news.


How to use?
===========

This is address of server (for example):

http://localhost:8080/

This is The link of news:

http://www.theguardian.com/higher-education-network/blog/2014/mar/01/mental-health-issue-phd-research-university

You must send this request to server:

http://localhost:8080/services/stat?url=http://www.theguardian.com/higher-education-network/blog/2014/mar/01/mental-health-issue-phd-research-university

You will receive a json like this:

'{"GPlus": 191.0, "Pinterest": 30, "Twitter": 1333, "LinkedIn": 86, "Facebook": 46217, "Total": 47857.0}'
