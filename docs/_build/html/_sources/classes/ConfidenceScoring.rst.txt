ConfidenceScoring
=================

.. py:class:: ConfidenceScoring


   Bases: :py:class:`object`


Cython implementation of _ConfidenceScoring


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConfidenceScoring.html




.. py:method:: ConfidenceScoring.initialize


Cython signature: void initialize(TargetedExperiment & targeted, size_t n_decoys, size_t n_transitions, TransformationDescription trafo)




.. py:method:: ConfidenceScoring.initializeGlm


Cython signature: void initializeGlm(double intercept, double rt_coef, double int_coef)




.. py:method:: ConfidenceScoring.scoreMap


Cython signature: void scoreMap(FeatureMap & map)
Score a feature map -> make sure the class is properly initialized




