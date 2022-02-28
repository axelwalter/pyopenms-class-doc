IMSAlphabet
===========

.. py:class:: IMSAlphabet


   Bases: :py:class:`object`


Cython implementation of _IMSAlphabet


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::ims::IMSAlphabet_1_1IMSAlphabet.html


 Holds an indexed list of bio-chemical elements.
 -----
 Presents an indexed list of bio-chemical elements of type (or derived from
 type) 'Element'. Due to indexed structure 'Alphabet' can be used similar
 to std::vector, for example to add a new element to 'Alphabet' function
 push_back(element_type) can be used. Elements or their properties (such
 as element's mass) can be accessed by index in a constant time. On the other
 hand accessing elements by their names takes linear time. Due to this and
 also the fact that 'Alphabet' is 'heavy-weighted' (consisting of
 'Element' -s or their derivatives where the depth of derivation as well is
 undefined resulting in possibly 'heavy' access operations) it is recommended
 not use 'Alphabet' directly in operations where fast access to
 'Element' 's properties is required. Instead consider to use
 'light-weighted' equivalents, such as 'Weights'
 -----
 :param map: MSExperiment to receive the identifications
 :param fmap: FeatureMap with PeptideIdentifications for the MSExperiment
 :param clear_ids: Reset peptide and protein identifications of each scan before annotating
 :param map_ms1: Attach Ids to MS1 spectra using RT mapping only (without precursor, without m/z)




.. py:method:: IMSAlphabet.clear


Cython signature: void clear()
Clears the alphabet data




.. py:method:: IMSAlphabet.erase


Cython signature: bool erase(libcpp_string & name)
Removes the element with 'name' from the alphabet




.. py:method:: IMSAlphabet.getAverageMasses


Cython signature: libcpp_vector[double] getAverageMasses()
Gets average masses of elements




.. py:method:: IMSAlphabet.getElement


- Cython signature: IMSElement getElement(libcpp_string & name)
  Gets the element with 'index' and returns element with the given index in alphabet


- Cython signature: IMSElement getElement(int index)
  Gets the element with 'index'




.. py:method:: IMSAlphabet.getMass


- Cython signature: double getMass(libcpp_string & name)
  Gets mono isotopic mass of the element with the symbol 'name'
- Cython signature: double getMass(int index)
  Gets mass of the element with an 'index' in alphabet




.. py:method:: IMSAlphabet.getMasses


Cython signature: libcpp_vector[double] getMasses(int isotope_index)
Gets masses of elements isotopes given by 'isotope_index'




.. py:method:: IMSAlphabet.getName


Cython signature: libcpp_string getName(int index)
Gets the symbol of the element with an 'index' in alphabet




.. py:method:: IMSAlphabet.hasName


Cython signature: bool hasName(libcpp_string & name)
Returns true if there is an element with symbol 'name' in the alphabet, false - otherwise




.. py:method:: IMSAlphabet.load


Cython signature: void load(String & fname)
Loads the alphabet data from the file 'fname' using the default parser. If there is no file 'fname', throws an 'IOException'




.. py:method:: IMSAlphabet.push_back


- Cython signature: void push_back(libcpp_string & name, double value)
  Adds a new element with 'name' and mass 'value'


- Cython signature: void push_back(IMSElement & element)
  Adds a new 'element' to the alphabet




.. py:method:: IMSAlphabet.setElement


Cython signature: void setElement(libcpp_string & name, double mass, bool forced)
Overwrites an element in the alphabet with the 'name' with a new element constructed from the given 'name' and 'mass'




.. py:method:: IMSAlphabet.size


Cython signature: int size()




.. py:method:: IMSAlphabet.sortByNames


Cython signature: void sortByNames()
Sorts the alphabet by names




.. py:method:: IMSAlphabet.sortByValues


Cython signature: void sortByValues()
Sorts the alphabet by mass values




