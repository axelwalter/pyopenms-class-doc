MSDataSqlConsumer
=================

.. py:class:: MSDataSqlConsumer


   Bases: :py:class:`object`


Cython implementation of _MSDataSqlConsumer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSDataSqlConsumer.html




.. py:method:: MSDataSqlConsumer.consumeChromatogram


Cython signature: void consumeChromatogram(MSChromatogram & c)
Write a chromatogram to the output file




.. py:method:: MSDataSqlConsumer.consumeSpectrum


Cython signature: void consumeSpectrum(MSSpectrum & s)
Write a spectrum to the output file




.. py:method:: MSDataSqlConsumer.flush


Cython signature: void flush()


Flushes the data for good
-----
After calling this function, no more data is held in the buffer but the
class is still able to receive new data




.. py:method:: MSDataSqlConsumer.setExpectedSize


Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)




.. py:method:: MSDataSqlConsumer.setExperimentalSettings


Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)




