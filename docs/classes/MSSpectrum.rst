MSSpectrum
==========

.. py:class:: MSSpectrum


   Bases: :py:class:`object`


Cython implementation of _MSSpectrum


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSSpectrum.html
 -- Inherits from ['SpectrumSettings', 'RangeManagerMzInt']


 The representation of a 1D spectrum.
 Raw data access is proved by `get_peaks` and `set_peaks`, which yields numpy arrays
 Iterations yields access to underlying peak objects but is slower
 Extra data arrays can be accessed through getFloatDataArrays / getIntegerDataArrays / getStringDataArrays
 See help(SpectrumSettings) for information about meta-information
 -----
 Usage:
   ms_level = spectrum.getMSLevel()
   rt = spectrum.getRT()
   mz, intensities = spectrum.get_peaks()




.. py:method:: MSSpectrum.calculateTIC


Cython signature: double calculateTIC()
Returns the total ion current (=sum) of peak intensities in the spectrum




.. py:method:: MSSpectrum.clear


Cython signature: void clear(bool clear_meta_data)
Clears all data (and meta data if clear_meta_data is true)




.. py:method:: MSSpectrum.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MSSpectrum.clearRanges


Cython signature: void clearRanges()
Resets all range dimensions as empty




.. py:method:: MSSpectrum.findHighestInWindow


Cython signature: int findHighestInWindow(double mz, double tolerance_left, double tolerance_right)
Returns the index of the highest peak in the provided abs. m/z tolerance window to the left and right (-1 if none match)




.. py:method:: MSSpectrum.findNearest


- Cython signature: int findNearest(double mz)
  Returns the index of the closest peak in m/z


- Cython signature: int findNearest(double mz, double tolerance)
  Returns the index of the closest peak in the provided +/- m/z tolerance window (-1 if none match)


- Cython signature: int findNearest(double mz, double tolerance_left, double tolerance_right)
  Returns the index of the closest peak in the provided abs. m/z tolerance window to the left and right (-1 if none match)




.. py:method:: MSSpectrum.getAcquisitionInfo


Cython signature: AcquisitionInfo getAcquisitionInfo()
Returns a const reference to the acquisition info




.. py:method:: MSSpectrum.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: MSSpectrum.getDataProcessing


Cython signature: libcpp_vector[shared_ptr[DataProcessing]] getDataProcessing()




.. py:method:: MSSpectrum.getDriftTime


Cython signature: double getDriftTime()
Returns the drift time (-1 if not set)




.. py:method:: MSSpectrum.getFloatDataArrays


Cython signature: libcpp_vector[FloatDataArray] getFloatDataArrays()
Returns the additional float data arrays to store e.g. meta data




.. py:method:: MSSpectrum.getInstrumentSettings


Cython signature: InstrumentSettings getInstrumentSettings()
Returns a const reference to the instrument settings of the current spectrum




.. py:method:: MSSpectrum.getIntegerDataArrays


Cython signature: libcpp_vector[IntegerDataArray] getIntegerDataArrays()
Returns the additional int data arrays to store e.g. meta data




.. py:method:: MSSpectrum.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MSSpectrum.getMSLevel


Cython signature: unsigned int getMSLevel()
Returns the MS level




.. py:method:: MSSpectrum.getMaxIntensity


Cython signature: double getMaxIntensity()
Returns the maximum intensity




.. py:method:: MSSpectrum.getMaxMZ


Cython signature: double getMaxMZ()
Returns the maximum m/z




.. py:method:: MSSpectrum.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MSSpectrum.getMinIntensity


Cython signature: double getMinIntensity()
Returns the minimum intensity




.. py:method:: MSSpectrum.getMinMZ


Cython signature: double getMinMZ()
Returns the minimum m/z




.. py:method:: MSSpectrum.getName


Cython signature: String getName()




.. py:method:: MSSpectrum.getNativeID


Cython signature: String getNativeID()
Returns the native identifier for the spectrum, used by the acquisition software




.. py:method:: MSSpectrum.getPeptideIdentifications


Cython signature: libcpp_vector[PeptideIdentification] getPeptideIdentifications()
Returns a const reference to the PeptideIdentification vector




.. py:method:: MSSpectrum.getPrecursors


Cython signature: libcpp_vector[Precursor] getPrecursors()
Returns a const reference to the precursors




.. py:method:: MSSpectrum.getProducts


Cython signature: libcpp_vector[Product] getProducts()
Returns a const reference to the products




.. py:method:: MSSpectrum.getRT


Cython signature: double getRT()
Returns the absolute retention time (in seconds)




.. py:method:: MSSpectrum.getSourceFile


Cython signature: SourceFile getSourceFile()
Returns a const reference to the source file




.. py:method:: MSSpectrum.getStringDataArrays


Cython signature: libcpp_vector[StringDataArray] getStringDataArrays()
Returns the additional string data arrays to store e.g. meta data




.. py:method:: MSSpectrum.getType


Cython signature: int getType()
Returns the spectrum type (centroided (PEAKS) or profile data (RAW))




.. py:method:: MSSpectrum.get_peaks


Cython signature: numpy_vector, numpy_vector get_peaks()


Will return a tuple of two numpy arrays (m/z, intensity) corresponding
to the peaks in the MSSpectrum. Provides fast access to peaks.




.. py:method:: MSSpectrum.intensityInRange




.. py:method:: MSSpectrum.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MSSpectrum.isSorted


Cython signature: bool isSorted()
Returns true if the spectrum is sorte by m/z




.. py:method:: MSSpectrum.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MSSpectrum.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MSSpectrum.push_back


Cython signature: void push_back(Peak1D)
Append a peak




.. py:method:: MSSpectrum.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MSSpectrum.reserve


Cython signature: void reserve(size_t n)




.. py:method:: MSSpectrum.select


Cython signature: MSSpectrum select(libcpp_vector[size_t] & indices)
Subset the spectrum by indices. Also applies to associated data arrays if present.




.. py:method:: MSSpectrum.setAcquisitionInfo


Cython signature: void setAcquisitionInfo(AcquisitionInfo)
Sets the acquisition info




.. py:method:: MSSpectrum.setComment


Cython signature: void setComment(String)
Sets the free-text comment




.. py:method:: MSSpectrum.setDataProcessing


Cython signature: void setDataProcessing(libcpp_vector[shared_ptr[DataProcessing]])




.. py:method:: MSSpectrum.setDriftTime


Cython signature: void setDriftTime(double)
Sets the drift time (-1 if not set)




.. py:method:: MSSpectrum.setFloatDataArrays


Cython signature: void setFloatDataArrays(libcpp_vector[FloatDataArray] fda)
Sets the additional float data arrays to store e.g. meta data




.. py:method:: MSSpectrum.setInstrumentSettings


Cython signature: void setInstrumentSettings(InstrumentSettings)
Sets the instrument settings of the current spectrum




.. py:method:: MSSpectrum.setIntegerDataArrays


Cython signature: void setIntegerDataArrays(libcpp_vector[IntegerDataArray] ida)
Sets the additional int data arrays to store e.g. meta data




.. py:method:: MSSpectrum.setMSLevel


Cython signature: void setMSLevel(unsigned int)
Sets the MS level




.. py:method:: MSSpectrum.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MSSpectrum.setName


Cython signature: void setName(String)




.. py:method:: MSSpectrum.setNativeID


Cython signature: void setNativeID(String)
Sets the native identifier for the spectrum, used by the acquisition software




.. py:method:: MSSpectrum.setPeptideIdentifications


Cython signature: void setPeptideIdentifications(libcpp_vector[PeptideIdentification])
Sets the PeptideIdentification vector




.. py:method:: MSSpectrum.setPrecursors


Cython signature: void setPrecursors(libcpp_vector[Precursor])
Sets the precursors




.. py:method:: MSSpectrum.setProducts


Cython signature: void setProducts(libcpp_vector[Product])
Sets the products




.. py:method:: MSSpectrum.setRT


Cython signature: void setRT(double)
Sets the absolute retention time (in seconds)




.. py:method:: MSSpectrum.setSourceFile


Cython signature: void setSourceFile(SourceFile)
Sets the source file




.. py:method:: MSSpectrum.setStringDataArrays


Cython signature: void setStringDataArrays(libcpp_vector[StringDataArray] sda)
Sets the additional string data arrays to store e.g. meta data




.. py:method:: MSSpectrum.setType


Cython signature: void setType(SpectrumType)
Sets the spectrum type




.. py:method:: MSSpectrum.set_peaks


Cython signature: set_peaks((numpy_vector, numpy_vector))


Takes a tuple or list of two arrays (m/z, intensity) and populates the
MSSpectrum. The arrays can be numpy arrays (faster).




.. py:method:: MSSpectrum.size


Cython signature: size_t size()
Returns the number of peaks in the spectrum




.. py:method:: MSSpectrum.sortByIntensity


Cython signature: void sortByIntensity(bool reverse)




.. py:method:: MSSpectrum.sortByPosition


Cython signature: void sortByPosition()




.. py:method:: MSSpectrum.unify


Cython signature: void unify(SpectrumSettings)




.. py:method:: MSSpectrum.updateRanges


Cython signature: void updateRanges()




