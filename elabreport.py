import requests
import os
import img2pdf

def gen_report(username, password, elabx, level):

	computingskill_c = {'url': 'http://care.srmuniv.ac.in/computingskill/', 'code': 'c/c.code.php', 'key': 'c'}
	computingskill_cpp = {'url': 'http://care.srmuniv.ac.in/computingskill/', 'code': 'cpp/cpp.code.php', 'key': 'CPP'}
	computingskill_java = {'url': 'http://care.srmuniv.ac.in/computingskill/', 'code': 'java/java.code.php', 'key': 'JAVA'}
	computingskill_ds = {'url': 'http://care.srmuniv.ac.in/computingskill/', 'code': 'data-structure/data-structure.code.php', 'key': 'DATA-STRUCTURE'}
	computingskill_ml = {'url': 'http://care.srmuniv.ac.in/computingskill/', 'code': 'mathslab/mathslab.code.php', 'key': 'MATHSLAB'}
	computingskill_py = {'url': 'http://care.srmuniv.ac.in/computingskill/', 'code': 'python/python.code.php', 'key': 'PYTHON'}
	java1 = {'url': 'http://care.srmuniv.ac.in/ktrcsejava1/', 'code': 'java/java.code.php', 'key': 'java'}
	java2 = {'url': 'http://care.srmuniv.ac.in/ktrcsejava2/', 'code': 'java/java.code.php', 'key': 'java'}
	ada = {'url': 'http://care.srmuniv.ac.in/ktrcseada/', 'code': 'daa/daa.code.php', 'key': 'daa'}
	pdd = {'url': 'http://care.srmuniv.ac.in/ktrcsepdd/', 'code': 'c/c.code.php', 'key': 'c'}
	it_ada = {'url': 'http://care1.srmuniv.ac.in/ktritada/', 'code': 'daa/daa.code.php', 'key': 'daa'}
	it_java = {'url': 'http://care1.srmuniv.ac.in/ktritjava/', 'code': 'java/java.code.php', 'key': 'java'}

	if(elabx == 'computingskill_c'):
		elab = computingskill_c
	elif(elabx == 'computingskill_cpp'):
		elab = computingskill_cpp
	elif(elabx == 'computingskill_java'):
		elab = computingskill_java
	elif(elabx == 'computingskill_ds'):
		elab = computingskill_ds
	elif(elabx == 'computingskill_ml'):
		elab = computingskill_ml
	elif(elabx == 'computingskill_py'):
		elab = computingskill_py
	elif(elabx == 'java1'):
		elab = java1
	elif(elabx == 'java2'):
		elab = java2
	elif(elabx == 'ada'):
		elab = ada
	elif(elabx == 'it_java'):
		elab = it_java
	elif(elabx == 'it_ada'):
		elab = it_ada
	elif(elabx == 'pdd'):
		elab = pdd;
	else:
		return
	
	login_page = elab['url'] + 'login_check.php'
	home_page = elab['url'] + 'login/student/home.php'
	question_page = elab['url'] + 'login/student/code/' + elab['code'] + '?id=' + level + '&value='
	
	payload = {
		'uname': username,
		'pass': password
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
	
		s.get(elab['url'] + 'login/student/code/' + elab['code'] + '?id=' + level + '&value=0')
		s.get(elab['url'] + 'Code-mirror/lib/codemirror.js')
		s.get(elab['url'] + 'Code-mirror/mode/clike/clike.js')
		s.get(elab['url'] + 'login/student/code/' + elab['key'] + '/code.elab.js')
		s.post(elab['url'] + 'login/student/code/code.get.php')
		s.post(elab['url'] + 'login/student/code/flag.checker.php')
	
	
		# get the code, evaluate it and download the report (if 100%)
		
		i = 0

		while i < 100:
	
			present_question = question_page + str(i)
			s.get(present_question)

			if(s.get(present_question).text.find('NOT ALLOCATED')==-1):
				code = s.get(elab['url'] + 'login/student/code/code.get.php')			

				if(code.text != ''):
		
					if(elab['key'] == 'daa'):
			
							evaluate_payload_c = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'c'})
							evaluate_payload_cpp = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'cpp'})
							evaluate_payload_java = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'java'})
							evaluate_payload_python = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'python'})
							evaluate_payload_mathslab = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': '', 'language': 'mathslab'})
		
							if '100' in [evaluate_payload_c.text[-4:-1], evaluate_payload_cpp.text[-4:-1], evaluate_payload_java.text[-4:-1], evaluate_payload_python.text[-4:-1], evaluate_payload_mathslab[-4:-1]]:
								complete_percent = '100'
							else:
								complete_percent = '0'
			
					else:
						evaluate_payload = s.post(elab['url'] + 'login/student/code/' + elab['key'] + '/code.evaluate.elab.php', data={'code': code.text, 'input': ''})
						complete_percent = evaluate_payload.text[-4:-1]
		
				
		
					if(complete_percent == '100'):
			
						print(str(i + 1) + ' : getting report')
						file = s.get(elab['url'] + 'login/student/code/getReport.php')
		
						with open(payload['uname'] + '-' + str(i).zfill(3) + '.png', 'wb') as f:
							f.write(file.content)
			
					else:

						if elab['key'] == 'java':

							if evaluate_payload.text.lower().find('score')==-1 and evaluate_payload.text.lower().find('exception')==-1 and evaluate_payload.text.lower()[60:].find('error')==-1:
								print(str(i + 1) + ' : Error... Trying again')
								i-=1;
						
						else:
							print(str(i + 1) + ' : evaluation error : Couldn\'t get report')
		
				else:		
					print(str(i + 1) + ' : No code written')

			else:
				print(str(i + 1) + ' : Question not allocated')

			i+=1


		# put all the images to PDF
	
		filename = payload['uname'] + '-' + elabx.upper() + '-Level-' + level + '.pdf'
		with open(filename, "ab") as f:
			f.write(img2pdf.convert([i for i in sorted(os.listdir('.')) if i.endswith('.png')]))
	
		print('PDF file named ' + filename + ' generated')
	

		# remove the image files
	
		for i in range(0, 100):
			if(os.path.isfile(payload['uname'] + '-' + str(i).zfill(3) + '.png')):
				os.remove(payload['uname'] + '-' + str(i).zfill(3) + '.png')
	
		print('Image files cleared')

		return filename

def gen_report_all(username, password, elabx):

	java1 = {'url': 'http://care.srmuniv.ac.in/ktrcsejava1/', 'code': 'java/java.code.php', 'key': 'java'}
	java2 = {'url': 'http://care.srmuniv.ac.in/ktrcsejava2/', 'code': 'java/java.code.php', 'key': 'java'}
	ada = {'url': 'http://care.srmuniv.ac.in/ktrcseada/', 'code': 'daa/daa.code.php', 'key': 'daa'}
	pdd = {'url': 'http://care.srmuniv.ac.in/ktrcsepdd/', 'code': 'c/c.code.php', 'key': 'c'}
	it_ada = {'url': 'http://care1.srmuniv.ac.in/ktritada/', 'code': 'daa/daa.code.php', 'key': 'daa'}
	it_java = {'url': 'http://care1.srmuniv.ac.in/ktritjava/', 'code': 'java/java.code.php', 'key': 'java'}
	
	if(elabx == 'java1'):
		elab = java1
	elif(elabx == 'java2'):
		elab = java2
	elif(elabx == 'ada'):
		elab = ada
	elif(elabx == 'it_java'):
		elab = it_java
	elif(elabx == 'it_ada'):
		elab = it_ada
	elif(elabx == 'pdd'):
		elab = pdd
	else:
		return
	
	login_page = elab['url'] + 'login_check.php'
	home_page = elab['url'] + 'login/student/home.php'
	
	payload = {
		'uname': username,
		'pass': password
	}
	
	print('eLab Report Generator : ' + payload['uname'])
	
	with requests.Session() as s:
	
		s.post(login_page, data=payload)
		s.post(elab['url'] + 'login/student/home.helper.php', data={'text': elab['key'].upper()})
		s.post(elab['url'] + 'login/student/course.get.php', data={'q': 'SESSION'})
		s.post(elab['url'] + 'login/student/course.get.php', data={'q': 'VALUES'})
		s.post(elab['url'] + 'login/student/code/code.get.php')
		s.post(elab['url'] + 'login/student/code/flag.checker.php')

		for level in range(1, 4):

			question_page = elab['url'] + 'login/student/code/' + elab['code'] + '?id=' + str(level) + '&value='
			print("LEVEL " + str(level))

			i = 0

			while i < 100:
		
				present_question = question_page + str(i)

				if(s.get(present_question).text.find('NOT ALLOCATED')==-1):
					code = s.get(elab['url'] + 'login/student/code/code.get.php')			

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
				
							print(str(i + 1) + ' : getting report')
							file = s.get(elab['url'] + 'login/student/code/getReport.php')
			
							with open(payload['uname'] + '-' + str(i//10) + '-' + str(level) + '-' + str(i).zfill(3) + '.png', 'wb') as f:
								f.write(file.content)
				
						else:

							if elab['key'] == 'java':

								if evaluate_payload.text.lower().find('score')==-1 and evaluate_payload.text.lower().find('exception')==-1 and evaluate_payload.text.lower()[60:].find('error')==-1:
									print(str(i + 1) + ' : Error... Trying again')
									i-=1;
							
							else:
								print(str(i + 1) + ' : evaluation error : Couldn\'t get report')
			
					else:		
						print(str(i + 1) + ' : Please Write the Code')

				else:
					print(str(i + 1) + ' : Question not allocated: Contact CARE')

				i+=1


		# put all the images to PDF
	
		filename = payload['uname'] + '-' + elabx.upper() + '-All-Levels' + '.pdf'
		with open(filename, "ab") as f:
			f.write(img2pdf.convert([i for i in sorted(os.listdir('.')) if i.endswith('.png')]))
	
		print('PDF file named ' + filename + ' generated')
	

		# remove the image files
	
		for level in range(1,4):
			for i in range(0, 100):
				if(os.path.isfile(payload['uname'] + '-' + str(i//10) + '-' + str(level) + '-' + str(i).zfill(3) + '.png')):
					os.remove(payload['uname'] + '-' + str(i//10) + '-' + str(level) + '-' + str(i).zfill(3) + '.png')
					print('Cleared File: '+str(i))
	
		print('Image files cleared')

		return filename
