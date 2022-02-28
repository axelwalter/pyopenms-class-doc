TransformationModelLinear
=========================

.. py:class:: TransformationModelLinear


   Bases: :py:class:`object`


Cython implementation of _TransformationModelLinear


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransformationModelLinear.html
 -- Inherits from ['TransformationModel']




.. py:method:: TransformationModelLinear.checkDatumRange


Cython signature: double checkDatumRange(const double & datum, const double & datum_min, const double & datum_max)
Check that the datum is within the valid min and max bounds




.. py:method:: TransformationModelLinear.checkValidWeight


Cython signature: bool checkValidWeight(const String & weight, libcpp_vector[String] & valid_weights)
Check for a valid weighting function string




.. py:method:: TransformationModelLinear.evaluate


Cython signature: double evaluate(double value)




.. py:method:: TransformationModelLinear.getDefaultParameters


Cython signature: void getDefaultParameters(Param &)




.. py:method:: TransformationModelLinear.getParameters


Cython signature: Param getParameters()




.. py:method:: TransformationModelLinear.getValidXWeights


Cython signature: libcpp_vector[String] getValidXWeights()
Returns a list of valid x weight function stringss




.. py:method:: TransformationModelLinear.getValidYWeights


Cython signature: libcpp_vector[String] getValidYWeights()
Returns a list of valid y weight function strings




.. py:method:: TransformationModelLinear.invert


Cython signature: void invert()




.. py:method:: TransformationModelLinear.unWeightData


Cython signature: void unWeightData(libcpp_vector[TM_DataPoint] & data)
Unweight the data by the given weight function




.. py:method:: TransformationModelLinear.unWeightDatum


Cython signature: double unWeightDatum(double & datum, const String & weight)
Apply the reverse of the weighting function to the data




.. py:method:: TransformationModelLinear.weightData


Cython signature: void weightData(libcpp_vector[TM_DataPoint] & data)
Weight the data by the given weight function




.. py:method:: TransformationModelLinear.weightDatum


Cython signature: double weightDatum(double & datum, const String & weight)
Weight the data according to the weighting function




