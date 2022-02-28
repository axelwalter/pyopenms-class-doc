IntegerDataArray
================

.. py:class:: IntegerDataArray


   Bases: :py:class:`object`


Cython implementation of _IntegerDataArray


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::DataArrays_1_1IntegerDataArray.html
 -- Inherits from ['MetaInfoDescription']


 The representation of extra integer data attached to a spectrum or chromatogram.
 Raw data access is proved by `get_peaks` and `set_peaks`, which yields numpy arrays




.. py:method:: IntegerDataArray.clear


Cython signature: void clear()




.. py:method:: IntegerDataArray.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: IntegerDataArray.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
Returns a reference to the description of the applied processing




.. py:method:: IntegerDataArray.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: IntegerDataArray.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: IntegerDataArray.getName


Cython signature: String getName()
Returns the name of the peak annotations




.. py:method:: IntegerDataArray.get_data


Gets the raw data for the integer data array


Example usage:


  idata = pyopenms.IntegerDataArray()
  data = idata.get_data()






.. py:method:: IntegerDataArray.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: IntegerDataArray.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: IntegerDataArray.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: IntegerDataArray.push_back


Cython signature: void push_back(int)




.. py:method:: IntegerDataArray.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: IntegerDataArray.reserve


Cython signature: void reserve(size_t n)




.. py:method:: IntegerDataArray.resize


Cython signature: void resize(size_t n)




.. py:method:: IntegerDataArray.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
Sets the description of the applied processing




.. py:method:: IntegerDataArray.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: IntegerDataArray.setName


Cython signature: void setName(String name)
Sets the name of the peak annotations




.. py:method:: IntegerDataArray.set_data


Sets the raw data for the integer data array


Example usage:


  idata = pyopenms.IntegerDataArray()
  data = numpy.array( [1, 2, 3, 5 ,6] ).astype(np.intc)
  idata.set_data(data)






.. py:method:: IntegerDataArray.size


Cython signature: size_t size()




