IDFilter
========

.. py:class:: IDFilter


   Bases: :py:class:`object`


Cython implementation of _IDFilter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IDFilter.html


 Finds the best-scoring hit in a vector of peptide or protein identifications
 -----
 This class provides functions for filtering collections of peptide or protein identifications according to various criteria.
 It also contains helper functions and classes (functors that implement predicates) that are used in this context.
 -----
 The filter functions modify their inputs, rather than creating filtered copies.
 -----
 Most filters work on the hit level, i.e. they remove peptide or protein hits from peptide or protein identifications (IDs).
 A few filters work on the ID level instead, i.e. they remove peptide or protein IDs from vectors thereof.
 Independent of this, the inputs for all filter functions are vectors of IDs, because the data most often comes in this form.
 This design also allows many helper objects to be set up only once per vector, rather than once per ID.
 -----
 The filter functions for vectors of peptide/protein IDs do not include clean-up steps (e.g. removal of IDs without hits, reassignment of hit ranks, ...).
 They only carry out their specific filtering operations.
 This is so filters can be chained without having to repeat clean-up operations.
 The group of clean-up functions provides helpers that are useful to ensure data integrity after filters have been applied, but it is up to the individual developer to use them when necessary.
 -----
 The filter functions for MS/MS experiments do include clean-up steps, because they filter peptide and protein IDs in conjunction and potential contradictions between the two must be eliminated.




.. py:attribute:: IDFilter.DigestionFilter


alias of :py:class:`pyopenms.pyopenms_1.__DigestionFilter`


.. py:method:: IDFilter.countHits


- Cython signature: size_t countHits(libcpp_vector[PeptideIdentification] identifications)
  Returns the total number of peptide hits in a vector of peptide identifications


- Cython signature: size_t countHits(libcpp_vector[ProteinIdentification] identifications)
  Returns the total number of protein hits in a vector of protein identifications




.. py:method:: IDFilter.extractPeptideSequences


Cython signature: void extractPeptideSequences(libcpp_vector[PeptideIdentification] & peptides, libcpp_set[String] & sequences, bool ignore_mods)


Extracts all unique peptide sequences from a list of peptide IDs
-----
:param peptides
:param ignore_mods: Boolean operator default to false in case of any modifications in sequences during extraction
:returns: Sequences




.. py:method:: IDFilter.filterHitsByRank


         - Cython signature: void filterHitsByRank(libcpp_vector[PeptideIdentification] & ids, size_t min_rank, size_t max_rank)


Filters peptide or protein identifications according to the ranking of the hits
-----
The hits between 'min_rank' and 'max_rank' (both inclusive) in each ID are kept
Counting starts at 1, i.e. the best (highest/lowest scoring) hit has rank 1
The ranks are (re-)computed before filtering
'max_rank' is ignored if it is smaller than 'min_rank'
-----
Note: that there may be several hits with the same rank in a peptide or protein ID (if the scores are the same)
This method is useful if a range of higher hits is needed for decoy fairness analysis
         - Cython signature: void filterHitsByRank(libcpp_vector[ProteinIdentification] & ids, size_t min_rank, size_t max_rank)


Filters peptide or protein identifications according to the ranking of the hits
-----
The hits between 'min_rank' and 'max_rank' (both inclusive) in each ID are kept
Counting starts at 1, i.e. the best (highest/lowest scoring) hit has rank 1
The ranks are (re-)computed before filtering
'max_rank' is ignored if it is smaller than 'min_rank'
-----
Note: that there may be several hits with the same rank in a peptide or protein ID (if the scores are the same)
This method is useful if a range of higher hits is needed for decoy fairness analysis




.. py:method:: IDFilter.filterHitsByScore


- Cython signature: void filterHitsByScore(libcpp_vector[PeptideIdentification] & ids, double threshold_score)
  Filters peptide or protein identifications according to the score of the hits. The score orientation has to be set to higherscorebetter in each PeptideIdentification. Only peptide/protein hits with a score at least as good as 'threshold_score' are kept


- Cython signature: void filterHitsByScore(libcpp_vector[ProteinIdentification] & ids, double threshold_score)
  Filters peptide or protein identifications according to the score of the hits. The score orientation has to be set to higherscorebetter in each PeptideIdentification/ProteinIdentifiation. Only peptide/protein hits with a score at least as good as 'threshold_score' are kept


- Cython signature: void filterHitsByScore(MSExperiment & experiment, double peptide_threshold_score, double protein_threshold_score)
  Filters an MS/MS experiment according to score thresholds




.. py:method:: IDFilter.filterPeptidesByCharge


Cython signature: void filterPeptidesByCharge(libcpp_vector[PeptideIdentification] & peptides, size_t min_charge, size_t max_charge)
Filters peptide identifications according to charge state




.. py:method:: IDFilter.filterPeptidesByLength


Cython signature: void filterPeptidesByLength(libcpp_vector[PeptideIdentification] & peptides, size_t min_length, size_t max_length)
Filters peptide identifications according to peptide sequence length




.. py:method:: IDFilter.filterPeptidesByMZ


Cython signature: void filterPeptidesByMZ(libcpp_vector[PeptideIdentification] & peptides, size_t min_mz, size_t max_mz)
Filters peptide identifications by precursor m/z, keeping only IDs in the given range




.. py:method:: IDFilter.filterPeptidesByMZError


Cython signature: void filterPeptidesByMZError(libcpp_vector[PeptideIdentification] & peptides, double mass_error, bool unit_ppm)
Filter peptide identifications according to mass deviation




.. py:method:: IDFilter.filterPeptidesByRT


Cython signature: void filterPeptidesByRT(libcpp_vector[PeptideIdentification] & peptides, size_t min_rt, size_t max_rt)
Filters peptide identifications by precursor RT, keeping only IDs in the given range




.. py:method:: IDFilter.filterPeptidesByRTPredictPValue


Cython signature: void filterPeptidesByRTPredictPValue(libcpp_vector[PeptideIdentification] & peptides, const String & metavalue_key, double threshold)


Filters peptide identifications according to p-values from RTPredict
-----
Filters the peptide hits by the probability (p-value) of a correct peptide identification having a deviation between observed and predicted RT equal to or greater than allowed
-----
:param peptides: Input/output
:param metavalue_key: Name of the meta value that holds the p-value: "predicted_RT_p_value" or "predicted_RT_p_value_first_dim"
:param threshold: P-value threshold




.. py:method:: IDFilter.getBestHit


         - Cython signature: bool getBestHit(libcpp_vector[PeptideIdentification] identifications, bool assume_sorted, PeptideHit & best_hit)


Finds the best-scoring hit in a vector of peptide or protein identifications
-----
If there are several hits with the best score, the first one is taken
-----
:param identifications: Vector of peptide or protein IDs, each containing one or more (peptide/protein) hits
:param assume_sorted: Are hits sorted by score (best score first) already? This allows for faster query, since only the first hit needs to be looked at
:param best_hit: Contains the best hit if successful in a vector of peptide identifications
:returns: true if a hit was present, false otherwise
Finds the best-scoring hit in a vector of peptide or protein identifications
-----
If there are several hits with the best score, the first one is taken
-----
:param identifications: Vector of peptide or protein IDs, each containing one or more (peptide/protein) hits
:param assume_sorted: Are hits sorted by score (best score first) already? This allows for faster query, since only the first hit needs to be looked at
:param best_hit: Contains the best hit if successful in a vector of protein identifications
:returns: true if a hit was present, false otherwise
         - Cython signature: bool getBestHit(libcpp_vector[ProteinIdentification] identifications, bool assume_sorted, ProteinHit & best_hit)


Finds the best-scoring hit in a vector of peptide or protein identifications
-----
If there are several hits with the best score, the first one is taken
-----
:param identifications: Vector of peptide or protein IDs, each containing one or more (peptide/protein) hits
:param assume_sorted: Are hits sorted by score (best score first) already? This allows for faster query, since only the first hit needs to be looked at
:param best_hit: Contains the best hit if successful in a vector of protein identifications
:returns: true if a hit was present, false otherwise




.. py:method:: IDFilter.keepBestPeptideHits


Cython signature: void keepBestPeptideHits(libcpp_vector[PeptideIdentification] & peptides, bool strict)


Filters peptide identifications keeping only the single best-scoring hit per ID
-----
:param peptides: Input/output
:param strict: If set, keep the best hit only if its score is unique - i.e. ties are not allowed. (Otherwise all hits with the best score is kept.)




.. py:method:: IDFilter.keepBestPerPeptide


Cython signature: void keepBestPerPeptide(libcpp_vector[PeptideIdentification] & peptides, bool ignore_mods, bool ignore_charges, size_t nr_best_spectrum)
Filters PeptideHits from PeptideIdentification by keeping only the best peptide hits for every peptide sequence




.. py:method:: IDFilter.keepBestPerPeptidePerRun


Cython signature: void keepBestPerPeptidePerRun(libcpp_vector[ProteinIdentification] & prot_ids, libcpp_vector[PeptideIdentification] & peptides, bool ignore_mods, bool ignore_charges, size_t nr_best_spectrum)
Filters PeptideHits from PeptideIdentification by keeping only the best peptide hits for every peptide sequence on a per run basis




.. py:method:: IDFilter.keepHitsMatchingProteins


- Cython signature: void keepHitsMatchingProteins(libcpp_vector[PeptideIdentification] & ids, libcpp_set[String] accessions)
  Filters peptide or protein identifications according to the given proteins (positive)


- Cython signature: void keepHitsMatchingProteins(libcpp_vector[ProteinIdentification] & ids, libcpp_set[String] accessions)
  Filters peptide or protein identifications according to the given proteins (positive)


- Cython signature: void keepHitsMatchingProteins(MSExperiment & experiment, libcpp_vector[FASTAEntry] & proteins)




.. py:method:: IDFilter.keepNBestHits


- Cython signature: void keepNBestHits(libcpp_vector[PeptideIdentification] & ids, size_t n)
- Cython signature: void keepNBestHits(libcpp_vector[ProteinIdentification] & ids, size_t n)
- Cython signature: void keepNBestHits(MSExperiment & experiment, size_t n)
  Filters an MS/MS experiment by keeping the N best peptide hits for every spectrum




.. py:method:: IDFilter.keepNBestSpectra


Cython signature: void keepNBestSpectra(libcpp_vector[PeptideIdentification] & peptides, size_t n)
Filter identifications by "N best" PeptideIdentification objects (better PeptideIdentification means better [best] PeptideHit than other)




.. py:method:: IDFilter.keepPeptidesWithMatchingModifications


Cython signature: void keepPeptidesWithMatchingModifications(libcpp_vector[PeptideIdentification] & peptides, libcpp_set[String] & modifications)
Keeps only peptide hits that have at least one of the given modifications




.. py:method:: IDFilter.keepPeptidesWithMatchingSequences


Cython signature: void keepPeptidesWithMatchingSequences(libcpp_vector[PeptideIdentification] & peptides, libcpp_vector[PeptideIdentification] & bad_peptides, bool ignore_mods)
Removes all peptide hits with a sequence that does not match one in 'good_peptides'




.. py:method:: IDFilter.keepUniquePeptidesPerProtein


Cython signature: void keepUniquePeptidesPerProtein(libcpp_vector[PeptideIdentification] & peptides)
Removes all peptides that are not annotated as unique for a protein (by PeptideIndexer)




.. py:method:: IDFilter.removeDecoyHits


- Cython signature: void removeDecoyHits(libcpp_vector[PeptideIdentification] & ids)
  Removes hits annotated as decoys from peptide or protein identifications. Checks for meta values named "target_decoy" and "isDecoy", and removes protein/peptide hits if the values are "decoy" and "true", respectively


- Cython signature: void removeDecoyHits(libcpp_vector[ProteinIdentification] & ids)
  Removes hits annotated as decoys from peptide or protein identifications. Checks for meta values named "target_decoy" and "isDecoy", and removes protein/peptide hits if the values are "decoy" and "true", respectively




.. py:method:: IDFilter.removeDuplicatePeptideHits


Cython signature: void removeDuplicatePeptideHits(libcpp_vector[PeptideIdentification] & peptides)
Removes duplicate peptide hits from each peptide identification, keeping only unique hits (per ID)




.. py:method:: IDFilter.removeEmptyIdentifications


- Cython signature: void removeEmptyIdentifications(libcpp_vector[PeptideIdentification] & ids)
  Removes peptide or protein identifications that have no hits in them


- Cython signature: void removeEmptyIdentifications(libcpp_vector[ProteinIdentification] & ids)
  Removes peptide or protein identifications that have no hits in them




.. py:method:: IDFilter.removeHitsMatchingProteins


- Cython signature: void removeHitsMatchingProteins(libcpp_vector[PeptideIdentification] & ids, libcpp_set[String] accessions)
  Filters peptide or protein identifications according to the given proteins (negative)


- Cython signature: void removeHitsMatchingProteins(libcpp_vector[ProteinIdentification] & ids, libcpp_set[String] accessions)
  Filters peptide or protein identifications according to the given proteins (negative)




.. py:method:: IDFilter.removePeptidesWithMatchingModifications


Cython signature: void removePeptidesWithMatchingModifications(libcpp_vector[PeptideIdentification] & peptides, libcpp_set[String] & modifications)
Removes all peptide hits that have at least one of the given modifications




.. py:method:: IDFilter.removePeptidesWithMatchingSequences


Cython signature: void removePeptidesWithMatchingSequences(libcpp_vector[PeptideIdentification] & peptides, libcpp_vector[PeptideIdentification] & bad_peptides, bool ignore_mods)
Removes all peptide hits with a sequence that matches one in 'bad_peptides'




.. py:method:: IDFilter.removeUnreferencedProteins


Cython signature: void removeUnreferencedProteins(libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides)
Removes protein hits from the protein IDs in a 'cmap' that are not referenced by a peptide in the features or if requested in the unassigned peptide list




.. py:method:: IDFilter.updateHitRanks


- Cython signature: void updateHitRanks(libcpp_vector[PeptideIdentification] & identifications)
  Updates the hit ranks on all peptide or protein IDs


- Cython signature: void updateHitRanks(libcpp_vector[ProteinIdentification] & identifications)
  Updates the hit ranks on all peptide or protein IDs




.. py:method:: IDFilter.updateProteinGroups


Cython signature: bool updateProteinGroups(libcpp_vector[ProteinGroup] & groups, libcpp_vector[ProteinHit] & hits)


Update protein groups after protein hits were filtered
-----
:param groups: Input/output protein groups
:param hits: Available protein hits (all others are removed from the groups)
:return: Returns whether the groups are still valid (which is the case if only whole groups, if any, were removed)




.. py:method:: IDFilter.updateProteinReferences


Cython signature: void updateProteinReferences(libcpp_vector[PeptideIdentification] & peptides, libcpp_vector[ProteinIdentification] & proteins, bool remove_peptides_without_reference)
Removes references to missing proteins. Only PeptideEvidence entries that reference protein hits in 'proteins' are kept in the peptide hits




