ResidueDB
=========

.. py:class:: ResidueDB


   Bases: :py:class:`object`


Cython implementation of _ResidueDB


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ResidueDB.html




.. py:method:: ResidueDB.getModifiedResidue


- Cython signature: const Residue * getModifiedResidue(const String & name)
  Returns a pointer to a modified residue given a modification name


- Cython signature: const Residue * getModifiedResidue(Residue * residue, const String & name)
  Returns a pointer to a modified residue given a residue and a modification name




.. py:method:: ResidueDB.getNumberOfModifiedResidues


Cython signature: size_t getNumberOfModifiedResidues()
Returns the number of modified residues stored




.. py:method:: ResidueDB.getNumberOfResidues


Cython signature: size_t getNumberOfResidues()
Returns the number of residues stored




.. py:method:: ResidueDB.getResidue


Cython signature: const Residue * getResidue(const String & name)
Returns a pointer to the residue with name, 3 letter code or 1 letter code name




.. py:method:: ResidueDB.getResidueSets


Cython signature: libcpp_set[String] getResidueSets()
Returns all residue sets that are registered which this instance




.. py:method:: ResidueDB.getResidues


Cython signature: libcpp_set[const Residue *] getResidues(const String & residue_set)
Returns a set of all residues stored in this residue db




.. py:method:: ResidueDB.hasResidue


Cython signature: bool hasResidue(const String & name)
Returns true if the db contains a residue with the given name




