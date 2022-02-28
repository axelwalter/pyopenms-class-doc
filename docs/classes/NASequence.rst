NASequence
==========

.. py:class:: NASequence


   Bases: :py:class:`object`


Cython implementation of _NASequence


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1NASequence.html


 Representation of an RNA sequence
 This class represents nucleic acid sequences in OpenMS. An NASequence
 instance primarily contains a sequence of ribonucleotides.




.. py:attribute:: NASequence.NASFragmentType


alias of :py:class:`pyopenms.pyopenms_4.__NASFragmentType`


.. py:method:: NASequence.empty


Cython signature: bool empty()
Check if sequence is empty




.. py:method:: NASequence.fromString


Cython signature: NASequence fromString(const String & s)




.. py:method:: NASequence.get


Cython signature: const Ribonucleotide * get(size_t index)
Returns the residue at position index




.. py:method:: NASequence.getAverageWeight


- Cython signature: double getAverageWeight()
  Returns the average weight of the peptide


- Cython signature: double getAverageWeight(NASFragmentType type_, int charge)




.. py:method:: NASequence.getFivePrimeMod


Cython signature: const Ribonucleotide * getFivePrimeMod()
Returns the name (ID) of the N-terminal modification, or an empty string if none is set




.. py:method:: NASequence.getFormula


- Cython signature: EmpiricalFormula getFormula()
  Returns the formula of the peptide


- Cython signature: EmpiricalFormula getFormula(NASFragmentType type_, int charge)




.. py:method:: NASequence.getMonoWeight


- Cython signature: double getMonoWeight()
  Returns the mono isotopic weight of the peptide


- Cython signature: double getMonoWeight(NASFragmentType type_, int charge)




.. py:method:: NASequence.getPrefix


Cython signature: NASequence getPrefix(size_t length)
Returns a peptide sequence of the first index residues




.. py:method:: NASequence.getSequence


Cython signature: libcpp_vector[const Ribonucleotide *] getSequence()




.. py:method:: NASequence.getSubsequence


Cython signature: NASequence getSubsequence(size_t start, size_t length)
Returns a peptide sequence of number residues, beginning at position index




.. py:method:: NASequence.getSuffix


Cython signature: NASequence getSuffix(size_t length)
Returns a peptide sequence of the last index residues




.. py:method:: NASequence.getThreePrimeMod


Cython signature: const Ribonucleotide * getThreePrimeMod()




.. py:method:: NASequence.set


Cython signature: void set(size_t index, const Ribonucleotide * r)
Sets the residue at position index




.. py:method:: NASequence.setFivePrimeMod


Cython signature: void setFivePrimeMod(const Ribonucleotide * modification)
Sets the 5' modification




.. py:method:: NASequence.setSequence


Cython signature: void setSequence(const libcpp_vector[const Ribonucleotide *] & seq)




.. py:method:: NASequence.setThreePrimeMod


Cython signature: void setThreePrimeMod(const Ribonucleotide * modification)
Sets the 3' modification




.. py:method:: NASequence.size


Cython signature: size_t size()
Returns the number of residues




.. py:method:: NASequence.toString


Cython signature: String toString()
Returns the peptide as string with modifications embedded in brackets




