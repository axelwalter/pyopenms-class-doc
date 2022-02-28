IdentificationData
==================

.. py:class:: IdentificationData


   Bases: :py:class:`object`


Cython implementation of _IdentificationData


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IdentificationData.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: IdentificationData.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: IdentificationData.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: IdentificationData.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: IdentificationData.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: IdentificationData.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: IdentificationData.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: IdentificationData.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: IdentificationData.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




