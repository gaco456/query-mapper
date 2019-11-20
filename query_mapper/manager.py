import os
from json import loads
from json import dump
from .specFilter import filter_spec

class Manager:

    qrys = {}
    db_config = None
    
    def __init__(self , resource_dir="./resources" , generateDefalutJson = True):
        self._resource_dir = resource_dir

        if generateDefalutJson:
            if os.path.exists(resource_dir):
                pass
            else:
                os.mkdir(resource_dir)

            self._generate_dbconfig_json()
            self._generate_dummy_json()

    def _generate_dbconfig_json(self):
        db_cfg = {"SPEC": { "TYPE": "DB-CONFIG"},"HOST": "","USER": "","PASSWD": "","DB": ""}

        if os.path.exists(os.path.join(self._resource_dir , 'db.json')):
            pass
        else:
            with open(os.path.join(self._resource_dir, 'db.json'), 'w') as fp:
                dump(db_cfg, fp, indent=4)

    def _generate_dummy_json(self):
        dummy = { "SPEC" : {
                    "TYPE" : "QUERY",
                    "KEY" : "dummy"
                },
                "INSERT" :
                {
                    "INSERT_SOME_QUERY" : "INSERT INTO (`test`) VALUES (`test`)",
                    "INSERT_SOME_QUERY2" : "INSERT INTO (`test`) VALUES (`test`)"
                },
                "SELECT" :
                {
                    "SELECT_SOME_QUERY" : "SELECT * from test",
                    "SELECT_SOME_QUERY2" : "SELECT * from test"
                },
                "DELETE" :
                {
                    "DELETE_SOME_QUERY" : "DELETE FROM test WHERE test=1",
                    "DELETE_SOME_QUERY2" : "DELETE FROM test WHERE test=1"
                },
                "ANYTHING":
                {

                }
            }
        if os.path.exists(os.path.join(self._resource_dir , 'dummy.json')):
            pass
        else:
            with open(os.path.join(self._resource_dir , 'dummy.json'), 'w') as fp:
                dump( dummy, fp , indent=4 )

    def read_resources(self):
        rs_dir = self._resource_dir
        json_list = os.listdir(rs_dir)

        for item in json_list:
            idict = loads(open(os.path.join(rs_dir , item)).read())
            key , res = filter_spec(idict)

            if key == "DB-CONFIG":
                Manager.db_config = res
            else:
                Manager.qrys[key] = res