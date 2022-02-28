SpectrumMetaDataLookup
======================

.. py:class:: SpectrumMetaDataLookup


   Bases: :py:class:`object`


Cython implementation of _SpectrumMetaDataLookup


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumMetaDataLookup.html
 -- Inherits from ['SpectrumLookup']




.. py:method:: SpectrumMetaDataLookup.addMissingRTsToPeptideIDs


Cython signature: bool addMissingRTsToPeptideIDs(libcpp_vector[PeptideIdentification], String filename, bool stop_on_error)




.. py:method:: SpectrumMetaDataLookup.addMissingSpectrumReferences


Cython signature: bool addMissingSpectrumReferences(libcpp_vector[PeptideIdentification], String filename, bool stop_on_error, bool override_spectra_data, bool override_spectra_references, libcpp_vector[ProteinIdentification] proteins)




.. py:method:: SpectrumMetaDataLookup.addReferenceFormat


Cython signature: void addReferenceFormat(String regexp)


Register a possible format for a spectrum reference
-----
:param regexp: Regular expression defining the format




.. py:method:: SpectrumMetaDataLookup.empty


Cython signature: bool empty()
Check if any spectra were set




.. py:method:: SpectrumMetaDataLookup.extractScanNumber


Cython signature: int extractScanNumber(const String & native_id, const String & native_id_type_accession)




.. py:method:: SpectrumMetaDataLookup.findByIndex


Cython signature: size_t findByIndex(size_t index, bool count_from_one)


Look up spectrum by index (position in the vector of spectra)
-----
:param index: Index to look up
:param count_from_one: Do indexes start counting at one (default zero)?
:returns: Index of the spectrum that matched




.. py:method:: SpectrumMetaDataLookup.findByNativeID


Cython signature: size_t findByNativeID(String native_id)


Look up spectrum by native ID
-----
:param native_id: Native ID to look up
:returns: Index of the spectrum that matched




.. py:method:: SpectrumMetaDataLookup.findByRT


Cython signature: size_t findByRT(double rt)


Look up spectrum by retention time (RT)
-----
:param rt: Retention time to look up
:returns: Index of the spectrum that matched




.. py:method:: SpectrumMetaDataLookup.findByReference


Cython signature: size_t findByReference(String spectrum_ref)


Look up spectrum by reference
-----
:param spectrum_ref: Spectrum reference to parse
:returns: Index of the spectrum that matched




.. py:method:: SpectrumMetaDataLookup.findByScanNumber


Cython signature: size_t findByScanNumber(size_t scan_number)


Look up spectrum by scan number (extracted from the native ID)
-----
:param scan_number: Scan number to look up
:returns: Index of the spectrum that matched




.. py:method:: SpectrumMetaDataLookup.getSpectrumMetaData


Cython signature: void getSpectrumMetaData(MSSpectrum spectrum, SpectrumMetaData & meta)




.. py:method:: SpectrumMetaDataLookup.readSpectra


         - Cython signature: void readSpectra(MSExperiment spectra, String scan_regexp, bool get_precursor_rt)


Read spectra and store their meta data
-----
:param SpectrumContainer: Spectrum container class, must support `size` and `operator[]`
:param spectra: Container of spectra
:param scan_regexp: Regular expression for matching scan numbers in spectrum native IDs (must contain the named group "?<SCAN>")
:param get_precursor_rt: Assign precursor retention times? (This relies on all precursor spectra being present and in the right order.)
         - Cython signature: void readSpectra(MSExperiment spectra, String scan_regexp)


Read and index spectra for later look-up
-----
:param spectra: Container of spectra
:param scan_regexp: Regular expression for matching scan numbers in spectrum native IDs (must contain the named group "?<SCAN>")




.. py:method:: SpectrumMetaDataLookup.setSpectraDataRef


Cython signature: void setSpectraDataRef(const String & spectra_data)




