import requests
from bs4 import BeautifulSoup

login_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login_check.php'
home_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/home.php'

question = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/question.php'

question_page = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id=1&value='
evaluation_url = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/code.evaluate.elab.php'

get_code = 'http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php'

payload = {
	'uname': 'RA1611003010***',
	'pass': 'password'
}

with requests.Session() as s:

	#log in with given creds
	login = s.post(login_page, data=payload)

	#navigate to the homepage
	get_home_page = s.get(home_page)

	#print(get_home_page.text)

	questionp = s.get(question)

	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/home.helper.php', data={'text': 'JAVA'})
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/question.php')

	#print(questionp.text)
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/question.list.js')

	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/course.get.php')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/course.get.php')

	#print(w.text)

	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id=1&value=0')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/Code-mirror/lib/codemirror.js')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/Code-mirror/mode/clike/clike.js')
	s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/code.elab.js')
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
	s.post('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/flag.checker.php')



	g = s.get('http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/code.get.php')
	print(g.text)

	'''for i in range(0, 5):
		present_question = question_page + str(i)

		print(present_question)

		goto_question = s.get(present_question)

		print(goto_question.text)

		got_code = s.get(get_code)

		print(got_code.text)


		
		#print(soup.prettify())
		#s.post(evaluation_url, data=)'''
