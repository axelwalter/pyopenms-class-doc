ElementDB
=========

.. py:class:: ElementDB


   Bases: :py:class:`object`


Cython implementation of _ElementDB


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ElementDB.html




.. py:method:: ElementDB.getElement


- Cython signature: const Element * getElement(const String & name)
- Cython signature: const Element * getElement(unsigned int atomic_number)




.. py:method:: ElementDB.hasElement


- Cython signature: bool hasElement(const String & name)
  Returns true if the db contains an element with the given name, else false


- Cython signature: bool hasElement(unsigned int atomic_number)
  Returns true if the db contains an element with the given atomic_number, else false




