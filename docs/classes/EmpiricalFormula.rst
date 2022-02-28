EmpiricalFormula
================

.. py:class:: EmpiricalFormula


   Bases: :py:class:`object`


Cython implementation of _EmpiricalFormula


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1EmpiricalFormula.html




.. py:method:: EmpiricalFormula.calculateTheoreticalIsotopesNumber


Cython signature: double calculateTheoreticalIsotopesNumber()




.. py:method:: EmpiricalFormula.contains


Cython signature: bool contains(EmpiricalFormula ef)
Returns true if all elements from `ef` ( empirical formula ) are LESS abundant (negative allowed) than the corresponding elements of this EmpiricalFormula




.. py:method:: EmpiricalFormula.estimateFromWeightAndComp


Cython signature: bool estimateFromWeightAndComp(double average_weight, double C, double H, double N, double O, double S, double P)
Fills this EmpiricalFormula with an approximate elemental composition for a given average weight and approximate elemental stoichiometry




.. py:method:: EmpiricalFormula.estimateFromWeightAndCompAndS


Cython signature: bool estimateFromWeightAndCompAndS(double average_weight, unsigned int S, double C, double H, double N, double O, double P)
Fills this EmpiricalFormula with an approximate elemental composition for a given average weight, exact number of sulfurs, and approximate elemental stoichiometry




.. py:method:: EmpiricalFormula.getAverageWeight


Cython signature: double getAverageWeight()
Returns the average weight of the formula (includes proton charges)




.. py:method:: EmpiricalFormula.getCharge


Cython signature: ptrdiff_t getCharge()
Returns the total charge




.. py:method:: EmpiricalFormula.getConditionalFragmentIsotopeDist


Cython signature: IsotopeDistribution getConditionalFragmentIsotopeDist(EmpiricalFormula & precursor, libcpp_set[unsigned int] & precursor_isotopes, CoarseIsotopePatternGenerator method)




.. py:method:: EmpiricalFormula.getElementalComposition


Cython signature: libcpp_map[libcpp_string,int] getElementalComposition()
Get elemental composition as a hash {'Symbol' -> NrAtoms}




.. py:method:: EmpiricalFormula.getIsotopeDistribution


- Cython signature: IsotopeDistribution getIsotopeDistribution(CoarseIsotopePatternGenerator)
  Computes the isotope distribution of an empirical formula using the CoarseIsotopePatternGenerator or the FineIsotopePatternGenerator method


- Cython signature: IsotopeDistribution getIsotopeDistribution(FineIsotopePatternGenerator)




.. py:method:: EmpiricalFormula.getMonoWeight


Cython signature: double getMonoWeight()
Returns the mono isotopic weight of the formula (includes proton charges)




.. py:method:: EmpiricalFormula.getNumberOfAtoms


Cython signature: size_t getNumberOfAtoms()
Returns the total number of atoms




.. py:method:: EmpiricalFormula.hasElement


Cython signature: bool hasElement(Element * element)
Returns true if the formula contains the element




.. py:method:: EmpiricalFormula.isCharged


Cython signature: bool isCharged()
Returns true if charge is not equal to zero




.. py:method:: EmpiricalFormula.isEmpty


Cython signature: bool isEmpty()
Returns true if the formula does not contain a element




.. py:method:: EmpiricalFormula.setCharge


Cython signature: void setCharge(ptrdiff_t charge)
Sets the charge




.. py:method:: EmpiricalFormula.toString


Cython signature: String toString()
Returns the formula as a string (charges are not included)




