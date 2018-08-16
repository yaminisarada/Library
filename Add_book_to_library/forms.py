from wtforms import Form, StringField, SelectField


class BookSearchForm(Form):
    choices = [('Academic', 'Academic'),
               ('Biography', 'Biography'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for Book:', choices=choices)
    search = StringField('')


class BiographyForm(Form):
    languages = [('English', 'English'),
                   ('Telugu', 'Telugu'),
                   ('Hindi', 'Hindi')
                   ]
    academics = StringField('Academic')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    language = SelectField('Language', choices=languages)
