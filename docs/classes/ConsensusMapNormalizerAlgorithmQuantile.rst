ConsensusMapNormalizerAlgorithmQuantile
=======================================

.. py:class:: ConsensusMapNormalizerAlgorithmQuantile


   Bases: :py:class:`object`


Cython implementation of _ConsensusMapNormalizerAlgorithmQuantile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusMapNormalizerAlgorithmQuantile.html




.. py:method:: ConsensusMapNormalizerAlgorithmQuantile.extractIntensityVectors


Cython signature: void extractIntensityVectors(ConsensusMap & map_, libcpp_vector[libcpp_vector[double]] & out_intensities)
Extracts the intensities of the features of the different maps




.. py:method:: ConsensusMapNormalizerAlgorithmQuantile.normalizeMaps


Cython signature: void normalizeMaps(ConsensusMap & input_map)




.. py:method:: ConsensusMapNormalizerAlgorithmQuantile.resample


Cython signature: void resample(libcpp_vector[double] & data_in, libcpp_vector[double] & data_out, unsigned int n_resampling_points)
Resamples data_in and writes the results to data_out




.. py:method:: ConsensusMapNormalizerAlgorithmQuantile.setNormalizedIntensityValues


Cython signature: void setNormalizedIntensityValues(libcpp_vector[libcpp_vector[double]] & feature_ints, ConsensusMap & map_)
Writes the intensity values in feature_ints to the corresponding features in map




