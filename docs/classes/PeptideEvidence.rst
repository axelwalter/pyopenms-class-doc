PeptideEvidence
===============

.. py:class:: PeptideEvidence


   Bases: :py:class:`object`


Cython implementation of _PeptideEvidence


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideEvidence.html




.. py:method:: PeptideEvidence.getAAAfter


Cython signature: char getAAAfter()
Returns the amino acid single letter code after the sequence (subsequent amino acid in the protein). If not available, UNKNOWN_AA is returned. If C-terminal, C_TERMINAL_AA is returned




.. py:method:: PeptideEvidence.getAABefore


Cython signature: char getAABefore()
Returns the amino acid single letter code before the sequence (preceding amino acid in the protein). If not available, UNKNOWN_AA is returned. If N-terminal, N_TERMINAL_AA is returned




.. py:method:: PeptideEvidence.getEnd


Cython signature: int getEnd()
Returns the position of the last AA of the peptide in protein coordinates (starting at 0 for the N-terminus). If not available UNKNOWN_POSITION constant is returned




.. py:method:: PeptideEvidence.getProteinAccession


Cython signature: String getProteinAccession()
Returns the protein accession the peptide matches to. If not available the empty string is returned




.. py:method:: PeptideEvidence.getStart


Cython signature: int getStart()
Returns the position in the protein (starting at 0 for the N-terminus). If not available UNKNOWN_POSITION constant is returned




.. py:method:: PeptideEvidence.hasValidLimits


Cython signature: bool hasValidLimits()
Start and end numbers in evidence represent actual numeric indices




.. py:method:: PeptideEvidence.setAAAfter


Cython signature: void setAAAfter(char rhs)
Sets the amino acid single letter code after the sequence (subsequent amino acid in the protein). If not available, set to UNKNOWN_AA. If C-terminal set to C_TERMINAL_AA




.. py:method:: PeptideEvidence.setAABefore


Cython signature: void setAABefore(char rhs)
Sets the amino acid single letter code before the sequence (preceding amino acid in the protein). If not available, set to UNKNOWN_AA. If N-terminal set to N_TERMINAL_AA




.. py:method:: PeptideEvidence.setEnd


Cython signature: void setEnd(int end)
Sets the position of the last AA of the peptide in protein coordinates (starting at 0 for the N-terminus). If not available, set UNKNOWN_POSITION. C-terminal positions must be marked with C_TERMINAL_AA




.. py:method:: PeptideEvidence.setProteinAccession


Cython signature: void setProteinAccession(String s)
Sets the protein accession the peptide matches to. If not available set to empty string




.. py:method:: PeptideEvidence.setStart


Cython signature: void setStart(int start)
Sets the position of the last AA of the peptide in protein coordinates (starting at 0 for the N-terminus). If not available, set to UNKNOWN_POSITION. N-terminal positions must be marked with `N_TERMINAL_AA`




