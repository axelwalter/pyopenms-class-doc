IDRipper
========

.. py:class:: IDRipper


   Bases: :py:class:`object`


Cython implementation of _IDRipper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::IDRipper_1_1IDRipper.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: IDRipper.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: IDRipper.getName


Cython signature: String getName()
Returns the name




.. py:method:: IDRipper.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: IDRipper.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: IDRipper.rip


Cython signature: void rip(libcpp_vector[RipFileIdentifier] & rfis, libcpp_vector[RipFileContent] & rfcs, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides, bool full_split, bool split_ident_runs)




.. py:method:: IDRipper.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: IDRipper.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




