MSDataCachedConsumer
====================

.. py:class:: MSDataCachedConsumer


   Bases: :py:class:`object`


Cython implementation of _MSDataCachedConsumer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSDataCachedConsumer.html


 Transforming and cached writing consumer of MS data
 -----
 Is able to transform a spectrum on the fly while it is read using a
 function pointer that can be set on the object. The spectra is then
 cached to disk using the functions provided in CachedMzMLHandler.




.. py:method:: MSDataCachedConsumer.consumeChromatogram


Cython signature: void consumeChromatogram(MSChromatogram & c)


Write a chromatogram to the output file
-----
May delete data from chromatogram (if clearData is set)




.. py:method:: MSDataCachedConsumer.consumeSpectrum


Cython signature: void consumeSpectrum(MSSpectrum & s)


Write a spectrum to the output file
-----
May delete data from spectrum (if clearData is set)




.. py:method:: MSDataCachedConsumer.setExpectedSize


Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)




.. py:method:: MSDataCachedConsumer.setExperimentalSettings


Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)




