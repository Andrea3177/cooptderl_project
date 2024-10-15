from ast import IfExp
from xml.sax.handler import all_features
from flask import redirect, url_for, render_template, request, session, flash
from flask_login import current_user, UserMixin, login_manager, login_required, login_user, logout_user, LoginManager
from app_package import db_open, app
from .models import associated, doc_id, res_as, users
from main import login_manager, db


# ----------------------------RUTAS PRINCIPALES----------------------------------------------------------------------------

#la primera pagina al abrir 127.00.00.00, para mientras

@app.route('/')
def page1():
   print('2')
   return redirect(url_for('login'))

#login config

@login_manager.user_loader
def load_user(user_id):
     user_data = users.query.filter_by(user_cod = user_id).first()
     if user_data:
         print ('everything okay') 
         return user_data
     pass


@login_manager.request_loader
def load_user_from_request(request):
    user_id = request.cookies.get('user_id')
    if user_id:
        return load_user(user_id)  
    return None



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form['nickname_form']
        passwd = request.form['password_form']
        
        actual_user = users.query.filter_by(nickname= nickname).first()

        if nickname == actual_user.nickname and passwd == actual_user.password_:
         login_user(actual_user)
         session['username'] = actual_user.nickname
         home = session.pop('next', '/')
         return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('loging.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


#home

@app.route('/cooptder/buscar', methods =['POST'])
@login_required
def buscar():
    if request.method == 'POST':
        buscar = request.form['search']
        
        print(buscar)

        db0=db_open()
        cursor = db0.cursor()
        cursor.execute('SELECT * FROM associated WHERE name_ = %s OR lastname = %s', (buscar, buscar))
        buscados= cursor.fetchall()
        db0.close

        print(buscados)

        buscados_html = []
        for option in buscados:
            buscados_html.append(f'<li class="list-group-item">{option[1]} {option[2]}<button class="btn btn-dark" style="float: right;"><i class="fas fa-edit"></i></button></li>')

        print(buscados_html)
    return render_template('base.html', buscados_html = buscados_html)


@app.route('/cooptderl/home', methods=['GET', 'POST'])
@login_required
def home():
    if current_user.is_authenticated:
        # El usuario está autenticado, puedes acceder a sus propiedades
        user_cod = current_user.user_cod
        print(user_cod)
    return render_template('base.html')  # Show the profile page


#registrar nuevo asociado

@app.route('/cooptderl/register', methods=['GET', 'POST'])
@login_required
def register():
    
    db0 = db_open()
    cursor = db0.cursor()
    cursor.execute('SELECT * FROM country')
    pais = cursor.fetchall()

    paises_html = []

    cursor = db0.cursor()
    cursor.execute('SELECT * FROM doc_type')
    doc= cursor.fetchall()
 
    docs_html = [] 
    
    cursor = db0.cursor()
    cursor.execute('SELECT * FROM civil_state')
    civil_state= cursor.fetchall()

    civil_state_html = []
    
    cursor = db0.cursor()
    cursor.execute('SELECT * FROM dept')
    all_depts= cursor.fetchall()

    all_depts_html = []
    
    cursor = db0.cursor()
    cursor.execute('SELECT * FROM muni')
    all_munis= cursor.fetchall()

    all_muni_html = []
    
    cursor = db0.cursor()
    cursor.execute('SELECT * FROM gender')
    all_genders= cursor.fetchall()

    all_genders_html = []
    
    cursor = db0.cursor()
    cursor.execute('SELECT * FROM house_type')
    all_houses_t= cursor.fetchall()

    all_houses_t_html = []

    cursor = db0.cursor()
    cursor.execute('SELECT * FROM distr')
    all_distrs= cursor.fetchall()
    db0.close()
    all_distr_html = []
    

    if request.method == 'GET':
        for option in pais:
            paises_html.append(f'<option value="{option[0]}">{option[1]}</option>')
        for option in doc:
            docs_html.append(f'<option value="{option[0]}">{option[1]}</option>')
        for option in civil_state:
           civil_state_html.append(f'<option value="{option[0]}">{option[1]}</option>')
        for option in all_depts:
            all_depts_html.append(f'<option value="{option[0]}">{option[2]}</option>')
        for option in all_munis:
            all_muni_html.append(f'<option value="{option[0]}">{option[2]}</option>')
        for option in all_distrs:
            all_distr_html.append(f'<option value="{option[0]}">{option[2]}</option>')
        for option in all_genders:
            all_genders_html.append(f'<option value="{option[0]}">{option[1]}</option>')
        for option in all_houses_t:
            all_houses_t_html.append(f'<option value="{option[0]}">{option[1]}</option>')
              
    if request.method == 'POST':
        
        print(current_user.get_id)
        id_user = current_user.get_id()
        
        associated1= associated(id_as = request.form['id'],
                                name_ = request.form['nombres'],
                                lastname = request.form['apellidos'],
                                married_lastname = request.form['cas_apellido'],
                                gender_as = request.form['gender'],
                                birth_country = request.form['paises'], 
                                birth_dept = request.form['depts'], 
                                birth_muni = request.form['muni'], 
                                birth_distr = request.form['distr'], 
                                birthday = request.form['birthday'], 
                                house_type = request.form['tipo_casa'], 
                                time_to_res_months = request.form['time_to_live'], 
                                civil_state = request.form['est_civil'], 
                                dui_profession = request.form['profesion_dui'], 
                                economy_activity = request.form['act_economica'], 
                                email = request.form['email'], 
                                phone_number = request.form['n_phone'], 
                                ISS = request.form['iss'], 
                                NUP = request.form['nup'], 
                                n_people_to_maintance = request.form['n_personas_eco'], 
                                respon_us = id_user, 
                                notes = '', 
                                num_contribuyente = request.form['num_contribuyente'], 
                                cat_contribuyente = request.form['cat_contribuyente'] )
        doc_id_as1 = doc_id(number_id = request.form['num_doc'], 
                            id_as = request.form['id'] , 
                            type_id = request.form['doc_tipo'], 
                            expiration_date = request.form['exp_doc'])
        res_as1 = res_as(id_res = '1', 
                         id_as = request.form['id'], 
                         country_res = request.form['paises_res'], 
                         dept_res = request.form['depts_res'] , 
                         muni_res = request.form['muni_res'], 
                         dist_res = request.form['distr_res'], 
                         adress = request.form['direccion'])

        db.session.add(associated1)
        db.session.add(doc_id_as1) 
        db.session.add(res_as1)
        
        db.session.commit()
        var = 'Registrado exitosamente'
        return redirect(url_for('addnew', var=var))

        print('registered!!')

    return render_template('register.html', paises=paises_html, docs=docs_html, civil_states=civil_state_html, depts=all_depts_html, munis = all_muni_html, distrs = all_distr_html, genders = all_genders_html, houses = all_houses_t_html)


@app.route('/cooptderl/anadir', methods=['GET', 'POST'])
@login_required 
def addnew():
    if request.method == 'GET':
        return render_template('addnew.html')

#avisos

@app.route('/cooptderl/avisos', methods=['GET', 'POST'])
@login_required
def avisos():
    if request.method == 'POST':
        return 'Thank you.'
    return render_template('avisos.html')

# --------------------------------------------------------------------acciones-----------------------------------------------------
# registrar asociado


@app.route('/cooptderl/registrar_as', methods=['GET, POST'])
@login_required
def registrar_as():
    if request.method == 'POST':
        
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        apellido_casada = request.form["cas_apellido"]
        genero = request.form["gender"]
        birthday = request.form["birthday"]
        pais_nacimiento = request.form["paises"]
        dept_nacimiento = request.form["depts"]
        muni_nacimiento = request.form["muni"]
        distr_nacimiento = request.form["distr"]
        tiempo_de_residencia = request.form["time_to_live"]
        id_tipo = request.form['doc_tipo']
        id_ = request.form['num_doc']
        reg_contribuyente = request.form['num_contribuyente']
        cat_contribuyente = request.form['cat_contribuyente']
        act_economica = request.form['act_economica']
        nit = request.form['nit']
        est_civil = request.form['est_civil']
        profession_dui = request.form['profession_dui']
        n_personas_eco = request.form['n_personas_eco']
        email = request.form['email']
        n_phone = request.form['n_phone']
        direccion= request.form['direccion']
        dept_res = request.form["depts_res"]
        muni_res = request.form["muni_res"]
        distr_res = request.form["distr_res"]

        try:
         conn = db_open()
         with conn.cursor() as cursor:
             # Crea un nuevo registro
             sql = "insert into associated (id_as, name_, lastname, married_lastname, gender_as, birth_country, birth_dept, birth_muni, birth_distr, birthday, house_type, time_to_res_months, civil_state, dui_profession, economy_activity, email, phone_number, ISS, NUP, n_people_to_maintance, entry_money, respon_us, notes) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
             

         # Confirma los cambios
             conn.commit()
         print("Registro insertado correctamente")
        finally:
         # Cierra la conexión
         conn.close()
