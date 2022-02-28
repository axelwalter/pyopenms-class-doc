PeakWidthEstimator
==================

.. py:class:: PeakWidthEstimator


   Bases: :py:class:`object`


Cython implementation of _PeakWidthEstimator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakWidthEstimator.html


 Rough estimation of the peak width at m/z
 -----
 Based on the peaks of the dataset (peak position & width) and the peak
 boundaries as reported by the PeakPickerHiRes, the typical peak width is
 estimated for arbitrary m/z using a spline interpolationThis struct can be used to store both peak or feature indices`




.. py:method:: PeakWidthEstimator.getPeakWidth


Cython signature: double getPeakWidth(double mz)
Returns the estimated peak width at m/z




