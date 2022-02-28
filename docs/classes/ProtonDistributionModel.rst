ProtonDistributionModel
=======================

.. py:class:: ProtonDistributionModel


   Bases: :py:class:`object`


Cython implementation of _ProtonDistributionModel


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProtonDistributionModel.html
 -- Inherits from ['DefaultParamHandler']


 A proton distribution model to calculate the proton distribution over charged peptides
 -----
 The model uses proton affinity values of backbone nitrogens and sidechains to calculate the
 proton distribution of charged peptide among these sites. The possible sites are the peptide
 bonds between the amino acids, the side chains and the C-terminus and N-terminus. The calculation
 is done calculating a Boltzmann distribution of the sites
 -----
 Details and the proton affinities can be found in
 Z. Zhang, Prediction of Low-Energy Collision-Induced Dissociation Spectra of Peptides,
 Anal. Chem., 76 (14), 3908 - 3922, 2004
 -----
 A proton distribution can be calculated using the getProtonDistribution method. The backbone
 probabilities are reported in the first parameter (index 0 for the N-terminus, index 1 for the
 first peptide bond...), the site chain probabilities are reported in the second parameter
 (index 0, for the first amino acid...). The peptide and the number of protons as well as type
 of peptide (can be Reside::YIon for peptides and y-ions and any other ion type)
 -----
 Charge state intensities of differently charged equal (e.g. y7+ and y7++) ions can be calculated
 using the getChargeStateIntensities function




.. py:attribute:: ProtonDistributionModel.FragmentationType


alias of :py:class:`pyopenms.pyopenms_1.__FragmentationType`


.. py:method:: ProtonDistributionModel.getChargeStateIntensities


Cython signature: void getChargeStateIntensities(AASequence & peptide, AASequence & n_term_ion, AASequence & c_term_ion, int charge, ResidueType n_term_type, libcpp_vector[double] & n_term_intensities, libcpp_vector[double] & c_term_intensities, FragmentationType type_)


Calculates the charge state intensities of different charge states of the same ion
-----
:param peptide: The peptide
:param n_term_ion: The prefix ion sequence
:param c_term_ion: The suffix ion sequence
:param charge: The charge
:param n_term_type: The ion type of the N-terminal ion; valid values are Residue::AIon, Residue::BIon
:param n_term_intensities: The probability of seeing a charged prefix ions (first index corresponds to ion of charge 1)
:param c_term_intensities: The probability of seeing a charged suffix ions (first index corresponds to ion of charge 2)
:param type: The type of fragmentation (charge-directed, charge-remote of side chain)




.. py:method:: ProtonDistributionModel.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: ProtonDistributionModel.getName


Cython signature: String getName()
Returns the name




.. py:method:: ProtonDistributionModel.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: ProtonDistributionModel.getProtonDistribution


Cython signature: void getProtonDistribution(libcpp_vector[double] & bb_charges, libcpp_vector[double] & sc_charges, AASequence & peptide, int charge, ResidueType res_type)


Calculates a proton distribution of the given charged peptide
-----
:param bb_charges: The calculated probabilities of the backbone sites (including N-terminus and C-terminus)
:param sc_charges: The calculated probabilities of the side chain sites
:param peptide The peptide
:param charge The charge
:param res_type: The type of the ion given in peptide. Peptides are handled as y-ions, i.e. Residue::YIon




.. py:method:: ProtonDistributionModel.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: ProtonDistributionModel.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: ProtonDistributionModel.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: ProtonDistributionModel.setPeptideProtonDistribution


Cython signature: void setPeptideProtonDistribution(libcpp_vector[double] & bb_charge, libcpp_vector[double] & sc_charge)




