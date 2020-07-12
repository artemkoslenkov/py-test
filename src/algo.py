import sys
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017", 27017)
db = client.tododb
col = db.todo_collection


def upd_match(uid, id):
    col.update_one({'_id': uid}, {'$push': {'match': id}})


def comp_offer(offer, id):
    m = col.find({'seeking': offer})
    for each in m:
        val = each.get('match')
        if val is not None:
            if id not in val:
                upd_match(each.get('_id'), id)
        else:
            upd_match(each.get('_id'), id)


def match():
    try:
        collection = col.find()
        for one in collection:
            comp_offer(one['offering'], one['id'])
    except:
        print("Unexpected error:", sys.exc_info()[0])
    return 0
