IsotopeModel
============

.. py:class:: IsotopeModel


   Bases: :py:class:`object`


Cython implementation of _IsotopeModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeModel.html


 Isotope distribution approximated using linear interpolation
 -----
 This models a smoothed (widened) distribution, i.e. can be used to sample actual raw peaks (depending on the points you query)
 If you only want the distribution (no widening), use either
 EmpiricalFormula::getIsotopeDistribution() // for a certain sum formula
 or
 IsotopeDistribution::estimateFromPeptideWeight (double average_weight)  // for averagine
 -----
 Peak widening is achieved by either a Gaussian or Lorentzian shape




.. py:attribute:: IsotopeModel.Averagines


alias of :py:class:`pyopenms.pyopenms_4.__Averagines`


.. py:method:: IsotopeModel.getCenter


Cython signature: double getCenter()


Get the center of the Isotope model
-----
This is a m/z-value not necessarily the monoisotopic mass




.. py:method:: IsotopeModel.getCharge


Cython signature: unsigned int getCharge()




.. py:method:: IsotopeModel.getFormula


Cython signature: EmpiricalFormula getFormula()
Return the Averagine peptide formula (mass calculated from mean mass and charge -- use .setParameters() to set them)




.. py:method:: IsotopeModel.getIsotopeDistribution


Cython signature: IsotopeDistribution getIsotopeDistribution()


Get the Isotope distribution (without widening) from the last setSamples() call
-----
Useful to determine the number of isotopes that the model contains and their position




.. py:method:: IsotopeModel.getOffset


Cython signature: double getOffset()
Get the offset of the model




.. py:method:: IsotopeModel.getProductName


Cython signature: String getProductName()
Name of the model (needed by Factory)




.. py:method:: IsotopeModel.setOffset


Cython signature: void setOffset(double offset)


Set the offset of the model
-----
The whole model will be shifted to the new offset without being computing all over
This leaves a discrepancy which is minor in small shifts (i.e. shifting by one or two
standard deviations) but can get significant otherwise. In that case use setParameters()
which enforces a recomputation of the model




.. py:method:: IsotopeModel.setSamples


Cython signature: void setSamples(EmpiricalFormula & formula)
Set sample/supporting points of interpolation




