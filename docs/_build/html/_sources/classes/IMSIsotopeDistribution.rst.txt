IMSIsotopeDistribution
======================

.. py:class:: IMSIsotopeDistribution


   Bases: :py:class:`object`


Cython implementation of _IMSIsotopeDistribution


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ims::IMSIsotopeDistribution_1_1IMSIsotopeDistribution.html


 Represents a distribution of isotopes restricted to the first K elements
 -----
 Represents a distribution of isotopes of chemical elements as a list
 of peaks each as a pair of mass and abundance. 'IsotopeDistribution'
 unlike 'IsotopeSpecies' has one abundance per a nominal mass.
 Here is an example in the format (mass; abundance %)
 for molecule H2O (values are taken randomly):
 -----
 - IsotopeDistribution
     (18.00221; 99.03 %)
     (19.00334; 0.8 %)
     (20.00476; 0.17 %)
 -----
 - IsotopeSpecies
     (18.00197; 98.012 %)
     (18.00989; 1.018 %)
     (19.00312; 0.683 %)
     (19.00531; 0.117 %)
     (20.00413; 0.134 %)
     (20.00831; 0.036 %)
 -----
 To the sake of faster computations distribution is restricted
 to the first K elements, where K can be set by adjusting size
 'SIZE' of distribution. @note For the elements most abundant in
 living beings (CHNOPS) this restriction is negligible, since abundances
 decrease dramatically in isotopes order and are usually of no interest
 starting from +10 isotope.
 -----
 'IsotopeDistribution' implements folding with other distribution using an
 algorithm described in details in paper:
 Boecker et al. "Decomposing metabolic isotope patterns" WABI 2006. doi: 10.1007/11851561_2
 -----
 Folding with itself is done using Russian Multiplication Scheme




.. py:attribute:: IMSIsotopeDistribution.ABUNDANCES_SUM_ERROR




.. py:attribute:: IMSIsotopeDistribution.SIZE




.. py:method:: IMSIsotopeDistribution.empty


Cython signature: bool empty()
Returns true if the distribution has no peaks, false - otherwise




.. py:method:: IMSIsotopeDistribution.getAbundance


Cython signature: double getAbundance(int i)




.. py:method:: IMSIsotopeDistribution.getAbundances


Cython signature: libcpp_vector[double] getAbundances()
Gets an abundance of isotope 'i'




.. py:method:: IMSIsotopeDistribution.getAverageMass


Cython signature: double getAverageMass()




.. py:method:: IMSIsotopeDistribution.getMass


Cython signature: double getMass(int i)




.. py:method:: IMSIsotopeDistribution.getMasses


Cython signature: libcpp_vector[double] getMasses()
Gets a mass of isotope 'i'




.. py:method:: IMSIsotopeDistribution.getNominalMass


Cython signature: unsigned int getNominalMass()




.. py:method:: IMSIsotopeDistribution.normalize


Cython signature: void normalize()
Normalizes distribution, i.e. scaling abundances to be summed up to 1 with an error




.. py:method:: IMSIsotopeDistribution.setNominalMass


Cython signature: void setNominalMass(unsigned int nominalMass)




.. py:method:: IMSIsotopeDistribution.size


Cython signature: int size()




