MetaInfoInterface
=================

.. py:class:: MetaInfoInterface


   Bases: :py:class:`object`


Cython implementation of _MetaInfoInterface


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaInfoInterface.html


 Interface for classes that can store arbitrary meta information
 (Type-Name-Value tuples).
 -----
 MetaInfoInterface is a base class for all classes that use one MetaInfo
 object as member.  If you want to add meta information to a class, let it
 publicly inherit the MetaInfoInterface.  Meta information is an array of
 Type-Name-Value tuples.
 -----
 Usage:
   k = []
   exp.getKeys(k) # explore available key-value pairs
   exp.getMetaValue("someMetaName")




.. py:method:: MetaInfoInterface.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MetaInfoInterface.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MetaInfoInterface.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MetaInfoInterface.getMetaValues


Cython signature: dict getMetaValues()


Returns all meta values in a Python dictionary.




.. py:method:: MetaInfoInterface.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MetaInfoInterface.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MetaInfoInterface.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MetaInfoInterface.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MetaInfoInterface.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MetaInfoInterface.setMetaValues


Cython signature: setMetaValues(dict values)


Sets the meta values given in the Python dictionary.




