MSDataStoringConsumer
=====================

.. py:class:: MSDataStoringConsumer


   Bases: :py:class:`object`


Cython implementation of _MSDataStoringConsumer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSDataStoringConsumer.html


 Consumer class that simply stores the data
 -----
 This class is able to keep spectra and chromatograms passed to it in memory
 and the data can be accessed through getData()




.. py:method:: MSDataStoringConsumer.consumeChromatogram


Cython signature: void consumeChromatogram(MSChromatogram &)




.. py:method:: MSDataStoringConsumer.consumeSpectrum


Cython signature: void consumeSpectrum(MSSpectrum & s)




.. py:method:: MSDataStoringConsumer.getData


Cython signature: MSExperiment getData()




.. py:method:: MSDataStoringConsumer.setExpectedSize


Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)
Sets expected size




.. py:method:: MSDataStoringConsumer.setExperimentalSettings


Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)
Sets experimental settings




