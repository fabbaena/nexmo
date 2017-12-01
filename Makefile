CustomerAnswer.zip:
	${MAKE} -C CustomerAnswer

install: CustomerAnswer.zip
	aws --region us-east-1 lambda update-function-code --function-name CustomerAnswer --zip-file fileb://./CustomerAnswer.zip 

clean:
	rm CustomerAnswer.zip 

