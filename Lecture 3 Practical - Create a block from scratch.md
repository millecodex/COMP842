
# Create a block from scratch


```python
# the hash library
import * from hashlib as hash
# data encoding service
import pickle
```

our block of data will contain many fields such as an:
    identifier
    time
    previous hash
    merkle root
    list of transactions
These can be stored in a python dictionary which is a key-value structure

dict = { key:value,
         key2:value2,
        .
        .
        keyn:valuen    
}


```python
block = {'height':1,
        'time':0,
        'prevHash':'000000000000000000000000',
        'merkleRoot': 'abcd'
        }
print(block)
```

    {'height': 1, 'time': 0, 'prevHash': '000000000000000000000000', 'merkleRoot': 'abcd'}
    


```python
code='jeff'
print(code)
```

    jeff
    


```python
import hashlib
hashedcode = hashlib.md5(code.encode())
print(hashedcode)
```

    <md5 HASH object @ 0x000001AC7386F878>
    
