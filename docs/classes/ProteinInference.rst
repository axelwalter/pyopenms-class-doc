ProteinInference
================

.. py:class:: ProteinInference


   Bases: :py:class:`object`


Cython implementation of _ProteinInference


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteinInference.html


 [experimental class] given a peptide quantitation, infer corresponding protein quantities
 -----
 Infers protein ratios from peptide ratios (currently using unique peptides only).
 Use the IDMapper class to add protein and peptide information to a
 quantitative ConsensusMap prior to this step




.. py:method:: ProteinInference.infer


Cython signature: void infer(ConsensusMap & consensus_map, unsigned int reference_map)


Given a peptide quantitation, infer corresponding protein quantities
-----
Infers protein ratios from peptide ratios (currently using unique peptides only).
Use the IDMapper class to add protein and peptide information to a
quantitative ConsensusMap prior to this step
-----
:param consensus_map: Peptide quantitation with ProteinIdentifications attached, where
     Protein quantitation will be attached
:param reference_map: Index of (iTRAQ) reference channel within the consensus map




