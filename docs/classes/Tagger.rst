Tagger
======

.. py:class:: Tagger


   Bases: :py:class:`object`


Cython implementation of _Tagger


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Tagger.html


 Constructor for Tagger
 -----
 The parameter `max_charge_` should be >= `min_charge_`
 Also `max_tag_length` should be >= `min_tag_length`
 -----
 :param min_tag_length: The minimal sequence tag length
 :param ppm: The tolerance for matching residue masses to peak delta masses
 :param max_tag_length: The maximal sequence tag length
 :param min_charge: Minimal fragment charge considered for each sequence tag
 :param max_charge: Maximal fragment charge considered for each sequence tag
 :param fixed_mods: A list of modification names. The modified residues replace the unmodified versions
 :param var_mods: A list of modification names. The modified residues are added as additional entries to the list of residues




.. py:method:: Tagger.getTag


         - Cython signature: void getTag(const libcpp_vector[double] & mzs, libcpp_vector[libcpp_utf8_string] & tags)


Generate tags from mass vector `mzs`
-----
The parameter `tags` is filled with one string per sequence tag
It uses the standard residues from ResidueDB including
the fixed and variable modifications given to the constructor
-----
:param mzs: A vector of mz values, containing the mz values from a centroided fragment spectrum
:param tags: The vector of tags, that is filled with this function
         - Cython signature: void getTag(const MSSpectrum & spec, libcpp_vector[libcpp_utf8_string] & tags)


Generate tags from an MSSpectrum
-----
The parameter `tags` is filled with one string per sequence tag
It uses the standard residues from ResidueDB including
the fixed and variable modifications given to the constructor
-----
:param spec: A centroided fragment spectrum
:param tags: The vector of tags, that is filled with this function




.. py:method:: Tagger.setMaxCharge


Cython signature: void setMaxCharge(size_t max_charge)


Change the maximal charge considered by the tagger
-----
Allows to change the maximal considered charge e.g. based on a spectra
precursor charge without calling the constructor multiple times
-----
:param max_charge: The new maximal charge




