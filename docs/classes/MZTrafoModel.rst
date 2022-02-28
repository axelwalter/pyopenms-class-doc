MZTrafoModel
============

.. py:class:: MZTrafoModel


   Bases: :py:class:`object`


Cython implementation of _MZTrafoModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MZTrafoModel.html


 Create and apply models of a mass recalibration function
 -----
 The input is a list of calibration points (ideally spanning a wide m/z range to prevent extrapolation when applying to model)
 -----
 Models (LINEAR, LINEAR_WEIGHTED, QUADRATIC, QUADRATIC_WEIGHTED) can be trained using CalData points (or a subset of them)
 Calibration points can have different retention time points, and a model should be build such that it captures
 the local (in time) decalibration of the instrument, i.e. choose appropriate time windows along RT to calibrate the
 spectra in this RT region
 From the available calibrant data, a model is build. Later, any uncalibrated m/z value can be fed to the model, to obtain
 a calibrated m/z
 -----
 The input domain can either be absolute mass differences in [Th], or relative differences in [ppm]
 The models are build based on this input
 -----
 Outlier detection before model building via the RANSAC algorithm is supported for LINEAR and QUADRATIC models




.. py:method:: MZTrafoModel.enumToName


Cython signature: libcpp_string enumToName(MZTrafoModel_MODELTYPE mt)




.. py:method:: MZTrafoModel.findNearest


Cython signature: size_t findNearest(libcpp_vector[MZTrafoModel] & tms, double rt)




.. py:method:: MZTrafoModel.getCoefficients


Cython signature: void getCoefficients(double & intercept, double & slope, double & power)


Get model coefficients
-----
Parameters will be filled with internal model parameters
The model must be trained before; Exception is thrown otherwise!
-----
:param intercept: The intercept
:param slope: The slope
:param power: The coefficient for x*x (will be 0 for linear models)




.. py:method:: MZTrafoModel.getRT


Cython signature: double getRT()
Get RT associated with the model (training region)




.. py:method:: MZTrafoModel.isTrained


Cython signature: bool isTrained()
Returns true if the model have coefficients (i.e. was trained successfully)




.. py:method:: MZTrafoModel.isValidModel


Cython signature: bool isValidModel(MZTrafoModel & trafo)




.. py:method:: MZTrafoModel.nameToEnum


Cython signature: MZTrafoModel_MODELTYPE nameToEnum(libcpp_string name)




.. py:method:: MZTrafoModel.predict


Cython signature: double predict(double mz)


Apply the model to an uncalibrated m/z value
-----
Make sure the model was trained (train()) and is valid (isValidModel()) before calling this function!
-----
Applies the function y = intercept + slope*mz + power*mz^2
and returns y
-----
:param mz: The uncalibrated m/z value
:returns The calibrated m/z value




.. py:method:: MZTrafoModel.setCoefficientLimits


Cython signature: void setCoefficientLimits(double offset, double scale, double power)




.. py:method:: MZTrafoModel.setCoefficients


         - Cython signature: void setCoefficients(MZTrafoModel)
           Copy model coefficients from another model


         - Cython signature: void setCoefficients(double, double, double)


Manually set model coefficients
-----
Can be used instead of train(), so manually set coefficients
It must be exactly three values. If you want a linear model, set 'power' to zero
If you want a constant model, set slope to zero in addition
-----
:param intercept: The offset
:param slope: The slope
:param power: The x*x coefficient (for quadratic models)




.. py:method:: MZTrafoModel.setRANSACParams


Cython signature: void setRANSACParams(RANSACParam p)




.. py:method:: MZTrafoModel.toString


Cython signature: String toString()




.. py:method:: MZTrafoModel.train


         - Cython signature: bool train(CalibrationData cd, MZTrafoModel_MODELTYPE md, bool use_RANSAC, double rt_left, double rt_right)


Train a model using calibrant data
-----
If the CalibrationData was created using peak groups (usually corresponding to mass traces),
the median for each group is used as a group representative. This
is more robust, and reduces the number of data points drastically, i.e. one value per group
-----
Internally, these steps take place:
- apply RT filter
- [compute median per group] (only if groups were given in 'cd')
- set Model's rt position
- call train() (see overloaded method)
-----
:param cd: List of calibrants
:param md: Type of model (linear, quadratic, ...)
:param use_RANSAC: Remove outliers before computing the model?
:param rt_left: Filter 'cd' by RT; all calibrants with RT < 'rt_left' are removed
:param rt_right: Filter 'cd' by RT; all calibrants with RT > 'rt_right' are removed
:returns: True if model was build, false otherwise
         - Cython signature: bool train(libcpp_vector[double] error_mz, libcpp_vector[double] theo_mz, libcpp_vector[double] weights, MZTrafoModel_MODELTYPE md, bool use_RANSAC)


Train a model using calibrant data
-----
Given theoretical and observed mass values (and corresponding weights),
a model (linear, quadratic, ...) is build
Outlier removal is applied before
The 'obs_mz' can be either given as absolute masses in [Th] or relative deviations in [ppm]
The MZTrafoModel must be constructed accordingly (see constructor). This has no influence on the model building itself, but
rather on how 'predict()' works internally
-----
Outlier detection before model building via the RANSAC algorithm is supported for LINEAR and QUADRATIC models
-----
Internally, these steps take place:
- [apply RANSAC] (depending on 'use_RANSAC')
- build model and store its parameters internally
-----
:param error_mz: Observed Mass error (in ppm or Th)
:param theo_mz: Theoretical m/z values, corresponding to 'error_mz'
:param weights: For weighted models only: weight of calibrants; ignored otherwise
:param md: Type of model (linear, quadratic, ...)
:param use_RANSAC: Remove outliers before computing the model?
:returns: True if model was build, false otherwise




