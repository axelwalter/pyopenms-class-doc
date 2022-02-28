MetaInfoDescription
===================

.. py:class:: MetaInfoDescription


   Bases: :py:class:`object`


Cython implementation of _MetaInfoDescription


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaInfoDescription.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: MetaInfoDescription.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MetaInfoDescription.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
Returns a reference to the description of the applied processing




.. py:method:: MetaInfoDescription.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MetaInfoDescription.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MetaInfoDescription.getName


Cython signature: String getName()
Returns the name of the peak annotations




.. py:method:: MetaInfoDescription.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MetaInfoDescription.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MetaInfoDescription.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MetaInfoDescription.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MetaInfoDescription.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
Sets the description of the applied processing




.. py:method:: MetaInfoDescription.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MetaInfoDescription.setName


Cython signature: void setName(String name)
Sets the name of the peak annotations




