GaussTraceFitter
================

.. py:class:: GaussTraceFitter


   Bases: :py:class:`object`


Cython implementation of _GaussTraceFitter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1GaussTraceFitter.html




.. py:method:: GaussTraceFitter.checkMaximalRTSpan


Cython signature: bool checkMaximalRTSpan(double max_rt_span)




.. py:method:: GaussTraceFitter.checkMinimalRTSpan


Cython signature: bool checkMinimalRTSpan(libcpp_pair[double,double] & rt_bounds, double min_rt_span)




.. py:method:: GaussTraceFitter.computeTheoretical


Cython signature: double computeTheoretical(MassTrace & trace, size_t k)




.. py:method:: GaussTraceFitter.fit


Cython signature: void fit(MassTraces & traces)
Override important methods




.. py:method:: GaussTraceFitter.getArea


Cython signature: double getArea()
Returns area of the fitted gaussian model




.. py:method:: GaussTraceFitter.getCenter


Cython signature: double getCenter()
Returns center of the fitted gaussian model




.. py:method:: GaussTraceFitter.getFWHM


Cython signature: double getFWHM()
Returns FWHM of the fitted gaussian model




.. py:method:: GaussTraceFitter.getGnuplotFormula


Cython signature: String getGnuplotFormula(MassTrace & trace, char function_name, double baseline, double rt_shift)




.. py:method:: GaussTraceFitter.getHeight


Cython signature: double getHeight()
Returns height of the fitted gaussian model




.. py:method:: GaussTraceFitter.getLowerRTBound


Cython signature: double getLowerRTBound()
Returns the lower RT bound




.. py:method:: GaussTraceFitter.getSigma


Cython signature: double getSigma()
Returns Sigma of the fitted gaussian model




.. py:method:: GaussTraceFitter.getUpperRTBound


Cython signature: double getUpperRTBound()
Returns the upper RT bound




.. py:method:: GaussTraceFitter.getValue


Cython signature: double getValue(double rt)
Returns value of the fitted gaussian model




