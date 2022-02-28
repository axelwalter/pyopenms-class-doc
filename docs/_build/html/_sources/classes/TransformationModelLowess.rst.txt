TransformationModelLowess
=========================

.. py:class:: TransformationModelLowess


   Bases: :py:class:`object`


Cython implementation of _TransformationModelLowess


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TransformationModelLowess.html
 -- Inherits from ['TransformationModel']




.. py:method:: TransformationModelLowess.checkDatumRange


Cython signature: double checkDatumRange(const double & datum, const double & datum_min, const double & datum_max)
Check that the datum is within the valid min and max bounds




.. py:method:: TransformationModelLowess.checkValidWeight


Cython signature: bool checkValidWeight(const String & weight, libcpp_vector[String] & valid_weights)
Check for a valid weighting function string




.. py:method:: TransformationModelLowess.evaluate


Cython signature: double evaluate(double value)




.. py:method:: TransformationModelLowess.getDefaultParameters


Cython signature: void getDefaultParameters(Param &)




.. py:method:: TransformationModelLowess.getParameters


Cython signature: Param getParameters()




.. py:method:: TransformationModelLowess.getValidXWeights


Cython signature: libcpp_vector[String] getValidXWeights()
Returns a list of valid x weight function stringss




.. py:method:: TransformationModelLowess.getValidYWeights


Cython signature: libcpp_vector[String] getValidYWeights()
Returns a list of valid y weight function strings




.. py:method:: TransformationModelLowess.unWeightData


Cython signature: void unWeightData(libcpp_vector[TM_DataPoint] & data)
Unweight the data by the given weight function




.. py:method:: TransformationModelLowess.unWeightDatum


Cython signature: double unWeightDatum(double & datum, const String & weight)
Apply the reverse of the weighting function to the data




.. py:method:: TransformationModelLowess.weightData


Cython signature: void weightData(libcpp_vector[TM_DataPoint] & data)
Weight the data by the given weight function




.. py:method:: TransformationModelLowess.weightDatum


Cython signature: double weightDatum(double & datum, const String & weight)
Weight the data according to the weighting function




