TransformationModelInterpolated
===============================

.. py:class:: TransformationModelInterpolated


   Bases: :py:class:`object`


Cython implementation of _TransformationModelInterpolated


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransformationModelInterpolated.html
 -- Inherits from ['TransformationModel']




.. py:method:: TransformationModelInterpolated.checkDatumRange


Cython signature: double checkDatumRange(const double & datum, const double & datum_min, const double & datum_max)
Check that the datum is within the valid min and max bounds




.. py:method:: TransformationModelInterpolated.checkValidWeight


Cython signature: bool checkValidWeight(const String & weight, libcpp_vector[String] & valid_weights)
Check for a valid weighting function string




.. py:method:: TransformationModelInterpolated.evaluate


Cython signature: double evaluate(double value)


Evaluate the interpolation model at the given value
-----
:param value: The position where the interpolation should be evaluated
:returns: The interpolated value




.. py:method:: TransformationModelInterpolated.getDefaultParameters


Cython signature: void getDefaultParameters(Param &)
Gets the default parameters




.. py:method:: TransformationModelInterpolated.getParameters


Cython signature: Param getParameters()




.. py:method:: TransformationModelInterpolated.getValidXWeights


Cython signature: libcpp_vector[String] getValidXWeights()
Returns a list of valid x weight function stringss




.. py:method:: TransformationModelInterpolated.getValidYWeights


Cython signature: libcpp_vector[String] getValidYWeights()
Returns a list of valid y weight function strings




.. py:method:: TransformationModelInterpolated.unWeightData


Cython signature: void unWeightData(libcpp_vector[TM_DataPoint] & data)
Unweight the data by the given weight function




.. py:method:: TransformationModelInterpolated.unWeightDatum


Cython signature: double unWeightDatum(double & datum, const String & weight)
Apply the reverse of the weighting function to the data




.. py:method:: TransformationModelInterpolated.weightData


Cython signature: void weightData(libcpp_vector[TM_DataPoint] & data)
Weight the data by the given weight function




.. py:method:: TransformationModelInterpolated.weightDatum


Cython signature: double weightDatum(double & datum, const String & weight)
Weight the data according to the weighting function




