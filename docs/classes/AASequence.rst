AASequence
==========

.. py:class:: AASequence


   Bases: :py:class:`object`


Cython implementation of _AASequence


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1AASequence.html


 Representation of a peptide/protein sequence
 This class represents amino acid sequences in OpenMS. An AASequence
 instance primarily contains a sequence of residues.




.. py:method:: AASequence.empty


Cython signature: bool empty()
Check if sequence is empty




.. py:method:: AASequence.fromString


Cython signature: AASequence fromString(String s)




.. py:method:: AASequence.fromStringPermissive


Cython signature: AASequence fromStringPermissive(String s, bool permissive)




.. py:method:: AASequence.getAAFrequencies




.. py:method:: AASequence.getAverageWeight


- Cython signature: double getAverageWeight()
  Returns the average weight of the peptide


- Cython signature: double getAverageWeight(ResidueType type_, int charge)




.. py:method:: AASequence.getCTerminalModification


Cython signature: const ResidueModification * getCTerminalModification()
Returns a copy of the name C-terminal modification object, or None




.. py:method:: AASequence.getCTerminalModificationName


Cython signature: String getCTerminalModificationName()
Returns the name (ID) of the C-terminal modification, or an empty string if none is set




.. py:method:: AASequence.getFormula


- Cython signature: EmpiricalFormula getFormula()
  Convenience function with ResidueType=Full and charge = 0 by default


- Cython signature: EmpiricalFormula getFormula(ResidueType type_, int charge)




.. py:method:: AASequence.getMZ


- Cython signature: double getMZ(int charge)
  Returns the mass-to-charge ratio of the peptide


- Cython signature: double getMZ(int charge, ResidueType type_)




.. py:method:: AASequence.getMonoWeight


- Cython signature: double getMonoWeight()
  Returns the mono isotopic weight of the peptide


- Cython signature: double getMonoWeight(ResidueType type_, int charge)




.. py:method:: AASequence.getNTerminalModification


Cython signature: const ResidueModification * getNTerminalModification()
Returns a copy of the name N-terminal modification object, or None




.. py:method:: AASequence.getNTerminalModificationName


Cython signature: String getNTerminalModificationName()
Returns the name (ID) of the N-terminal modification, or an empty string if none is set




.. py:method:: AASequence.getPrefix


Cython signature: AASequence getPrefix(size_t index)
Returns a peptide sequence of the first index residues




.. py:method:: AASequence.getResidue


Cython signature: Residue getResidue(size_t index)
Returns the residue at position index




.. py:method:: AASequence.getSubsequence


Cython signature: AASequence getSubsequence(size_t index, unsigned int number)
Returns a peptide sequence of number residues, beginning at position index




.. py:method:: AASequence.getSuffix


Cython signature: AASequence getSuffix(size_t index)
Returns a peptide sequence of the last index residues




.. py:method:: AASequence.has


Cython signature: bool has(Residue residue)
Returns true if the peptide contains the given residue




.. py:method:: AASequence.hasCTerminalModification


Cython signature: bool hasCTerminalModification()
Predicate which is true if the peptide is C-term modified




.. py:method:: AASequence.hasNTerminalModification


Cython signature: bool hasNTerminalModification()
Predicate which is true if the peptide is N-term modified




.. py:method:: AASequence.hasPrefix


Cython signature: bool hasPrefix(AASequence peptide)
Returns true if the peptide has the given prefix




.. py:method:: AASequence.hasSubsequence


Cython signature: bool hasSubsequence(AASequence peptide)
Returns true if the peptide contains the given peptide




.. py:method:: AASequence.hasSuffix


Cython signature: bool hasSuffix(AASequence peptide)
Returns true if the peptide has the given suffix




.. py:method:: AASequence.isModified


Cython signature: bool isModified()
Returns true if any of the residues or termini are modified




.. py:method:: AASequence.setCTerminalModification


- Cython signature: void setCTerminalModification(String modification)
  Sets the C-terminal modification (by lookup in the mod names of the ModificationsDB). Throws if nothing is found (since the name is not enough information to create a new mod)


- Cython signature: void setCTerminalModification(const ResidueModification & mod)
  Sets the C-terminal modification (copies and adds to database if not present)




.. py:method:: AASequence.setCTerminalModificationByDiffMonoMass


Cython signature: void setCTerminalModificationByDiffMonoMass(double diffMonoMass, bool protein_term)
Sets the C-terminal modification by the monoisotopic mass difference it introduces (creates a "user-defined" mod if not present)




.. py:method:: AASequence.setModification


- Cython signature: void setModification(size_t index, const String & modification)
  Sets the modification of the residue at position index. If an empty string is passed replaces the residue with its unmodified version


- Cython signature: void setModification(size_t index, const ResidueModification & modification)
  Sets the modification of AA at index by providing a ResidueModification object. Stricter than just looking for the name and adds the Modification to the DB if not present




.. py:method:: AASequence.setModificationByDiffMonoMass


Cython signature: void setModificationByDiffMonoMass(size_t index, double diffMonoMass)
Modifies the residue at index in the sequence and potentially in the ResidueDB




.. py:method:: AASequence.setNTerminalModification


- Cython signature: void setNTerminalModification(String modification)
  Sets the N-terminal modification (by lookup in the mod names of the ModificationsDB). Throws if nothing is found (since the name is not enough information to create a new mod)


- Cython signature: void setNTerminalModification(const ResidueModification & mod)
  Sets the N-terminal modification (copies and adds to database if not present)




.. py:method:: AASequence.setNTerminalModificationByDiffMonoMass


Cython signature: void setNTerminalModificationByDiffMonoMass(double diffMonoMass, bool protein_term)
Sets the N-terminal modification by the monoisotopic mass difference it introduces (creates a "user-defined" mod if not present)




.. py:method:: AASequence.size


Cython signature: size_t size()
Returns the number of residues




.. py:method:: AASequence.toBracketString


- Cython signature: String toBracketString()
  Create a TPP compatible string of the modified sequence using bracket notation. Uses integer mass by default


- Cython signature: String toBracketString(bool integer_mass)
  Create a TPP compatible string of the modified sequence using bracket notation


- Cython signature: String toBracketString(bool integer_mass, bool mass_delta)
  Create a TPP compatible string of the modified sequence using bracket notation.


- Cython signature: String toBracketString(bool integer_mass, bool mass_delta, libcpp_vector[String] fixed_modifications)
  Create a TPP compatible string of the modified sequence using bracket notation




.. py:method:: AASequence.toString


Cython signature: String toString()
Returns the peptide as string with modifications embedded in brackets




.. py:method:: AASequence.toUniModString


Cython signature: String toUniModString()
Returns the peptide as string with UniMod-style modifications embedded in brackets




.. py:method:: AASequence.toUnmodifiedString


Cython signature: String toUnmodifiedString()
Returns the peptide as string without any modifications




