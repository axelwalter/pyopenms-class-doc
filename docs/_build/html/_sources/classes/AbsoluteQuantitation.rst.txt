AbsoluteQuantitation
====================

.. py:class:: AbsoluteQuantitation


   Bases: :py:class:`object`


Cython implementation of _AbsoluteQuantitation


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1AbsoluteQuantitation.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: AbsoluteQuantitation.applyCalibration


Cython signature: double applyCalibration(const Feature & component, const Feature & IS_component, const String & feature_name, const String & transformation_model, const Param & transformation_model_params)




.. py:method:: AbsoluteQuantitation.calculateBias


Cython signature: double calculateBias(double actual_concentration, double calculated_concentration)
This function calculates the bias of the calibration




.. py:method:: AbsoluteQuantitation.calculateBiasAndR


Cython signature: void calculateBiasAndR(libcpp_vector[AQS_featureConcentration] & component_concentrations, const String & feature_name, const String & transformation_model, Param & transformation_model_params, libcpp_vector[double] & biases, double & correlation_coefficient)




.. py:method:: AbsoluteQuantitation.calculateRatio


Cython signature: double calculateRatio(Feature & component_1, Feature & component_2, const String & feature_name)




.. py:method:: AbsoluteQuantitation.fitCalibration


Cython signature: Param fitCalibration(libcpp_vector[AQS_featureConcentration] & component_concentrations, const String & feature_name, const String & transformation_model, Param transformation_model_params)




.. py:method:: AbsoluteQuantitation.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: AbsoluteQuantitation.getName


Cython signature: String getName()
Returns the name




.. py:method:: AbsoluteQuantitation.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: AbsoluteQuantitation.getQuantMethods


Cython signature: libcpp_vector[AbsoluteQuantitationMethod] getQuantMethods()




.. py:method:: AbsoluteQuantitation.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: AbsoluteQuantitation.optimizeCalibrationCurveIterative


Cython signature: bool optimizeCalibrationCurveIterative(libcpp_vector[AQS_featureConcentration] & component_concentrations, const String & feature_name, const String & transformation_model, const Param & transformation_model_params, Param & optimized_params)




.. py:method:: AbsoluteQuantitation.optimizeSingleCalibrationCurve


Cython signature: void optimizeSingleCalibrationCurve(const String & component_name, libcpp_vector[AQS_featureConcentration] & component_concentrations)




.. py:method:: AbsoluteQuantitation.quantifyComponents


Cython signature: void quantifyComponents(FeatureMap & unknowns)
This function applies the calibration curve, hence quantifying all the components




.. py:method:: AbsoluteQuantitation.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: AbsoluteQuantitation.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: AbsoluteQuantitation.setQuantMethods


Cython signature: void setQuantMethods(libcpp_vector[AbsoluteQuantitationMethod] & quant_methods)




