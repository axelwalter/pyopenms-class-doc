ParamNode
=========

.. py:class:: ParamNode


   Bases: :py:class:`object`


Cython implementation of _ParamNode


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Param_1_1ParamNode.html




.. py:attribute:: ParamNode.description




.. py:attribute:: ParamNode.entries




.. py:method:: ParamNode.findEntryRecursive


Cython signature: ParamEntry * findEntryRecursive(const String & name)




.. py:method:: ParamNode.findParentOf


Cython signature: ParamNode * findParentOf(const String & name)




.. py:method:: ParamNode.insert


- Cython signature: void insert(ParamNode & node, const String & prefix)
- Cython signature: void insert(ParamEntry & entry, const String & prefix)




.. py:attribute:: ParamNode.name




.. py:attribute:: ParamNode.nodes




.. py:method:: ParamNode.size


Cython signature: size_t size()




.. py:method:: ParamNode.suffix


Cython signature: String suffix(const String & key)




