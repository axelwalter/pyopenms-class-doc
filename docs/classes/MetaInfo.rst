MetaInfo
========

.. py:class:: MetaInfo


   Bases: :py:class:`object`


Cython implementation of _MetaInfo


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaInfo.html


 A Type-Name-Value tuple class
 -----
 MetaInfo maps an index (an integer corresponding to a string) to
 DataValue objects.  The mapping of strings to the index is performed by
 the MetaInfoRegistry, which can be accessed by the method registry()
 -----
 There are two versions of nearly all members. One which operates with a
 string name and another one which operates on an index. The index version
 is always faster, as it does not need to look up the index corresponding
 to the string in the MetaInfoRegistry
 -----
 If you wish to add a MetaInfo member to a class, consider deriving that
 class from MetaInfoInterface, instead of simply adding MetaInfo as
 member. MetaInfoInterface implements a full interface to a MetaInfo
 member and is more memory efficient if no meta info gets added




.. py:method:: MetaInfo.clear


Cython signature: void clear()
Removes all meta values




.. py:method:: MetaInfo.empty


Cython signature: bool empty()
Returns if the MetaInfo is empty




.. py:method:: MetaInfo.exists


- Cython signature: bool exists(String name)
  Returns if this MetaInfo is set


- Cython signature: bool exists(unsigned int index)
  Returns if this MetaInfo is set




.. py:method:: MetaInfo.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MetaInfo.getKeysAsIntegers


Cython signature: void getKeysAsIntegers(libcpp_vector[unsigned int] & keys)




.. py:method:: MetaInfo.getValue


- Cython signature: DataValue getValue(String name)
  Returns the value corresponding to a string


- Cython signature: DataValue getValue(unsigned int index)
  Returns the value corresponding to an index


- Cython signature: DataValue getValue(String name, DataValue default_value)
  Returns the value corresponding to a string


- Cython signature: DataValue getValue(unsigned int index, DataValue default_value)
  Returns the value corresponding to an index




.. py:method:: MetaInfo.registry


Cython signature: MetaInfoRegistry registry()




.. py:method:: MetaInfo.removeValue


- Cython signature: void removeValue(String name)
  Removes the DataValue corresponding to `name` if it exists


- Cython signature: void removeValue(unsigned int index)
  Removes the DataValue corresponding to `index` if it exists




.. py:method:: MetaInfo.setValue


- Cython signature: void setValue(String name, DataValue value)
  Sets the DataValue corresponding to a name


- Cython signature: void setValue(unsigned int index, DataValue value)
  Sets the DataValue corresponding to an index




