FloatDataArray
==============

.. py:class:: FloatDataArray


   Bases: :py:class:`object`


Cython implementation of _FloatDataArray


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::DataArrays_1_1FloatDataArray.html
 -- Inherits from ['MetaInfoDescription']


 The representation of extra float data attached to a spectrum or chromatogram.
 Raw data access is proved by `get_peaks` and `set_peaks`, which yields numpy arrays




.. py:method:: FloatDataArray.clear


Cython signature: void clear()




.. py:method:: FloatDataArray.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: FloatDataArray.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
Returns a reference to the description of the applied processing




.. py:method:: FloatDataArray.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: FloatDataArray.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: FloatDataArray.getName


Cython signature: String getName()
Returns the name of the peak annotations




.. py:method:: FloatDataArray.get_data


Gets the raw data for the float data array


Example usage:


  fd = pyopenms.FloatDataArray()
  data = fd.get_data()






.. py:method:: FloatDataArray.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: FloatDataArray.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: FloatDataArray.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: FloatDataArray.push_back


Cython signature: void push_back(float)




.. py:method:: FloatDataArray.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: FloatDataArray.reserve


Cython signature: void reserve(size_t n)




.. py:method:: FloatDataArray.resize


Cython signature: void resize(size_t n)




.. py:method:: FloatDataArray.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
Sets the description of the applied processing




.. py:method:: FloatDataArray.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: FloatDataArray.setName


Cython signature: void setName(String name)
Sets the name of the peak annotations




.. py:method:: FloatDataArray.set_data


Sets the raw data for the float data array


Example usage:


  fd = pyopenms.FloatDataArray()
  data = numpy.array( [1, 2, 3, 5 ,6] ).astype(numpy.float32)
  fd.set_data(data)






.. py:method:: FloatDataArray.size


Cython signature: size_t size()




