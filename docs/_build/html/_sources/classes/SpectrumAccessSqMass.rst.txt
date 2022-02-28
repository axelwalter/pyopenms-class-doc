SpectrumAccessSqMass
====================

.. py:class:: SpectrumAccessSqMass


   Bases: :py:class:`object`


Cython implementation of _SpectrumAccessSqMass


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessSqMass.html
 -- Inherits from ['ISpectrumAccess']




.. py:method:: SpectrumAccessSqMass.getChromatogramById


Cython signature: shared_ptr[OSChromatogram] getChromatogramById(int id_)
Returns a pointer to a chromatogram at the given id




.. py:method:: SpectrumAccessSqMass.getChromatogramNativeID


Cython signature: libcpp_utf8_output_string getChromatogramNativeID(int id_)




.. py:method:: SpectrumAccessSqMass.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms available




.. py:method:: SpectrumAccessSqMass.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the number of spectra available




.. py:method:: SpectrumAccessSqMass.getSpectraByRT


Cython signature: libcpp_vector[size_t] getSpectraByRT(double RT, double deltaRT)
Returns a vector of ids of spectra that are within RT +/- deltaRT




.. py:method:: SpectrumAccessSqMass.getSpectrumById


Cython signature: shared_ptr[OSSpectrum] getSpectrumById(int id_)
Returns a pointer to a spectrum at the given string id




