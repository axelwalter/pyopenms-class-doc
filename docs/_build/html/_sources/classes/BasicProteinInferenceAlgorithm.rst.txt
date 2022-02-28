BasicProteinInferenceAlgorithm
==============================

.. py:class:: BasicProteinInferenceAlgorithm


   Bases: :py:class:`object`


Cython implementation of _BasicProteinInferenceAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1BasicProteinInferenceAlgorithm.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']


 Algorithm class that implements simple protein inference by aggregation of peptide scores.
 -----
 It has multiple parameter options like the aggregation method, when to distinguish peptidoforms,
 and if you want to use shared peptides ("use_shared_peptides").
 First, the best PSM per spectrum is used, then only the best PSM per peptidoform is aggregated.
 Peptidoforms can optionally be distinguished via the treat_X_separate parameters:
 - Modifications (modified sequence string)
 - Charge states
 The algorithm assumes posteriors or posterior error probabilities and converts to posteriors initially.
 Possible aggregation methods that can be set via the parameter "aggregation_method" are:
 - "best" (default)
 - "sum"
 - "product" (ignoring zeroes)
 Annotation of the number of peptides used for aggregation can be disabled (see parameters).
 Supports multiple runs but goes through them one by one iterating over the full PeptideIdentification vector.
 Warning: Does not "link" the peptides to the resulting protein run. If you wish to do that you have to do
 it manually.
 -----
 Usage:
   from pyopenms import *
   from urllib.request import urlretrieve
   urlretrieve("https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/tests/class_tests/openms/data/newMergerTest_out.idXML", "BasicProteinInference_test.idXML")
   proteins = []
   peptides = []
   idf = IdXMLFile()
   idf.load("BasicProteinInference_test.idXML", proteins, peptides);
   bpia = BasicProteinInferenceAlgorithm()
   p = bpia.getParameters();
   p.setValue("min_peptides_per_protein", 0);
   bpia.setParameters(p);
   bpia.run(peptides, proteins);
   #
   hits = proteins[0].getHits()
   print(hits[0].getScore()) # 0.6
   print(hits[5].getScore()) # 0.9
   print(hits[0].getMetaValue("nr_found_peptides")) # 1
   print(hits[3].getMetaValue("nr_found_peptides")) # 2
 -----




.. py:method:: BasicProteinInferenceAlgorithm.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: BasicProteinInferenceAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: BasicProteinInferenceAlgorithm.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: BasicProteinInferenceAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: BasicProteinInferenceAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: BasicProteinInferenceAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: BasicProteinInferenceAlgorithm.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: BasicProteinInferenceAlgorithm.run


         - Cython signature: void run(libcpp_vector[PeptideIdentification] & pep_ids, libcpp_vector[ProteinIdentification] & prot_ids)


Performs basic aggregation-based inference per ProteinIdentification run. See class help.
-----
:param pep_ids: Vector of peptide identifications
:param prot_ids: Vector of protein identification runs. Scores will be overwritten and groups added.
:return: Writes its results into prot_ids
         - Cython signature: void run(libcpp_vector[PeptideIdentification] & pep_ids, ProteinIdentification & prot_id)


Performs basic aggregation-based inference on single ProteinIdentification run. See class help.
-----
:param pep_ids: Vector of peptide identifications
:param prot_id: ProteinIdentification run with possible proteins. Scores will be overwritten and groups added.
:return: Writes its results into prot_ids
         - Cython signature: void run(ConsensusMap & cmap, ProteinIdentification & prot_id, bool include_unassigned)


Performs basic aggregation-based inference on identifications in a ConsensusMap. See class help.
-----
prot_id should contain the union of all proteins in the map. E.g. use ConsensusMapMergerAlgorithm and
then pass the first=merged run.
-----
:param cmap: ConsensusMap = Consensus features with metadata and peptide identifications
:param prot_id: ProteinIdentification run with possible proteins. Scores will be overwritten and groups added.
:return: Writes its results into prot_ids




.. py:method:: BasicProteinInferenceAlgorithm.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: BasicProteinInferenceAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: BasicProteinInferenceAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: BasicProteinInferenceAlgorithm.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: BasicProteinInferenceAlgorithm.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




