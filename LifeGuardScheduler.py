import math
from random import randint
beaches = ['Civic','Middle', '2 Chair', 'Main', 'Malibu', 'Nassau 2', 'Nassau 5', 'Reef', 'Anchor', 'E.lido', 'Lido', 'W.Lido', 'Surfing Bay', 'Lido West', 'EAB', 'E.EAB', 'Sea Glades']
lifeguards = ['Rodriguez','Mills', 'L Fitzgerald', 'Laibach', 'Hannon', 'Ruddick', 'Pitzer', 'TFlannigann', 'Vurro', 'Harrington', 'Chase', 'Clarkson', 'Digregorio', 'Nicharkwick', 'Riobo', 'Czartoyski', 'Meringolo', 'Brady', 'Barklow', 'Treadwell', 'Flynn', 'Geodecke', 'Murphy', 'Spinella', 'Joyce', 'TFitzgerald', 'Dreidy', 'EMquade', 'Schroeder', 'Mcveigh', 'Harloff', 'Rtreadwell', 'Cdauria', 'Ochs', 'Mriordan', 'Scibelli', 'Shanley', 'Charkowick', 'Kappel', 'Shutkind', 'Tcrafa', 'BCreigh', 'JCrafa', 'Creagh', 'Fitzpatrick', 'Curry', 'KFlannigan', 'Schlicte', 'Aicher', 'Kinneally', 'CCrafa', 'Fahy', 'Mulloolly', 'Zimmerman', 'Marcote', 'Kluss', 'Wiets', 'Duaria', 'PMquade', 'Campbell', 'Ptucker', 'Henderson', 'Lupia', 'Dunn', 'Rainus', 'lark', 'Peers', 'TLark',  'Martinez', 'Scheinburg', 'Rainus', 'Techera', 'Mcglughlin', 'Carr', 'Farrel', 'Bergin', 'Demeo', 'Trebel', 'Vanella', 'Serrao', 'Brown', 'Paoli', 'Dilsner', 'Swanson', 'JBurns', 'Stapleton', 'Correa', 'Formes', 'Hurst', 'BHarrington', 'Marks', 'MByrne', 'Boccio', 'Neuwieth', 'Babel', 'Hooker', 'Orourke', 'Martinsen', 'Leone', 'Wiessburg', 'Compton', 'Mazur', 'Tucker', 'Kerr', 'Dunster', 'Hutchinson', 'TFahy', 'Giordana', 'Hughes', 'Mahony', 'Gallego', 'CoNewby', 'Vitale', 'Shineburg', 'Longo', 'Michelman', 'Henne']
days_off = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

class LifeGuards:
	def __init__(self):
		self.beach = ""
		self.dayAssigned = ""
		self.dayOff = ""

class LifeGuardScheduler:
	counter =0
	maximum = len(lifeguards)-1
	minimum = 0;
	def __init__(self):
		self.lifeguardList = {}
		for lifeguard in lifeguards:
			lf = LifeGuards()
			self.lifeguardList[lifeguard] = lf

	
	def schedule(self):
		lifeguardName = self.randomLifeguards(self.maximum,self.minimum)
		isBeachUpdated = self.assignBeach(lifeguardName)
		if (isBeachUpdated):
			isDayAssignedUpdated = self.assignDay(lifeguardName)
			if(isDayAssignedUpdated):
				isOffDayUpdated = self.assignOffDay(lifeguardName)
				if(isOffDayUpdated):
					self.counter=self.counter+1

		print(self.lifeguardList)
			
		#if(self.counter<self.maximum):
			   #self.schedule()
		#else:
			#print(self.lifeguardList)
		   
	

	
	def randomChoose(self,ma, mi):
		return math.floor(randint(mi,ma))

	def randomLifeguards(self,ma,mi):
				rand = self.randomChoose(ma,mi)
				randName = lifeguards[rand]
				if(self.lifeguardList[randName].beach!="" and self.lifeguardList[randName].dayAssigned!="" and self.lifeguardList[randName].dayOff!=""):
						self.randomLifeguards(ma,mi)
	
				else:
						return randName;
	
	def findUniqueBeach(self,randBeach,ma,mi):
				rand=0
				if(randBeach.find("-Added")!=-1):
						rand = self.randomChoose(ma,mi)
						randBeach = beaches[rand]
						self.findUniqueBeach(randBeach,ma,mi)
	
				else:
						return randBeach;
	
	def assignBeach(self,lifeguardName):
		if(lifeguardName!=None and self.lifeguardList[lifeguardName].beach == ""):
			ma = len(beaches) -1
			mi = 0
			rand = self.randomChoose(ma,mi)
			randBeach = self.findUniqueBeach(beaches[rand],ma,mi)
			if(randBeach!=None):
							self.lifeguardList[lifeguardName].beach = randBeach
							beaches[rand] = randBeach+"-Added"
							return True
	
		else:
			return False
	
	def assignDay(self,lifeguardName):
				if(self.lifeguardList[lifeguardName].beach!="" and self.lifeguardList[lifeguardName].dayAssigned==""):
						ma = len(days_off)-1
						mi=0
						rand = self.randomChoose(ma,mi)
						randDay = days_off[rand]
						self.lifeguardList[lifeguardName].dayAssigned = randDay
						return True
	
				else:
						return False
	

	def assignOffDay(self,lifeguardName):
				if(self.lifeguardList[lifeguardName].beach!="" and self.lifeguardList[lifeguardName].dayAssigned!="" and self.lifeguardList[lifeguardName].dayOff==""):
						ma = len(days_off)-1
						mi=0
						rand = self.randomChoose(ma,mi)
						randOffDay = days_off[rand];
						if(randOffDay==self.lifeguardList[lifeguardName].dayAssigned):
								rand = 0
								randOffDay=days_off[rand]
		
						self.lifeguardList[lifeguardName].dayOff = randOffDay
						return True
	
				else:
						return False
	




ob = LifeGuardScheduler()
ob.schedule()
