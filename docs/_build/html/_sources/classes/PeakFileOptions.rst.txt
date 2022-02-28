PeakFileOptions
===============

.. py:class:: PeakFileOptions


   Bases: :py:class:`object`


Cython implementation of _PeakFileOptions


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakFileOptions.html


 Options for loading files containing peak data




.. py:method:: PeakFileOptions.addMSLevel


Cython signature: void addMSLevel(int level)
Adds a desired MS level for peaks to load




.. py:method:: PeakFileOptions.clearMSLevels


Cython signature: void clearMSLevels()
Clears the MS levels




.. py:method:: PeakFileOptions.containsMSLevel


Cython signature: bool containsMSLevel(int level)
Returns true, if MS level `level` has been set




.. py:method:: PeakFileOptions.getCompression


Cython signature: bool getCompression()
Returns true, if data should be compressed when writing




.. py:method:: PeakFileOptions.getFillData


Cython signature: bool getFillData()
Returns whether to fill the actual data into the container (spectrum/chromatogram)




.. py:method:: PeakFileOptions.getForceMQCompatability


Cython signature: bool getForceMQCompatability()
[mzXML only!]Returns Whether to write a scan-index and meta data to indicate a Thermo FTMS/ITMS instrument (required to have parameter control in MQ)




.. py:method:: PeakFileOptions.getForceTPPCompatability


Cython signature: bool getForceTPPCompatability()
[mzML only!]Returns Whether to skip writing the \<isolationWindow\> tag so that TPP finds the correct precursor m/z




.. py:method:: PeakFileOptions.getIntensity32Bit


Cython signature: bool getIntensity32Bit()
Returns true, if intensity data should be stored with 32bit precision




.. py:method:: PeakFileOptions.getIntensityRange


Cython signature: DRange1 getIntensityRange()
Returns the intensity range




.. py:method:: PeakFileOptions.getMSLevels


Cython signature: libcpp_vector[int] getMSLevels()
Returns the set MS levels




.. py:method:: PeakFileOptions.getMZRange


Cython signature: DRange1 getMZRange()
Returns the MZ range




.. py:method:: PeakFileOptions.getMaxDataPoolSize


Cython signature: size_t getMaxDataPoolSize()
Returns maximal size of the data pool




.. py:method:: PeakFileOptions.getMetadataOnly


Cython signature: bool getMetadataOnly()
Returns whether or not to load only meta data




.. py:method:: PeakFileOptions.getMz32Bit


Cython signature: bool getMz32Bit()
Returns true, if mz-data and rt-data should be stored with 32bit precision




.. py:method:: PeakFileOptions.getNumpressConfigurationFloatDataArray


Cython signature: NumpressConfig getNumpressConfigurationFloatDataArray()
Sets numpress configuration options for float data arrays




.. py:method:: PeakFileOptions.getNumpressConfigurationIntensity


Cython signature: NumpressConfig getNumpressConfigurationIntensity()
Sets numpress configuration options for intensity dimension




.. py:method:: PeakFileOptions.getNumpressConfigurationMassTime


Cython signature: NumpressConfig getNumpressConfigurationMassTime()
Sets numpress configuration options for m/z or rt dimension




.. py:method:: PeakFileOptions.getRTRange


Cython signature: DRange1 getRTRange()
Returns the RT range




.. py:method:: PeakFileOptions.getSkipXMLChecks


Cython signature: bool getSkipXMLChecks()
Returns whether to skip some XML checks and be fast instead




.. py:method:: PeakFileOptions.getSortChromatogramsByRT


Cython signature: bool getSortChromatogramsByRT()
Returns whether or not peaks in chromatograms should be sorted




.. py:method:: PeakFileOptions.getSortSpectraByMZ


Cython signature: bool getSortSpectraByMZ()
Returns whether or not peaks in spectra should be sorted




.. py:method:: PeakFileOptions.getWriteIndex


Cython signature: bool getWriteIndex()
Returns whether to write an index at the end of the file (e.g. indexedmzML file format)




.. py:method:: PeakFileOptions.getWriteSupplementalData


Cython signature: bool getWriteSupplementalData()
Returns whether or not to write supplemental peak data in MzData files




.. py:method:: PeakFileOptions.hasFilters


Cython signature: bool hasFilters()




.. py:method:: PeakFileOptions.hasIntensityRange


Cython signature: bool hasIntensityRange()
Returns true if an intensity range has been set




.. py:method:: PeakFileOptions.hasMSLevels


Cython signature: bool hasMSLevels()
Returns true, if MS levels have been set




.. py:method:: PeakFileOptions.hasMZRange


Cython signature: bool hasMZRange()
Returns true if an MZ range has been set




.. py:method:: PeakFileOptions.hasRTRange


Cython signature: bool hasRTRange()
Returns true if an RT range has been set




.. py:method:: PeakFileOptions.setCompression


Cython signature: void setCompression(bool)
Sets if data should be compressed when writing




.. py:method:: PeakFileOptions.setFillData


Cython signature: void setFillData(bool only)
Sets whether to fill the actual data into the container (spectrum/chromatogram)




.. py:method:: PeakFileOptions.setForceMQCompatability


Cython signature: void setForceMQCompatability(bool forceMQ)
[mzXML only!]Returns Whether to write a scan-index and meta data to indicate a Thermo FTMS/ITMS instrument (required to have parameter control in MQ)




.. py:method:: PeakFileOptions.setForceTPPCompatability


Cython signature: void setForceTPPCompatability(bool forceTPP)
[ mzML only!]Returns Whether to skip writing the \<isolationWindow\> tag so that TPP finds the correct precursor m/z




.. py:method:: PeakFileOptions.setIntensity32Bit


Cython signature: void setIntensity32Bit(bool int_32_bit)
Sets if intensity data should be stored with 32bit or 64bit precision




.. py:method:: PeakFileOptions.setIntensityRange


Cython signature: void setIntensityRange(DRange1 & range_)
Restricts the range of intensity values for peaks to load




.. py:method:: PeakFileOptions.setMSLevels


Cython signature: void setMSLevels(libcpp_vector[int] levels)
Sets the desired MS levels for peaks to load




.. py:method:: PeakFileOptions.setMZRange


Cython signature: void setMZRange(DRange1 & range_)
Restricts the range of MZ values for peaks to load




.. py:method:: PeakFileOptions.setMaxDataPoolSize


Cython signature: void setMaxDataPoolSize(size_t s)
Sets maximal size of the data pool




.. py:method:: PeakFileOptions.setMetadataOnly


Cython signature: void setMetadataOnly(bool)
Sets whether or not to load only meta data




.. py:method:: PeakFileOptions.setMz32Bit


Cython signature: void setMz32Bit(bool mz_32_bit)
Sets if mz-data and rt-data should be stored with 32bit or 64bit precision




.. py:method:: PeakFileOptions.setNumpressConfigurationFloatDataArray


Cython signature: void setNumpressConfigurationFloatDataArray(NumpressConfig config)
Returns numpress configuration options for float data arrays




.. py:method:: PeakFileOptions.setNumpressConfigurationIntensity


Cython signature: void setNumpressConfigurationIntensity(NumpressConfig config)
Returns numpress configuration options for intensity dimension




.. py:method:: PeakFileOptions.setNumpressConfigurationMassTime


Cython signature: void setNumpressConfigurationMassTime(NumpressConfig config)
Returns numpress configuration options for m/z or rt dimension




.. py:method:: PeakFileOptions.setRTRange


Cython signature: void setRTRange(DRange1 & range_)
Restricts the range of RT values for peaks to load




.. py:method:: PeakFileOptions.setSkipXMLChecks


Cython signature: void setSkipXMLChecks(bool only)
Sets whether to skip some XML checks and be fast instead




.. py:method:: PeakFileOptions.setSortChromatogramsByRT


Cython signature: void setSortChromatogramsByRT(bool doSort)
Sets whether or not to sort peaks in chromatograms




.. py:method:: PeakFileOptions.setSortSpectraByMZ


Cython signature: void setSortSpectraByMZ(bool doSort)
Sets whether or not to sort peaks in spectra




.. py:method:: PeakFileOptions.setWriteIndex


Cython signature: void setWriteIndex(bool write_index)
Returns whether to write an index at the end of the file (e.g. indexedmzML file format)




.. py:method:: PeakFileOptions.setWriteSupplementalData


Cython signature: void setWriteSupplementalData(bool)
Sets whether or not to write supplemental peak data in MzData files




