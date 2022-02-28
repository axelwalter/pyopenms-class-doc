MSChromatogram
==============

.. py:class:: MSChromatogram


   Bases: :py:class:`object`


Cython implementation of _MSChromatogram


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSChromatogram.html
 -- Inherits from ['ChromatogramSettings', 'RangeManagerRtInt']


 The representation of a chromatogram.
 Raw data access is proved by `get_peaks` and `set_peaks`, which yields numpy arrays
 Iterations yields access to underlying peak objects but is slower
 Extra data arrays can be accessed through getFloatDataArrays / getIntegerDataArrays / getStringDataArrays
 See help(ChromatogramSettings) for information about meta-information
 -----
 Usage:
   precursor = chromatogram.getPrecursor()
   product = chromatogram.getProduct()
   rt, intensities = chromatogram.get_peaks()
 -----




.. py:method:: MSChromatogram.clear


Cython signature: void clear(int)


Clears all data and meta data
-----
:param clear_meta_data: If true, all meta data is cleared in addition to the data




.. py:method:: MSChromatogram.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MSChromatogram.clearRanges


Cython signature: void clearRanges()
Resets all range dimensions as empty




.. py:method:: MSChromatogram.findNearest


Cython signature: int findNearest(double)


Binary search for the peak nearest to a specific RT
-----
:param rt: The searched for mass-to-charge ratio searched
:returns: Returns the index of the peak.
-----
:note: Make sure the chromatogram is sorted with respect to RT! Otherwise the result is undefined
-----
:raises:
  Exception: Precondition is thrown if the chromatogram is empty (not only in debug mode)




.. py:method:: MSChromatogram.getAcquisitionInfo


Cython signature: AcquisitionInfo getAcquisitionInfo()
Returns the acquisition info




.. py:method:: MSChromatogram.getChromatogramType


Cython signature: ChromatogramType getChromatogramType()
Get the chromatogram type




.. py:method:: MSChromatogram.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: MSChromatogram.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()
Returns the description of the applied processing




.. py:method:: MSChromatogram.getFloatDataArrays


Cython signature: libcpp_vector[FloatDataArray] getFloatDataArrays()
Returns a reference to the float meta data arrays




.. py:method:: MSChromatogram.getInstrumentSettings


Cython signature: InstrumentSettings getInstrumentSettings()
Returns the instrument settings of the current spectrum




.. py:method:: MSChromatogram.getIntegerDataArrays


Cython signature: libcpp_vector[IntegerDataArray] getIntegerDataArrays()
Returns a reference to the integer meta data arrays




.. py:method:: MSChromatogram.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MSChromatogram.getMZ


Cython signature: double getMZ()
Returns the mz of the product entry, makes sense especially for MRM scans




.. py:method:: MSChromatogram.getMaxIntensity


Cython signature: double getMaxIntensity()
Returns the maximum intensity




.. py:method:: MSChromatogram.getMaxRT


Cython signature: double getMaxRT()
Returns the maximum RT




.. py:method:: MSChromatogram.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MSChromatogram.getMinIntensity


Cython signature: double getMinIntensity()
Returns the minimum intensity




.. py:method:: MSChromatogram.getMinRT


Cython signature: double getMinRT()
Returns the minimum RT




.. py:method:: MSChromatogram.getName


Cython signature: String getName()
Returns the name




.. py:method:: MSChromatogram.getNativeID


Cython signature: String getNativeID()
Returns the native identifier for the spectrum, used by the acquisition software.




.. py:method:: MSChromatogram.getPrecursor


Cython signature: Precursor getPrecursor()
Returns the precursors




.. py:method:: MSChromatogram.getProduct


Cython signature: Product getProduct()
Returns the product ion




.. py:method:: MSChromatogram.getSourceFile


Cython signature: SourceFile getSourceFile()
Returns the source file




.. py:method:: MSChromatogram.getStringDataArrays


Cython signature: libcpp_vector[StringDataArray] getStringDataArrays()
Returns a reference to the string meta data arrays




.. py:method:: MSChromatogram.get_peaks




.. py:method:: MSChromatogram.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MSChromatogram.isSorted


Cython signature: bool isSorted()
Checks if all peaks are sorted with respect to ascending RT




.. py:method:: MSChromatogram.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MSChromatogram.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MSChromatogram.push_back


Cython signature: void push_back(ChromatogramPeak)
Append a peak




.. py:method:: MSChromatogram.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MSChromatogram.reserve


Cython signature: void reserve(size_t n)




.. py:method:: MSChromatogram.setAcquisitionInfo


Cython signature: void setAcquisitionInfo(AcquisitionInfo acquisition_info)
Sets the acquisition info




.. py:method:: MSChromatogram.setChromatogramType


Cython signature: void setChromatogramType(ChromatogramType type)
Sets the chromatogram type




.. py:method:: MSChromatogram.setComment


Cython signature: void setComment(String comment)
Sets the free-text comment




.. py:method:: MSChromatogram.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])
Sets the description of the applied processing




.. py:method:: MSChromatogram.setFloatDataArrays


Cython signature: void setFloatDataArrays(libcpp_vector[FloatDataArray] fda)
Sets the float meta data arrays




.. py:method:: MSChromatogram.setInstrumentSettings


Cython signature: void setInstrumentSettings(InstrumentSettings instrument_settings)
Sets the instrument settings of the current spectrum




.. py:method:: MSChromatogram.setIntegerDataArrays


Cython signature: void setIntegerDataArrays(libcpp_vector[IntegerDataArray] ida)
Sets the integer meta data arrays




.. py:method:: MSChromatogram.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MSChromatogram.setName


Cython signature: void setName(String)
Sets the name




.. py:method:: MSChromatogram.setNativeID


Cython signature: void setNativeID(String native_id)
Sets the native identifier for the spectrum, used by the acquisition software.




.. py:method:: MSChromatogram.setPrecursor


Cython signature: void setPrecursor(Precursor precursor)
Sets the precursors




.. py:method:: MSChromatogram.setProduct


Cython signature: void setProduct(Product p)
Sets the product ion




.. py:method:: MSChromatogram.setSourceFile


Cython signature: void setSourceFile(SourceFile source_file)
Sets the source file




.. py:method:: MSChromatogram.setStringDataArrays


Cython signature: void setStringDataArrays(libcpp_vector[StringDataArray] sda)
Sets the string meta data arrays




.. py:method:: MSChromatogram.set_peaks




.. py:method:: MSChromatogram.size


Cython signature: size_t size()




.. py:method:: MSChromatogram.sortByIntensity


Cython signature: void sortByIntensity(bool reverse)


Lexicographically sorts the peaks by their intensity
-----
Sorts the peaks according to ascending intensity. Meta data arrays will be sorted accordingly




.. py:method:: MSChromatogram.sortByPosition


Cython signature: void sortByPosition()


Lexicographically sorts the peaks by their position
-----
The chromatogram is sorted with respect to position. Meta data arrays will be sorted accordingly




.. py:method:: MSChromatogram.updateRanges


Cython signature: void updateRanges()




