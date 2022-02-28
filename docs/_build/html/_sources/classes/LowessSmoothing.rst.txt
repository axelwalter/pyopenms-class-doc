LowessSmoothing
===============

.. py:class:: LowessSmoothing


   Bases: :py:class:`object`


Cython implementation of _LowessSmoothing


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LowessSmoothing.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: LowessSmoothing.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: LowessSmoothing.getName


Cython signature: String getName()
Returns the name




.. py:method:: LowessSmoothing.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: LowessSmoothing.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: LowessSmoothing.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: LowessSmoothing.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: LowessSmoothing.smoothData


Cython signature: void smoothData(libcpp_vector[double] x, libcpp_vector[double] y, libcpp_vector[double] & y_smoothed)
Smoothing method that receives x and y coordinates (e.g., RT and intensities) and computes smoothed intensities




