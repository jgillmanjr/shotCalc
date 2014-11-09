"""
A grotesquely oversimplified shot calculator.
It's more of an exercise.
"""
class projectile():
	""" A projectile object """
	def __init__(self, muzzleVel, cDrag, atmosphere, referenceArea):
		"""
		* muzzleVel: The velocity of the round as it leaves the barrel in m/s.
		* cDrag: Drag coefficient
		* atmosphere: An atmosphere object
		* referenceArea: The reference area in mm^2
		"""
		self.muzzleVel		= muzzleVel
		self.cDrag			= cDrag
		self.atmosphere		= atmosphere
		self.referenceArea	= referenceArea / 1000000 # Convert to Sq. Meters

	def getDrag(self, velocity):
		"""
		* velocity: In m/s
		"""
		density = self.atmosphere.density
		dragForce = .5*(density*(velocity**2)*self.cDrag*self.referenceArea)
		return dragForce
		
class atmosphere():
	""" Dry Air """
	def __baroPa(self, baro):
		""" inHg to Pa """
		return baro * 3386

	def __tempK(self, temp):
		""" *F to *K """
		return ((temp - 32)/1.8) + 273.15

	def __density(self, baro, temp, gasConstant):
		""" Pass in SI units for the above """
		return baro/(temp * gasConstant) # Result will be in kg/m^3

	def __init__(self, baro, temp):
		"""
		* baro: Atmospheric pressure in inHg
		* temp: Temperature in *F
		"""
		self.baro			= self.__baroPa(baro) # inHg to Pascal conversion
		self.temp			= self.__tempK(temp) # Farenheit to Kelvin conversion
		self.gasConstant	= 287.058 # For dry air
		self.density		= self.__density(self.baro, self.temp, self.gasConstant)
