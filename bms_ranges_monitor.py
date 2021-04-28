def current_ranges(range_list):
  if validate_input(range_list):
    largest = max(range_list)
    smallest = min(range_list)
    print ('Range'+" , "+ 'Reading')
    print(str(smallest)+"-"+str(largest)+" , "+str(len(range_list)))
    return 'Valid Input'
  return 'Invalid Input'
    
def validate_input(ranges):
    return not(None in ranges)
