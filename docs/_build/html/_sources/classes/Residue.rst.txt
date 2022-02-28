Residue
=======

.. py:class:: Residue


   Bases: :py:class:`object`


Cython implementation of _Residue


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Residue.html




.. py:attribute:: Residue.ResidueType


alias of :py:class:`pyopenms.pyopenms_1.__ResidueType`


.. py:method:: Residue.addLossFormula


Cython signature: void addLossFormula(EmpiricalFormula)
Adds a neutral loss formula




.. py:method:: Residue.addLossName


Cython signature: void addLossName(String name)
Adds neutral loss molecule name




.. py:method:: Residue.addNTermLossFormula


Cython signature: void addNTermLossFormula(EmpiricalFormula)
Adds N-terminal losses




.. py:method:: Residue.addNTermLossName


Cython signature: void addNTermLossName(String name)
Adds a N-terminal loss name




.. py:method:: Residue.addResidueSet


Cython signature: void addResidueSet(String residue_sets)
Adds a residue set to the residue sets




.. py:method:: Residue.addSynonym


Cython signature: void addSynonym(String synonym)
Adds a synonym




.. py:method:: Residue.getAverageWeight


- Cython signature: double getAverageWeight()
  Returns average weight of the residue


- Cython signature: double getAverageWeight(ResidueType res_type)




.. py:method:: Residue.getBackboneBasicityLeft


Cython signature: double getBackboneBasicityLeft()
Returns the backbone basicitiy if located in N-terminal direction




.. py:method:: Residue.getBackboneBasicityRight


Cython signature: double getBackboneBasicityRight()
Returns the C-terminal direction backbone basicitiy




.. py:method:: Residue.getFormula


- Cython signature: EmpiricalFormula getFormula()
  Returns the empirical formula of the residue


- Cython signature: EmpiricalFormula getFormula(ResidueType res_type)




.. py:method:: Residue.getInternalToAIon


Cython signature: EmpiricalFormula getInternalToAIon()




.. py:method:: Residue.getInternalToBIon


Cython signature: EmpiricalFormula getInternalToBIon()




.. py:method:: Residue.getInternalToCIon


Cython signature: EmpiricalFormula getInternalToCIon()




.. py:method:: Residue.getInternalToCTerm


Cython signature: EmpiricalFormula getInternalToCTerm()




.. py:method:: Residue.getInternalToFull


Cython signature: EmpiricalFormula getInternalToFull()




.. py:method:: Residue.getInternalToNTerm


Cython signature: EmpiricalFormula getInternalToNTerm()




.. py:method:: Residue.getInternalToXIon


Cython signature: EmpiricalFormula getInternalToXIon()




.. py:method:: Residue.getInternalToYIon


Cython signature: EmpiricalFormula getInternalToYIon()




.. py:method:: Residue.getInternalToZIon


Cython signature: EmpiricalFormula getInternalToZIon()




.. py:method:: Residue.getLossFormulas


Cython signature: libcpp_vector[EmpiricalFormula] getLossFormulas()
Returns the neutral loss formulas




.. py:method:: Residue.getLossNames


Cython signature: libcpp_vector[String] getLossNames()
Gets neutral loss name (if there is one, else returns an empty string)




.. py:method:: Residue.getLowMassIons


Cython signature: libcpp_vector[EmpiricalFormula] getLowMassIons()
Returns a vector of formulas with the low mass markers of the residue




.. py:method:: Residue.getModification


Cython signature: const ResidueModification * getModification()




.. py:method:: Residue.getModificationName


Cython signature: String getModificationName()
Returns the name of the modification to the modification




.. py:method:: Residue.getMonoWeight


- Cython signature: double getMonoWeight()
  Returns monoisotopic weight of the residue


- Cython signature: double getMonoWeight(ResidueType res_type)




.. py:method:: Residue.getNTermLossFormulas


Cython signature: libcpp_vector[EmpiricalFormula] getNTermLossFormulas()
Returns N-terminal loss formulas




.. py:method:: Residue.getNTermLossNames


Cython signature: libcpp_vector[String] getNTermLossNames()
Returns the N-terminal loss names




.. py:method:: Residue.getName


Cython signature: String getName()
Returns the name of the residue




.. py:method:: Residue.getOneLetterCode


Cython signature: String getOneLetterCode()
Returns the name as one letter code




.. py:method:: Residue.getPiValue


Cython signature: double getPiValue()
Calculates the isoelectric point using the pk values




.. py:method:: Residue.getPka


Cython signature: double getPka()
Returns the pka of the residue




.. py:method:: Residue.getPkb


Cython signature: double getPkb()
Returns the pkb of the residue




.. py:method:: Residue.getPkc


Cython signature: double getPkc()
Returns the pkc of the residue if it exists otherwise -1




.. py:method:: Residue.getResidueSets


Cython signature: libcpp_set[String] getResidueSets()
Returns the residue sets this residue is contained in




.. py:method:: Residue.getResidueTypeName


Cython signature: String getResidueTypeName(ResidueType res_type)
Returns the ion name given as a residue type




.. py:method:: Residue.getSideChainBasicity


Cython signature: double getSideChainBasicity()
Returns the side chain basicity




.. py:method:: Residue.getSynonyms


Cython signature: libcpp_set[String] getSynonyms()
Returns the sysnonyms




.. py:method:: Residue.getThreeLetterCode


Cython signature: String getThreeLetterCode()
Returns the name of the residue as three letter code




.. py:method:: Residue.hasNTermNeutralLosses


Cython signature: bool hasNTermNeutralLosses()
True if N-terminal neutral losses are set




.. py:method:: Residue.hasNeutralLoss


Cython signature: bool hasNeutralLoss()
True if the residue has neutral loss




.. py:method:: Residue.isInResidueSet


Cython signature: bool isInResidueSet(String residue_set)
True if the residue is contained in the set




.. py:method:: Residue.isModified


Cython signature: bool isModified()
True if the residue is a modified one




.. py:method:: Residue.residueTypeToIonLetter


Cython signature: char residueTypeToIonLetter(ResidueType res_type)
Helper for mapping residue types to letters for Text annotations and labels




.. py:method:: Residue.setAverageWeight


Cython signature: void setAverageWeight(double weight)
Sets average weight of the residue (must be full, with N and C-terminus)




.. py:method:: Residue.setBackboneBasicityLeft


Cython signature: void setBackboneBasicityLeft(double gb_bb_l)
Sets the N-terminal direction backbone basicitiy




.. py:method:: Residue.setBackboneBasicityRight


Cython signature: void setBackboneBasicityRight(double gb_bb_r)
Sets the C-terminal direction backbone basicity




.. py:method:: Residue.setFormula


Cython signature: void setFormula(EmpiricalFormula formula)
Sets empirical formula of the residue (must be full, with N and C-terminus)




.. py:method:: Residue.setLossFormulas


Cython signature: void setLossFormulas(libcpp_vector[EmpiricalFormula])
Sets the neutral loss formulas




.. py:method:: Residue.setLossNames


Cython signature: void setLossNames(libcpp_vector[String] name)
Sets the neutral loss molecule name




.. py:method:: Residue.setLowMassIons


Cython signature: void setLowMassIons(libcpp_vector[EmpiricalFormula] low_mass_ions)
Sets the low mass marker ions as a vector of formulas




.. py:method:: Residue.setModification


- Cython signature: void setModification(String name)
  Sets the modification by name; the mod should be present in ModificationsDB


- Cython signature: void setModification(const ResidueModification & mod)
  Sets the modification by a ResidueModification object; checks if present in ModificationsDB and adds if not.




.. py:method:: Residue.setModificationByDiffMonoMass


Cython signature: void setModificationByDiffMonoMass(double diffMonoMass)
Sets the modification by monoisotopic mass difference in Da; checks if present in ModificationsDB with tolerance and adds a "user-defined" modification if not (for later lookups).




.. py:method:: Residue.setMonoWeight


Cython signature: void setMonoWeight(double weight)
Sets monoisotopic weight of the residue (must be full, with N and C-terminus)




.. py:method:: Residue.setNTermLossFormulas


Cython signature: void setNTermLossFormulas(libcpp_vector[EmpiricalFormula])
Sets the N-terminal losses




.. py:method:: Residue.setNTermLossNames


Cython signature: void setNTermLossNames(libcpp_vector[String] name)
Sets the N-terminal loss names




.. py:method:: Residue.setName


Cython signature: void setName(String name)
Sets the name of the residue




.. py:method:: Residue.setOneLetterCode


Cython signature: void setOneLetterCode(String one_letter_code)
Sets the name as one letter code




.. py:method:: Residue.setPka


Cython signature: void setPka(double value)
Sets the pka of the residue




.. py:method:: Residue.setPkb


Cython signature: void setPkb(double value)
Sets the pkb of the residue




.. py:method:: Residue.setPkc


Cython signature: void setPkc(double value)
Sets the pkc of the residue




.. py:method:: Residue.setResidueSets


Cython signature: void setResidueSets(libcpp_set[String] residues_sets)
Sets the residue sets the amino acid is contained in




.. py:method:: Residue.setSideChainBasicity


Cython signature: void setSideChainBasicity(double gb_sc)
Sets the side chain basicity




.. py:method:: Residue.setSynonyms


Cython signature: void setSynonyms(libcpp_set[String] synonyms)
Sets the synonyms




.. py:method:: Residue.setThreeLetterCode


Cython signature: void setThreeLetterCode(String three_letter_code)
Sets the name of the residue as three letter code




