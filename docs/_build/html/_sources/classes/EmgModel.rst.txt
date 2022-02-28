EmgModel
========

.. py:class:: EmgModel


   Bases: :py:class:`object`


Cython implementation of _EmgModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1EmgModel.html
 -- Inherits from ['InterpolationModel']




.. py:method:: EmgModel.getCenter


Cython signature: double getCenter()
Returns the "center" of the model, particular definition (depends on the derived model)




.. py:method:: EmgModel.getIntensity


Cython signature: double getIntensity(double coord)
Access model predicted intensity at position 'pos'




.. py:method:: EmgModel.getInterpolation


Cython signature: LinearInterpolation getInterpolation()
Returns the interpolation class




.. py:method:: EmgModel.getProductName


Cython signature: String getProductName()
Name of the model




.. py:method:: EmgModel.getScalingFactor


Cython signature: double getScalingFactor()
Returns the interpolation class




.. py:method:: EmgModel.setInterpolationStep


Cython signature: void setInterpolationStep(double interpolation_step)
Sets the interpolation step for the linear interpolation of the model




.. py:method:: EmgModel.setOffset


Cython signature: void setOffset(double offset)
Sets the offset of the model




.. py:method:: EmgModel.setSamples


Cython signature: void setSamples()
Sets sample/supporting points of interpolation wrt params




.. py:method:: EmgModel.setScalingFactor


Cython signature: void setScalingFactor(double scaling)
Sets the scaling factor of the model




