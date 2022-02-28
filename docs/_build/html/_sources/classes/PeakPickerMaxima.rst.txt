PeakPickerMaxima
================

.. py:class:: PeakPickerMaxima


   Bases: :py:class:`object`


Cython implementation of _PeakPickerMaxima


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerMaxima.html


 This class implements a fast peak-picking algorithm best suited for
 high resolution MS data (FT-ICR-MS, Orbitrap). In high resolution data, the
 signals of ions with similar mass-to-charge ratios (m/z) exhibit little or
 no overlapping and therefore allow for a clear separation. Furthermore, ion
 signals tend to show well-defined peak shapes with narrow peak width
 -----
 This peak-picking algorithm detects ion signals in raw data and
 reconstructs the corresponding peak shape by cubic spline interpolation.
 Signal detection depends on the signal-to-noise ratio which is adjustable
 by the user (see parameter signal_to_noise). A picked peak's m/z and
 intensity value is given by the maximum of the underlying peak spline
 -----
 So far, this peak picker was mainly tested on high resolution data. With
 appropriate preprocessing steps (e.g. noise reduction and baseline
 subtraction), it might be also applied to low resolution data




.. py:method:: PeakPickerMaxima.findMaxima


Cython signature: void findMaxima(libcpp_vector[double] mz_array, libcpp_vector[double] int_array, libcpp_vector[PeakCandidate] & pc)


Will find local maxima in raw data
-----
:param mz_array: The array containing m/z values
:param int_array: The array containing intensity values
:param pc: The resulting array containing the peak candidates
:param check_spacings: Check spacing constraints (recommended settings: yes for spectra, no for chromatograms)




.. py:method:: PeakPickerMaxima.pick


Cython signature: void pick(libcpp_vector[double] mz_array, libcpp_vector[double] int_array, libcpp_vector[PeakCandidate] & pc)




