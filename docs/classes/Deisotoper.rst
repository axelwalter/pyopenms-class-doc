Deisotoper
==========

.. py:class:: Deisotoper


   Bases: :py:class:`object`


Cython implementation of _Deisotoper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Deisotoper.html




.. py:method:: Deisotoper.deisotopeAndSingleCharge


Cython signature: void deisotopeAndSingleCharge(MSSpectrum & spectra, double fragment_tolerance, bool fragment_unit_ppm, int min_charge, int max_charge, bool keep_only_deisotoped, unsigned int min_isopeaks, unsigned int max_isopeaks, bool make_single_charged, bool annotate_charge, bool annotate_iso_peak_count, bool use_decreasing_model, unsigned int start_intensity_check, bool add_up_intensity)




.. py:method:: Deisotoper.deisotopeAndSingleChargeDefault


Cython signature: void deisotopeAndSingleChargeDefault(MSSpectrum & spectra, double fragment_tolerance, bool fragment_unit_ppm)




.. py:method:: Deisotoper.deisotopeWithAveragineModel


Cython signature: void deisotopeWithAveragineModel(MSSpectrum & spectrum, double fragment_tolerance, bool fragment_unit_ppm, int number_of_final_peaks, int min_charge, int max_charge, bool keep_only_deisotoped, unsigned int min_isopeaks, unsigned int max_isopeaks, bool make_single_charged, bool annotate_charge, bool annotate_iso_peak_count, bool add_up_intensity)




