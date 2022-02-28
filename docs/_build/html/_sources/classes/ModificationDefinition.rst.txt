ModificationDefinition
======================

.. py:class:: ModificationDefinition


   Bases: :py:class:`object`


Cython implementation of _ModificationDefinition


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ModificationDefinition.html




.. py:method:: ModificationDefinition.getMaxOccurrences


Cython signature: unsigned int getMaxOccurrences()
Returns the maximal number of occurrences per peptide




.. py:method:: ModificationDefinition.getModification


Cython signature: ResidueModification getModification()




.. py:method:: ModificationDefinition.getModificationName


Cython signature: String getModificationName()
Returns the name of the modification




.. py:method:: ModificationDefinition.isFixedModification


Cython signature: bool isFixedModification()
Returns if the modification if fixed true, else false




.. py:method:: ModificationDefinition.setFixedModification


Cython signature: void setFixedModification(bool fixed)
Sets whether this modification definition is fixed or variable (modification must occur vs. can occur)




.. py:method:: ModificationDefinition.setMaxOccurrences


Cython signature: void setMaxOccurrences(unsigned int num)
Sets the maximal number of occurrences per peptide (unbounded if 0)




.. py:method:: ModificationDefinition.setModification


Cython signature: void setModification(const String & modification)
Sets the modification, allowed are unique names provided by ModificationsDB




