### demjson
```
import demjson

# from
js_obj = '{x:1, y:2, z:3}'

# to
py_obj = demjson.decode(js_obj)
```

### jsonnet
```
import json, _jsonnet

# from
js_obj = '{x:1, y:2, z:3}'

# to
py_obj = json.loads(_jsonnet.evaluate_snippet('snippet', js_obj))
```

### ast
```
import ast

# from
js_obj = "{'x':1, 'y':2, 'z':3}"

# to
py_obj = ast.literal_eval(js_obj)
```
