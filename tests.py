from django.test import TestCase
import httplib

httpServ = httplib.HTTPConnection("localhost", 8000)
httpServ.connect()


def checksnippet_detail():
	n=1
	while n
		bod="/snippets/"+n+"/"
		httpServ.request('GET', bod)
		if response.status == 404:
			print "Unautorized access"
			n=n+1
			Sys.exit(n)





