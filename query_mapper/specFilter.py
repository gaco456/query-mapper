spec = "SPEC"
type = "TYPE"
key = "KEY"

types = ["DB-CONFIG","QUERY"]

def filter_spec(poj):
    try:
        spec_type = poj[spec][type]

        if spec_type in types:
            return type_div(poj, spec_type)
        else:
            # error ret
            print(spec_type , " can't match type")

    except KeyError as e:
        print("json has no attribute `spec`")


def type_div(poj , type):
    
    if type == "DB-CONFIG":
        del poj[spec]
        return "DB-CONFIG" , poj
    
    elif type == "QUERY":
        key_str = poj[spec][key]
        del poj[spec]
        return key_str , poj