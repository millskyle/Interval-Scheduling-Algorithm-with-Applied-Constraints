



class UserPreferences():
   def __init__(self):
      self.semester = "201509"
      self.MaximizeDaysOff = True
      self.PreferredDaysOff = []
      self.PreferTimeOfDay = "Evening" 
      # Options "Morning", "Afternoon", "Evening"
      self.optimumTimeOfDay = "0800"
      # Sets preferred time for Gaussian
      self.preferredCampus = "None"
      #"None" for none, "North" for north, "Downtown" for dt
      self.preferredCRNs = []
      self.preferMinGaps = True
UserPrefs = UserPreferences()
