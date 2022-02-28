AcquisitionInfo
===============

.. py:class:: AcquisitionInfo


   Bases: :py:class:`object`


Cython implementation of _AcquisitionInfo


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1AcquisitionInfo.html
 -- Inherits from ['MetaInfoInterface']




.. py:method:: AcquisitionInfo.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: AcquisitionInfo.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: AcquisitionInfo.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: AcquisitionInfo.getMethodOfCombination


Cython signature: String getMethodOfCombination()
Returns the method of combination




.. py:method:: AcquisitionInfo.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: AcquisitionInfo.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: AcquisitionInfo.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: AcquisitionInfo.push_back


Cython signature: void push_back(Acquisition)
Append a Acquisition object




.. py:method:: AcquisitionInfo.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: AcquisitionInfo.resize


Cython signature: void resize(size_t n)




.. py:method:: AcquisitionInfo.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: AcquisitionInfo.setMethodOfCombination


Cython signature: void setMethodOfCombination(String method)
Sets the method of combination




.. py:method:: AcquisitionInfo.size


Cython signature: size_t size()
Number a Acquisition objects




