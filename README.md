# ddcc
Driver and rider fatalities in reported collisions: percentage over the legal blood alcohol limit by vehicle type and driver age: GB

ddcc
This dataset was successfully built.

Assuming that RAS2032: Driver and rider fatalities in reported collisions: percentage over the legal blood alcohol limit by vehicle type and driver age: GB [notes 1,2] is the correct dataset, then the following observations can be made.

The source document has two notes, which are relevant to the data and must be included in the metadata. These notes were:

On 5 December 2014 the limit in Scotland was reduced to 50 milligrams of alcohol per 100 millilitres of blood. It remains at 80 milligrams of alcohol per 100 millilitres of blood in England and Wales.
Excludes accidents involving only pedal cyclists or horse riders.
Both notes one and two were attached to the dataset title, which means it would be appropriate to add it to the description of the dataset as they establish scope. This was not done, thus omitting critical context for the interpretation of these data. (describe)
The dataset has a single measure, the percentage of driver and rider fatalities in reported collisions over the legal blood alcohol limit, whereas five measures were created (component id). This also omits critical data as the five measures are effectively another dimension, the age of reported fatalities. This dataset should have been converted to standard shape (component separation, transform).
This dataset is calendar years not goverment years. (describe)
The observation values are identified as numbers whereas the source material identifies them as percentages, the population being segmented was not defined in the CSV-W. (describe)
The UK uses DWI (Driving While Intoxicated) as the term for drink driving, not DUI (Driving Under the Influence) which is American for keywords. (describe)
Why is the Total column relabelled as "Licensed"? This is inaccurate and misleading. (describe)
