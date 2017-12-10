'''
Created by Roman Beya and Malcom McCarthy
Created on 4-12-17
Created for ICS3U
This program is an introduction to structures!!
'''
class Postal_Service():
	def __init__(self, full_name, city, province, address, street, postal_code):
		self.full_name = full_name
		self.city = city
		self.province = province
		self.address = address
		self.street = street
		self.postal_code = postal_code

FULL_NAME = raw_input("Enter your full name: ")
CITY = raw_input("Enter the city in which you reside: ")
PROVINCE = raw_input("Enter the province that you live in: ")
ADDRESS = raw_input("Enter your house/apt that you live at: ")
STREET = raw_input("Enter your street name: ")
POSTAL_CODE = raw_input("Enter your postal code: ")

canada_post = Postal_Service(FULL_NAME, CITY, PROVINCE, ADDRESS, STREET, POSTAL_CODE)

print canada_post.full_name, canada_post.city, canada_post.province, canada_post.address, canada_post.street, canada_post.postal_code
