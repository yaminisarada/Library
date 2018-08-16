from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('Id', show=False)
    academics = Col('Academic')
    title = Col('Title')
    release_date = Col('Release Date')
    publisher = Col('Publisher')
    language = Col('Language')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))