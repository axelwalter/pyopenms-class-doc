EnzymaticDigestionLogModel
==========================

.. py:class:: EnzymaticDigestionLogModel


   Bases: :py:class:`object`


Cython implementation of _EnzymaticDigestionLogModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1EnzymaticDigestionLogModel.html




.. py:method:: EnzymaticDigestionLogModel.digest


Cython signature: void digest(AASequence & protein, libcpp_vector[AASequence] & output)
Performs the enzymatic digestion of a protein




.. py:method:: EnzymaticDigestionLogModel.getEnzymeName


Cython signature: String getEnzymeName()
Returns the enzyme for the digestion




.. py:method:: EnzymaticDigestionLogModel.getLogThreshold


Cython signature: double getLogThreshold()
Returns the threshold which needs to be exceeded to call a cleavage (only for the trained cleavage model on real data)




.. py:method:: EnzymaticDigestionLogModel.peptideCount


Cython signature: size_t peptideCount(AASequence & protein)


Returns the number of peptides a digestion of `protein` would yield under the current enzyme and missed cleavage settings
-----
:param protein: Name of protein




.. py:method:: EnzymaticDigestionLogModel.setEnzyme


Cython signature: void setEnzyme(String name)
Sets the enzyme for the digestion




.. py:method:: EnzymaticDigestionLogModel.setLogThreshold


Cython signature: void setLogThreshold(double threshold)
Sets the threshold which needs to be exceeded to call a cleavage (only for the trained cleavage model on real data). Default is 0.25




