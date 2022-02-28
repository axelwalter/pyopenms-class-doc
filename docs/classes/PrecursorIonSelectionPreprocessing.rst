PrecursorIonSelectionPreprocessing
==================================

.. py:class:: PrecursorIonSelectionPreprocessing


   Bases: :py:class:`object`


Cython implementation of _PrecursorIonSelectionPreprocessing


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PrecursorIonSelectionPreprocessing.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: PrecursorIonSelectionPreprocessing.dbPreprocessing


         - Cython signature: void dbPreprocessing(String db_path, bool save)


Calculates tryptic peptide masses of a given database and stores masses and peptide sequences
-----
:param db_path: Path to database file (fasta)
:param save: Flag if preprocessing should be stored
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be found
:raises:
  Exception: UnableToCreateFile if preprocessing file can't be written
         - Cython signature: void dbPreprocessing(String db_path, String rt_model_path, String dt_model_path, bool save)


Calculates tryptic peptide masses of a given database and stores masses and peptide sequences
-----
:param db_path: Path to database file (fasta)
:param rt_model_path
:param dt_model_path
:param save: Flag if preprocessing should be stored
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be found
:raises:
  Exception: UnableToCreateFile if preprocessing file can't be written




.. py:method:: PrecursorIonSelectionPreprocessing.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PrecursorIonSelectionPreprocessing.getGaussMu


Cython signature: double getGaussMu()
Returns the Gauss Mu value




.. py:method:: PrecursorIonSelectionPreprocessing.getGaussSigma


Cython signature: double getGaussSigma()
Returns the Gauss Sigma value




.. py:method:: PrecursorIonSelectionPreprocessing.getMasses


Cython signature: libcpp_vector[double] getMasses(String acc)




.. py:method:: PrecursorIonSelectionPreprocessing.getName


Cython signature: String getName()
Returns the name




.. py:method:: PrecursorIonSelectionPreprocessing.getPT


Cython signature: double getPT(String prot_id, size_t peptide_index)
Returns the PT value




.. py:method:: PrecursorIonSelectionPreprocessing.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PrecursorIonSelectionPreprocessing.getRT


Cython signature: double getRT(String prot_id, size_t peptide_index)
Returns the RT value




.. py:method:: PrecursorIonSelectionPreprocessing.getRTProbability


- Cython signature: double getRTProbability(String prot_id, size_t peptide_index, Feature & feature)
- Cython signature: double getRTProbability(double pred_rt, Feature & feature)




.. py:method:: PrecursorIonSelectionPreprocessing.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PrecursorIonSelectionPreprocessing.getWeight


Cython signature: double getWeight(double mass)
Returns the weighted frequency of a mass




.. py:method:: PrecursorIonSelectionPreprocessing.loadPreprocessing


Cython signature: void loadPreprocessing()
Loads tryptic peptide masses of a given database




.. py:method:: PrecursorIonSelectionPreprocessing.setFixedModifications


Cython signature: void setFixedModifications(StringList & modifications)




.. py:method:: PrecursorIonSelectionPreprocessing.setGaussianParameters


Cython signature: void setGaussianParameters(double mu, double sigma)




.. py:method:: PrecursorIonSelectionPreprocessing.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PrecursorIonSelectionPreprocessing.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




