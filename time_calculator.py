def add_time(start, duration, dayofweek=""): #dayofweek is an optional parameter, to make an optional paramater is as simple as initializing it in the function definition
  daysoftheweek_dict={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
  daysoftheweek_index=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  dayselapsedstr = ""
  dayselapsed = 0
  count=""
  pos1 = start.find(':')
  pos2 = duration.find(':')
  #This could also be done with the partition method
  Hour1 = start[:pos1]
  Minutes1 = start[pos1+1:pos1+3]
  am_or_pm = start[pos1+4:]
  am_or_pmflip = {"AM":"PM", "PM":"AM"}
  Hour2 = duration[:pos2]
  Minutes2 = duration[pos2+1:]
  #Used method find to locate the ':' that separates hours and minutes to operate with them separately
  
  sum1 = int(Hour1) + int(Hour2)
  strsum1 = str(sum1)
  sum2 = int(Minutes1) + int(Minutes2)
  strsum2 = str(sum2)
  if sum2 > 60:
    addhour = sum2 // 60
    sum2 = sum2 % 60
    sum1 = sum1 + addhour
    strsum2 = str(sum2)
  #In the case where minutes exceeds 60, we take the remainder and than add a hours to the calculated amount
  if sum1 >= 24:
    sumhours = sum1%24
    strsum1 = str(sumhours)
#If hours exceed 24 reset the time    
  if sum1 >= 12:
    sumhours = sum1%12
    strsum1 = str(sumhours)
    if sumhours == 0:
      strsum1 = "12"
  #Deal with the am pm format where it is 12:XX and then 1:XX
    changes = sum1 // 12
    parity = changes % 2
    if am_or_pm == "PM":
      sum1 = sum1-12
      count=1
      dayselapsed = sum1//24 + count
      if dayselapsed == 1:
        dayselapsedstr= " (next day)"
      if dayselapsed > 1:
        dayselapsedstr= " (" + str(dayselapsed) + " days later)"
    if am_or_pm == "AM":
      dayselapsed = sum1//24
      if dayselapsed == 1:
        dayselapsedstr= " (next day)"
      if dayselapsed > 1:
        dayselapsedstr= " (" + str(dayselapsed) + " days later)"
    
        
  #This part is for the advancement of days, it will also be used in case the parameter of the actual day of the week is passed. It checks if the actual time is more than 12, if it is and also the start time was pm then it advances a day, if it were to be more than 12 hours it would check if more days had passed, if it was am it wont count the additional day given by those first 12 hours.
    
    am_or_pm = am_or_pmflip[am_or_pm] if parity == 1 else am_or_pm
      
  #Independently of the hour, if you add 12 hours you would change from AM to PM. I used the parity of the number of changes so that AM changes to PM if number of cahnges is odd
  
  if sum2 < 10:
    strsum2 = "0" + str(sum2)
  #If the hour or minutes is something like 0X we need to add the string 0 to it 
  # Returns: 6:10 PM is the format we want
  timestring = strsum1 + ":" + strsum2 + " " + am_or_pm + dayselapsedstr
  
  dayofweek = dayofweek.lower() #Use lower method so that we have format consistency even when it is case insensitive
  if dayofweek != "":
    for day in daysoftheweek_dict.keys():
      if day == dayofweek:
        n = daysoftheweek_dict[day]
        calculated_day = int(n) + dayselapsed
        calculated_day = calculated_day % 7
        currentdaystr = ", " + daysoftheweek_index[calculated_day]
        timestring = strsum1 + ":" + strsum2 + " " + am_or_pm + currentdaystr + dayselapsedstr
#In the case we have got a day of the week, we search for that day in the dictionary, then we get its value, add the number of days elapsed and we use the days of the week index to make the string needed for the format
  
  return timestring
