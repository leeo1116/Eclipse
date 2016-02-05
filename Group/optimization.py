"""
Maximize the minimum value*score that can be inserted

Schedule for area 1:

--------  ########	   -----      ^^^^^^^
+++++    !!!!!  ~~~~~    #####@@@@@@@@@@@
&&&&&&&&&			*********************
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ... N

1. Max value*score
Insert from area with higher value to lower value

2. Find room to insert
time 1 --> N:
	insert_start = time
	insert_end = insert_start
	if content length <= 2 and no conflict content
		insert_end += 1
if insert_end - insert_start >= duration
	candidate_insert_slots.append(insert_start)

3. Calculate total value*score and find the minimum
for candidate_insert_start in candidate_insert_slots:
	for time in range(candidate_insert_start, candidate_insert_start+duration)
		calculate total average value*score
	save total average value*score

find minimum total average value*score

4. Insert
		
"""