from app import app
from db_setup import init_db, db_session
from forms import BookSearchForm, BiographyForm
from flask import flash, render_template, request, redirect
from models import Biography, Academic
from tables import Results

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    search = BookSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Academic':
            qry = db_session.query(Biography, Academic).filter(
                Academic.id == Biography.academics_id).filter(
					Academic.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Biography':
            qry = db_session.query(Biography).filter(
                Biography.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Publisher':
            qry = db_session.query(Biography).filter(
                Biography.publisher.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Biography)
            results = qry.all()
    else:
        qry = db_session.query(Biography)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_book', methods=['GET', 'POST'])
def new_Biography():
    """
    Add a new Biography
    """
    form = BiographyForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the Biography
        biography = Biography()
        save_changes(biography, form, new=True)
        flash('Book created successfully!')
        return redirect('/')
    return render_template('new_book.html', form=form)


def save_changes(biography, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    academics = Academic()
    academics.name = form.academics.data

    biography.academics = academics
    biography.title = form.title.data
    biography.release_date = form.release_date.data
    biography.publisher = form.publisher.data
    biography.media_type = form.media_type.data

    if new:
        # Add the new Biography to the database
        db_session.add(biography)

    # commit the data to the database
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Biography).filter(
        Biography.id == id)
    Biography = qry.first()

    if Biography:
        form = BiographyForm(formdata=request.form, obj=biography)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(biography, form)
            flash('Book updated successfully!')
            return redirect('/')
        return render_template('edit_book.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Biography).filter(
        Biography.id == id)
    biography = qry.first()

    if biography:
        form = BiographyForm(formdata=request.form, obj=biography)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(biography)
            db_session.commit()

            flash('Book deleted successfully!')
            return redirect('/')
        return render_template('delete_book.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


if __name__ == '__main__':
    app.run()
