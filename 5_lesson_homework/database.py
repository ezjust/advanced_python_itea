import shelve

db_name = 'local.db'

with shelve.open(db_name) as db:
    db['Country'] = 'Ukraine'