"query_mapper" 


stop writing sql query in your code .. like this.


    cursor.execute("SELECT concat(p.rolename, "_", perm) as perm FROM user_group ug, group_permission gp, agilesoda_permission p \
           WHERE ug.groupid = gp.groupid \
           AND gp.permissionid = p.permissionid \
           AND p.kind in ( 'service', 'tool' ) \
           AND ug.userid = ? \
           AND p.rolename = ?" , **args)
           
# usage

`pip install query-mapper`


make some test.py and copy this code
~~~~
from query_mapper import Manager 

manager = Manager()
manager.read_resources() 
print(manager.qrys)
print(manager.db_config)
~~~~
run  test.py
`python test.py`

~~~~
{'dummy': {'INSERT': {'INSERT_SOME_QUERY': 'INSERT INTO (`test`) VALUES (`test`)', 'INSERT_SOME_QUERY2': 'INSERT INTO (`test`) VALUES (`test`)'}, 'SELECT': {'SELECT_SOME_QUERY': 'SELECT * from test', 'SELECT_SOME_QUERY2': 'SELECT * from test'}, 'DELETE': {'DELETE_SOME
_QUERY': 'DELETE FROM test WHERE test=1', 'DELETE_SOME_QUERY2': 'DELETE FROM test WHERE test=1'}, 'ANYTHING': {}}}
{'HOST': '', 'USER': '', 'PASSWD': '', 'DB': ''}
~~~~
let's checkout printed out

and check on resources directory

~~~~
// dummy.json
{
    "SPEC": {
        "TYPE": "QUERY",
        "KEY": "dummy"
    },
    "INSERT": {
        "INSERT_SOME_QUERY": "INSERT INTO (`test`) VALUES (`test`)",
        "INSERT_SOME_QUERY2": "INSERT INTO (`test`) VALUES (`test`)"
    },
    "SELECT": {
        "SELECT_SOME_QUERY": "SELECT * from test",
        "SELECT_SOME_QUERY2": "SELECT * from test"
    },
    "DELETE": {
        "DELETE_SOME_QUERY": "DELETE FROM test WHERE test=1",
        "DELETE_SOME_QUERY2": "DELETE FROM test WHERE test=1"
    },
    "ANYTHING": {}
}
~~~~

~~~~
// db.json
{
    "SPEC": {
        "TYPE": "DB-CONFIG"
    },
    "HOST": "",
    "USER": "",
    "PASSWD": "",
    "DB": ""
}
~~~~
version 0.9 have 2 types QUERY , DB-CONFIG


### usage example


~~~~
// resources/example-account-db-querys.json

{
    "SPEC" : {
        "TYPE" : "QUERY",
        "KEY" : "account"
    },
    "INSERT" :
    {
        "INSERT_USER" :"INSERT INTO `user` (`userid`, `passwd`,`passwdsalt`) VALUES (%s, %s , %s);"
    },
    "DELETE" :
    {
        "DELETE_USER" : "DELETE FROM `user` WHERE  `userid`=%s;"
    },
    "SELECT" :
    {
        "QUERY_PASSWORD_BY_USERID" : "SELECT `passwd` , `passwdsalt` FROM user WHERE userid = %s;"
    },
    "UPDATE" :
    {
        "UPDATE_USER_PASSWORD" : "UPDATE `user` SET `passwd`=%s , `passwdsalt`=%s WHERE `userid`=%s;"
    }
}
~~~~

~~~~
from query_mapper import Manager

man = Manager()
man.read_resources()

accqrys = man.qrys['account']
qry = accqrys['INSERT']['INSERT_USER']

print("query : " , qry)
~~~~

~~~~
query :  INSERT INTO `user` (`userid`, `passwd`,`passwdsalt`) VALUES (%s, %s , %s);
~~~~