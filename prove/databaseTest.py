#import pymongo
#from pymongo import MongoClient

#class DBConnection(object):
    
#    def __init__(self, host="localhost", port=27017, db="database"):
#        super().__init__()    
#        self.conn = MongoClient(host, port)[db]

#    def find(self, field, value):
#        elem = self.conn.dispositivi.find({ field : value })
#        for p in elem:
#            return p["login"]