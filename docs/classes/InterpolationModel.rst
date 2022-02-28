InterpolationModel
==================

.. py:class:: InterpolationModel


   Bases: :py:class:`object`


Cython implementation of _InterpolationModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1InterpolationModel.html




.. py:method:: InterpolationModel.getCenter


Cython signature: double getCenter()
Returns the "center" of the model, particular definition (depends on the derived model)




.. py:method:: InterpolationModel.getIntensity


Cython signature: double getIntensity(double coord)
Access model predicted intensity at position 'pos'




.. py:method:: InterpolationModel.getInterpolation


Cython signature: LinearInterpolation getInterpolation()
Returns the interpolation class




.. py:method:: InterpolationModel.getScalingFactor


Cython signature: double getScalingFactor()
Returns the interpolation class




.. py:method:: InterpolationModel.setInterpolationStep


Cython signature: void setInterpolationStep(double interpolation_step)
Sets the interpolation step for the linear interpolation of the model




.. py:method:: InterpolationModel.setOffset


Cython signature: void setOffset(double offset)
Sets the offset of the model




.. py:method:: InterpolationModel.setSamples


Cython signature: void setSamples()
Sets sample/supporting points of interpolation wrt params




.. py:method:: InterpolationModel.setScalingFactor


Cython signature: void setScalingFactor(double scaling)
Sets the scaling factor of the model




