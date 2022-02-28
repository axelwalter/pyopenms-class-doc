ExperimentalDesign
==================

.. py:class:: ExperimentalDesign


   Bases: :py:class:`object`


Cython implementation of _ExperimentalDesign


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ExperimentalDesign.html


 Representation of an experimental design in OpenMS. Instances can be loaded with the ExperimentalDesignFile class




.. py:method:: ExperimentalDesign.fromConsensusMap


Cython signature: ExperimentalDesign fromConsensusMap(ConsensusMap c)




.. py:method:: ExperimentalDesign.fromFeatureMap


Cython signature: ExperimentalDesign fromFeatureMap(FeatureMap f)




.. py:method:: ExperimentalDesign.fromIdentifications


Cython signature: ExperimentalDesign fromIdentifications(libcpp_vector[ProteinIdentification] & proteins)




.. py:method:: ExperimentalDesign.getMSFileSection


Cython signature: libcpp_vector[ExperimentalDesign_MSFileSectionEntry] getMSFileSection()




.. py:method:: ExperimentalDesign.getNumberOfFractionGroups


Cython signature: unsigned int getNumberOfFractionGroups()
Allows to group fraction ids and source files. Return the number of fraction_groups




.. py:method:: ExperimentalDesign.getNumberOfFractions


Cython signature: unsigned int getNumberOfFractions()
Returns the number of fractions (= highest fraction index)




.. py:method:: ExperimentalDesign.getNumberOfLabels


Cython signature: unsigned int getNumberOfLabels()
Returns the number of labels per file




.. py:method:: ExperimentalDesign.getNumberOfMSFiles


Cython signature: unsigned int getNumberOfMSFiles()
Returns the number of MS files (= fractions * fraction_groups)




.. py:method:: ExperimentalDesign.getNumberOfSamples


Cython signature: unsigned int getNumberOfSamples()
Returns the number of samples measured (= highest sample index)




.. py:method:: ExperimentalDesign.getSample


Cython signature: unsigned int getSample(unsigned int fraction_group, unsigned int label)
Returns sample index (depends on fraction_group and label)




.. py:method:: ExperimentalDesign.getSampleSection


Cython signature: ExperimentalDesign_SampleSection getSampleSection()
Returns the Sample Section of the experimental design file




.. py:method:: ExperimentalDesign.isFractionated


Cython signature: bool isFractionated()
Returns whether at least one fraction_group in this experimental design is fractionated




.. py:method:: ExperimentalDesign.sameNrOfMSFilesPerFraction


Cython signature: bool sameNrOfMSFilesPerFraction()
Returns if each fraction number is associated with the same number of fraction_group




.. py:method:: ExperimentalDesign.setMSFileSection


Cython signature: void setMSFileSection(libcpp_vector[ExperimentalDesign_MSFileSectionEntry] msfile_section)




.. py:method:: ExperimentalDesign.setSampleSection


Cython signature: void setSampleSection(ExperimentalDesign_SampleSection sample_section)
Sets the Sample Section of the experimental design file




