ColumnHeader
============

.. py:class:: ColumnHeader


   Bases: :py:class:`object`


Cython implementation of _ColumnHeader


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ConsensusMap_1_1ColumnHeader.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: ColumnHeader.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:attribute:: ColumnHeader.filename




.. py:method:: ColumnHeader.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: ColumnHeader.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: ColumnHeader.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:attribute:: ColumnHeader.label




.. py:method:: ColumnHeader.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: ColumnHeader.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: ColumnHeader.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: ColumnHeader.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:attribute:: ColumnHeader.size




.. py:attribute:: ColumnHeader.unique_id




