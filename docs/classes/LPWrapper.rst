LPWrapper
=========

.. py:class:: LPWrapper


   Bases: :py:class:`object`


Cython implementation of _LPWrapper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LPWrapper.html




.. py:attribute:: LPWrapper.LPWrapper_Type


alias of :py:class:`pyopenms.pyopenms_2.__LPWrapper_Type`


.. py:attribute:: LPWrapper.SOLVER


alias of :py:class:`pyopenms.pyopenms_2.__SOLVER`


.. py:attribute:: LPWrapper.Sense


alias of :py:class:`pyopenms.pyopenms_2.__Sense`


.. py:attribute:: LPWrapper.SolverStatus


alias of :py:class:`pyopenms.pyopenms_2.__SolverStatus`


.. py:attribute:: LPWrapper.VariableType


alias of :py:class:`pyopenms.pyopenms_2.__VariableType`


.. py:attribute:: LPWrapper.WriteFormat


alias of :py:class:`pyopenms.pyopenms_2.__WriteFormat`


.. py:method:: LPWrapper.addColumn


- Cython signature: int addColumn()
  Adds an empty column to the LP matrix, returns index


- Cython signature: int addColumn(libcpp_vector[int] column_indices, libcpp_vector[double] column_values, const String & name)
  Adds a column to the LP matrix, returns index


- Cython signature: int addColumn(libcpp_vector[int] & column_indices, libcpp_vector[double] & column_values, const String & name, double lower_bound, double upper_bound, LPWrapper_Type type_)
  Adds a column with boundaries to the LP matrix, returns index




.. py:method:: LPWrapper.addRow


- Cython signature: int addRow(libcpp_vector[int] row_indices, libcpp_vector[double] row_values, const String & name)
  Adds a row to the LP matrix, returns index


- Cython signature: int addRow(libcpp_vector[int] & row_indices, libcpp_vector[double] & row_values, const String & name, double lower_bound, double upper_bound, LPWrapper_Type type_)
  Adds a row with boundaries to the LP matrix, returns index




.. py:method:: LPWrapper.deleteRow


Cython signature: void deleteRow(int index)
Delete index-th row




.. py:method:: LPWrapper.getColumnIndex


Cython signature: int getColumnIndex(const String & name)
Returns index of the column with name




.. py:method:: LPWrapper.getColumnLowerBound


Cython signature: double getColumnLowerBound(int index)
Returns column's lower bound




.. py:method:: LPWrapper.getColumnName


Cython signature: String getColumnName(int index)
Returns name of the index-th column




.. py:method:: LPWrapper.getColumnType


Cython signature: VariableType getColumnType(int index)
Returns column/variable type.




.. py:method:: LPWrapper.getColumnUpperBound


Cython signature: double getColumnUpperBound(int index)
Returns column's upper bound




.. py:method:: LPWrapper.getColumnValue


Cython signature: double getColumnValue(int index)




.. py:method:: LPWrapper.getElement


Cython signature: double getElement(int row_index, int column_index)
Returns the element




.. py:method:: LPWrapper.getMatrixRow


Cython signature: void getMatrixRow(int idx, libcpp_vector[int] & indexes)




.. py:method:: LPWrapper.getNumberOfColumns


Cython signature: int getNumberOfColumns()
Returns number of columns




.. py:method:: LPWrapper.getNumberOfNonZeroEntriesInRow


Cython signature: int getNumberOfNonZeroEntriesInRow(int idx)




.. py:method:: LPWrapper.getNumberOfRows


Cython signature: int getNumberOfRows()
Returns number of rows




.. py:method:: LPWrapper.getObjective


Cython signature: double getObjective(int index)
Returns objective value for column with index




.. py:method:: LPWrapper.getObjectiveSense


Cython signature: Sense getObjectiveSense()
Returns objective sense




.. py:method:: LPWrapper.getObjectiveValue


Cython signature: double getObjectiveValue()




.. py:method:: LPWrapper.getRowIndex


Cython signature: int getRowIndex(const String & name)
Returns index of the row with name




.. py:method:: LPWrapper.getRowLowerBound


Cython signature: double getRowLowerBound(int index)
Returns row's lower bound




.. py:method:: LPWrapper.getRowName


Cython signature: String getRowName(int index)
Sets name of the index-th row




.. py:method:: LPWrapper.getRowUpperBound


Cython signature: double getRowUpperBound(int index)
Returns row's upper bound




.. py:method:: LPWrapper.getSolver


Cython signature: SOLVER getSolver()
Returns currently active solver




.. py:method:: LPWrapper.getStatus


Cython signature: SolverStatus getStatus()


Returns solution status
-----
:returns: status: 1 - undefined, 2 - integer optimal, 3- integer feasible (no optimality proven), 4- no integer feasible solution




.. py:method:: LPWrapper.readProblem


Cython signature: void readProblem(String filename, String format_)


Read LP from file
-----
:param filename: Filename where to store the LP problem
:param format: LP, MPS or GLPK




.. py:method:: LPWrapper.setColumnBounds


Cython signature: void setColumnBounds(int index, double lower_bound, double upper_bound, LPWrapper_Type type_)
Sets column bounds




.. py:method:: LPWrapper.setColumnName


Cython signature: void setColumnName(int index, const String & name)
Sets name of the index-th column




.. py:method:: LPWrapper.setColumnType


Cython signature: void setColumnType(int index, VariableType type_)
Sets column/variable type.




.. py:method:: LPWrapper.setElement


Cython signature: void setElement(int row_index, int column_index, double value)
Sets the element




.. py:method:: LPWrapper.setObjective


Cython signature: void setObjective(int index, double obj_value)
Sets objective value for column with index




.. py:method:: LPWrapper.setObjectiveSense


Cython signature: void setObjectiveSense(Sense sense)
Sets objective direction




.. py:method:: LPWrapper.setRowBounds


Cython signature: void setRowBounds(int index, double lower_bound, double upper_bound, LPWrapper_Type type_)
Sets row bounds




.. py:method:: LPWrapper.setRowName


Cython signature: void setRowName(int index, const String & name)
Sets name of the index-th row




.. py:method:: LPWrapper.solve


Cython signature: int solve(SolverParam & solver_param, size_t verbose_level)


Solve problems, parameters like enabled heuristics can be given via solver_param
-----
The verbose level (0,1,2) determines if the solver prints status messages and internals
-----
:param solver_param: Parameters of the solver introduced by SolverParam
:param verbose_level: Sets verbose level
:returns: solver dependent




.. py:method:: LPWrapper.writeProblem


Cython signature: void writeProblem(const String & filename, WriteFormat format_)


Write LP formulation to a file
-----
:param filename: Output filename, if the filename ends with '.gz' it will be compressed
:param format: MPS-format is supported by GLPK and COIN-OR; LP and GLPK-formats only by GLPK




