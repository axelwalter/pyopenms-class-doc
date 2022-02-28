OptimizePeakDeconvolution
=========================

.. py:class:: OptimizePeakDeconvolution


   Bases: :py:class:`object`


Cython implementation of _OptimizePeakDeconvolution


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OptimizePeakDeconvolution.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: OptimizePeakDeconvolution.getCharge


Cython signature: int getCharge()
Returns the charge




.. py:method:: OptimizePeakDeconvolution.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: OptimizePeakDeconvolution.getName


Cython signature: String getName()
Returns the name




.. py:method:: OptimizePeakDeconvolution.getNumberOfPeaks_


Cython signature: size_t getNumberOfPeaks_(int charge, libcpp_vector[PeakShape] & temp_shapes, OptimizePeakDeconvolution_Data & data)




.. py:method:: OptimizePeakDeconvolution.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: OptimizePeakDeconvolution.getPenalties


Cython signature: PenaltyFactorsIntensity getPenalties()
Returns the penalty parameter




.. py:method:: OptimizePeakDeconvolution.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: OptimizePeakDeconvolution.optimize


Cython signature: bool optimize(libcpp_vector[PeakShape] & peaks, OptimizePeakDeconvolution_Data & data)
Performs a nonlinear optimization of the peaks that belong to the current isotope pattern




.. py:method:: OptimizePeakDeconvolution.setCharge


Cython signature: void setCharge(int charge)
Sets the charge




.. py:method:: OptimizePeakDeconvolution.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: OptimizePeakDeconvolution.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: OptimizePeakDeconvolution.setPenalties


Cython signature: void setPenalties(PenaltyFactorsIntensity & penalties)
Sets the penalty parameter




