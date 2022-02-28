SequestInfile
=============

.. py:class:: SequestInfile


   Bases: :py:class:`object`


Cython implementation of _SequestInfile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SequestInfile.html




.. py:method:: SequestInfile.addEnzymeInfo


Cython signature: void addEnzymeInfo(libcpp_vector[String] & enzyme_info)
Adds an enzyme to the list and sets is as used




.. py:method:: SequestInfile.getDatabase


Cython signature: String getDatabase()
Returns the used database




.. py:method:: SequestInfile.getEnzymeInfoAsString


Cython signature: String getEnzymeInfoAsString()
Returns the enzyme list as a string




.. py:method:: SequestInfile.getEnzymeName


Cython signature: String getEnzymeName()
Returns the enzyme used for cleavage




.. py:method:: SequestInfile.getEnzymeNumber


Cython signature: size_t getEnzymeNumber()
Returns the enzyme used for cleavage (by means of the number from a list of enzymes)




.. py:method:: SequestInfile.getIonCutoffPercentage


Cython signature: float getIonCutoffPercentage()
Returns the the cutoff of the ratio matching theoretical peaks/theoretical peaks




.. py:method:: SequestInfile.getIonSeriesWeights


Cython signature: String getIonSeriesWeights()
Returns the weights for the a-, b-, c-, d-, v-, w-, x-, y- and z-ion series




.. py:method:: SequestInfile.getMassTypeFragment


Cython signature: bool getMassTypeFragment()
Returns the mass type of the fragments (0 - monoisotopic, 1 - average mass)




.. py:method:: SequestInfile.getMassTypeParent


Cython signature: bool getMassTypeParent()
Returns the mass type of the parent (0 - monoisotopic, 1 - average mass)




.. py:method:: SequestInfile.getMatchPeakAllowedError


Cython signature: size_t getMatchPeakAllowedError()
Returns the number of top abundant peaks that are allowed not to match with a theoretical peak




.. py:method:: SequestInfile.getMatchPeakCount


Cython signature: size_t getMatchPeakCount()
Returns the number of top abundant peaks to match with theoretical ones




.. py:method:: SequestInfile.getMatchPeakTolerance


Cython signature: float getMatchPeakTolerance()
Returns the match peak tolerance




.. py:method:: SequestInfile.getMaxAAPerModPerPeptide


Cython signature: size_t getMaxAAPerModPerPeptide()
Returns the maximum number of amino acids containing the same modification in a peptide




.. py:method:: SequestInfile.getMaxInternalCleavageSites


Cython signature: size_t getMaxInternalCleavageSites()
Returns the maximum number of internal cleavage sites




.. py:method:: SequestInfile.getMaxModsPerPeptide


Cython signature: size_t getMaxModsPerPeptide()
Returns the maximum number of modifications that are allowed in a peptide




.. py:method:: SequestInfile.getModifications




.. py:method:: SequestInfile.getNeutralLossesForIons


Cython signature: String getNeutralLossesForIons()
Returns whether neutral losses are considered for the a-, b- and y-ions




.. py:method:: SequestInfile.getNormalizeXcorr


Cython signature: bool getNormalizeXcorr()
Returns whether normalized xcorr values are displayed




.. py:method:: SequestInfile.getNucleotideReadingFrame


Cython signature: size_t getNucleotideReadingFrame()
Returns the nucleotide reading frame




.. py:method:: SequestInfile.getOutputLines


Cython signature: size_t getOutputLines()
Returns the number of peptides to be displayed




.. py:method:: SequestInfile.getPartialSequence


Cython signature: String getPartialSequence()
Returns the partial sequences (space delimited) that have to occur in the theoretical spectra




.. py:method:: SequestInfile.getPeakMassTolerance


Cython signature: float getPeakMassTolerance()
Returns the peak mass tolerance




.. py:method:: SequestInfile.getPeptideMassUnit


Cython signature: size_t getPeptideMassUnit()
Returns the peptide mass unit




.. py:method:: SequestInfile.getPrecursorMassTolerance


Cython signature: float getPrecursorMassTolerance()
Returns the precursor mass tolerance




.. py:method:: SequestInfile.getPrintDuplicateReferences


Cython signature: bool getPrintDuplicateReferences()
Returns whether all proteins containing a found peptide should be displayed




.. py:method:: SequestInfile.getProteinMassFilter


Cython signature: String getProteinMassFilter()
Returns the protein mass filter (either min and max mass, or mass and tolerance value in percent)




.. py:method:: SequestInfile.getRemovePrecursorNearPeaks


Cython signature: bool getRemovePrecursorNearPeaks()
Returns whether peaks near (15 amu) the precursor peak are removed




.. py:method:: SequestInfile.getResiduesInUpperCase


Cython signature: bool getResiduesInUpperCase()
Returns whether residues are in upper case




.. py:method:: SequestInfile.getSequenceHeaderFilter


Cython signature: String getSequenceHeaderFilter()
Returns the sequences (space delimited) that have to occur, or be absent (preceded by a tilde) in the header of a protein to be considered




.. py:method:: SequestInfile.getShowFragmentIons


Cython signature: bool getShowFragmentIons()
Returns whether fragment ions shall be displayed




.. py:method:: SequestInfile.handlePTMs


Cython signature: void handlePTMs(const String & modification_line, const String & modifications_filename, bool monoisotopic)




.. py:method:: SequestInfile.setDatabase


Cython signature: void setDatabase(const String & database)
Sets the used database




.. py:method:: SequestInfile.setEnzyme


Cython signature: size_t setEnzyme(String enzyme_name)
Sets the enzyme used for cleavage (by means of the number from a list of enzymes)




.. py:method:: SequestInfile.setIonCutoffPercentage


Cython signature: void setIonCutoffPercentage(float ion_cutoff_percentage)
Sets the ion cutoff of the ratio matching theoretical peaks/theoretical peaks




.. py:method:: SequestInfile.setIonSeriesWeights


Cython signature: void setIonSeriesWeights(const String & ion_series_weights)
Sets the weights for the a-, b-, c-, d-, v-, w-, x-, y- and z-ion series




.. py:method:: SequestInfile.setMassTypeFragment


Cython signature: void setMassTypeFragment(bool mass_type_fragment)
Sets the mass type of the fragments (0 - monoisotopic, 1 - average mass)




.. py:method:: SequestInfile.setMassTypeParent


Cython signature: void setMassTypeParent(bool mass_type_parent)
Sets the mass type of the parent (0 - monoisotopic, 1 - average mass)




.. py:method:: SequestInfile.setMatchPeakAllowedError


Cython signature: void setMatchPeakAllowedError(size_t match_peak_allowed_error)
Sets the number of top abundant peaks that are allowed not to match with a theoretical peak




.. py:method:: SequestInfile.setMatchPeakCount


Cython signature: void setMatchPeakCount(size_t match_peak_count)
Sets the number of top abundant peaks to with theoretical ones




.. py:method:: SequestInfile.setMatchPeakTolerance


Cython signature: void setMatchPeakTolerance(float match_peak_tolerance)
Sets the match peak tolerance




.. py:method:: SequestInfile.setMaxAAPerModPerPeptide


Cython signature: void setMaxAAPerModPerPeptide(size_t max_aa_per_mod_per_peptide)
Sets the maximum number of amino acids containing the same modification in a peptide




.. py:method:: SequestInfile.setMaxInternalCleavageSites


Cython signature: void setMaxInternalCleavageSites(size_t max_internal_cleavage_sites)
Sets the maximum number of internal cleavage sites




.. py:method:: SequestInfile.setMaxModsPerPeptide


Cython signature: void setMaxModsPerPeptide(size_t max_mods_per_peptide)
Sets the maximum number of modifications that are allowed in a peptide




.. py:method:: SequestInfile.setNeutralLossesForIons


Cython signature: void setNeutralLossesForIons(const String & neutral_losses_for_ions)
Sets whether neutral losses are considered for the a-, b- and y-ions




.. py:method:: SequestInfile.setNormalizeXcorr


Cython signature: void setNormalizeXcorr(bool normalize_xcorr)
Sets whether normalized xcorr values are displayed




.. py:method:: SequestInfile.setNucleotideReadingFrame


Cython signature: void setNucleotideReadingFrame(size_t nucleotide_reading_frame)
Sets the nucleotide reading frame




.. py:method:: SequestInfile.setOutputLines


Cython signature: void setOutputLines(size_t output_lines)
Sets the number of peptides to be displayed




.. py:method:: SequestInfile.setPartialSequence


Cython signature: void setPartialSequence(const String & partial_sequence)
Sets the partial sequences (space delimited) that have to occur in the theoretical spectra




.. py:method:: SequestInfile.setPeakMassTolerance


Cython signature: void setPeakMassTolerance(float peak_mass_tolerance)
Sets the peak mass tolerance




.. py:method:: SequestInfile.setPeptideMassUnit


Cython signature: void setPeptideMassUnit(size_t peptide_mass_unit)
Sets the peptide mass unit




.. py:method:: SequestInfile.setPrecursorMassTolerance


Cython signature: void setPrecursorMassTolerance(float precursor_mass_tolerance)
Sets the precursor mass tolerance




.. py:method:: SequestInfile.setPrintDuplicateReferences


Cython signature: void setPrintDuplicateReferences(bool print_duplicate_references)
Sets whether all proteins containing a found peptide should be displayed




.. py:method:: SequestInfile.setProteinMassFilter


Cython signature: void setProteinMassFilter(const String & protein_mass_filter)
Sets the protein mass filter (either min and max mass, or mass and tolerance value in percent)




.. py:method:: SequestInfile.setRemovePrecursorNearPeaks


Cython signature: void setRemovePrecursorNearPeaks(bool remove_precursor_near_peaks)
Sets whether peaks near (15 amu) the precursor peak are removed




.. py:method:: SequestInfile.setResiduesInUpperCase


Cython signature: void setResiduesInUpperCase(bool residues_in_upper_case)
Sets whether residues are in upper case




.. py:method:: SequestInfile.setSequenceHeaderFilter


Cython signature: void setSequenceHeaderFilter(const String & sequence_header_filter)
Sets the sequences (space delimited) that have to occur, or be absent (preceded by a tilde) in the header of a protein to be considered




.. py:method:: SequestInfile.setShowFragmentIons


Cython signature: void setShowFragmentIons(bool show_fragments)
Sets whether fragment ions shall be displayed




.. py:method:: SequestInfile.store


Cython signature: void store(const String & filename)


Stores the experiment data in a Sequest input file that can be used as input for Sequest shell execution
-----
:param filename: the name of the file in which the infile is stored into




