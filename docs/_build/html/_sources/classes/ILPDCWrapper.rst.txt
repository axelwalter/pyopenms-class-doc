ILPDCWrapper
============

.. py:class:: ILPDCWrapper


   Bases: :py:class:`object`


Cython implementation of _ILPDCWrapper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ILPDCWrapper.html




.. py:method:: ILPDCWrapper.compute


Cython signature: double compute(FeatureMap fm, libcpp_vector[ChargePair] & pairs, size_t verbose_level)
Compute optimal solution and return value of objective function. If the input feature map is empty, a warning is issued and -1 is returned




