import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def create_insert_query(table_name, params):
    keys = params.keys()
    values = params.values()
    columns = '('+','.join(keys)+')'
    values = '(\''+'\',\''.join(values)+'\')'
    query = "INSERT INTO %s%s VALUES%s;" % (table_name,columns,values)
    logger.info("Query %s" % query)
    return query

def create_update_query(table_name, params, where_fields):
    set_clause = []
    for key,value in params.items():
        clause_str = " %s = '%s'" % (key,value)
        set_clause.append(clause_str)
    set_clause = ','.join(set_clause)
    where_clause = []
    for key,value in where_fields.items():
        clause_str = " %s = '%s'" % (key,value)
        where_clause.append(clause_str)
    where_clause = ' WHERE '+(' and '.join(where_clause))
    query = "UPDATE %s SET %s %s;" % (table_name,set_clause,where_clause)
    logger.info("Query %s" % query)
    return query

def create_delete_query(table_name, where_fields):
    where_clause = []
    for key,value in where_fields.items():
        clause_str = " %s = '%s'" % (key,value)
        where_clause.append(clause_str)
    where_clause = ' WHERE '+(' and '.join(where_clause))
    query = "DELETE FROM %s %s" % (table_name, where_clause)
    logger.info("Query %s" % query)
    return query

def create_get_query(table_name, where_fields, data=False):
    where_clause = []
    for key,value in where_fields.items():
        clause_str = " %s = '%s'" % (key,value)
        where_clause.append(clause_str)
    if where_clause:
        where_clause = ' WHERE '+(' and '.join(where_clause))
    else:
        where_clause = ''
    limit_clause = ''
    if data and 'limit' in data:
        data['limit'] = int(data['limit'])
        limit_clause = 'LIMIT %s' % data['limit']
    if data and 'page_no' in data:
        data['page_no'] = int(data['page_no'])
        limit_clause+= ', %s' % (data['page_no']*data['limit'])
    query = "SELECT * FROM %s %s %s" % (table_name, where_clause, limit_clause)
    logger.info("Query %s" % query)
    return query
