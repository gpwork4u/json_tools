# json_search tool

a tool for analysis json content with some key

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
for ret in json_tool.search(test_data, 'c'):
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