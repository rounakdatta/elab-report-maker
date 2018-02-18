import requests
from bs4 import BeautifulSoup
import os
import img2pdf

login_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login_check.php'
home_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/home.php'
quesion_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id=1&value='

payload = {
	'uname': 'RA1611003010672',
	'pass': '***'
}

with requests.Session() as s:

	# login page

	s.post(login_page, data=payload)


	# home page

	s.get(home_page)


	# question page requests & responses

	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/question.php')
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/home.helper.php', data={'text': 'JAVA'})
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/question.php')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/question.list.js')
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/course.get.php', data={'q': 'SESSION'})
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/course.get.php', data={'q': 'VALUES'})


	# individual question -> code page

	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id=1&value=0')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/Code-mirror/lib/codemirror.js')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/Code-mirror/mode/clike/clike.js')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/code.elab.js')
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/flag.checker.php')

	# get the code

	'''g = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
	print(g.text)

	n = s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/code.evaluate.elab.php', data={'code': g.text, 'input': ''})

	complete_percent = n.text[-4:-1]

	if(complete_percent == '100'):

		file = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/getReport.php')

		with open('report', 'wb') as f:
			f.write(file.content)'''

	for i in range(0, 5):

		present_question = quesion_page + str(i)
		s.get(present_question)
		code = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
		evaluate_payload = s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/code.evaluate.elab.php', data={'code': code.text, 'input': ''})

		complete_percent = evaluate_payload.text[-4:-1]

		if(complete_percent == '100'):

			file = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/getReport.php')

			with open(str(i), 'wb') as f:
				f.write(file.content)

	#with open("output.pdf", "wb") as f:
	#	f.write(img2pdf.convert([i for i in os.listdir('./maja') if i.endswith('.PNG')]))
