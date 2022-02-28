SpectrumLookup
==============

.. py:class:: SpectrumLookup


   Bases: :py:class:`object`


Cython implementation of _SpectrumLookup


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumLookup.html




.. py:method:: SpectrumLookup.addReferenceFormat


Cython signature: void addReferenceFormat(String regexp)


Register a possible format for a spectrum reference
-----
:param regexp: Regular expression defining the format




.. py:method:: SpectrumLookup.empty


Cython signature: bool empty()
Check if any spectra were set




.. py:method:: SpectrumLookup.extractScanNumber


Cython signature: int extractScanNumber(const String & native_id, const String & native_id_type_accession)




.. py:method:: SpectrumLookup.findByIndex


Cython signature: size_t findByIndex(size_t index, bool count_from_one)


Look up spectrum by index (position in the vector of spectra)
-----
:param index: Index to look up
:param count_from_one: Do indexes start counting at one (default zero)?
:returns: Index of the spectrum that matched




.. py:method:: SpectrumLookup.findByNativeID


Cython signature: size_t findByNativeID(String native_id)


Look up spectrum by native ID
-----
:param native_id: Native ID to look up
:returns: Index of the spectrum that matched




.. py:method:: SpectrumLookup.findByRT


Cython signature: size_t findByRT(double rt)


Look up spectrum by retention time (RT)
-----
:param rt: Retention time to look up
:returns: Index of the spectrum that matched




.. py:method:: SpectrumLookup.findByReference


Cython signature: size_t findByReference(String spectrum_ref)


Look up spectrum by reference
-----
:param spectrum_ref: Spectrum reference to parse
:returns: Index of the spectrum that matched




.. py:method:: SpectrumLookup.findByScanNumber


Cython signature: size_t findByScanNumber(size_t scan_number)


Look up spectrum by scan number (extracted from the native ID)
-----
:param scan_number: Scan number to look up
:returns: Index of the spectrum that matched




.. py:method:: SpectrumLookup.readSpectra


Cython signature: void readSpectra(MSExperiment spectra, String scan_regexp)


Read and index spectra for later look-up
-----
:param spectra: Container of spectra
:param scan_regexp: Regular expression for matching scan numbers in spectrum native IDs (must contain the named group "?<SCAN>")




.. py:attribute:: SpectrumLookup.rt_tolerance




