# json_tools

A tool for analysis json content


## install

```shell
pip install json-tools-python
```

## How to use

```python
import json_tools
test_data = {
    'a':{
        'b':{
            'c':'123',
            'd':{
                'c':123,
            },
            'e':[{'a':1}, {'b':2}, {'c':3}],
            'f':[
                {'a':
                    {'c':1}
                },
                {'b':
                    {'c':2}
                }
            ]
        }
    }
}
for ret in json_tools.search(test_data, 'c'):
    print(ret)
```
result:
```python
['a', 'b', 'c']
['a', 'b', 'd', 'c']
['a', 'b', 'e', 2, 'c']
['a', 'b', 'f', 0, 'a', 'c']
['a', 'b', 'f', 1, 'b', 'c']
```