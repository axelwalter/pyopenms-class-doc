TargetedExperiment
==================

.. py:class:: TargetedExperiment


   Bases: :py:class:`object`


Cython implementation of _TargetedExperiment


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TargetedExperiment.html




.. py:method:: TargetedExperiment.addCV


Cython signature: void addCV(CV cv)




.. py:method:: TargetedExperiment.addCompound


Cython signature: void addCompound(Compound rhs)




.. py:method:: TargetedExperiment.addContact


Cython signature: void addContact(Contact contact)




.. py:method:: TargetedExperiment.addExcludeTarget


Cython signature: void addExcludeTarget(IncludeExcludeTarget target)




.. py:method:: TargetedExperiment.addIncludeTarget


Cython signature: void addIncludeTarget(IncludeExcludeTarget target)




.. py:method:: TargetedExperiment.addInstrument


Cython signature: void addInstrument(TargetedExperiment_Instrument instrument)




.. py:method:: TargetedExperiment.addPeptide


Cython signature: void addPeptide(Peptide rhs)




.. py:method:: TargetedExperiment.addProtein


Cython signature: void addProtein(Protein protein)




.. py:method:: TargetedExperiment.addPublication


Cython signature: void addPublication(Publication publication)




.. py:method:: TargetedExperiment.addSoftware


Cython signature: void addSoftware(Software software)




.. py:method:: TargetedExperiment.addSourceFile


Cython signature: void addSourceFile(SourceFile source_file)




.. py:method:: TargetedExperiment.addTargetCVTerm


Cython signature: void addTargetCVTerm(CVTerm cv_term)




.. py:method:: TargetedExperiment.addTransition


Cython signature: void addTransition(ReactionMonitoringTransition transition)




.. py:method:: TargetedExperiment.clear


Cython signature: void clear(bool clear_meta_data)




.. py:method:: TargetedExperiment.containsInvalidReferences


Cython signature: bool containsInvalidReferences()




.. py:method:: TargetedExperiment.getCVs


Cython signature: libcpp_vector[CV] getCVs()




.. py:method:: TargetedExperiment.getCompoundByRef


Cython signature: Compound getCompoundByRef(String ref)




.. py:method:: TargetedExperiment.getCompounds


Cython signature: libcpp_vector[Compound] getCompounds()




.. py:method:: TargetedExperiment.getContacts


Cython signature: libcpp_vector[Contact] getContacts()




.. py:method:: TargetedExperiment.getExcludeTargets


Cython signature: libcpp_vector[IncludeExcludeTarget] getExcludeTargets()




.. py:method:: TargetedExperiment.getIncludeTargets


Cython signature: libcpp_vector[IncludeExcludeTarget] getIncludeTargets()




.. py:method:: TargetedExperiment.getInstruments


Cython signature: libcpp_vector[TargetedExperiment_Instrument] getInstruments()




.. py:method:: TargetedExperiment.getPeptideByRef


Cython signature: Peptide getPeptideByRef(String ref)




.. py:method:: TargetedExperiment.getPeptides


Cython signature: libcpp_vector[Peptide] getPeptides()




.. py:method:: TargetedExperiment.getProteinByRef


Cython signature: Protein getProteinByRef(String ref)




.. py:method:: TargetedExperiment.getProteins


Cython signature: libcpp_vector[Protein] getProteins()




.. py:method:: TargetedExperiment.getPublications


Cython signature: libcpp_vector[Publication] getPublications()




.. py:method:: TargetedExperiment.getSoftware


Cython signature: libcpp_vector[Software] getSoftware()




.. py:method:: TargetedExperiment.getSourceFiles


Cython signature: libcpp_vector[SourceFile] getSourceFiles()




.. py:method:: TargetedExperiment.getTargetCVTerms


Cython signature: CVTermList getTargetCVTerms()




.. py:method:: TargetedExperiment.getTransitions


Cython signature: libcpp_vector[ReactionMonitoringTransition] getTransitions()




.. py:method:: TargetedExperiment.hasCompound


Cython signature: bool hasCompound(String ref)




.. py:method:: TargetedExperiment.hasPeptide


Cython signature: bool hasPeptide(String ref)




.. py:method:: TargetedExperiment.hasProtein


Cython signature: bool hasProtein(String ref)




.. py:method:: TargetedExperiment.setCVs


Cython signature: void setCVs(libcpp_vector[CV] cvs)




.. py:method:: TargetedExperiment.setCompounds


Cython signature: void setCompounds(libcpp_vector[Compound] rhs)




.. py:method:: TargetedExperiment.setContacts


Cython signature: void setContacts(libcpp_vector[Contact] contacts)




.. py:method:: TargetedExperiment.setExcludeTargets


Cython signature: void setExcludeTargets(libcpp_vector[IncludeExcludeTarget] targets)




.. py:method:: TargetedExperiment.setIncludeTargets


Cython signature: void setIncludeTargets(libcpp_vector[IncludeExcludeTarget] targets)




.. py:method:: TargetedExperiment.setInstruments


Cython signature: void setInstruments(libcpp_vector[TargetedExperiment_Instrument] instruments)




.. py:method:: TargetedExperiment.setPeptides


Cython signature: void setPeptides(libcpp_vector[Peptide] rhs)




.. py:method:: TargetedExperiment.setProteins


Cython signature: void setProteins(libcpp_vector[Protein] proteins)




.. py:method:: TargetedExperiment.setPublications


Cython signature: void setPublications(libcpp_vector[Publication] publications)




.. py:method:: TargetedExperiment.setSoftware


Cython signature: void setSoftware(libcpp_vector[Software] software)




.. py:method:: TargetedExperiment.setSourceFiles


Cython signature: void setSourceFiles(libcpp_vector[SourceFile] source_files)




.. py:method:: TargetedExperiment.setTargetCVTerms


Cython signature: void setTargetCVTerms(CVTermList cv_terms)




.. py:method:: TargetedExperiment.setTargetMetaValue


Cython signature: void setTargetMetaValue(String name, DataValue value)




.. py:method:: TargetedExperiment.setTransitions


Cython signature: void setTransitions(libcpp_vector[ReactionMonitoringTransition] transitions)




.. py:method:: TargetedExperiment.sortTransitionsByProductMZ


Cython signature: void sortTransitionsByProductMZ()




