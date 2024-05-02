
import pytest
from hash_table import HashTable

def test_delete_existing_key():
    ht = HashTable(10)
    ht.insert('key1', 'value1')
    assert ht.delete('key1') is True, "Should return True when deleting an existing key"
    assert ht.get('key1') is None, "Deleted key should not be found"

def test_delete_non_existing_key():
    ht = HashTable(10)
    ht.insert('key1', 'value1')
    assert ht.delete('key2') is False, "Should return False when trying to delete a non-existing key"

def test_delete_key_twice():
    ht = HashTable(10)
    ht.insert('key1', 'value1')
    ht.delete('key1')
    assert ht.delete('key1') is False, "Should return False when deleting an already deleted key"

def test_delete_from_collision():
    ht = HashTable(10)
    # Assuming hash function might collide 'key1' and 'key2' at the same index
    ht.insert('key1', 'value1')
    ht.insert('key2', 'value2')
    ht.delete('key1')
    assert ht.get('key1') is None, "Deleted key should not be found"
    assert ht.get('key2') == 'value2', "Other keys in the same bucket should not be affected by delete"
