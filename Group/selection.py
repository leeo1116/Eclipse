"""
value_area_pairs = [(value1, area1), (value2, area2), (value3, area3), (value4, area4), (value5, area5), (value6, area6)]

area_schedule_dict = {
						area_1: [(score1, content1), (score2, content2), (score3, content3)]
						...
						area_6: [(score16 content16), (score14, content14), (score18, content18)]
					 }
					 
score_content_pairs = area_schedule_dict[area_i]

optimized_area_content_dict = {area1: content1, area2: content3, ...}
"""
from heapq import heapify, heappop


class selection(object):
	def __init__(self):
		self.value_area_pairs = []
		self.area_schedule_dict = {}
		self.optimized_area_content_dict = {}
		
		
	def add_to_value_area_pairs(self, area_schedule):
		value_area_pair = (location_value_dict[area_schedule.locationID], area_schedule.locationID)
		if value_area_pair not in self.value_area_pairs:
			self.value_area_pairs.append(value_area_pair)
	
	
	def add_to_value_schedule_dict(self, area_schedule):
		if area_schedule.locationID not in self.area_schedule_dict.keys():
			self.area_schedule_dict[area_schedule.locationID] = []
		content_list = self.area_schedule_dict[area_schedule.locationID]
		score_content_pair = (content_score_dict[area_schedule.contentID], area_schedule.contentID)
		content_list.append(score_content_pair)
		self.area_schedule_dict[area_schedule.locationID] = content_list
		
		
	def select(self, schedule_request_in, time, schedule_request_out):
		while schedule_request_in.hasNext():
			area_schedule = schedule_request_in.next
			self.add_to_value_area_pairs(area_schedule)
			self.add_to_area_schedule_dict(area_schedule)
		
		heapify(self.value_area_pairs)
		self.value_area_pairs = self.value_area_pairs[::-1]
		
		while self.value_area_pairs:
			value_area_pair = heappop(self.value_area_pairs)
			content_list = self.area_schedule_dict[value_area_pair[1]]
			
			heapify(content_list)
			content_list = content_list[::-1]
			
			while content_list:
				score_content_pair = heappop(content_list)
				if score_content_pair[1] in self.optimized_area_content_dict.values():
					continue
				else:
					self.optimized_area_content_dict[value_area_pair[1]] = score_content_pair[1]
			if value_area_pair[1] not in self.optimized_area_content_dict.keys():
				self.optimized_area_content_dict[value_area_pair[1]] = None
			
		sum = 0
		for area, content in self.optimized_area_content_dict.items():
			sum += location_value_dict[area]*content_score_dict[content]
		return sum
		