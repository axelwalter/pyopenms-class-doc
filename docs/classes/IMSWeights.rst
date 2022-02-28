IMSWeights
==========

.. py:class:: IMSWeights


   Bases: :py:class:`object`


Cython implementation of _IMSWeights


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ims::Weights_1_1IMSWeights.html




.. py:method:: IMSWeights.back


Cython signature: unsigned long int back()
Gets a last weight




.. py:method:: IMSWeights.divideByGCD


Cython signature: bool divideByGCD()
Divides the integer weights by their gcd. The precision is also adjusted




.. py:method:: IMSWeights.getAlphabetMass


Cython signature: double getAlphabetMass(int i)
Gets an original (double) alphabet mass by index




.. py:method:: IMSWeights.getMaxRoundingError


Cython signature: double getMaxRoundingError()




.. py:method:: IMSWeights.getMinRoundingError


Cython signature: double getMinRoundingError()




.. py:method:: IMSWeights.getParentMass


Cython signature: double getParentMass(libcpp_vector[unsigned int] & decomposition)
Returns a parent mass for a given `decomposition`




.. py:method:: IMSWeights.getPrecision


Cython signature: double getPrecision()
Gets precision.




.. py:method:: IMSWeights.getWeight


Cython signature: unsigned long int getWeight(int i)
Gets a scaled integer weight by index




.. py:method:: IMSWeights.setPrecision


Cython signature: void setPrecision(double precision)
Sets a new precision to scale double values to integer




.. py:method:: IMSWeights.size


Cython signature: int size()
Gets size of a set of weights




.. py:method:: IMSWeights.swap


Cython signature: void swap(int index1, int index2)
Exchanges weight and mass at index1 with weight and mass at index2




