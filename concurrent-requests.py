#!/usr/bin/python3

import requests
import hashlib
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed

def hashGenerator():
	# Generating an array of possible hashes
	hashes = []
	brute_range = range(0,10 ** 2)
	for v in brute_range:
		new_hash = str(v)
		sha_hash = hashlib.sha1(new_hash.encode()).hexdigest()
		hashes.append(sha_hash)
	return hashes

def concurrentRequests():
	# Random hash generator
	hashes = hashGenerator()

	# Using futures for async response
	session = FuturesSession()
	url = 'url'
	futures = []

	# Requests
	for h in hashes:
		future = session.get(url + "&param=" + h)
		future.h = h
		futures.append(future)

	# Responses
	for future in as_completed(futures):
		resp = future.result()
		if "unique term" in resp.text:
			print("Success")

def main():
	concurrentRequests()

if __name__ == "__main__":
    main()