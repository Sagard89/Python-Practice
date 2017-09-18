import glob
import pyttsx
from textblob import TextBlob

class TextToSpeech(object):
	def __init__(self):
		self.engine = pyttsx.init()

	def speak(self,line):
		self.engine.say(line)
		self.engine.runAndWait()

class FileClass(object):        
	def __init__(self,name):
		self.fileName = name
		self.lines = []
		self.overallSentiment = ""

	def updateLines(self,line):
		self.lines.append(line)

	def updateSentiment(self,sentiment):
		self.overallSentiment = sentiment


class FileClient(object):
	textToSpeechObj = TextToSpeech()
	def __init__(self):
		self.fileObjects = []
		try:
			files = glob.glob('*.txt')
			for i,file_name in enumerate(sorted(files)):
				self.fileObjects.append(FileClass(file_name))
				with open(file_name) as f:
					for line in f:
						singleLine = line.strip(' \t\n\r').split(".")
						for sl in singleLine:
							if (sl.strip(' \t\n\r') and len(sl.strip(' \t\n\r'))!=1):
								self.fileObjects[i].updateLines(sl.strip(' \t\n\r'))
				
		except Exception as e:
			print("Error: File reading error ", e)

	
	def get_line_sentiment(self, line):
		analysis = TextBlob(line)
		return analysis.sentiment.polarity

	def calculateFileOverallSentiment(self,fileObj):
		positiveSentiment = 0
		neutralSentiment = 0
		negativeSentiment = 0
		for l in fileObj.lines:
			sentimentPolarity = self.get_line_sentiment(l)
			if sentimentPolarity > 0:
				positiveSentiment = positiveSentiment + 1
			elif sentimentPolarity == 0:
				neutralSentiment = neutralSentiment + 1
			else:
				negativeSentiment = negativeSentiment + 1

		numOflines = len(fileObj.lines)
		positiveSentimentPer = (positiveSentiment * 100)/numOflines
		negativeSentimentPer = (negativeSentiment * 100)/numOflines
		neutralSentimentPer = (neutralSentiment * 100)/numOflines

		print("Positive Sentiments: ", positiveSentimentPer)
		print("Negative Sentiments: ", negativeSentimentPer)
		print("Neutral Sentiments: ", neutralSentimentPer)

		if(positiveSentimentPer > neutralSentimentPer and positiveSentimentPer > negativeSentimentPer):
			fileObj.updateSentiment("positive")
		elif(neutralSentimentPer > positiveSentimentPer and neutralSentimentPer > negativeSentimentPer):
			fileObj.updateSentiment("neutral")
		elif(negativeSentimentPer > positiveSentimentPer and negativeSentimentPer > neutralSentimentPer):
			fileObj.updateSentiment("negative")
		elif(positiveSentimentPer==negativeSentimentPer):
			fileObj.updateSentiment("neutral")
		elif(neutralSentimentPer==negativeSentimentPer):
			fileobj.updateSentiment("negative")
		elif(positiveSentimentPer==neutralSentimentPer):
			fileObj.updateSentiment("positive")
		else:
			fileObj.updateSentiment("Check the function")
		return fileObj

	def set_sentiments(self):
		for f in self.fileObjects:
			t = "Processing for: "+ f.fileName
			self.textToSpeechObj.speak(t)
			print(t)
			f = self.calculateFileOverallSentiment(f)

	def get_sentiments(self):
		for f in self.fileObjects:
			print("Telling for :",f.fileName)
			self.textToSpeechObj.speak("Overall sentiment of the file " + f.fileName + " is "+ f.overallSentiment)
			#for l in f.lines:
				#textToSpeechObj.speak(l)
			print("*****************************************************")
	       

def main():
	
	fileClient = FileClient()
	fileClient.set_sentiments()
	fileClient.get_sentiments()

if __name__ == "__main__":
	# calling main function
	main()
