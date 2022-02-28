MSExperiment
============

.. py:class:: MSExperiment


   Bases: :py:class:`object`


Cython implementation of _MSExperiment


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSExperiment.html
 -- Inherits from ['ExperimentalSettings', 'RangeManagerRtMzInt']


 In-Memory representation of a mass spectrometry experiment.
 -----
 Contains the data and metadata of an experiment performed with an MS (or
 HPLC and MS). This representation of an MS experiment is organized as list
 of spectra and chromatograms and provides an in-memory representation of
 popular mass-spectrometric file formats such as mzXML or mzML. The
 meta-data associated with an experiment is contained in
 ExperimentalSettings (by inheritance) while the raw data (as well as
 spectra and chromatogram level meta data) is stored in objects of type
 MSSpectrum and MSChromatogram, which are accessible through the getSpectrum
 and getChromatogram functions.
 -----
 Spectra can be accessed by direct iteration or by getSpectrum(),
 while chromatograms are accessed through getChromatogram().
 See help(ExperimentalSettings) for information about meta-data.
 -----
 Usage:
   exp = MSExperiment()
   MzMLFile().load(path_to_file, exp)
   for spectrum in exp:
     print(spectrum.size()) # prints number of peaks
     mz, intensities = spectrum.get_peaks()
 -----




.. py:method:: MSExperiment.addChromatogram


Cython signature: void addChromatogram(MSChromatogram chromatogram)




.. py:method:: MSExperiment.addSpectrum


Cython signature: void addSpectrum(MSSpectrum spec)




.. py:method:: MSExperiment.calculateTIC


Cython signature: MSChromatogram calculateTIC()
Returns the total ion chromatogram




.. py:method:: MSExperiment.clear


Cython signature: void clear(bool clear_meta_data)
Clear all spectra data and meta data (if called with True)




.. py:method:: MSExperiment.clearMetaDataArrays


Cython signature: bool clearMetaDataArrays()




.. py:method:: MSExperiment.clearMetaInfo


Cython signature: void clearMetaInfo()
Removes all meta values




.. py:method:: MSExperiment.clearRanges


Cython signature: void clearRanges()
Resets all range dimensions as empty




.. py:method:: MSExperiment.empty


Cython signature: bool empty()




.. py:method:: MSExperiment.get2DPeakDataLong


Cython signature: tuple[np.array[float] rt, np.array[float] mz, np.array[float] inty] get2DPeakDataLong(float min_rt, float max_rt, float min_mz, float max_mz)




.. py:method:: MSExperiment.getChromatogram


Cython signature: MSChromatogram getChromatogram(size_t id_)




.. py:method:: MSExperiment.getChromatograms


Cython signature: libcpp_vector[MSChromatogram] getChromatograms()




.. py:method:: MSExperiment.getComment


Cython signature: String getComment()
Returns the free-text comment




.. py:method:: MSExperiment.getContacts


Cython signature: libcpp_vector[ContactPerson] getContacts()
Returns a reference to the list of contact persons




.. py:method:: MSExperiment.getDateTime


Cython signature: DateTime getDateTime()
Returns the date the experiment was performed




.. py:method:: MSExperiment.getExperimentalSettings


Cython signature: ExperimentalSettings getExperimentalSettings()




.. py:method:: MSExperiment.getFractionIdentifier


Cython signature: String getFractionIdentifier()
Returns fraction identifier




.. py:method:: MSExperiment.getHPLC


Cython signature: HPLC getHPLC()
Returns a reference to the description of the HPLC run




.. py:method:: MSExperiment.getIdentifier


Cython signature: String getIdentifier()
Retrieve document identifier (e.g. an LSID)




.. py:method:: MSExperiment.getInstrument


Cython signature: Instrument getInstrument()
Returns a reference to the MS instrument description




.. py:method:: MSExperiment.getKeys


Cython signature: void getKeys(libcpp_vector[String] & keys)
Fills the given vector with a list of all keys for which a value is set




.. py:method:: MSExperiment.getLoadedFilePath


Cython signature: String getLoadedFilePath()
Returns the file_name which is the absolute path to the file loaded




.. py:method:: MSExperiment.getLoadedFileType


Cython signature: int getLoadedFileType()
Returns the file_type (e.g. featureXML, consensusXML, mzData, mzXML, mzML, ...) of the file loaded




.. py:method:: MSExperiment.getMSLevels


Cython signature: list[int] getMSLevels()




.. py:method:: MSExperiment.getMaxIntensity


Cython signature: double getMaxIntensity()
Returns the maximum intensity




.. py:method:: MSExperiment.getMaxMZ


Cython signature: double getMaxMZ()
Returns the maximum m/z




.. py:method:: MSExperiment.getMaxRT


Cython signature: double getMaxRT()
Returns the maximum RT




.. py:method:: MSExperiment.getMetaValue


Cython signature: DataValue getMetaValue(String)
Returns the value corresponding to a string, or




.. py:method:: MSExperiment.getMinIntensity


Cython signature: double getMinIntensity()
Returns the minimum intensity




.. py:method:: MSExperiment.getMinMZ


Cython signature: double getMinMZ()
Returns the minimum m/z




.. py:method:: MSExperiment.getMinRT


Cython signature: double getMinRT()
Returns the minimum RT




.. py:method:: MSExperiment.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms




.. py:method:: MSExperiment.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the number of MS spectra




.. py:method:: MSExperiment.getPrecursorSpectrum


Cython signature: int getPrecursorSpectrum(int zero_based_index)
Returns the index of the precursor spectrum for spectrum at index @p zero_based_index




.. py:method:: MSExperiment.getPrimaryMSRunPath


Cython signature: void getPrimaryMSRunPath(StringList & toFill)
References to the first MS file(s) after conversions. Used to trace results back to original data.




.. py:method:: MSExperiment.getProteinIdentifications


Cython signature: libcpp_vector[ProteinIdentification] getProteinIdentifications()
Returns a reference to the protein ProteinIdentification vector




.. py:method:: MSExperiment.getSample


Cython signature: Sample getSample()
Returns a reference to the sample description




.. py:method:: MSExperiment.getSize


Cython signature: uint64_t getSize()
Returns the total number of peaks




.. py:method:: MSExperiment.getSourceFiles


Cython signature: libcpp_vector[SourceFile] getSourceFiles()
Returns a reference to the source data file




.. py:method:: MSExperiment.getSpectra


Cython signature: libcpp_vector[MSSpectrum] getSpectra()




.. py:method:: MSExperiment.getSpectrum


Cython signature: MSSpectrum getSpectrum(size_t id_)




.. py:method:: MSExperiment.isMetaEmpty


Cython signature: bool isMetaEmpty()
Returns if the MetaInfo is empty




.. py:method:: MSExperiment.isSorted


- Cython signature: bool isSorted(bool check_mz)
  Checks if all spectra are sorted with respect to ascending RT


- Cython signature: bool isSorted()




.. py:method:: MSExperiment.metaRegistry


Cython signature: MetaInfoRegistry metaRegistry()
Returns a reference to the MetaInfoRegistry




.. py:method:: MSExperiment.metaValueExists


Cython signature: bool metaValueExists(String)
Returns whether an entry with the given name exists




.. py:method:: MSExperiment.removeMetaValue


Cython signature: void removeMetaValue(String)
Removes the DataValue corresponding to `name` if it exists




.. py:method:: MSExperiment.reserve


Cython signature: void reserve(size_t s)




.. py:method:: MSExperiment.reserveSpaceChromatograms


Cython signature: void reserveSpaceChromatograms(size_t s)




.. py:method:: MSExperiment.reserveSpaceSpectra


Cython signature: void reserveSpaceSpectra(size_t s)




.. py:method:: MSExperiment.reset


Cython signature: void reset()




.. py:method:: MSExperiment.resize


Cython signature: void resize(size_t s)




.. py:method:: MSExperiment.setChromatograms


Cython signature: void setChromatograms(libcpp_vector[MSChromatogram] chromatograms)




.. py:method:: MSExperiment.setComment


Cython signature: void setComment(String comment)
Sets the free-text comment




.. py:method:: MSExperiment.setContacts


Cython signature: void setContacts(libcpp_vector[ContactPerson] contacts)
Sets the list of contact persons




.. py:method:: MSExperiment.setDateTime


Cython signature: void setDateTime(DateTime date_time)
Sets the date the experiment was performed




.. py:method:: MSExperiment.setFractionIdentifier


Cython signature: void setFractionIdentifier(String fraction_identifier)
Sets the fraction identifier




.. py:method:: MSExperiment.setHPLC


Cython signature: void setHPLC(HPLC hplc)
Sets the description of the HPLC run




.. py:method:: MSExperiment.setIdentifier


Cython signature: void setIdentifier(String id)
Sets document identifier (e.g. an LSID)




.. py:method:: MSExperiment.setInstrument


Cython signature: void setInstrument(Instrument instrument)
Sets the MS instrument description




.. py:method:: MSExperiment.setLoadedFilePath


Cython signature: void setLoadedFilePath(String file_name)
Sets the file_name according to absolute path of the file loaded, preferably done whilst loading




.. py:method:: MSExperiment.setLoadedFileType


Cython signature: void setLoadedFileType(String file_name)
Sets the file_type according to the type of the file loaded from, preferably done whilst loading




.. py:method:: MSExperiment.setMetaValue


Cython signature: void setMetaValue(String, DataValue)
Sets the DataValue corresponding to a name




.. py:method:: MSExperiment.setProteinIdentifications


Cython signature: void setProteinIdentifications(libcpp_vector[ProteinIdentification] protein_identifications)
Sets the protein ProteinIdentification vector




.. py:method:: MSExperiment.setSample


Cython signature: void setSample(Sample sample)
Sets the sample description




.. py:method:: MSExperiment.setSourceFiles


Cython signature: void setSourceFiles(libcpp_vector[SourceFile] source_files)
Sets the source data file




.. py:method:: MSExperiment.setSpectra


Cython signature: void setSpectra(libcpp_vector[MSSpectrum] & spectra)




.. py:method:: MSExperiment.size


Cython signature: int size()




.. py:method:: MSExperiment.sortChromatograms


- Cython signature: void sortChromatograms(bool sort_rt)
  Sorts chromatograms by m/z. If sort_rt=True also sort each chromatogram RT


- Cython signature: void sortChromatograms()




.. py:method:: MSExperiment.sortSpectra


- Cython signature: void sortSpectra(bool sort_mz)
  Sorts spectra by RT. If sort_mz=True also sort each peak in a spectrum by m/z


- Cython signature: void sortSpectra()




.. py:method:: MSExperiment.swap


Cython signature: void swap(MSExperiment)




.. py:method:: MSExperiment.updateRanges


- Cython signature: void updateRanges()
  Recalculate global RT and m/z ranges after changes to the data has been made.


- Cython signature: void updateRanges(int msLevel)
  Recalculate RT and m/z ranges for a specific MS level




