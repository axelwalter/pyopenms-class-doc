SimpleSVM
=========

.. py:class:: SimpleSVM


   Bases: :py:class:`object`


Cython implementation of _SimpleSVM


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SimpleSVM.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: SimpleSVM.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SimpleSVM.getFeatureWeights


Cython signature: void getFeatureWeights(libcpp_map[String,double] & feature_weights)


Returns the weights used for features (predictors) in the SVM model
-----
Currently only supported for two-class classification
If a linear kernel is used, the weights are informative for ranking features




.. py:method:: SimpleSVM.getName


Cython signature: String getName()
Returns the name




.. py:method:: SimpleSVM.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SimpleSVM.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SimpleSVM.predict


Cython signature: void predict(libcpp_vector[SVMPrediction] & predictions, libcpp_vector[size_t] indexes)


Predict class labels (and probabilities)
-----
:param predictions: Output vector of prediction results (same order as ``)
:param indexes: Vector of observation indexes for which predictions are desired. If empty (default), predictions are made for all observations




.. py:method:: SimpleSVM.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SimpleSVM.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: SimpleSVM.writeXvalResults


Cython signature: void writeXvalResults(const String & path)




