SpectrumAccessTransforming
==========================

.. py:class:: SpectrumAccessTransforming


   Bases: :py:class:`object`


Cython implementation of _SpectrumAccessTransforming


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessTransforming.html
 -- Inherits from ['ISpectrumAccess']




.. py:method:: SpectrumAccessTransforming.getChromatogramById


Cython signature: shared_ptr[OSChromatogram] getChromatogramById(int id_)
Returns a pointer to a chromatogram at the given id




.. py:method:: SpectrumAccessTransforming.getChromatogramNativeID


Cython signature: libcpp_utf8_output_string getChromatogramNativeID(int id_)




.. py:method:: SpectrumAccessTransforming.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms available




.. py:method:: SpectrumAccessTransforming.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the number of spectra available




.. py:method:: SpectrumAccessTransforming.getSpectraByRT


Cython signature: libcpp_vector[size_t] getSpectraByRT(double RT, double deltaRT)
Returns a vector of ids of spectra that are within RT +/- deltaRT




.. py:method:: SpectrumAccessTransforming.getSpectrumById


Cython signature: shared_ptr[OSSpectrum] getSpectrumById(int id_)
Returns a pointer to a spectrum at the given string id




