SpectrumAccessQuadMZTransforming
================================

.. py:class:: SpectrumAccessQuadMZTransforming


   Bases: :py:class:`object`


Cython implementation of _SpectrumAccessQuadMZTransforming


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAccessQuadMZTransforming.html
 -- Inherits from ['SpectrumAccessTransforming']




.. py:method:: SpectrumAccessQuadMZTransforming.getChromatogramById


Cython signature: shared_ptr[OSChromatogram] getChromatogramById(int id_)
Returns a pointer to a chromatogram at the given id




.. py:method:: SpectrumAccessQuadMZTransforming.getChromatogramNativeID


Cython signature: libcpp_utf8_output_string getChromatogramNativeID(int id_)




.. py:method:: SpectrumAccessQuadMZTransforming.getNrChromatograms


Cython signature: size_t getNrChromatograms()
Returns the number of chromatograms available




.. py:method:: SpectrumAccessQuadMZTransforming.getNrSpectra


Cython signature: size_t getNrSpectra()
Returns the number of spectra available




.. py:method:: SpectrumAccessQuadMZTransforming.getSpectraByRT


Cython signature: libcpp_vector[size_t] getSpectraByRT(double RT, double deltaRT)
Returns a vector of ids of spectra that are within RT +/- deltaRT




.. py:method:: SpectrumAccessQuadMZTransforming.getSpectrumById


Cython signature: shared_ptr[OSSpectrum] getSpectrumById(int id_)
Returns a pointer to a spectrum at the given string id




