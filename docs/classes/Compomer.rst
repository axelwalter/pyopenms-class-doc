Compomer
========

.. py:class:: Compomer


   Bases: :py:class:`object`


Cython implementation of _Compomer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Compomer.html




.. py:method:: Compomer.add


Cython signature: void add(Adduct & a, unsigned int side)




.. py:method:: Compomer.getAdductsAsString


- Cython signature: String getAdductsAsString()
  Get adducts with their abundance as compact string for both sides


- Cython signature: String getAdductsAsString(unsigned int side)
  Get adducts with their abundance as compact string (amounts are absolute unless side=BOTH)




.. py:method:: Compomer.getID


Cython signature: size_t getID()
Returns Id which allows unique identification of this compomer




.. py:method:: Compomer.getLabels


Cython signature: StringList getLabels(unsigned int side)
Returns the adduct labels from parameter(side) given. (LEFT or RIGHT)




.. py:method:: Compomer.getLogP


Cython signature: double getLogP()
Returns the log probability




.. py:method:: Compomer.getMass


Cython signature: double getMass()
Mass of all contained adducts




.. py:method:: Compomer.getNegativeCharges


Cython signature: int getNegativeCharges()
Summed negative charges of contained adducts




.. py:method:: Compomer.getNetCharge


Cython signature: int getNetCharge()
Net charge of compomer (i.e. difference between left and right side of compomer)




.. py:method:: Compomer.getPositiveCharges


Cython signature: int getPositiveCharges()
Summed positive charges of contained adducts




.. py:method:: Compomer.getRTShift


Cython signature: double getRTShift()
Returns the log probability




.. py:method:: Compomer.isConflicting


Cython signature: bool isConflicting(Compomer & cmp, unsigned int side_this, unsigned int side_other)




.. py:method:: Compomer.isSingleAdduct


Cython signature: bool isSingleAdduct(Adduct & a, unsigned int side)
Check if Compomer only contains a single adduct on side @p side




.. py:method:: Compomer.removeAdduct


- Cython signature: Compomer removeAdduct(Adduct & a)
  Remove ALL instances of the given adduct


- Cython signature: Compomer removeAdduct(Adduct & a, unsigned int side)




.. py:method:: Compomer.setID


Cython signature: void setID(size_t id)
Sets an Id which allows unique identification of a compomer




