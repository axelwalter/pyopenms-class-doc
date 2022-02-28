Acquisition
===========

.. py:class:: Acquisition


   Bases: :py:class:`object`


Cython implementation of _Acquisition


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Acquisition.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: Acquisition.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: Acquisition.getIdentifier


Cython signature: String getIdentifier()




.. py:method:: Acquisition.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: Acquisition.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: Acquisition.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: Acquisition.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: Acquisition.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: Acquisition.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: Acquisition.setIdentifier


Cython signature: void setIdentifier(const String & identifier)




.. py:method:: Acquisition.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




