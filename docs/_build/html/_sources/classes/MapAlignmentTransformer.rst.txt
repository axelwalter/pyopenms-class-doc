MapAlignmentTransformer
=======================

.. py:class:: MapAlignmentTransformer


   Bases: :py:class:`object`


Cython implementation of _MapAlignmentTransformer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MapAlignmentTransformer.html


This class collects functions for applying retention time transformations to data structures




.. py:method:: MapAlignmentTransformer.transformRetentionTimes


- Cython signature: void transformRetentionTimes(MSExperiment &, TransformationDescription &, bool)
  Applies the given transformation to a peak map


- Cython signature: void transformRetentionTimes(FeatureMap &, TransformationDescription &, bool)
  Applies the given transformation to a feature map


- Cython signature: void transformRetentionTimes(ConsensusMap &, TransformationDescription &, bool)
  Applies the given transformation to a consensus map


- Cython signature: void transformRetentionTimes(libcpp_vector[PeptideIdentification] &, TransformationDescription &, bool)
  Applies the given transformation to peptide identifications




