ProteaseDigestion
=================

.. py:class:: ProteaseDigestion


   Bases: :py:class:`object`


Cython implementation of _ProteaseDigestion


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteaseDigestion.html
 -- Inherits from ['EnzymaticDigestion']


   Class for the enzymatic digestion of proteins
   -----
   Digestion can be performed using simple regular expressions, e.g. [KR] | [^P] for trypsin.
   Also missed cleavages can be modeled, i.e. adjacent peptides are not cleaved
   due to enzyme malfunction/access restrictions. If n missed cleavages are allowed, all possible resulting
   peptides (cleaved and uncleaved) with up to n missed cleavages are returned.
   Thus no random selection of just n specific missed cleavage sites is performed.
   -----
   Usage:
       from pyopenms import *
       from urllib.request import urlretrieve
       #
       urlretrieve ("http://www.uniprot.org/uniprot/P02769.fasta", "bsa.fasta")
       #
       dig = ProteaseDigestion()
       dig.setEnzyme('Lys-C')
       bsa_string = "".join([l.strip() for l in open("bsa.fasta").readlines()[1:]])
       bsa_oms_string = String(bsa_string) # convert python string to OpenMS::String for further processing
       #
       minlen = 6
       maxlen = 30
       #
       # Using AASequence and digest
       result_digest = []
       result_digest_min_max = []
       bsa_aaseq = AASequence.fromString(bsa_oms_string)
       dig.digest(bsa_aaseq, result_digest)
       dig.digest(bsa_aaseq, result_digest_min_max, minlen, maxlen)
       print(result_digest[4].toString()) # GLVLIAFSQYLQQCPFDEHVK
       print(len(result_digest)) # 57 peptides
       print(result_digest_min_max[4].toString()) # LVNELTEFAK
       print(len(result_digest_min_max)) # 42 peptides
       #
       # Using digestUnmodified without the need for AASequence from the EnzymaticDigestion base class
       result_digest_unmodified = []
       dig.digestUnmodified(StringView(bsa_oms_string), result_digest_unmodified, minlen, maxlen)
       print(result_digest_unmodified[4].getString()) # LVNELTEFAK
       print(len(result_digest_unmodified)) # 42 peptides




.. py:method:: ProteaseDigestion.digest


       - Cython signature: size_t digest(AASequence & protein, libcpp_vector[AASequence] & output)
       - Cython signature: size_t digest(AASequence & protein, libcpp_vector[AASequence] & output, size_t min_length, size_t max_length)


Performs the enzymatic digestion of a protein.
-----
:param protein: Sequence to digest
:param output: Digestion products (peptides)
:param min_length: Minimal length of reported products
:param max_length: Maximal length of reported products (0 = no restriction)
:returns: Number of discarded digestion products (which are not matching length restrictions)




.. py:method:: ProteaseDigestion.digestUnmodified


Cython signature: size_t digestUnmodified(StringView sequence, libcpp_vector[StringView] & output, size_t min_length, size_t max_length)


Performs the enzymatic digestion of an unmodified sequence
-----
By returning only references into the original string this is very fast
-----
:param sequence: Sequence to digest
:param output: Digestion products
:param min_length: Minimal length of reported products
:param max_length: Maximal length of reported products (0 = no restriction)
:returns: Number of discarded digestion products (which are not matching length restrictions)




.. py:method:: ProteaseDigestion.getEnzymeName


Cython signature: String getEnzymeName()
Returns the enzyme for the digestion




.. py:method:: ProteaseDigestion.getMissedCleavages


Cython signature: size_t getMissedCleavages()
Returns the number of missed cleavages for the digestion




.. py:method:: ProteaseDigestion.getSpecificity


Cython signature: Specificity getSpecificity()
Returns the specificity for the digestion




.. py:method:: ProteaseDigestion.getSpecificityByName


Cython signature: Specificity getSpecificityByName(String name)
Returns the specificity by name. Returns SPEC_UNKNOWN if name is not valid




.. py:method:: ProteaseDigestion.isValidProduct


         - Cython signature: bool isValidProduct(AASequence protein, size_t pep_pos, size_t pep_length, bool ignore_missed_cleavages, bool methionine_cleavage)


  Variant of EnzymaticDigestion::isValidProduct() with support for n-term protein cleavage and random D|P cleavage
  -----
  Checks if peptide is a valid digestion product of the enzyme, taking into account specificity and the flags provided here
  -----
  :param protein: Protein sequence
  :param pep_pos: Starting index of potential peptide
  :param pep_length: Length of potential peptide
  :param ignore_missed_cleavages: Do not compare MC's of potential peptide to the maximum allowed MC's
  :param allow_nterm_protein_cleavage: Regard peptide as n-terminal of protein if it starts only at pos=1 or 2 and protein starts with 'M'
  :param allow_random_asp_pro_cleavage: Allow cleavage at D|P sites to count as n/c-terminal
  :returns: True if peptide has correct n/c terminals (according to enzyme, specificity and above flags)
         - Cython signature: bool isValidProduct(String protein, size_t pep_pos, size_t pep_length, bool ignore_missed_cleavages, bool methionine_cleavage)
           Forwards to isValidProduct using protein.toUnmodifiedString()


         - Cython signature: bool isValidProduct(String sequence, int pos, int length, bool ignore_missed_cleavages)


Boolean operator returns true if the peptide fragment starting at position `pos` with length `length` within the sequence `sequence` generated by the current enzyme
-----
Checks if peptide is a valid digestion product of the enzyme, taking into account specificity and the MC flag provided here
-----
:param protein: Protein sequence
:param pep_pos: Starting index of potential peptide
:param pep_length: Length of potential peptide
:param ignore_missed_cleavages: Do not compare MC's of potential peptide to the maximum allowed MC's
:returns: True if peptide has correct n/c terminals (according to enzyme, specificity and missed cleavages)




.. py:method:: ProteaseDigestion.peptideCount


Cython signature: size_t peptideCount(AASequence & protein)
Returns the number of peptides a digestion of protein would yield under the current enzyme and missed cleavage settings




.. py:method:: ProteaseDigestion.setEnzyme


- Cython signature: void setEnzyme(String name)
  Sets the enzyme for the digestion (by name)


- Cython signature: void setEnzyme(DigestionEnzyme * enzyme)
  Sets the enzyme for the digestion




.. py:method:: ProteaseDigestion.setMissedCleavages


Cython signature: void setMissedCleavages(size_t missed_cleavages)
Sets the number of missed cleavages for the digestion (default is 0). This setting is ignored when log model is used




.. py:method:: ProteaseDigestion.setSpecificity


Cython signature: void setSpecificity(Specificity spec)
Sets the specificity for the digestion (default is SPEC_FULL)




