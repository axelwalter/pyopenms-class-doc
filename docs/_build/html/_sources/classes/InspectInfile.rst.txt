InspectInfile
=============

.. py:class:: InspectInfile


   Bases: :py:class:`object`


Cython implementation of _InspectInfile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1InspectInfile.html




.. py:method:: InspectInfile.getBlind


Cython signature: unsigned int getBlind()
Run inspect in a blind mode




.. py:method:: InspectInfile.getDb


Cython signature: String getDb()
Specifies the name of a database (.trie file) to search




.. py:method:: InspectInfile.getEnzyme


Cython signature: String getEnzyme()
Specifies the name of a enzyme. "Trypsin", "None", and "Chymotrypsin" are the available values




.. py:method:: InspectInfile.getInstrument


Cython signature: String getInstrument()
If set to QTOF, uses a QTOF-derived fragmentation model, and does not attempt to correct the parent mass




.. py:method:: InspectInfile.getMaxPTMsize


Cython signature: float getMaxPTMsize()
The maximum modification size (in Da) to consider in a blind search




.. py:method:: InspectInfile.getModifications




.. py:method:: InspectInfile.getModificationsPerPeptide


Cython signature: int getModificationsPerPeptide()
Number of PTMs permitted in a single peptide




.. py:method:: InspectInfile.getMulticharge


Cython signature: unsigned int getMulticharge()
If set to true, attempt to guess the precursor charge and mass, and consider multiple charge states if feasible




.. py:method:: InspectInfile.getPeakMassTolerance


Cython signature: float getPeakMassTolerance()
How far b and y peaks can be shifted from their expected masses.




.. py:method:: InspectInfile.getPrecursorMassTolerance


Cython signature: float getPrecursorMassTolerance()
Specifies the parent mass tolerance, in Daltons




.. py:method:: InspectInfile.getSpectra


Cython signature: String getSpectra()
Specifies a spectrum file to search




.. py:method:: InspectInfile.getTagCount


Cython signature: int getTagCount()
Number of tags to generate




.. py:method:: InspectInfile.handlePTMs


Cython signature: void handlePTMs(const String & modification_line, const String & modifications_filename, bool monoisotopic)


Retrieves the name, mass change, affected residues, type and position for all modifications from a string
-----
:param modification_line
:param modifications_filename
:param monoisotopic: if true, masses are considered to be monoisotopic
:raises:
  Exception: FileNotReadable if the modifications_filename could not be read
:raises:
  Exception: FileNotFound if modifications_filename could not be found
:raises:
  Exception: ParseError if modifications_filename could not be parsed




.. py:method:: InspectInfile.setBlind


Cython signature: void setBlind(unsigned int blind)
Run inspect in a blind mode




.. py:method:: InspectInfile.setDb


Cython signature: void setDb(const String & db)
Specifies the name of a database (.trie file) to search




.. py:method:: InspectInfile.setEnzyme


Cython signature: void setEnzyme(const String & enzyme)
Specifies the name of a enzyme. "Trypsin", "None", and "Chymotrypsin" are the available values




.. py:method:: InspectInfile.setInstrument


Cython signature: void setInstrument(const String & instrument)
If set to QTOF, uses a QTOF-derived fragmentation model, and does not attempt to correct the parent mass




.. py:method:: InspectInfile.setMaxPTMsize


Cython signature: void setMaxPTMsize(float maxptmsize)
The maximum modification size (in Da) to consider in a blind search




.. py:method:: InspectInfile.setModificationsPerPeptide


Cython signature: void setModificationsPerPeptide(int modifications_per_peptide)
Number of PTMs permitted in a single peptide




.. py:method:: InspectInfile.setMulticharge


Cython signature: void setMulticharge(unsigned int multicharge)
If set to true, attempt to guess the precursor charge and mass, and consider multiple charge states if feasible




.. py:method:: InspectInfile.setPeakMassTolerance


Cython signature: void setPeakMassTolerance(float peak_mass_tolerance)
How far b and y peaks can be shifted from their expected masses




.. py:method:: InspectInfile.setPrecursorMassTolerance


Cython signature: void setPrecursorMassTolerance(float precursor_mass_tolerance)
Specifies the parent mass tolerance, in Daltons




.. py:method:: InspectInfile.setSpectra


Cython signature: void setSpectra(const String & spectra)
Specifies a spectrum file to search




.. py:method:: InspectInfile.setTagCount


Cython signature: void setTagCount(int TagCount)
Number of tags to generate




.. py:method:: InspectInfile.store


Cython signature: void store(const String & filename)
Stores the experiment data in an Inspect input file that can be used as input for Inspect shell execution




