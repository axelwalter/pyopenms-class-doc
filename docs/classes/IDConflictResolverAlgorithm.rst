IDConflictResolverAlgorithm
===========================

.. py:class:: IDConflictResolverAlgorithm


   Bases: :py:class:`object`


Cython implementation of _IDConflictResolverAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IDConflictResolverAlgorithm.html




.. py:method:: IDConflictResolverAlgorithm.resolve


         - Cython signature: void resolve(FeatureMap & features)


Resolves ambiguous annotations of features with peptide identifications
-----
The the filtered identifications are added to the vector of unassigned peptides
and also reduced to a single best hit
-----
:param keep_matching: Keeps all IDs that match the modified sequence of the best hit in the feature (e.g. keeps all IDs in a ConsensusMap if id'd same across multiple runs)
         - Cython signature: void resolve(ConsensusMap & features)


Resolves ambiguous annotations of consensus features with peptide identifications
-----
The the filtered identifications are added to the vector of unassigned peptides
and also reduced to a single best hit
-----
:param keep_matching: Keeps all IDs that match the modified sequence of the best hit in the feature (e.g. keeps all IDs in a ConsensusMap if id'd same across multiple runs)




.. py:method:: IDConflictResolverAlgorithm.resolveBetweenFeatures


         - Cython signature: void resolveBetweenFeatures(FeatureMap & features)


In a single (feature/consensus) map, features with the same (possibly modified) sequence and charge state may appear
-----
This filter removes the peptide sequence annotations from features, if a higher-intensity feature with the same (charge, sequence)
combination exists in the map. The total number of features remains unchanged. In the final output, each (charge, sequence) combination
appears only once, i.e. no multiplicities
         - Cython signature: void resolveBetweenFeatures(ConsensusMap & features)


In a single (feature/consensus) map, features with the same (possibly modified) sequence and charge state may appear
-----
This filter removes the peptide sequence annotations from features, if a higher-intensity feature with the same (charge, sequence)
combination exists in the map. The total number of features remains unchanged. In the final output, each (charge, sequence) combination
appears only once, i.e. no multiplicities




