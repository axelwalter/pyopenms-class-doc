OnDiscMSExperiment
==================

.. py:class:: OnDiscMSExperiment


   Bases: :py:class:`object`


Cython implementation of _OnDiscMSExperiment


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OnDiscMSExperiment.html


 Representation of a mass spectrometry experiment on disk.




.. py:method:: OnDiscMSExperiment.getChromatogram


Cython signature: MSChromatogram getChromatogram(size_t id)


Returns a single chromatogram
-----
:param id: The index of the chromatogram




.. py:method:: OnDiscMSExperiment.getChromatogramById


Cython signature: shared_ptr[_Interfaces_Chromatogram] getChromatogramById(int id_)
Returns a single chromatogram




.. py:method:: OnDiscMSExperiment.getChromatogramByNativeId


Cython signature: MSChromatogram getChromatogramByNativeId(String id)


Returns a single chromatogram
-----
:param id: The native identifier of the chromatogram




.. py:method:: OnDiscMSExperiment.getExperimentalSettings


Cython signature: shared_ptr[const ExperimentalSettings] getExperimentalSettings()
Returns the meta information of this experiment (const access)




.. py:method:: OnDiscMSExperiment.getMetaData


Cython signature: shared_ptr[MSExperiment] getMetaData()
Returns the meta information of this experiment




.. py:method:: OnDiscMSExperiment.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the total number of chromatograms available




.. py:method:: OnDiscMSExperiment.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the total number of spectra available




.. py:method:: OnDiscMSExperiment.getSpectrum


Cython signature: MSSpectrum getSpectrum(size_t id)


Returns a single spectrum
-----
:param id: The index of the spectrum




.. py:method:: OnDiscMSExperiment.getSpectrumById


Cython signature: shared_ptr[_Interfaces_Spectrum] getSpectrumById(int id_)
Returns a single spectrum




.. py:method:: OnDiscMSExperiment.getSpectrumByNativeId


Cython signature: MSSpectrum getSpectrumByNativeId(String id)


Returns a single spectrum
-----
:param id: The native identifier of the spectrum




.. py:method:: OnDiscMSExperiment.openFile


         - Cython signature: bool openFile(String filename)
         - Cython signature: bool openFile(String filename, bool skipLoadingMetaData)


Open a specific file on disk
-----
This tries to read the indexed mzML by parsing the index and then reading the meta information into memory
-----
returns: Whether the parsing of the file was successful (if false, the file most likely was not an indexed mzML file)




.. py:method:: OnDiscMSExperiment.setSkipXMLChecks


Cython signature: void setSkipXMLChecks(bool skip)
Sets whether to skip some XML checks and be fast instead




