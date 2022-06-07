class Postcode:
    def __init__(self, dict):
        self.postcode = dict['postocde']
        self.country = dict['country']
        self.region = dict['region']
        self.admin_district = dict['admin_district']
        self.parish = dict['parish']



# The Postcode object will be initialised by passing in a dictionary.