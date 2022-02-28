OptimizePick
============

.. py:class:: OptimizePick


   Bases: :py:class:`object`


Cython implementation of _OptimizePick


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OptimizePick.html


 This class provides the non-linear optimization of the peak parameters
 -----
 Given a vector of peak shapes, this class optimizes all peak shapes parameters using a non-linear optimization
 For the non-linear optimization we use the Levenberg-Marquardt algorithm provided by the Eigen




.. py:method:: OptimizePick.getNumberIterations


Cython signature: unsigned int getNumberIterations()
Returns the number of iterations




.. py:method:: OptimizePick.getPenalties


Cython signature: OptimizationFunctions_PenaltyFactors getPenalties()
Returns the penalty factors




.. py:method:: OptimizePick.setNumberIterations


Cython signature: void setNumberIterations(int max_iteration)
Sets the number of iterations




.. py:method:: OptimizePick.setPenalties


Cython signature: void setPenalties(OptimizationFunctions_PenaltyFactors penalties)
Sets the penalty factors




