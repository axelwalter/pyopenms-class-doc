SpectrumAccessOpenMSInMemory
============================

.. py:class:: SpectrumAccessOpenMSInMemory


   Bases: :py:class:`object`


Cython implementation of _SpectrumAccessOpenMSInMemory


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessOpenMSInMemory.html
 -- Inherits from ['ISpectrumAccess']




.. py:method:: SpectrumAccessOpenMSInMemory.getChromatogramById


Cython signature: shared_ptr[OSChromatogram] getChromatogramById(int id_)
Returns a pointer to a chromatogram at the given id




.. py:method:: SpectrumAccessOpenMSInMemory.getChromatogramNativeID


Cython signature: libcpp_utf8_output_string getChromatogramNativeID(int id_)




.. py:method:: SpectrumAccessOpenMSInMemory.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms available




.. py:method:: SpectrumAccessOpenMSInMemory.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the number of spectra available




.. py:method:: SpectrumAccessOpenMSInMemory.getSpectraByRT


Cython signature: libcpp_vector[size_t] getSpectraByRT(double RT, double deltaRT)
Returns a vector of ids of spectra that are within RT +/- deltaRT




.. py:method:: SpectrumAccessOpenMSInMemory.getSpectrumById


Cython signature: shared_ptr[OSSpectrum] getSpectrumById(int id_)
Returns a pointer to a spectrum at the given string id




