IsotopeDistribution
===================

.. py:class:: IsotopeDistribution


   Bases: :py:class:`object`


Cython implementation of _IsotopeDistribution


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeDistribution.html


 Isotope distribution class
 -----
 A container that holds an isotope distribution. It consists of mass values
 and their correspondent probabilities (stored in the intensity slot)
 -----
 Isotope distributions can be calculated using either the
 CoarseIsotopePatternGenerator for quantized atomic masses which group
 isotopes with the same atomic number. Alternatively, the
 FineIsotopePatternGenerator can be used that calculates hyperfine isotopic
 distributions
  -----
 This class only describes the container that holds the isotopic
 distribution, calculations are done using classes derived from
 IsotopePatternGenerator




.. py:attribute:: IsotopeDistribution.Sorted


alias of :py:class:`pyopenms.pyopenms_3.__Sorted`


.. py:method:: IsotopeDistribution.averageMass


Cython signature: double averageMass()
Compute average mass of isotope distribution (weighted average of all isotopes)




.. py:method:: IsotopeDistribution.clear


Cython signature: void clear()
Clears the distribution and resets max isotope to 0




.. py:method:: IsotopeDistribution.getContainer


Cython signature: libcpp_vector[Peak1D] & getContainer()
Returns the container which holds the distribution




.. py:method:: IsotopeDistribution.getMax


Cython signature: size_t getMax()
Returns the maximal weight isotope which is stored in the distribution




.. py:method:: IsotopeDistribution.getMin


Cython signature: size_t getMin()
Returns the minimal weight isotope which is stored in the distribution




.. py:method:: IsotopeDistribution.getMostAbundant


Cython signature: Peak1D getMostAbundant()
Returns the most abundant isotope which is stored in the distribution




.. py:method:: IsotopeDistribution.insert


Cython signature: void insert(double mass, float intensity)




.. py:method:: IsotopeDistribution.merge


Cython signature: void merge(double, double)
Merges distributions of arbitrary data points with constant defined resolution




.. py:method:: IsotopeDistribution.renormalize


Cython signature: void renormalize()
Renormalizes the sum of the probabilities of the isotopes to 1




.. py:method:: IsotopeDistribution.resize


Cython signature: void resize(unsigned int size)
Resizes distribution container




.. py:method:: IsotopeDistribution.set


Cython signature: void set(libcpp_vector[Peak1D] & distribution)
Overwrites the container which holds the distribution using 'distribution'




.. py:method:: IsotopeDistribution.size


Cython signature: size_t size()
Returns the size of the distribution which is the number of isotopes in the distribution




.. py:method:: IsotopeDistribution.sortByIntensity


Cython signature: void sortByIntensity()
Sort isotope distribution by intensity




.. py:method:: IsotopeDistribution.sortByMass


Cython signature: void sortByMass()
Sort isotope distribution by mass




.. py:method:: IsotopeDistribution.trimIntensities


Cython signature: void trimIntensities(double cutoff)
Remove intensities below the cutoff




.. py:method:: IsotopeDistribution.trimLeft


Cython signature: void trimLeft(double cutoff)
Trims the left side of the isotope distribution to isotopes with a significant contribution




.. py:method:: IsotopeDistribution.trimRight


Cython signature: void trimRight(double cutoff)
Trims the right side of the isotope distribution to isotopes with a significant contribution




