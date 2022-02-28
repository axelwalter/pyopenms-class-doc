BayesianProteinInferenceAlgorithm
=================================

.. py:class:: BayesianProteinInferenceAlgorithm


   Bases: :py:class:`object`


Cython implementation of _BayesianProteinInferenceAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1BayesianProteinInferenceAlgorithm.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']


 Performs a Bayesian protein inference on Protein/Peptide identifications or ConsensusMap.
 -----
 - Filters for best n PSMs per spectrum.
 - Calculates and filters for best peptide per spectrum.
 - Builds a k-partite graph from the structures.
 - Finds and splits into connected components by DFS
 - Extends the graph by adding layers from indist. protein groups, peptides with the same parents and optionally
   some additional layers (peptide sequence, charge, replicate -> extended model = experimental)
 - Builds a factor graph representation of a Bayesian network using the Evergreen library
   See model param section. It is based on the Fido noisy-OR model with an option for
   regularizing the number of proteins per peptide.
 - Performs loopy belief propagation on the graph and queries protein, protein group and/or peptide posteriors
   See loopy_belief_propagation param section.
 - Learns best parameters via grid search if the parameters were not given in the param section.
 - Writes posteriors to peptides and/or proteins and adds indistinguishable protein groups to the underlying
   data structures.
 - Can make use of OpenMP to parallelize over connected components.
 -----
 Usage:
   from pyopenms import *
   from urllib.request import urlretrieve
   urlretrieve("https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/tests/class_tests/openms/data/BayesianProteinInference_test.idXML", "BayesianProteinInference_test.idXML")
   proteins = []
   peptides = []
   idf = IdXMLFile()
   idf.load("BayesianProteinInference_test.idXML", proteins, peptides)
   bpia = BayesianProteinInferenceAlgorithm()
   p = bpia.getParameters()
   p.setValue("update_PSM_probabilities", "false")
   bpia.setParameters(p)
   bpia.inferPosteriorProbabilities(proteins, peptides)
   #
   print(len(peptides)) # 9
   print(peptides[0].getHits()[0].getScore()) # 0.6
   print(proteins[0].getHits()[0].getScore()) # 0.624641
   print(proteins[0].getHits()[1].getScore()) # 0.648346
 -----




.. py:method:: BayesianProteinInferenceAlgorithm.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: BayesianProteinInferenceAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: BayesianProteinInferenceAlgorithm.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: BayesianProteinInferenceAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: BayesianProteinInferenceAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: BayesianProteinInferenceAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: BayesianProteinInferenceAlgorithm.inferPosteriorProbabilities


         - Cython signature: void inferPosteriorProbabilities(libcpp_vector[ProteinIdentification] & proteinIDs, libcpp_vector[PeptideIdentification] & peptideIDs, bool greedy_group_resolution)


Performs inference
-----
Optionally adds indistinguishable protein groups with separate scores, too
Currently only takes first proteinID run and all peptides
-----
:param proteinIDs: Vector of protein identifications
:param peptideIDs: Vector of peptide identifications
:return: Writes its results into protein and (optionally also) peptide hits (as new score)
         - Cython signature: void inferPosteriorProbabilities(libcpp_vector[ProteinIdentification] & proteinIDs, libcpp_vector[PeptideIdentification] & peptideIDs, bool greedy_group_resolution, ExperimentalDesign exp_des)


Performs inference
-----
Writes its results into protein and (optionally also) peptide hits (as new score).
Optionally adds indistinguishable protein groups with separate scores, too
Currently only takes first proteinID run and all peptides
Experimental design can be used to create an extended graph with replicate information. (experimental)
-----
:param proteinIDs: Vector of protein identifications
:param peptideIDs: Vector of peptide identifications
:param exp_des: Experimental Design
:return: Writes its results into protein and (optionally also) peptide hits (as new score)
         - Cython signature: void inferPosteriorProbabilities(ConsensusMap & cmap, bool greedy_group_resolution)


Performs inference
-----
Writes its results into protein and (optionally also) peptide hits (as new score)
Optionally adds indistinguishable protein groups with separate scores, too
Loops over all runs in the ConsensusMaps' protein IDs (experimental)
-----
:param cmap: ConsensusMaps with protein IDs
:param greedy_group_resolution: Adds indistinguishable protein groups with separate scores
:return: Writes its protein ID results into the ConsensusMap
         - Cython signature: void inferPosteriorProbabilities(ConsensusMap & cmap, bool greedy_group_resolution, ExperimentalDesign exp_des)


Performs inference
-----
Writes its results into protein and (optionally also) peptide hits (as new score)
Optionally adds indistinguishable protein groups with separate scores, too
Loops over all runs in the ConsensusMaps' protein IDs (experimental)
-----
:param cmap: ConsensusMaps with protein IDs.
:param greedy_group_resolution: Adds indistinguishable protein groups with separate scores
:param exp_des: Experimental Design
:return: Writes its protein ID results into the ConsensusMap




.. py:method:: BayesianProteinInferenceAlgorithm.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: BayesianProteinInferenceAlgorithm.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: BayesianProteinInferenceAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: BayesianProteinInferenceAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: BayesianProteinInferenceAlgorithm.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: BayesianProteinInferenceAlgorithm.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




