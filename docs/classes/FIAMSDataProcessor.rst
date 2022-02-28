FIAMSDataProcessor
==================

.. py:class:: FIAMSDataProcessor


   Bases: :py:class:`object`


Cython implementation of _FIAMSDataProcessor


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FIAMSDataProcessor.html
 -- Inherits from ['DefaultParamHandler']


   ADD PYTHON DOCUMENTATION HERE




.. py:method:: FIAMSDataProcessor.convertToFeatureMap


Cython signature: FeatureMap convertToFeatureMap(MSSpectrum & input_)


Convert a spectrum to a feature map with the corresponding polarity
-----
Applies `SavitzkyGolayFilter` and `PeakPickerHiRes`
-----
:param input: Input a picked spectrum
:returns: A feature map with the peaks converted to features and polarity from the parameters
Estimate noise for each peak
-----
Uses `SignalToNoiseEstimatorMedianRapid`
-----
:param input: Input a picked spectrum
:returns: A spectrum object storing logSN information




.. py:method:: FIAMSDataProcessor.extractPeaks


Cython signature: MSSpectrum extractPeaks(MSSpectrum & input_)


Pick peaks from the summed spectrum
-----
:param input: Input vector of spectra
:returns: A spectrum with picked peaks
Convert a spectrum to a feature map with the corresponding polarity
-----
Applies `SavitzkyGolayFilter` and `PeakPickerHiRes`
-----
:param input: Input a picked spectrum
:returns: A feature map with the peaks converted to features and polarity from the parameters
Estimate noise for each peak
-----
Uses `SignalToNoiseEstimatorMedianRapid`
-----
:param input: Input a picked spectrum
:returns: A spectrum object storing logSN information




.. py:method:: FIAMSDataProcessor.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FIAMSDataProcessor.getName


Cython signature: String getName()
Returns the name




.. py:method:: FIAMSDataProcessor.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FIAMSDataProcessor.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FIAMSDataProcessor.run


Cython signature: bool run(MSExperiment & experiment, float & n_seconds, MzTab & output, bool load_cached_spectrum)


Run the full analysis for the experiment for the given time interval
-----
The workflow steps are:
- the time axis of the experiment is cut to the interval from 0 to n_seconds
- the spectra are summed into one along the time axis with the bin size determined by mz and instrument resolution
- data is smoothed by applying the Savitzky-Golay filter
- peaks are picked
- the accurate mass search for all the picked peaks is performed




.. py:method:: FIAMSDataProcessor.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FIAMSDataProcessor.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: FIAMSDataProcessor.trackNoise


Cython signature: MSSpectrum trackNoise(MSSpectrum & input_)


Estimate noise for each peak
-----
Uses `SignalToNoiseEstimatorMedianRapid`
-----
:param input: Input a picked spectrum
:returns: A spectrum object storing logSN information




