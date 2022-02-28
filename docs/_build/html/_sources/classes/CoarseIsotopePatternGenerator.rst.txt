CoarseIsotopePatternGenerator
=============================

.. py:class:: CoarseIsotopePatternGenerator


   Bases: :py:class:`object`


Cython implementation of _CoarseIsotopePatternGenerator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CoarseIsotopePatternGenerator.html




.. py:method:: CoarseIsotopePatternGenerator.approximateFromPeptideWeight


Cython signature: IsotopeDistribution approximateFromPeptideWeight(double mass, unsigned int num_peaks, unsigned int charge)


Roughly approximate peptide IsotopeDistribution from monoisotopic weight using Poisson distribution.
m/z values approximated by adding one neutron mass (divided by charge) for every peak, starting at
the given monoisotopic weight. Foundation from: Bellew et al, https://dx.doi.org/10.1093/bioinformatics/btl276
This method is around 50 times faster than estimateFromPeptideWeight, but only an approximation.
The following are the intensities of the first 6 peaks generated for a monoisotopic mass of 1000:
estimateFromPeptideWeight:    0.571133000;0.306181000;0.095811100;0.022036900;0.004092170;0.000644568
approximateFromPeptideWeight: 0.573753000;0.318752000;0.088542200;0.016396700;0.002277320;0.000253036
KL divergences of the first 20 intensities of estimateFromPeptideWeight and this approximation range from 4.97E-5 for a
monoisotopic mass of 20 to 0.0144 for a mass of 2500. For comparison, when comparing an observed pattern with a
theoretical ground truth, the observed pattern is said to be an isotopic pattern if the KL between the two is below 0.05
for 2 peaks and below 0.6 for >=6 peaks by Guo Ci Teo et al.




.. py:method:: CoarseIsotopePatternGenerator.approximateIntensities


Cython signature: libcpp_vector[double] approximateIntensities(double mass, unsigned int num_peaks)


Roughly approximate peptidic isotope pattern intensities from monoisotopic weight using Poisson distribution.
Foundation from: Bellew et al, https://dx.doi.org/10.1093/bioinformatics/btl276
This method is around 100 times faster than estimateFromPeptideWeight, but only an approximation, see approximateFromPeptideWeight.




.. py:method:: CoarseIsotopePatternGenerator.calcFragmentIsotopeDist


Cython signature: IsotopeDistribution calcFragmentIsotopeDist(IsotopeDistribution & fragment_isotope_dist, IsotopeDistribution & comp_fragment_isotope_dist, libcpp_set[unsigned int] & precursor_isotopes, double fragment_mono_mass)
Calculate isotopic distribution for a fragment molecule




.. py:method:: CoarseIsotopePatternGenerator.estimateForFragmentFromDNAWeight


Cython signature: IsotopeDistribution estimateForFragmentFromDNAWeight(double average_weight_precursor, double average_weight_fragment, libcpp_set[unsigned int] & precursor_isotopes)


Estimate DNA fragment IsotopeDistribution from the precursor's average weight,
fragment's average weight, and a set of isolated precursor isotopes.




.. py:method:: CoarseIsotopePatternGenerator.estimateForFragmentFromPeptideWeight


Cython signature: IsotopeDistribution estimateForFragmentFromPeptideWeight(double average_weight_precursor, double average_weight_fragment, libcpp_set[unsigned int] & precursor_isotopes)
Estimate peptide fragment IsotopeDistribution from the precursor's average weight, fragment's average weight, and a set of isolated precursor isotopes




.. py:method:: CoarseIsotopePatternGenerator.estimateForFragmentFromPeptideWeightAndS


Cython signature: IsotopeDistribution estimateForFragmentFromPeptideWeightAndS(double average_weight_precursor, unsigned int S_precursor, double average_weight_fragment, unsigned int S_fragment, libcpp_set[unsigned int] & precursor_isotopes)


Estimate peptide fragment IsotopeDistribution from the precursor's average weight,
number of sulfurs in the precursor, fragment's average weight, number of sulfurs in the fragment,
and a set of isolated precursor isotopes.




.. py:method:: CoarseIsotopePatternGenerator.estimateForFragmentFromRNAWeight


Cython signature: IsotopeDistribution estimateForFragmentFromRNAWeight(double average_weight_precursor, double average_weight_fragment, libcpp_set[unsigned int] & precursor_isotopes)


Estimate RNA fragment IsotopeDistribution from the precursor's average weight,
fragment's average weight, and a set of isolated precursor isotopes




.. py:method:: CoarseIsotopePatternGenerator.estimateForFragmentFromWeightAndComp


Cython signature: IsotopeDistribution estimateForFragmentFromWeightAndComp(double average_weight_precursor, double average_weight_fragment, libcpp_set[unsigned int] & precursor_isotopes, double C, double H, double N, double O, double S, double P)


Estimate fragment IsotopeDistribution from the precursor's average weight,
fragment's average weight, a set of isolated precursor isotopes, and average composition




.. py:method:: CoarseIsotopePatternGenerator.estimateFromDNAWeight


Cython signature: IsotopeDistribution estimateFromDNAWeight(double average_weight)
Estimate Nucleotide Isotopedistribution from weight




.. py:method:: CoarseIsotopePatternGenerator.estimateFromPeptideWeight


Cython signature: IsotopeDistribution estimateFromPeptideWeight(double average_weight)
Estimate Peptide Isotopedistribution from weight and number of isotopes that should be reported




.. py:method:: CoarseIsotopePatternGenerator.estimateFromPeptideWeightAndS


Cython signature: IsotopeDistribution estimateFromPeptideWeightAndS(double average_weight, unsigned int S)
Estimate peptide IsotopeDistribution from average weight and exact number of sulfurs




.. py:method:: CoarseIsotopePatternGenerator.estimateFromRNAWeight


Cython signature: IsotopeDistribution estimateFromRNAWeight(double average_weight)
Estimate Nucleotide Isotopedistribution from weight




.. py:method:: CoarseIsotopePatternGenerator.estimateFromWeightAndComp


Cython signature: IsotopeDistribution estimateFromWeightAndComp(double average_weight, double C, double H, double N, double O, double S, double P)




.. py:method:: CoarseIsotopePatternGenerator.estimateFromWeightAndCompAndS


Cython signature: IsotopeDistribution estimateFromWeightAndCompAndS(double average_weight, unsigned int S, double C, double H, double N, double O, double P)
Estimate IsotopeDistribution from weight, exact number of sulfurs, and average remaining composition




.. py:method:: CoarseIsotopePatternGenerator.getMaxIsotope


Cython signature: size_t getMaxIsotope()
Returns the currently set maximum isotope




.. py:method:: CoarseIsotopePatternGenerator.getRoundMasses


Cython signature: bool getRoundMasses()
Returns the current value of the flag to round masses to integer values (true) or return accurate masses (false)




.. py:method:: CoarseIsotopePatternGenerator.run


Cython signature: IsotopeDistribution run(EmpiricalFormula)




.. py:method:: CoarseIsotopePatternGenerator.setMaxIsotope


Cython signature: void setMaxIsotope(size_t max_isotope)
Sets the maximal isotope with 'max_isotope'




.. py:method:: CoarseIsotopePatternGenerator.setRoundMasses


Cython signature: void setRoundMasses(bool round_masses_)
Sets the round_masses_ flag to round masses to integer values (true) or return accurate masses (false)




