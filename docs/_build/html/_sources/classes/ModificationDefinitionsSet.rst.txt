ModificationDefinitionsSet
==========================

.. py:class:: ModificationDefinitionsSet


   Bases: :py:class:`object`


Cython implementation of _ModificationDefinitionsSet


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ModificationDefinitionsSet.html




.. py:method:: ModificationDefinitionsSet.addModification


Cython signature: void addModification(ModificationDefinition & mod_def)
Adds a modification definition to the set




.. py:method:: ModificationDefinitionsSet.getFixedModificationNames


Cython signature: libcpp_set[String] getFixedModificationNames()
Returns only the names of the fixed modifications




.. py:method:: ModificationDefinitionsSet.getFixedModifications


Cython signature: libcpp_set[ModificationDefinition] getFixedModifications()
Returns the stored fixed modification definitions




.. py:method:: ModificationDefinitionsSet.getMaxModifications


Cython signature: size_t getMaxModifications()
Return the maximal number of modifications allowed per peptide




.. py:method:: ModificationDefinitionsSet.getModificationNames


- Cython signature: void getModificationNames(StringList & fixed_modifications, StringList & variable_modifications)
  Populates the output lists with the modification names (use e.g. for
- Cython signature: libcpp_set[String] getModificationNames()
  Returns only the names of the modifications stored in the set




.. py:method:: ModificationDefinitionsSet.getModifications


Cython signature: libcpp_set[ModificationDefinition] getModifications()
Returns the stored modification definitions




.. py:method:: ModificationDefinitionsSet.getNumberOfFixedModifications


Cython signature: size_t getNumberOfFixedModifications()
Returns the number of fixed modifications stored in this set




.. py:method:: ModificationDefinitionsSet.getNumberOfModifications


Cython signature: size_t getNumberOfModifications()
Returns the number of modifications stored in this set




.. py:method:: ModificationDefinitionsSet.getNumberOfVariableModifications


Cython signature: size_t getNumberOfVariableModifications()
Returns the number of variable modifications stored in this set




.. py:method:: ModificationDefinitionsSet.getVariableModificationNames


Cython signature: libcpp_set[String] getVariableModificationNames()
Returns only the names of the variable modifications




.. py:method:: ModificationDefinitionsSet.getVariableModifications


Cython signature: libcpp_set[ModificationDefinition] getVariableModifications()
Returns the stored variable modification definitions




.. py:method:: ModificationDefinitionsSet.inferFromPeptides


Cython signature: void inferFromPeptides(libcpp_vector[PeptideIdentification] & peptides)
Infers the sets of defined modifications from the modifications present on peptide identifications




.. py:method:: ModificationDefinitionsSet.isCompatible


Cython signature: bool isCompatible(AASequence & peptide)
Returns true if the peptide is compatible with the definitions, e.g. does not contain other modifications




.. py:method:: ModificationDefinitionsSet.setMaxModifications


Cython signature: void setMaxModifications(size_t max_mod)
Sets the maximal number of modifications allowed per peptide




.. py:method:: ModificationDefinitionsSet.setModifications


         - Cython signature: void setModifications(libcpp_set[ModificationDefinition] & mod_defs)
           Sets the modification definitions


         - Cython signature: void setModifications(const String & fixed_modifications, String & variable_modifications)


Set the modification definitions from a string
-----
The strings should contain a comma separated list of modifications. The names
can be PSI-MOD identifier or any other unique name supported by PSI-MOD. TermSpec
definitions and other specific definitions are given by the modifications themselves.
         - Cython signature: void setModifications(StringList & fixed_modifications, StringList & variable_modifications)
           Same as above, but using StringList instead of comma separated strings




