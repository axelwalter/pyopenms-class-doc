FineIsotopePatternGenerator
===========================

.. py:class:: FineIsotopePatternGenerator


   Bases: :py:class:`object`


Cython implementation of _FineIsotopePatternGenerator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FineIsotopePatternGenerator.html


 Isotope pattern generator for fine isotope distributions.
 Generates isotopes until a stop condition (threshold) is reached,
 the lower the threshold the more isotopes are generated. The
 parameter use_total_prob defines whether the stop condition is
 interpreted as the total probability that the distribution should
 cover (default) or as a threshold for individual peaks. Finally,
 the absolute parameter specifies for individual peak thresholding
 if the threshold is absolute or relative.




.. py:method:: FineIsotopePatternGenerator.getAbsolute


Cython signature: bool getAbsolute()




.. py:method:: FineIsotopePatternGenerator.getThreshold


Cython signature: double getThreshold()




.. py:method:: FineIsotopePatternGenerator.getTotalProbability


Cython signature: bool getTotalProbability()




.. py:method:: FineIsotopePatternGenerator.run


Cython signature: IsotopeDistribution run(EmpiricalFormula)




.. py:method:: FineIsotopePatternGenerator.setAbsolute


Cython signature: void setAbsolute(bool absolute)




.. py:method:: FineIsotopePatternGenerator.setThreshold


Cython signature: void setThreshold(double threshold)




.. py:method:: FineIsotopePatternGenerator.setTotalProbability


Cython signature: void setTotalProbability(bool total)




