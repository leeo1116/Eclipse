__doc__ = """
Input - ScheduleRequestInputStream: id, location, start_time, end_time, content_score_dict, location_value_dict
Output - Valid schedules and invalid schedules

Criteria 1. each schedule has up to 3 contents at one time
Criteria 2. for any of the schedules, no duplicated contents at the same time

"""


class Scheduling(object):
	"""
	Input:
	ScheduleRequestInputStream = id, location, start_time, end_time, content_score_dict, location_value_dict
	
	Output:
	Output = Valid schedules and invalid schedules
	
	Requirements:
	Criteria 1. each schedule has up to 3 contents at one time
	Criteria 2. for any of the schedules, no duplicated contents at the same time

	Data structure:
	location_schedule_dict = {'area1': {'t1': [c1, c2, c3], 
										't2': [c2, c3],
										't3': [c3, c4, c5],
										...
										'tN': [cN-1, cN]},
							  'area2': {'t1': [c1, c2],
										't2': [c1, c2, c3],
										't3': [c2, c3],
										...
										'tN': [cN-1, cN]
										},
							  'area3': {'t1': [c4, c5],
										't2': [c4, c5, c6],
										't3': [c4, c7],
										...
										'tN': [c8, cN},
							  ...
							  'area6': {'t1': [c1, c2],
										't2': [c1, c2, c3],
										't3': [c2, c3],
										...
										'tN': [cN-1, cN]}
							  }
	"""
	def __init__(self):
		self.location_schedule_dict = {}
	
	
	def check_size(self, area_schedule):
		if area_schedule.locationID in self.location_schedule_dict.keys():
			time_contents_dict = self.location_schedule_dict[area_schedule.locationID]
			for time in range(area_schedule.start_time, area_schedule.end_time+1):
				if time in time_contents_dict.keys():
					if len(time_contents_dict[time]) > 3:
						return False
		return True
			
			
	def check_conflict(self, area_schedule):
		if area_schedule.locationID in self.location_schedule_dict.keys():
			time_contents_dict = self.location_schedule_dict[area_schedule]
			for time in range(area_schedule.start_time, area_schedule.end_time+1):
				if time in time_contents_dict.keys():
					if area_schedule.contentID in time_contents_dict[time]:
						return False
		return True
		
		
	def add_to_dict(self, area_schedule):
		if area_schedule.locationID not in self.location_schedule_dict.keys():
			self.location_schedule_dict[area_schedule.locationID] = {}

		time_contents_dict = self.location_schedule_dict[area_schedule.locationID]
		for time in range(area_schedule.start_time, area_schedule.end_time+1):
			if time not in time_contents_dict.keys():
				time_contents_dict[time] = []
			time_contents_dict[time].append(area_schedule.contentID)
		self.location_schedule_dict[area_schedule.locationID] = time_contents_dict
		
		
	def schedule(self, schedule_request_in, schedule_request_out, schedule_request_reject)
		while schedule_request_in.hasNext():
			area_schedule = schedule_request_in.next()
			# check if contents are less than 3 at the same time
			if self.check_size(area_schedule):
				if self.check_conflict(area_schedule):
					schedule_request_out.write_schedule_request(area_schedule)
					self.add_to_dict(area_schedule)
					continue
			schedule_request_reject.write_schedule_request(area_schedule)
			