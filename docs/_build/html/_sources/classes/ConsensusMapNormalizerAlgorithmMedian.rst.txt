ConsensusMapNormalizerAlgorithmMedian
=====================================

.. py:class:: ConsensusMapNormalizerAlgorithmMedian


   Bases: :py:class:`object`


Cython implementation of _ConsensusMapNormalizerAlgorithmMedian


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ConsensusMapNormalizerAlgorithmMedian_1_1ConsensusMapNormalizerAlgorithmMedian.html




.. py:method:: ConsensusMapNormalizerAlgorithmMedian.computeMedians


Cython signature: size_t computeMedians(ConsensusMap & input_map, libcpp_vector[double] & medians, const String & acc_filter, const String & desc_filter)
Computes medians of all maps and returns index of map with most features




.. py:method:: ConsensusMapNormalizerAlgorithmMedian.normalizeMaps


Cython signature: void normalizeMaps(ConsensusMap & input_map, NormalizationMethod method, const String & acc_filter, const String & desc_filter)
Normalizes the maps of the consensusMap




