from flask import Blueprint, render_template, abort
from cms.admin.models import Type, Content, Setting, User

admin_bp = Blueprint(name='profile', import_name=__name__, url_prefix='/admin', template_folder=r'/Users/kuro/Desktop/pluralsight/PythonFlask-CMSBlueprints/cms/admin/templates')


## Admin Routes
def requested_type(type):
    types = [row.name for row in Type.query.all()]
    return True if type in types else False


@app.route('/admin/', defaults={'type': 'page'})
@app.route('/admin/<type>')
def content(type):
    if requested_type(type):
        content = Content.query.join(Type).filter(Type.name == type)
        return render_template('admin/content.html', type=type, content=content)
    else:
        abort(404)


@app.route('/admin/create/<type>')
def create(type):
    if requested_type(type):
        types = Type.query.all()
        return render_template('admin/content_form.html', title='Create', types=types, type_name=type)
    else:
        abort(404)


@app.route('/admin/users')
def users():
    users = User.query.all()
    return render_template('admin/users.html', title='Users', users=users)


@app.route('/admin/settings')
def settings():
    settings = Setting.query.all()
    return render_template('admin/settings.html', title='Settings', settings=settings)

# !
