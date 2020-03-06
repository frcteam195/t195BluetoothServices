from frcteam195.database import connect


def get(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    columns = [column[0] for column in cursor.description]
    results = None
    for row in cursor.fetchall():
        results = dict(zip(columns, row))
    return results

def get_list(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results

def put(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    conn.commit()
    if cursor.rowcount < 1:
        return("failure")
    else:
        return("success")

