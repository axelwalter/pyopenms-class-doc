MSSim
=====

.. py:class:: MSSim


   Bases: :py:class:`object`


Cython implementation of _MSSim


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSSim.html




.. py:method:: MSSim.getChargeConsensus


Cython signature: ConsensusMap getChargeConsensus()
Returns the charge consensus map of simulated features




.. py:method:: MSSim.getContaminants


Cython signature: FeatureMap getContaminants()
Returns the contaminants feature map of simulated features




.. py:method:: MSSim.getExperiment


Cython signature: MSExperiment getExperiment()
Returns the simulated experiment




.. py:method:: MSSim.getFeatureIdentifications


Cython signature: void getFeatureIdentifications(libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides)
Returns the simulated identifications (proteins and peptides) from feature annotations




.. py:method:: MSSim.getIdentifications


Cython signature: void getIdentifications(libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides)
Returns the simulated identifications (proteins and peptides)




.. py:method:: MSSim.getLabelingConsensus


Cython signature: ConsensusMap getLabelingConsensus()
Returns the labeling consensus map of simulated features




.. py:method:: MSSim.getMS2Identifications


Cython signature: void getMS2Identifications(libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides)
Returns the simulated MS2 identifications (proteins and peptides)




.. py:method:: MSSim.getParameters


Cython signature: Param getParameters()
Returns the default parameters for simulation including the labeling technique with name `labeling_name`




.. py:method:: MSSim.getPeakMap


Cython signature: MSExperiment getPeakMap()
Returns the labeling consensus map of simulated features




.. py:method:: MSSim.getSimulatedFeatures


Cython signature: FeatureMap getSimulatedFeatures()
Returns the simulated features




.. py:method:: MSSim.simulate


Cython signature: void simulate(shared_ptr[SimRandomNumberGenerator] rnd_gen, libcpp_vector[libcpp_vector[SimProtein]] peptides)


General purpose function to simulate a mass spectrometry run
-----
:param rnd_gen: Random number generator which will be passed to the different classes
:param peptides: List of peptides and abundances that will be simulated




