PeakIndex
=========

.. py:class:: PeakIndex


   Bases: :py:class:`object`


Cython implementation of _PeakIndex


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakIndex.html


 Index of a peak or feature
 -----
 This struct can be used to store both peak or feature indices




.. py:method:: PeakIndex.clear


Cython signature: void clear()
Invalidates the current index




.. py:method:: PeakIndex.getFeature


Cython signature: Feature getFeature(FeatureMap & map_)


Returns the feature (or consensus feature) corresponding to this index
-----
This method is intended for arrays of features e.g. FeatureMap
-----
The main advantage of using this method instead accessing the data directly is that range
check performed in debug mode
-----
:raises:
  Exception: Precondition is thrown if this index is invalid for the `map` (only in debug mode)




.. py:method:: PeakIndex.getPeak


Cython signature: Peak1D getPeak(MSExperiment & map_)


Returns a peak corresponding to this index
-----
This method is intended for arrays of DSpectra e.g. MSExperiment
-----
The main advantage of using this method instead accessing the data directly is that range
check performed in debug mode
-----
:raises:
  Exception: Precondition is thrown if this index is invalid for the `map` (only in debug mode)




.. py:method:: PeakIndex.getSpectrum


Cython signature: MSSpectrum getSpectrum(MSExperiment & map_)


Returns a spectrum corresponding to this index
-----
This method is intended for arrays of DSpectra e.g. MSExperiment
-----
The main advantage of using this method instead accessing the data directly is that range
check performed in debug mode
-----
:raises:
  Exception: Precondition is thrown if this index is invalid for the `map` (only in debug mode)




.. py:method:: PeakIndex.isValid


Cython signature: bool isValid()
Returns if the current peak ref is valid




.. py:attribute:: PeakIndex.peak




.. py:attribute:: PeakIndex.spectrum




