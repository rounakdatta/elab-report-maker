import requests
import os
import img2pdf

java1 = {'url': 'http://care.srmuniv.ac.in/ktrcsejava1/', 'code': 'java/java.code.php', 'key': 'java'}
java2 = {'url': 'http://care.srmuniv.ac.in/ktrcsejava2/', 'code': 'java/java.code.php', 'key': 'java'}
ada = {'url': 'http://care.srmuniv.ac.in/ktrcseada/', 'code': 'daa/daa.code.php', 'key': 'daa'}

elab = input()
if(elab == 'java1'):
	elab = java1
elif(elab == 'java2'):
	elab = java2
if(elab == 'ada'):
	elab = ada

login_page = elab['url'] + 'login_check.php'
home_page = elab['url'] + 'login/student/home.php'
question_page = elab['url'] + 'login/student/code/' + elab['code'] + '?id=1&value='

payload = {
	'uname': 'USERNAME',
	'pass': 'PASSWORD'
}

print('eLab Report Generator : ' + payload['uname'])

with requests.Session() as s:

	# login page

	s.post(login_page, data=payload)


	# home page

	s.get(home_page)


	# question page requests & responses

	s.get(elab['url'] + 'login/student/question.php')
	s.post(elab['url'] + 'login/student/home.helper.php', data={'text': elab['key'].upper()})
	s.get(elab['url'] + 'login/student/question.php')
	s.get(elab['url'] + 'login/student/question.list.js')
	s.post(elab['url'] + 'login/student/course.get.php', data={'q': 'SESSION'})
	s.post(elab['url'] + 'login/student/course.get.php', data={'q': 'VALUES'})


	# individual question -> code page

	s.get(elab['url'] + 'login/student/code/' + elab['code'] + '?id=1&value=0')
	s.get(elab['url'] + 'Code-mirror/lib/codemirror.js')
	s.get(elab['url'] + 'Code-mirror/mode/clike/clike.js')
	s.get(elab['url'] + 'login/student/code/' + elab['key'] + '/code.elab.js')
	s.post(elab['url'] + 'login/student/code/code.get.php')
	s.post(elab['url'] + 'login/student/code/flag.checker.php')


	# get the code, evaluate it and download the report (if 100%)

	for i in range(0, 20):

		present_question = question_page + str(i)
		s.get(present_question)
		code = s.get(elab['url'] + 'login/student/code/code.get.php')

		#print(code.text)

		if(code.text != ''):

			if(elab['key'] == 'daa'):
	
					evaluate_payload_c = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'c'})
					evaluate_payload_cpp = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'cpp'})
					evaluate_payload_java = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'java'})
					evaluate_payload_python = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'python'})

					if '100' in [evaluate_payload_c.text[-4:-1], evaluate_payload_cpp.text[-4:-1], evaluate_payload_java.text[-4:-1], evaluate_payload_python.text[-4:-1]]:
						complete_percent = '100'
					else:
						complete_percent = '0'
	
			else:
				evaluate_payload = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': ''})
				complete_percent = evaluate_payload.text[-4:-1]

		

			if(complete_percent == '100'):
	
				print(str(i) + ' : getting report')
				file = s.get(elab['url'] + 'login/student/code/getReport.php')

				with open(str(i) + '.png', 'wb') as f:
					f.write(file.content)
	
			else:
	
				print(str(i) + ' : evaluation error : Couldn\'t get report')

		else:		
			print(str(i) + ' : No code written')


	# put all the images to PDF

	filename = payload['uname'] + '.pdf'
	with open(filename, "wb") as f:
		f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith('.png')]))

	print('PDF file named ' + filename + ' generated')

	# remove the image files

	for i in range(0, 20):
		if(os.path.isfile(str(i) + '.png')):
			os.remove(str(i) + '.png')

	print('Image files cleared')