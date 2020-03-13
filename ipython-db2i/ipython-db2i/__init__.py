from IPython.core.magic import Magics, magics_class, cell_magic, line_magic, needs_local_scope
from IPython.config.configurable import Configurable

import pandas as pd
import pyodbc, re

conn = None

def load_ipython_extension(ip):
    global conn
    conn = None
    ip.register_magics(Db2iMagic)

def unload_ipython_extension(ip):
    pass

@magics_class
class Db2iMagic(Magics, Configurable):
    
    def __init__(self, shell):
        Configurable.__init__(self, config=shell.config)
        Magics.__init__(self, shell=shell)

    @needs_local_scope
    @line_magic('db2i')
    @cell_magic('db2i')
    def execute(self, line='', cell='', local_ns={}):
        global conn
        if not conn:
            print('No active connection')
            if line:
                try:
                    split = line.split('://')
                    if split[0] != 'ibmi+pyodbc': # TODO: regex for invalid connection string...
                        return 'Invalid connection string -> ibmi+pyodbc://user:pwd@host'

                    creds = re.split('@ |:', split[1])
                    host,user,pwd = creds[2], creds[0], creds[1]

                    conn = pyodbc.connect(driver='{IBM i Access ODBC Driver}', system=host, uid=user, pwd=pwd)
                    print('Successfully connected to {} as {}'.format(host, user))
                except Exception as e:
                    return 'Failed to connect with passed connection string\n    ' + str(e)

        sql = ' '.join([x.replace('{','{{').replace('}','}}').replace('\n','').strip() for x in cell.split('\n')])
        if len(sql) > 0:
            sql = sql.format(**globals())
            if line.strip() != '-':
                return pd.read_sql(sql, conn)
            else:
                conn.execute(sql)
        else:
            print('Cannot execute blank query')
