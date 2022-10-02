#import alternative sessions module from flask import session

# Variables
site_title = 'huclu'

# functions
def nav_render(request, data = {}):
	session = request.session
	user = ''
	logged_in_links = ''
	login_logout = ''
	user_name = ''
	account_dropdown = ''
	search_string = ''
	# display Dash and Images links
	if 'user' in session:
		user = session['user']
		logged_in_links = ''\
							'<li class="nav-item mx-4">'\
								'<a class="nav-link" href="/">'\
									'Home'\
								'</a>'\
							'</li>'\
							'<li class="nav-item mx-4">'\
								'<a class="nav-link" href="/">'\
									'TV'\
								'</a>'\
							'</li>'\
							'<li class="nav-item mx-4">'\
								'<a class="nav-link" href="/">'\
									'Movies'\
								'</a>'\
							'</li>'\
							'<li class="nav-item mx-4">'\
								'<a class="nav-link" href="/">'\
									'News'\
								'</a>'\
							'</li>'\
							'<li class="nav-item mx-4">'\
								'<a class="nav-link" href="/">'\
									'My Stuff'\
								'</a>'\
							'</li>'\
							'<li class="nav-item mx-4">'\
								'<a class="nav-link" href="/">'\
									'Hubs'\
								'</a>'\
							'</li>'\
							
							
		login_logout = ''
		email = user['email']
		account_dropdown = ''\
			'<div class="dropdown">'\
				'<a class="dropdown-toggle_vii" type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">'\
					f'{user["first_name"][0:2].upper()}'\
				'</a>'\
				'<ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="dropdownMenuButton2">'\
					'<li><a class="dropdown-item" href="#">Account</a></li>'\
					'<li><a class="dropdown-item" href="#">Help Center</a></li>'\
					'<li><a class="dropdown-item" href="/logout">Logout</a></li>'\
					'<li><hr class="dropdown-divider"></li>'\
					f'<li><p class="dropdown-item">{email}</p></li>'\
				'</ul>'\
			'</div>'

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
						'<!-- Nav links that show up when logged in as a user -->'\
						f'{logged_in_links}'\
						'<li class="nav-item">'\
							f'{login_logout}'\
						'</li>'\
					'</ul>'\
				'</div>'\
				'<div class="account">'\
					f'{account_dropdown}'\
				'</div>'\
			'</div>'\
		'</nav>'
	return nav
