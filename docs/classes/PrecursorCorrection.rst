PrecursorCorrection
===================

.. py:class:: PrecursorCorrection


   Bases: :py:class:`object`


Cython implementation of _PrecursorCorrection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PrecursorCorrection.html




.. py:method:: PrecursorCorrection.correctToHighestIntensityMS1Peak


Cython signature: libcpp_set[size_t] correctToHighestIntensityMS1Peak(MSExperiment & exp, double mz_tolerance, bool ppm, libcpp_vector[double] & delta_mzs, libcpp_vector[double] & mzs, libcpp_vector[double] & rts)




.. py:method:: PrecursorCorrection.correctToNearestFeature


Cython signature: libcpp_set[size_t] correctToNearestFeature(FeatureMap & features, MSExperiment & exp, double rt_tolerance_s, double mz_tolerance, bool ppm, bool believe_charge, bool keep_original, bool all_matching_features, int max_trace, int debug_level)




.. py:method:: PrecursorCorrection.correctToNearestMS1Peak


Cython signature: libcpp_set[size_t] correctToNearestMS1Peak(MSExperiment & exp, double mz_tolerance, bool ppm, libcpp_vector[double] & delta_mzs, libcpp_vector[double] & mzs, libcpp_vector[double] & rts)




.. py:method:: PrecursorCorrection.getPrecursors


Cython signature: void getPrecursors(MSExperiment & exp, libcpp_vector[Precursor] & precursors, libcpp_vector[double] & precursors_rt, libcpp_vector[size_t] & precursor_scan_index)




.. py:method:: PrecursorCorrection.writeHist


Cython signature: void writeHist(String & out_csv, libcpp_vector[double] & delta_mzs, libcpp_vector[double] & mzs, libcpp_vector[double] & rts)




