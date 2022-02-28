ChargePair
==========

.. py:class:: ChargePair


   Bases: :py:class:`object`


Cython implementation of _ChargePair


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ChargePair.html




.. py:method:: ChargePair.getCharge


Cython signature: int getCharge(unsigned int pairID)
Returns the charge (for element 0 or 1)




.. py:method:: ChargePair.getCompomer


Cython signature: Compomer getCompomer()
Returns the Id of the compomer that explains the mass difference




.. py:method:: ChargePair.getEdgeScore


Cython signature: double getEdgeScore()
Returns the ILP edge score




.. py:method:: ChargePair.getElementIndex


Cython signature: size_t getElementIndex(unsigned int pairID)
Returns the element index (for element 0 or 1)




.. py:method:: ChargePair.getMassDiff


Cython signature: double getMassDiff()
Returns the mass difference




.. py:method:: ChargePair.isActive


Cython signature: bool isActive()
Is this pair realized?




.. py:method:: ChargePair.setActive


Cython signature: void setActive(bool active)




.. py:method:: ChargePair.setCharge


Cython signature: void setCharge(unsigned int pairID, int e)
Sets the charge (for element 0 or 1)




.. py:method:: ChargePair.setCompomer


Cython signature: void setCompomer(Compomer & compomer)
Sets the compomer id




.. py:method:: ChargePair.setEdgeScore


Cython signature: void setEdgeScore(double score)
Sets the ILP edge score




.. py:method:: ChargePair.setElementIndex


Cython signature: void setElementIndex(unsigned int pairID, size_t e)
Sets the element index (for element 0 or 1)




.. py:method:: ChargePair.setMassDiff


Cython signature: void setMassDiff(double mass_diff)
Sets the mass difference




