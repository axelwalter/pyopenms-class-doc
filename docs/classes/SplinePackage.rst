SplinePackage
=============

.. py:class:: SplinePackage


   Bases: :py:class:`object`


Cython implementation of _SplinePackage


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SplinePackage.html




.. py:method:: SplinePackage.eval


Cython signature: double eval(double pos)
Returns interpolated intensity position `pos`




.. py:method:: SplinePackage.getPosMax


Cython signature: double getPosMax()
Returns the maximum position for which the spline fit is valid




.. py:method:: SplinePackage.getPosMin


Cython signature: double getPosMin()
Returns the minimum position for which the spline fit is valid




.. py:method:: SplinePackage.getPosStepWidth


Cython signature: double getPosStepWidth()
Returns a sensible position step width for the package




.. py:method:: SplinePackage.isInPackage


Cython signature: bool isInPackage(double pos)
Returns true if position in




