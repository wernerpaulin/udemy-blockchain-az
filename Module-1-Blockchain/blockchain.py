# Module 1 - Create a Blockchain
# Packages required:
# python -m pip install --upgrade pip 
# pip install Flask
# Postman

import datetime
import hashlib 
import json
from flask import Flask, jsonify

print("Starting the Blockchain...")

# Part 1 - Building a Blockchain
class blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        

# Part 2 - Mining our Blockchain
