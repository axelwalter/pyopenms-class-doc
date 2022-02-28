MzMLSqliteHandler
=================

.. py:class:: MzMLSqliteHandler


   Bases: :py:class:`object`


Cython implementation of _MzMLSqliteHandler


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Internal_1_1MzMLSqliteHandler.html




.. py:method:: MzMLSqliteHandler.createTables


Cython signature: void createTables()
Create data tables for a new file




.. py:method:: MzMLSqliteHandler.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms in the file




.. py:method:: MzMLSqliteHandler.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns number of spectra in the file, reutrns the number of spectra




.. py:method:: MzMLSqliteHandler.getRunID


Cython signature: uint64_t getRunID()
Extract the `RUN` ID from the sqMass file




.. py:method:: MzMLSqliteHandler.getSpectraIndicesbyRT


Cython signature: libcpp_vector[size_t] getSpectraIndicesbyRT(double RT, double deltaRT, libcpp_vector[int] indices)


Returns spectral indices around a specific retention time
-----
:param RT: The retention time
:param deltaRT: Tolerance window around RT (if less or equal than zero, only the first spectrum *after* RT is returned)
:param indices: Spectra to consider (if empty, all spectra are considered)
:returns: The indices of the spectra within RT +/- deltaRT




.. py:method:: MzMLSqliteHandler.readChromatograms


Cython signature: void readChromatograms(libcpp_vector[MSChromatogram] & exp, libcpp_vector[int] indices, bool meta_only)


Read a set of chromatograms (potentially restricted to a subset)
-----
:param exp: The result data structure
:param indices: A list of indices restricting the resulting spectra only to those specified here
:param meta_only: Only read the meta data




.. py:method:: MzMLSqliteHandler.readExperiment


Cython signature: void readExperiment(MSExperiment & exp, bool meta_only)


Read an experiment into an MSExperiment structure
-----
:param exp: The result data structure
:param meta_only: Only read the meta data




.. py:method:: MzMLSqliteHandler.readSpectra


Cython signature: void readSpectra(libcpp_vector[MSSpectrum] & exp, libcpp_vector[int] indices, bool meta_only)


Read a set of spectra (potentially restricted to a subset)
-----
:param exp: The result data structure
:param indices: A list of indices restricting the resulting spectra only to those specified here
:param meta_only: Only read the meta data




.. py:method:: MzMLSqliteHandler.setConfig


Cython signature: void setConfig(bool write_full_meta, bool use_lossy_compression, double linear_abs_mass_acc)


Sets file configuration
-----
:param write_full_meta: Whether to write a complete mzML meta data structure into the RUN_EXTRA field (allows complete recovery of the input file)
:param use_lossy_compression: Whether to use lossy compression (ms numpress)
:param linear_abs_mass_acc: Accepted loss in mass accuracy (absolute m/z, in Th)




.. py:method:: MzMLSqliteHandler.writeChromatograms


Cython signature: void writeChromatograms(libcpp_vector[MSChromatogram] chroms)
Writes a set of chromatograms to disk




.. py:method:: MzMLSqliteHandler.writeExperiment


Cython signature: void writeExperiment(MSExperiment exp)
Write an MSExperiment to disk




.. py:method:: MzMLSqliteHandler.writeRunLevelInformation


Cython signature: void writeRunLevelInformation(MSExperiment exp, bool write_full_meta)


Write the run-level information for an experiment into tables
-----
This is a low level function, do not call this function unless you know what you are doing
-----
:param exp: The result data structure
:param meta_only: Only read the meta data




.. py:method:: MzMLSqliteHandler.writeSpectra


Cython signature: void writeSpectra(libcpp_vector[MSSpectrum] spectra)
Writes a set of spectra to disk




