BSpline2d
=========

.. py:class:: BSpline2d


   Bases: :py:class:`object`


Cython implementation of _BSpline2d


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1BSpline2d.html




.. py:method:: BSpline2d.debug


Cython signature: void debug(bool enable)
Enable or disable debug messages from the B-spline library




.. py:method:: BSpline2d.derivative


Cython signature: double derivative(double x)
Returns the first derivative of the spline curve at the given position x. Returns zero if the current state is not ok()




.. py:method:: BSpline2d.eval


Cython signature: double eval(double x)
Returns the evaluation of the smoothed curve at a particular x value. If current state is not ok(), returns zero




.. py:method:: BSpline2d.ok


Cython signature: bool ok()
Returns whether the spline fit was successful




.. py:method:: BSpline2d.solve


Cython signature: bool solve(libcpp_vector[double] y)
Solve the spline curve for a new set of y values. Returns false if the solution fails




