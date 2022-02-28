SeedListGenerator
=================

.. py:class:: SeedListGenerator


   Bases: :py:class:`object`


Cython implementation of _SeedListGenerator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SeedListGenerator.html




.. py:method:: SeedListGenerator.convertSeedList


- Cython signature: void convertSeedList(libcpp_vector[DPosition2] & seeds, FeatureMap & features)
  Converts a list of seed positions to a feature map (expected format for FeatureFinder)


- Cython signature: void convertSeedList(FeatureMap & features, libcpp_vector[DPosition2] & seeds)
  Converts a feature map with seed positions back to a simple list




.. py:method:: SeedListGenerator.generateSeedList


- Cython signature: void generateSeedList(MSExperiment exp, libcpp_vector[DPosition2] & seeds)
  Generate a seed list based on an MS experiment


- Cython signature: void generateSeedList(libcpp_vector[PeptideIdentification] & peptides, libcpp_vector[DPosition2] & seeds, bool use_peptide_mass)
  Generates a seed list based on a list of peptide identifications




