# Meeting Minutes**Meeting Information**

|     |     |
| --- | --- |
| Date: | The year of our Lord: 2/9/26 |
| Time: | 2:30 PM |
| Location: | AIEB Study Room |
| Meeting Called By: | Team Consensus |
| Note Taker: | Nolan Magee |

# **Attendees**Jack Bender, Jackson Taylor, Kenneth Creamer, Blake Hudson, Nolan Magee, Owen O’Connor

**Discussion**

Meeting with Owen

- Questions for Owen
    - Multithreading
- Caught Owen up on where we were at as a team
- Maybe including a heat sink for thermal optimization
- We may not need vents
    - Went through thermal load of ABS enclosure
    - \-10 to 40 C
- Multithreading vs pinging
    - Have one thread to process data and store in array and one thread ping the sensor (works either way we go with it)
    - Have something to wait at the end of the while loop
    - Probably only need one thread. Since we’re saving the data to the drive, we can have a 1 minute buffer to write to the file every time it iterates
    - 2 distinct programs on pi
- Questions about the PCB
    - Everything is solderable with a normal solder but becomes easier with more advanced equipment

# **Decisions**

1.  Submit BOM by Wednesday

# **Next Meeting**

Date: 2/18/26  
Time: 2:30 PM  
Location: AIEB Study Room
