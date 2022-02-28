ConsensusMapNormalizerAlgorithmThreshold
========================================

.. py:class:: ConsensusMapNormalizerAlgorithmThreshold


   Bases: :py:class:`object`


Cython implementation of _ConsensusMapNormalizerAlgorithmThreshold


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusMapNormalizerAlgorithmThreshold.html




.. py:method:: ConsensusMapNormalizerAlgorithmThreshold.computeCorrelation


Cython signature: libcpp_vector[double] computeCorrelation(ConsensusMap & input_map, double ratio_threshold, const String & acc_filter, const String & desc_filter)
Determines the ratio of all maps to the map with the most features




.. py:method:: ConsensusMapNormalizerAlgorithmThreshold.normalizeMaps


Cython signature: void normalizeMaps(ConsensusMap & input_map, libcpp_vector[double] & ratios)
Applies the given ratio to the maps of the consensusMap




