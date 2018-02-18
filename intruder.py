import requests
from bs4 import BeautifulSoup

login_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login_check.php'
home_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/home.php'

payload = {
	'uname': 'RA1611003010672',
	'pass': '**'
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



	g = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
	print(g.text)

	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id=1&value=1')
	x = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
	print(x.text)

	'''for i in range(0, 5):
		present_question = question_page + str(i)

		print(present_question)

		goto_question = s.get(present_question)

		print(goto_question.text)

		got_code = s.get(get_code)

		print(got_code.text)


		
		#print(soup.prettify())
		#s.post(evaluation_url, data=)'''
