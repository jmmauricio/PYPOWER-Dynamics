#!python3
#
# Copyright (C) 2014 Julius Susanto
#
# PYPOWER-Dynamics is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# PYPOWER-Dynamics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PYPOWER-Dynamics. If not, see <http://www.gnu.org/licenses/>.

"""
PYPOWER-Dynamics
Recorder Class
Sets up and manages the recording of signals and variables during the simulation
"""

class recorder:
    def __init__(self, filename):
        self.recordset = []
        self.record = {}
        self.t_axis = []         
        
        self.parser(filename)
        
        for line in self.recordset:
            self.record[line[0]] = []   
            
    def parser(self, filename):
        """
        Parse a recorder file (*.rcd) and populate recordset list
        """
        f = open(filename, 'r')
        
        for line in f:
            if line[0] != '#' and line.strip() != '':   # Ignore comments and blank lines
                tokens = line.strip().split(',')
                self.recordset.append([tokens[0].strip(), tokens[1].strip(), tokens[2].strip()])
                
        f.close()
    
    def record_variables(self, t, elements):
        """
        Records variables during a simulation
        """
        self.t_axis.append(t)
        
        for line in self.recordset:
            self.record[line[0]].append(elements[line[1]].signals[line[2]])
    
    def write_output(self, filename=None):
        """
        Write recorded variables to file
        (This method could be written in a more pythonic way...)
        """
        if filename != None:
            header = 'time'
            for line in self.recordset:
                header = header + ',' + line[0]
            
            f = open(filename, 'w')
            f.write(header + '\n')
            
            for i in range(len(self.t_axis)):
                newline = str(self.t_axis[i])
                for line in self.recordset:
                    newline = newline + ',' + str(self.record[line[0]][i])
                
                f.write(newline + '\n')
                
            f.close()
        else:
            print('No output file selected...')