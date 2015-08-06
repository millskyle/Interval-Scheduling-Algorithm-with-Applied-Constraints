



class UserPreferences():
   def __init__(self):
      self.semester = "201509"
      self.MaximizeDaysOff = True
      self.PreferredDaysOff = [1,2,3,4,5,6,7,8,9,10]
      self.PreferTimeOfDay = "Evening" 
      # Options "Morning", "Afternoon", "Evening"
      self.optimumTimeOfDay = "0800"
      # Sets preferred time for Gaussian
      self.preferredCampus = 0
      #0 for none, 1 for north, 2 for dt
      self.preferOnline = False
      self.preferredCRNs = ["40377",]
UserPrefs = UserPreferences()
