MRMIonSeries
============

.. py:class:: MRMIonSeries


   Bases: :py:class:`object`


Cython implementation of _MRMIonSeries


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMIonSeries.html




.. py:method:: MRMIonSeries.annotateTransition


Cython signature: void annotateTransition(ReactionMonitoringTransition & tr, Peptide peptide, double precursor_mz_threshold, double product_mz_threshold, bool enable_reannotation, libcpp_vector[String] fragment_types, libcpp_vector[size_t] fragment_charges, bool enable_specific_losses, bool enable_unspecific_losses, int round_decPow)


Annotates transition
-----
:param tr: The transition to annotate
:param peptide: The corresponding peptide
:param precursor_mz_threshold: The m/z threshold for annotation of the precursor ion
:param product_mz_threshold: The m/z threshold for annotation of the fragment ion
:param enable_reannotation: Whether the original (e.g. SpectraST) annotation should be used or reannotation should be conducted
:param fragment_types: The fragment ion types for reannotation
:param fragment_charges: The fragment ion charges for reannotation
:param enable_specific_losses: Whether specific neutral losses should be considered
:param enable_unspecific_losses: Whether unspecific neutral losses (H2O1, H3N1, C1H2N2, C1H2N1O1) should be considered
:param round_decPow: Round precursor and product m/z values to decimal power (default: -4)




.. py:method:: MRMIonSeries.annotateTransitionCV


Cython signature: void annotateTransitionCV(ReactionMonitoringTransition & tr, String annotation)


Annotates transition with CV terms
-----
:param tr: The transition to annotate
:param annotation: The fragment ion annotation




