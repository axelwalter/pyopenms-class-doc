MRMRTNormalizer
===============

.. py:class:: MRMRTNormalizer


   Bases: :py:class:`object`


Cython implementation of _MRMRTNormalizer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMRTNormalizer.html




.. py:method:: MRMRTNormalizer.chauvenet


Cython signature: bool chauvenet(libcpp_vector[double] residuals, int pos)




.. py:method:: MRMRTNormalizer.chauvenet_probability


Cython signature: double chauvenet_probability(libcpp_vector[double] residuals, int pos)




.. py:method:: MRMRTNormalizer.computeBinnedCoverage


Cython signature: bool computeBinnedCoverage(libcpp_pair[double,double] rtRange, libcpp_vector[libcpp_pair[double,double]] & pairs, int nrBins, int minPeptidesPerBin, int minBinsFilled)




.. py:method:: MRMRTNormalizer.removeOutliersIterative


Cython signature: libcpp_vector[libcpp_pair[double,double]] removeOutliersIterative(libcpp_vector[libcpp_pair[double,double]] & pairs, double rsq_limit, double coverage_limit, bool use_chauvenet, libcpp_string outlier_detection_method)




.. py:method:: MRMRTNormalizer.removeOutliersRANSAC


Cython signature: libcpp_vector[libcpp_pair[double,double]] removeOutliersRANSAC(libcpp_vector[libcpp_pair[double,double]] & pairs, double rsq_limit, double coverage_limit, size_t max_iterations, double max_rt_threshold, size_t sampling_size)




