StringDataArray
===============

.. py:class:: StringDataArray


   Bases: :py:class:`object`


Cython implementation of _StringDataArray


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::DataArrays_1_1StringDataArray.html
 -- Inherits from ['MetaInfoDescription']


 The representation of extra string data attached to a spectrum or chromatogram.




.. py:method:: StringDataArray.clear


Cython signature: void clear()




.. py:method:: StringDataArray.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: StringDataArray.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
Returns a reference to the description of the applied processing




.. py:method:: StringDataArray.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: StringDataArray.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: StringDataArray.getName


Cython signature: String getName()
Returns the name of the peak annotations




.. py:method:: StringDataArray.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: StringDataArray.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: StringDataArray.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: StringDataArray.push_back


Cython signature: void push_back(String)




.. py:method:: StringDataArray.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: StringDataArray.resize


Cython signature: void resize(size_t n)




.. py:method:: StringDataArray.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
Sets the description of the applied processing




.. py:method:: StringDataArray.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: StringDataArray.setName


Cython signature: void setName(String name)
Sets the name of the peak annotations




.. py:method:: StringDataArray.size


Cython signature: size_t size()




