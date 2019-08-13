import shelve

db_name = 'local.db'
# with shelve.open(db_name) as db:
#     db['Country'] = ('Ukraine', 'USA')
#
#     for c in db.values():
#         print(c)


def create_item(key, value):
    with shelve.open(db_name) as db:
        db[key] = value



def get_item(key):
    with shelve.open(db_name) as db:
        return db.get(key)


create_item('Name', 'EZ')
print(get_item('Name'))
