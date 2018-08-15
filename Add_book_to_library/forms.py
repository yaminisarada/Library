from wtforms import Form, StringField, SelectField


class BookSearchForm(Form):
    choices = [('Academic', 'Academic'),
               ('Biography', 'Biography'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for Book:', choices=choices)
    search = StringField('')


class BiographyForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    academics = StringField('Academic')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
