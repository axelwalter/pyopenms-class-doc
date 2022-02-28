PlainMSDataWritingConsumer
==========================

.. py:class:: PlainMSDataWritingConsumer


   Bases: :py:class:`object`


Cython implementation of _PlainMSDataWritingConsumer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PlainMSDataWritingConsumer.html




.. py:method:: PlainMSDataWritingConsumer.addDataProcessing


Cython signature: void addDataProcessing(DataProcessing d)


Optionally add a data processing method to each chromatogram and spectrum
-----
The provided DataProcessing object will be added to each chromatogram
and spectrum written to to the mzML file
-----
:param d: The DataProcessing object to be added




.. py:method:: PlainMSDataWritingConsumer.consumeChromatogram


Cython signature: void consumeChromatogram(MSChromatogram & c)




.. py:method:: PlainMSDataWritingConsumer.consumeSpectrum


Cython signature: void consumeSpectrum(MSSpectrum & s)




.. py:method:: PlainMSDataWritingConsumer.getNrChromatogramsWritten


Cython signature: size_t getNrChromatogramsWritten()
Returns the number of chromatograms written




.. py:method:: PlainMSDataWritingConsumer.getNrSpectraWritten


Cython signature: size_t getNrSpectraWritten()
Returns the number of spectra written




.. py:method:: PlainMSDataWritingConsumer.getOptions


Cython signature: PeakFileOptions getOptions()




.. py:method:: PlainMSDataWritingConsumer.setExpectedSize


Cython signature: void setExpectedSize(size_t expectedSpectra, size_t expectedChromatograms)


Set expected size of spectra and chromatograms to be written
-----
These numbers will be written in the spectrumList and chromatogramList
tag in the mzML file. Therefore, these will contain wrong numbers if
the expected size is not set correctly
-----
:param expectedSpectra: Number of spectra expected
:param expectedChromatograms: Number of chromatograms expected




.. py:method:: PlainMSDataWritingConsumer.setExperimentalSettings


Cython signature: void setExperimentalSettings(ExperimentalSettings & exp)


Set experimental settings for the whole file
-----
:param exp: Experimental settings to be used for this file (from this
and the first spectrum/chromatogram, the class will deduce most of
the header of the mzML file)




.. py:method:: PlainMSDataWritingConsumer.setOptions


Cython signature: void setOptions(PeakFileOptions opt)




