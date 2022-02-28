ResidueModification
===================

.. py:class:: ResidueModification


   Bases: :py:class:`object`


Cython implementation of _ResidueModification


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ResidueModification.html




.. py:attribute:: ResidueModification.SourceClassification


alias of :py:class:`pyopenms.pyopenms_5.__SourceClassification`


.. py:attribute:: ResidueModification.TermSpecificity


alias of :py:class:`pyopenms.pyopenms_5.__TermSpecificity`


.. py:method:: ResidueModification.addSynonym


Cython signature: void addSynonym(const String & synonym)
Adds a synonym to the unique list




.. py:method:: ResidueModification.getAverageMass


Cython signature: double getAverageMass()
Returns the average mass if set




.. py:method:: ResidueModification.getDiffAverageMass


Cython signature: double getDiffAverageMass()
Returns the difference average mass, or 0.0 if not set




.. py:method:: ResidueModification.getDiffFormula


Cython signature: EmpiricalFormula getDiffFormula()
Returns the diff formula if one was set




.. py:method:: ResidueModification.getDiffMonoMass


Cython signature: double getDiffMonoMass()
Returns the diff monoisotopic mass, or 0.0 if not set




.. py:method:: ResidueModification.getFormula


Cython signature: String getFormula()
Returns the chemical formula if set




.. py:method:: ResidueModification.getFullId


Cython signature: String getFullId()




.. py:method:: ResidueModification.getFullName


Cython signature: String getFullName()
Returns the full name of the modification




.. py:method:: ResidueModification.getId


Cython signature: String getId()
Returns the identifier of the modification




.. py:method:: ResidueModification.getMonoMass


Cython signature: double getMonoMass()
Return the monoisotopic mass, or 0.0 if not set




.. py:method:: ResidueModification.getName


Cython signature: String getName()
Returns the PSI-MS-label if available; e.g. Mascot uses this name




.. py:method:: ResidueModification.getNeutralLossAverageMasses


Cython signature: libcpp_vector[double] getNeutralLossAverageMasses()
Returns the neutral loss average weight




.. py:method:: ResidueModification.getNeutralLossDiffFormulas


Cython signature: libcpp_vector[EmpiricalFormula] getNeutralLossDiffFormulas()
Returns the neutral loss diff formula (if available)




.. py:method:: ResidueModification.getNeutralLossMonoMasses


Cython signature: libcpp_vector[double] getNeutralLossMonoMasses()
Returns the neutral loss mono weight




.. py:method:: ResidueModification.getOrigin


Cython signature: char getOrigin()
Returns the origin (i.e. modified amino acid)




.. py:method:: ResidueModification.getPSIMODAccession


Cython signature: String getPSIMODAccession()
Returns the PSI-MOD accession if available




.. py:method:: ResidueModification.getSourceClassification


Cython signature: SourceClassification getSourceClassification()
Returns the source classification, if none was set, it is unspecific




.. py:method:: ResidueModification.getSourceClassificationName


Cython signature: String getSourceClassificationName(SourceClassification classification)
Returns the classification




.. py:method:: ResidueModification.getSynonyms


Cython signature: libcpp_set[String] getSynonyms()
Returns the set of synonyms




.. py:method:: ResidueModification.getTermSpecificity


Cython signature: TermSpecificity getTermSpecificity()
Returns terminal specificity




.. py:method:: ResidueModification.getTermSpecificityName


Cython signature: String getTermSpecificityName(TermSpecificity)
Returns the name of the terminal specificity




.. py:method:: ResidueModification.getUniModAccession


Cython signature: String getUniModAccession()
Returns the unimod accession if available




.. py:method:: ResidueModification.getUniModRecordId


Cython signature: int getUniModRecordId()
Gets the unimod record id




.. py:method:: ResidueModification.hasNeutralLoss


Cython signature: bool hasNeutralLoss()
Returns true if a neutral loss formula is set




.. py:method:: ResidueModification.isUserDefined


Cython signature: bool isUserDefined()
Returns true if it is a user-defined modification (empty id)




.. py:method:: ResidueModification.setAverageMass


Cython signature: void setAverageMass(double mass)
Sets the average mass




.. py:method:: ResidueModification.setDiffAverageMass


Cython signature: void setDiffAverageMass(double mass)
Sets the difference average mass




.. py:method:: ResidueModification.setDiffFormula


Cython signature: void setDiffFormula(EmpiricalFormula & diff_formula)
Sets diff formula (no masses will be changed)




.. py:method:: ResidueModification.setDiffMonoMass


Cython signature: void setDiffMonoMass(double mass)
Sets the difference monoisotopic mass




.. py:method:: ResidueModification.setFormula


Cython signature: void setFormula(const String & composition)
Sets the formula (no masses will be changed)




.. py:method:: ResidueModification.setFullId


Cython signature: void setFullId(const String & full_id)
Sets the full identifier (Unimod Accession + origin, if available)




.. py:method:: ResidueModification.setFullName


Cython signature: void setFullName(const String & full_name)
Sets the full name of the modification; must NOT contain the origin (or . for terminals!)




.. py:method:: ResidueModification.setId


Cython signature: void setId(const String & id_)
Sets the identifier of the modification




.. py:method:: ResidueModification.setMonoMass


Cython signature: void setMonoMass(double mass)
Sets the monoisotopic mass (this must include the weight of the residue itself!)




.. py:method:: ResidueModification.setName


Cython signature: void setName(const String & name)
Sets the name of modification




.. py:method:: ResidueModification.setNeutralLossAverageMasses


Cython signature: void setNeutralLossAverageMasses(libcpp_vector[double] average_masses)
Sets the neutral loss average weight




.. py:method:: ResidueModification.setNeutralLossDiffFormulas


Cython signature: void setNeutralLossDiffFormulas(libcpp_vector[EmpiricalFormula] & diff_formulas)
Sets the neutral loss formula




.. py:method:: ResidueModification.setNeutralLossMonoMasses


Cython signature: void setNeutralLossMonoMasses(libcpp_vector[double] mono_masses)
Sets the neutral loss mono weight




.. py:method:: ResidueModification.setOrigin


Cython signature: void setOrigin(char origin)
Sets the origin (i.e. modified amino acid)




.. py:method:: ResidueModification.setPSIMODAccession


Cython signature: void setPSIMODAccession(const String & id_)
Sets the MOD-XXXXX accession of PSI-MOD




.. py:method:: ResidueModification.setSourceClassification


- Cython signature: void setSourceClassification(const String & classification)
  Classification as defined by the PSI-MOD


- Cython signature: void setSourceClassification(SourceClassification classification)
  Sets the source classification




.. py:method:: ResidueModification.setSynonyms


Cython signature: void setSynonyms(libcpp_set[String] & synonyms)
Sets the synonyms of that modification




.. py:method:: ResidueModification.setTermSpecificity


- Cython signature: void setTermSpecificity(TermSpecificity term_spec)
  Sets the term specificity


- Cython signature: void setTermSpecificity(const String & name)
  Sets the terminal specificity using a name




.. py:method:: ResidueModification.setUniModRecordId


Cython signature: void setUniModRecordId(int id_)
Sets the unimod record id




