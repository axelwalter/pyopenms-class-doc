MetaboTargetedTargetDecoy
=========================

.. py:class:: MetaboTargetedTargetDecoy


   Bases: :py:class:`object`


Cython implementation of _MetaboTargetedTargetDecoy


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaboTargetedTargetDecoy.html




.. py:method:: MetaboTargetedTargetDecoy.constructTargetDecoyMassMapping


Cython signature: libcpp_vector[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] constructTargetDecoyMassMapping(TargetedExperiment & t_exp)


Constructs a mass mapping of targets and decoys using the unique m_id identifier
-----
:param t_exp: TransitionExperiment holds compound and transition information used for the mapping




.. py:method:: MetaboTargetedTargetDecoy.generateMissingDecoysByMassShift


Cython signature: void generateMissingDecoysByMassShift(TargetedExperiment & t_exp, libcpp_vector[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] & mappings, double & mass_to_add)


Generate a decoy for targets where fragmentation tree re-rooting was not possible, by adding a specifiable mass to the target fragments
-----
:param t_exp: TransitionExperiment holds compound and transition information
:param mappings: Map of identifier to target and decoy masses
:param mass_to_add: The maximum number of transitions required per assay




.. py:method:: MetaboTargetedTargetDecoy.resolveOverlappingTargetDecoyMassesByIndividualMassShift


Cython signature: void resolveOverlappingTargetDecoyMassesByIndividualMassShift(TargetedExperiment & t_exp, libcpp_vector[MetaboTargetedTargetDecoy_MetaboTargetDecoyMassMapping] & mappings, double & mass_to_add)


Resolves overlapping target and decoy transition masses by adding a specifiable mass (e.g. CH2) to the overlapping decoy fragment
-----
:param t_exp: TransitionExperiment holds compound and transition information
:param mappings: Map of identifier to target and decoy masses
:param mass_to_add: (e.g. CH2)




