class ArrayQueue:
	def _init_ (self):
		self._data=[ ]
		self._size=0
		self._front= 0
	
	def _len_(self):
		return self._size

	def is_empty(self):
		return self._size ==0
	
	def enqueue(self,e):
		self._data.append(e)
		self._size = self._size +1
	
	def dequeue (self):
		if self. is_empty():
			raise Empty ('Queue is empty')
		value = self._data[self._front]
		self._data[self._front]= None
		self._front= self._front+1
		self._size = self._size -1
		return value
		
	def first(self):
		if self. is_empty():
			raise Empty ('Queue is empty')
		return self._data[self._front]
		
q =ArrayQueue ()
q.enqueue(10)
q.enqueue(20)
print ('Queue :',q._data)
print('length of queue:', len(q))
print('Dequeue:',q.dequeue())
print('After Dequeue:',q._data)
