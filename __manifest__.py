{
	'name': 'Library Management',
	'description': 'Gestisci il catalogo dei libri della biblioteca ed il relativo prestito.',
	'author': 'Amos Di Sabatino',
	'depends': ['base'],
 	'data': [
		 'security/library_security.xml',
		 'security/ir.model.access.csv',
		 'views/library_menu.xml',
		 'views/book_view.xml',
		 'views/book_list_template.xml',
	 ],
	 'application': True,
 }