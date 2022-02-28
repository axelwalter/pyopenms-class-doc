TransformationDescription
=========================

.. py:class:: TransformationDescription


   Bases: :py:class:`object`


Cython implementation of _TransformationDescription


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::TransformationDescription_1_1TransformationDescription.html




.. py:method:: TransformationDescription.apply


Cython signature: double apply(double)
Applies the transformation to `value`




.. py:method:: TransformationDescription.fitModel


- Cython signature: void fitModel(String model_type, Param params)
  Fits a model to the data


- Cython signature: void fitModel(String model_type)
  Fits a model to the data




.. py:method:: TransformationDescription.getDataPoints


Cython signature: libcpp_vector[TM_DataPoint] getDataPoints()
Returns the data points




.. py:method:: TransformationDescription.getDeviations


Cython signature: void getDeviations(libcpp_vector[double] & diffs, bool do_apply, bool do_sort)


Get the deviations between the data pairs
-----
:param diffs: Output
:param do_apply: Get deviations after applying the model?
:param do_sort: Sort `diffs` before returning?




.. py:method:: TransformationDescription.getModelParameters


Cython signature: Param getModelParameters()
Returns the model parameters




.. py:method:: TransformationDescription.getModelType


Cython signature: String getModelType()
Gets the type of the fitted model




.. py:method:: TransformationDescription.getModelTypes


Cython signature: void getModelTypes(StringList result)




.. py:method:: TransformationDescription.getStatistics


Cython signature: TransformationStatistics getStatistics()




.. py:method:: TransformationDescription.invert


Cython signature: void invert()
Computes an (approximate) inverse of the transformation




.. py:method:: TransformationDescription.setDataPoints


- Cython signature: void setDataPoints(libcpp_vector[TM_DataPoint] & data)
  Sets the data points. Removes the model that was previously fitted to the data (if any)


- Cython signature: void setDataPoints(libcpp_vector[libcpp_pair[double,double]] & data)
  Sets the data points (backwards-compatible overload). Removes the model that was previously fitted to the data (if any)




