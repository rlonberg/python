"""Implementation of the Map ADT using closed hashing and a probe with 
double hashing.
"""

class HashMap :
  """ A closed hashing (one key per slot) with a double hashing
      probe (2 hash functions)"""

  def __init__( self, capacity):                                     
    """Creates an empty map instance."""

    # Define the size of the table
    self.CAP = capacity

    # Create the data storage (empty hash table)
    self._array = [None] * self.CAP

    # how many items in the array
    self._size = 0
    
    # how many collisions so far
    self._collisions = 0

    # how can we iterate through our array
    self._step = 0
      
  def __len__( self ):
    """Returns the number of entries in the map."""
    return self._size

  def _hash1( self, key ):                               
    """The main hash function for mapping keys to table entries."""
    return abs( hash( key ) ) % len( self._array )
  
  def _hash2( self, key ):
    """ The second hash function used for backup."""
    return 1 + abs( hash( key ) ) % ( len( self._array ) - 2 )    
  

  def add( self, key, value ):
    """ If the key does not exist, adds a new entry to the map.
        If the key exists, update its value.
    """
    slot, contents = self._lookup( self._hash1, key )
    slot_2, contents_2 = self._lookup( self._hash2, key)

    if contents == None and contents_2 == None:
        if slot != None:
            self._array[slot] = _MapEntry(key,value)
            self._size += 1
        elif slot == None and slot_2 != None:
            self._array[slot_2] = _MapEntry(key,value)
            self._size += 1
        else:
            self._collisions += 1
            #print("fatal collision")

    elif contents == None and isinstance(contents_2, _MapEntry):
        if contents_2.key != key:
            if slot != None:
                self._array[slot] = _MapEntry(key,value)
                self._size += 1
            else:
                self._collisions += 1
                #print("fatal collision")
        else:
            self._array[slot_2] = _MapEntry(key,value)
            self._size += 1

    elif isinstance(contents, _MapEntry) and contents_2 == None:
        if contents.key == key:
            self._array[slot] == _MapEntry(key, value)
            self._size += 1
        else:
            if slot_2 != None:
                self._array[slot_2] == _MapEntry(key, value)
                self._size += 1
            else:
                self._collisions += 1
                #print("fatal collision")
    else:
        if slot != None: #and slot_2 == None or != None:
            self._array[slot] == _MapEntry(key, value)
            self._size += 1
        else:
            if slot_2 != None:
                self._array[slot_2] == _MapEntry(key, value)
                self._size += 1
            else:
                self._collisions += 1
                #print("fatal collision")
      
  def peek( self, key ):
    """ Returns the value associated with the key or returns None."""
    slot,contents = self._lookup(self._hash1, key)
    if contents == None:
      slot,contents = self._lookup(self._hash2, key)
      
    if contents == None:
      return None
    else:
      return contents.value

  def _lookup(self, hashFunction, key):
    """ Returns the slot matching the key and its contents.
        Returns slot,None if slot it should occupy is empty.
        Rteurns None,None if the slot it should occupy has other contents. """
    
    slot = hashFunction( key )
    contents = self._array[slot]
    if contents == None:
      return slot, None
    elif contents.key != key:
      return None, None
    else:
      return slot, contents

    
  def __iter__(self):
    """ Return an iterator for the hashmap. """
    return _MapIterator(self)
  
  def printStats( self ):
    """Print the number of items in the table and the total
    number of collisions due to insertion."""
    print( 'Entry count : ', self._size )
    print( 'Collision count : ', self._collisions )

  def remove( self, key ):
    """ Removes the entry associated with the key.
        If the key is not in the map, does nothing. """

    slot, contents = self._lookup(self._hash1,key)
    
    if contents != None:
        if contents.key == key:
            self._array[slot] = None
            self._size -= 1
        else:
            slot, contents = self._lookup(self._hash2,key)
            if contents == None:
                pass
            elif contents.key == key:
                self._array[slot] = None
                self._size -= 1
            else:
                pass
    else:
        slot, contents = self._lookup(self._hash2,key)
        if contents == None:
            pass
        elif contents.key == key:
            self._array[slot] = None
            self._size -= 1
        else:
            pass
        

# Storage class for holding a key/value pair.   
class _MapEntry :                       

  def __init__( self, key, value ):
    """Create the entry with key and value """
    self.key = key
    self.value = value 
  
  def __eq__( self, other ):
    """Overload __eq__ so key, value pairs can be compared using '==' """
    if other == None:
      return False
    return ( self.key == other.key and self.value == other.value )

class _MapIterator():
  def __init__(self,structure):
    """ Constructs the iterator, creating an empty data field for data.
    """
    self._array = structure._array
    self._step = 0
    self._cap = structure.CAP
    
  def __next__(self):
    """ Returns the next data in order in the ADT.
    If there is no next data, raise a StopIteration exception.
    """

    while True:
      if self._step == self._cap:
          break
        
      item = self._array[self._step]
      self._step += 1
      if item != None:
        return item.key#.key,item.value
        
    
    raise StopIteration()



