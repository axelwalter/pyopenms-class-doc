NoopMSDataWritingConsumer
=========================

.. py:class:: NoopMSDataWritingConsumer


   Bases: :py:class:`object`


Cython implementation of _NoopMSDataWritingConsumer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1NoopMSDataWritingConsumer.html


 Consumer class that perform no operation
 -----
 This is sometimes necessary to fulfill the requirement of passing an
 valid MSDataWritingConsumer object or pointer but no operation is
 required




.. py:method:: NoopMSDataWritingConsumer.addDataProcessing


Cython signature: void addDataProcessing(DataProcessing d)




.. py:method:: NoopMSDataWritingConsumer.consumeChromatogram


Cython signature: void consumeChromatogram(MSChromatogram & c)




.. py:method:: NoopMSDataWritingConsumer.consumeSpectrum


Cython signature: void consumeSpectrum(MSSpectrum & s)




.. py:method:: NoopMSDataWritingConsumer.getNrChromatogramsWritten


Cython signature: size_t getNrChromatogramsWritten()




.. py:method:: NoopMSDataWritingConsumer.getNrSpectraWritten


Cython signature: size_t getNrSpectraWritten()




.. py:method:: NoopMSDataWritingConsumer.setExpectedSize


Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)




.. py:method:: NoopMSDataWritingConsumer.setExperimentalSettings


Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)




