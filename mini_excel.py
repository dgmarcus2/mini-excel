def read_table(filename, sep=','):
  columns = {}
  rows = []
  #Opens file for reading.
  with open(filename, 'r') as fd:
    #Read & clean first line of file. Create column headers based on data in first line.
    line_1 = fd.readline()
    line_1_cleaned = (line_1).strip().split(',')
    for i in line_1_cleaned:
      columns.setdefault(i, [])
    #Convert columns to list so to iterate.
    spreadsheet = list(columns.items())

    #Read & clean remaining lines of file
    for line in fd:
      line_cleaned = (line.strip().split(','))
      #Append each number in a given line to a list, thereby forming an iterable row.
      for i in line_cleaned:
        rows.append(float(i))
      #For each number in each row...
      for i in rows:
        #For each column in spreadsheet...
        for k in spreadsheet:
          #If the index of the number in the row is the same as the index of the column key in the spreadsheet...
          if (rows.index(i) == spreadsheet.index(k)):
            #Append the number to the values of the spreadsheet key
            k[1].append(i)
      rows = []
    #Convert spreadsheet from list to dictionary
    spreadsheet = dict(spreadsheet)
    #Return spreadsheet
    return spreadsheet

def get_column_values(table, keys):
  return table[keys]

def get_row_values(table, row):
  out = []
  vals = table.values()
  for nums in vals:
    for i in nums:
      if (nums.index(i) == row):
        out.append(i)
  return out

def apply_to_column(table, key, fn):
  found_column = get_column_values(table, key)
  return (fn(found_column))

def apply_to_row(table, row, fn):
  found_row = get_row_values(table, row)
  return (fn(found_row))
