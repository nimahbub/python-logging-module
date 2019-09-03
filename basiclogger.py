"""
A basic small program where i used logging module to track and record all the events happening in this program when it runs.

"""
#import logging module
import logging 
#configure the logging
logging.basicConfig(filename='testFile.log',
	format='%(asctime)s - %(name)s -%(levelname)s - %(message)s - ',level=logging.INFO)


def addition(a,b):
	return a+b
def checkEvenNumber(number):
	if (number % 2) ==0:
		return True 
	else:
		return False 
logging.info('we are calling our addition function')
temp=addition(12,78)
print(temp)
logging.info('addition function executed ,task completed')
logging.info('we are calling our checkEvenNumber function')
temp=checkEvenNumber(4)
print(temp)
logging.info('checkEvenNumber function is executed ,task completed')

