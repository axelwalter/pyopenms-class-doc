SpectrumAccessOpenMSCached
==========================

.. py:class:: SpectrumAccessOpenMSCached


   Bases: :py:class:`object`


Cython implementation of _SpectrumAccessOpenMSCached


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessOpenMSCached.html
 -- Inherits from ['ISpectrumAccess']




.. py:method:: SpectrumAccessOpenMSCached.getChromatogramById


Cython signature: shared_ptr[OSChromatogram] getChromatogramById(int id_)
Returns a pointer to a chromatogram at the given id




.. py:method:: SpectrumAccessOpenMSCached.getChromatogramNativeID


Cython signature: libcpp_utf8_output_string getChromatogramNativeID(int id_)




.. py:method:: SpectrumAccessOpenMSCached.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms available




.. py:method:: SpectrumAccessOpenMSCached.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the number of spectra available




.. py:method:: SpectrumAccessOpenMSCached.getSpectraByRT


Cython signature: libcpp_vector[size_t] getSpectraByRT(double RT, double deltaRT)
Returns a vector of ids of spectra that are within RT +/- deltaRT




.. py:method:: SpectrumAccessOpenMSCached.getSpectrumById


Cython signature: shared_ptr[OSSpectrum] getSpectrumById(int id_)
Returns a pointer to a spectrum at the given string id




