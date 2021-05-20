import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library (e.g., collections.OrderedDict).
#       Implement the data structure yourself.
class Node:
  def __init__(self, data, prev_node=None, next_node=None):
    self.prev = prev_node
    self.data = data
    self.next = next_node
  
  def get_data(self):
    return self.data

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def get_tail(self):
    return self.tail
  
  def get_head(self):
    return self.head
  
  def append(self, data):
    if self.head is None:
      self.head = Node(data)
      self.tail = self.head
    new_node = Node(data, self.tail, None)
    self.tail.next = new_node
    return

  def delete_mid(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev

  def delete_head(self):
    self.head.next.prev = None
    self.head = self.head.next
  
  def get_all(self):
    ret_list = []
    current_node = self.tail
    while current_node:
      ret_list.append(current_node.data[0])
      current_node = current_node.prev
    return ret_list
  
  def print(self):
    temp = self.head
    while(temp is not None):
        print(temp.data, end=' ')
        temp = temp.get_next()

dlltest = DoublyLinkedList()
dlltest.append(1)
dlltest.append(2)
dlltest.append(3)
dlltest.print()


class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):
    ###########################
    # Write your code here :) #
    ###########################
    self.size = n
    self.cache_dict = {}
    self.dll = DoublyLinkedList()

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL
  def access_page(self, url, contents):
    ###########################
    # Write your code here :) #
    ###########################

    if self.cache_dict.get(url) == None:
      if len(self.cache_dict) < self.size:
        self.dll.append((url, contents))
        self.cache_dict[url] = self.dll.get_tail()
      else:
        self.cache_dict.pop(dll.get_head.data[0])
        self.dll.delete_head()
        self.dll.append((url, contents))
        self.cache_dict[url] = self.dll.get_tail()
    else:
      self.dll.delete_mid(cache_dict[url])
      self.dll.append((url, contents))
      self.cache_dict[url] = self.dll.get_tail()

  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    ###########################
    # Write your code here :) #
    ###########################
    return self.dll.get_all()

  def dict_debug(self):
    return self.cache_dict


# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  equal(cache.get_pages(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  equal(cache.get_pages(), ["a.com"])
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  
  # print(cache.dict_debug())
  # print(cache.get_pages())

  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["b.com", "a.com"])
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
  cache.access_page("c.com", "CCC")
  equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)

if __name__ == "__main__":
  cache_test()
