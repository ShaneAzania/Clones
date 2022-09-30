#import alternative sessions module from flask import session

# Variables
site_title = 'huclu'

# functions
def nav_render(request, data = {}):
	'''
	required data
	session_data = {
		'user_id': session["user_id"],
		'user_name': session["user_name"]
	data = {
		'search_string': search_string,
	}
	'''
	session = request.session
	user = ''
	logged_in_links = ''
	login_logout = ''
	user_name = ''
	search_string = ''
	# display Dash and Images links
	if 'user' in session:
		user = session['user']
		logged_in_links = ''\
							'<li class="nav-item">'\
								'<a class="nav-link" href="/user_dash">'\
									'Dash'\
								'</a>'\
							'</li>'\
							'<!li class="nav-item">'\
								f'<a class="nav-link" href="/user_account/{user["id"]}">'\
									'Account'\
								'</a>'\
							'</li>'
							
		login_logout = '<a class="nav-link" href="/logout">Logout</a>'
		user_name = user['email']
	else:
		login_logout = '<a class="nav-link" href="/login_signup">Login</a>'

	if "search_string" in data:
		search_string = data["search_string"]

	nav='<nav class="navbar navbar-expand-lg mb-3">'\
			'<div class="container-fluid">'\
				f'<a class="navbar-brand" href="/">{site_title}</a>'\
				'<button class="navbar-toggler mb-3" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">'\
					'<span class="navbar-toggler-icon"></span>'\
				'</button>'\
				'<div class="collapse navbar-collapse" id="navbarNav">'\
					'<ul class="navbar-nav ms-auto">'\
						'<!-- search  -->'\
						'<!--li class="nav-item me-2">'\
							'<form action="/images_search" method="post">'\
								'<div class="input-group mt-1">'\
									f'<input name="search" type="text" class="form-control" placeholder="Search" value="{search_string}">'\
								'</div>'\
							'</form>'\
						'</li-->'\
						'<li class="nav-item">'\
							'<!--a class="nav-link" href="/">Home</a-->'\
						'</li>'\
						'<!-- Nav links that show up when logged in as a user -->'\
						f'{logged_in_links}'\
						'<li class="nav-item">'\
							f'{login_logout}'\
						'</li>'\
						'<li class="nav-item">'\
							'<p class="nav-link pb-0">'\
								f'{user_name}'\
							'</p>'\
						'</li>'\
					'</ul>'\
				'</div>'\
			'</div>'\
		'</nav>'
	return nav
