GaussFitter
===========

.. py:class:: GaussFitter


   Bases: :py:class:`object`


Cython implementation of _GaussFitter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Math_1_1GaussFitter.html




.. py:method:: GaussFitter.fit


Cython signature: GaussFitResult fit(libcpp_vector[DPosition2] points)
Fits a Gaussian distribution to the given data points




.. py:method:: GaussFitter.setInitialParameters


Cython signature: void setInitialParameters(GaussFitResult & result)
Sets the initial parameters used by the fit method as initial guess for the Gaussian




