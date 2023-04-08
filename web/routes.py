from flask import Flask,make_response, render_template, url_for,flash, session, request, redirect, Response, jsonify, json
import bcrypt
from flask import *
from sqlalchemy import func
from flask_mysqldb import MySQLdb
from web import app, mysql, mail, db
import uuid
from flask_mail import Message, Mail
import pdfkit
from qr import qrgen
import os



class User(db.Model):
    __tablename__ = 'users'
    id_users = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    token = db.Column(db.String(255))
    level = db.Column(db.String(255))

    def __init__(self,email,password,level):
        self.email = email
        if password != '':
            self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.level = level

class Jenis_Karyawan(db.Model):
    __tablename__ = 'jenis_karyawan'
    id_jenis_karyawan = db.Column(db.Integer, primary_key=True)
    jeniskaryawan = db.Column(db.String(100))
    karyawans = db.relationship('Karyawan', backref=db.backref('jenis_karyawan', lazy = True))

    def __init__(self,id_jenis_karyawan,jenis_karyawan):
        self.id_jenis_karyawan = id_jenis_karyawan
        self.jenis_karyawan =jenis_karyawan

class Karyawan(db.Model):
    __tablename__ = 'karyawan'
    id_karyawan = db.Column(db.String(100), primary_key=True)
    nama_karyawan = db.Column(db.String(100))
    id_jenis_karyawan = db.Column(db.Integer, db.ForeignKey('jenis_karyawan.id_jenis_karyawan'))
    alamat = db.Column(db.String(100))
    no_telp = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, id_karyawan, nama_karyawan, id_jenis_karyawan, alamat, no_telp, email):
        self.id_karyawan = id_karyawan
        self.nama_karyawan = nama_karyawan
        self.id_jenis_karyawan = id_jenis_karyawan
        self.alamat = alamat
        self.no_telp = no_telp
        self.email = email

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id_supplier = db.Column(db.String(100), primary_key=True)
    nama_supplier = db.Column(db.String(100))
    alamat = db.Column(db.String(100))
    no_telp = db.Column(db.String(100))
    email = db.Column(db.String(100))
    penerimaans2 = db.relationship('Penerimaan', backref=db.backref('supplier', lazy = True))

    def __init__(self, id_supplier, nama_supplier, alamat, no_telp, email):
        self.id_supplier = id_supplier
        self.nama_supplier = nama_supplier
        self.alamat = alamat
        self.no_telp = no_telp
        self.email = email

class Jenis_Barang(db.Model):
    __tablename__ = 'jenis_barang'
    id_jenis = db.Column(db.Integer, primary_key=True)
    jenis_barang = db.Column(db.String(100))
    bahan = db.Column(db.String(100))
    barangs = db.relationship('Barang', backref=db.backref('jenis_barang', lazy = True))

    def __init__(self,id_jenis,jenis_barang,bahan):
        self.id_jenis = id_jenis
        self.jenis_barang =jenis_barang
        self.bahan = bahan

class Barang(db.Model):
    __tablename__ = 'barang'
    id_barang = db.Column(db.String(50), primary_key=True)
    nama_barang = db.Column(db.String(100))
    stok = db.Column(db.Integer)
    keterangan = db.Column(db.Text)
    id_jenis = db.Column(db.Integer, db.ForeignKey('jenis_barang.id_jenis'))
    penerimaans = db.relationship('Penerimaan', backref=db.backref('barang', lazy = True))
    pembukuans = db.relationship('Pembukuan', backref=db.backref('barang', lazy = True))

    def __init__(self, id_barang, nama_barang, stok, keterangan, id_jenis):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.stok = stok
        self.keterangan = keterangan
        self.id_jenis = id_jenis

class Penerimaan(db.Model):
    __tablename__ = 'penerimaan'
    id_terima = db.Column(db.Integer, primary_key=True)
    id_supplier = db.Column(db.String(100), db.ForeignKey('supplier.id_supplier'))
    tgl_terima = db.Column(db.Date)
    id_barang = db.Column(db.String(50), db.ForeignKey('barang.id_barang'))
    jumlah_terima = db.Column(db.Integer)

    def __init__(self, id_terima, id_supplier, tgl_terima, id_barang,jumlah_terima):
        self.id_terima = id_terima
        self.id_supplier = id_supplier
        self.tgl_terima = tgl_terima
        self.id_barang = id_barang
        self.jumlah_terima = jumlah_terima

class Pembukuan(db.Model):
    __tablename__ = 'pembukuan'
    id_pembukuan = db.Column(db.Integer, primary_key=True)
    id_barang = db.Column(db.String(50), db.ForeignKey('barang.id_barang'))
    barang_terjual = db.Column(db.Integer)
    harga_jual = db.Column(db.Integer)
    harga_beli = db.Column(db.Integer)
    laba = db.Column(db.Integer)
    tanggal_update = db.Column(db.Date)

    def __init__(self, id_pembukuan, barang_terjual, id_barang, harga_jual, harga_beli, laba, tanggal_update):
        self.id_pembukuan = id_pembukuan
        self.barang_terjual = barang_terjual
        self.id_barang = id_barang
        self.harga_jual = harga_jual
        self.harga_beli = harga_beli
        self.laba = laba
        self.tanggal_update = tanggal_update

with app.app_context():
    db.create_all()


@app.route('/converted',methods = ['POST'])
def convert():
    global tex
    tex = request.form['nama_barang']
    return render_template('donlod.html')

app.config['UPLOAD_FOLDER'] = '../'

@app.route('/download_qr', methods = ['GET'])
def download_qr():
    qrgen(tex)
    filename = tex +'.png'
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'],filename,as_attachment=True))




@app.route('/download')
def download():
    if 'loggedin' in session:
        barang = Barang.query.all()
        data = Pembukuan.query.order_by(Pembukuan.id_pembukuan.desc())

        html = render_template('pdf.html', data = data, barang=barang)
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdf = pdfkit.from_string(html, False, configuration=config)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=laporan.pdf'
        return response

    return render_template('login.html')
     

@app.route('/')
def Index():
    if 'loggedin' in session:
        barang = db.session.query(Barang).count()
        penerimaan = db.session.query(Penerimaan).count()
        laba = db.session.query(func.sum(Pembukuan.harga_jual-Pembukuan.harga_beli)).scalar()
        barangterjual = db.session.query(func.sum(Pembukuan.barang_terjual)).scalar()

        return render_template('index.html', barang = barang, penerimaan=penerimaan, laba=laba, barangterjual=barangterjual)

    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        level = request.form['level']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password,level) VALUES (%s, %s, %s,%s)", (name, email, hash_password,level))
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        session['level'] = level
        return redirect(url_for('Index'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cur.fetchone()
        cur.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
                session['loggedin'] = True
                session['name'] = user['name']
                session['email'] = user['email']
                session['level'] = user['level']
                return render_template('index.html')
            else:
                return "Error Password atau User tidak ditemukan"
    else:
        return render_template('login.html')

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "Rp.{:,.2f}".format(value)

@app.route('/forgot', methods = ['POST', 'GET'])
def forgot():
    if 'login' in session:
        return redirect('/')
    if request.method == 'POST':
        email = request.form['email']
        token = str(uuid.uuid4())
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        if result > 0 :
            data = cur.fetchone()
            msg = Message(subject="Forget password request ", sender="kiravelnote@gmail.com", recipients=[email,])
            msg.body = render_template("sent.html", token=token, data=data)
            mail.send(msg)
            cur = mysql.connection.cursor()
            cur.execute("UPDATE users SET token=%s WHERE email=%s", (token, email,))
            mysql.connection.commit()
            cur.close()
            flash("Email Already Sent To Your Email", "success")
            return redirect('/forgot')
        
        else :
            error = flash("Email do not match", "danger")

    return render_template('forgot.html')

@app.route('/send_email', methods = ['POST', 'GET'])
def send_email():
    if 'login' in session:
        return redirect('/')
    if request.method == 'POST':
            email = request.form['email']
            msg = Message(subject="Register Akun ", sender="kiravelnote@gmail.com", recipients=[email,])
            msg.body = render_template("kirim.html")
            mail.send(msg)
            flash(f"Pesan Telah Dikirim Ke {email}", "success")
            return redirect('/send_email')
        
    return redirect(url_for('VKary'))

@app.route('/reset/<token>', methods = ['POST', 'GET'])
def reset(token):
    if 'login' in session:
        return redirect('/')
    if request.method == 'POST':
        password = request.form['password'].encode('utf-8')
        confirm_password = request.form['confirm_password'].encode('utf-8')
        token1 = str(uuid.uuid4())
        if password != confirm_password:
            flash("Password do not match", "danger")
            return redirect('/reset')
        password = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE token=%s", (token,))
        user = cur.fetchone()
        if user:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE users SET token=%s, password=%s WHERE token=%s", (token1, password, token,))
            mysql.connection.commit()
            cur.close()
            flash("Your password successfully update", "success")
            return redirect('/login')
        else :
            flash("Your token is invalid", "danger")
            return redirect('/')
    return render_template('/reset.html')




@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('level', None)
    return redirect(url_for('Index'))


#supplier
@app.route('/vsup')
def VSup():
    if 'loggedin' in session:
        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Supplier.query.order_by(Supplier.id_supplier.desc()).paginate(page=page, per_page=10)

        return render_template('suplier.html', suplier = data)
    return render_template('login.html')

@app.route('/insertvsup',methods = ['POST'])
def insertvsup():
        if request.method == "POST":
            flash("Data Berhasil Ditambahkan")
            id_supplier = request.form['id_supplier']
            nama_supplier = request.form['nama_supplier']
            alamat = request.form['alamat']
            no_telp = request.form['no_telp']
            email = request.form['email']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO supplier VALUES (%s, %s, %s,%s,%s)", (id_supplier, nama_supplier,alamat,no_telp,email))
            mysql.connection.commit()
            return redirect(url_for('VSup'))

@app.route('/updatevsup', methods = ['POST', 'GET'])
def updatevsup():
    if request.method == 'POST':
        id_supplier = request.form['id_supplier']
        nama_supplier = request.form['nama_supplier']
        alamat = request.form['alamat']
        no_telp = request.form['no_telp']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE supplier 
        SET nama_supplier=%s, alamat=%s, no_telp=%s, email=%s WHERE id_supplier=%s
        """, ( nama_supplier,alamat,no_telp,email,id_supplier))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('VSup'))

@app.route('/deletevsup/<string:id_supplier>', methods = ['POST', 'GET'])
def deletevsup(id_supplier):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM supplier WHERE id_supplier = %s", (id_supplier,))
    mysql.connection.commit()
    return redirect(url_for('VSup'))

#jeniskaryawan
@app.route('/vjenisk')
def VJenisk():
    if 'loggedin' in session:
        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Jenis_Karyawan.query.order_by(Jenis_Karyawan.id_jenis_karyawan.desc()).paginate(page=page, per_page=10)
        return render_template('jeniskaryawan.html', jeniskaryawan = data)
    return render_template('login.html') 

@app.route('/insertvjenisk',methods = ['POST'])
def insertvjenisk():
    if request.method == "POST":
        flash("Data Berhasil Ditambahkan")
        jeniskaryawan = request.form['jeniskaryawan']
        

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO jenis_karyawan(jeniskaryawan) VALUES (%s)", ( jeniskaryawan,))
        mysql.connection.commit()
        return redirect(url_for('VJenisk'))

@app.route('/updatevjenisk', methods = ['POST', 'GET'])
def updatevjenisk():
    if request.method == "POST":
        id_jenis_karyawan = request.form['id_jenis_karyawan']
        jeniskaryawan = request.form['jeniskaryawan']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE jenis_karyawan 
        SET jeniskaryawan=%s WHERE id_jenis_karyawan=%s
        """, ( jeniskaryawan,id_jenis_karyawan))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('VJenisk'))

@app.route('/deletevjenisk/<string:id_jenis_karyawan>', methods = ['POST', 'GET'])
def deletevjenisk(id_jenis_karyawan):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM jenis_karyawan WHERE id_jenis_karyawan = %s", (id_jenis_karyawan,))
    mysql.connection.commit()
    return redirect(url_for('VJenisk'))


    #karyawan
@app.route('/vkary')
def VKary():
    if 'loggedin' in session:
        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Karyawan.query.order_by(Karyawan.id_karyawan.desc()).paginate(page=page, per_page=10)
        data1 = Jenis_Karyawan.query.all()

        return render_template('karyawan.html', karyawan = data, data1= data1)
    return render_template('login.html') 

@app.route('/insertvkary',methods = ['POST'])
def insertvkary():
    if request.method == "POST":
        flash("Data Berhasil Ditambahkan")
        id_karyawan= request.form['id_karyawan']
        nama_karyawan = request.form['nama_karyawan']
        id_jenis_karyawan = request.form['id_jenis_karyawan']
        alamat = request.form['alamat']
        no_telp = request.form['no_telp']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO karyawan VALUES (%s, %s, %s,%s,%s,%s)", (id_karyawan, nama_karyawan,id_jenis_karyawan,alamat,no_telp,email))
        mysql.connection.commit()
        return redirect(url_for('VKary'))

@app.route('/updatevkary', methods = ['POST', 'GET'])
def updatevkary():
    if request.method == "POST":
        id_karyawan = request.form['id_karyawan']
        nama_karyawan = request.form['nama_karyawan']
        id_jenis_karyawan = request.form['id_jenis_karyawan']
        alamat = request.form['alamat']
        no_telp = request.form['no_telp']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE karyawan 
        SET nama_karyawan=%s, id_jenis_karyawan=%s, alamat=%s, no_telp=%s, email=%s WHERE id_karyawan=%s
        """, ( nama_karyawan,id_jenis_karyawan,alamat,no_telp,email,id_karyawan))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('VKary'))

@app.route('/deletevkary/<string:id_karyawan>', methods = ['POST', 'GET'])
def deletevkary(id_karyawan):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM karyawan WHERE id_karyawan = %s", (id_karyawan,))
    mysql.connection.commit()
    return redirect(url_for('VKary'))


#item
@app.route('/vitem')
def VItem():
    if 'loggedin' in session:
        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Barang.query.order_by(Barang.id_barang.desc()).paginate(page=page, per_page=10)
        data1 = Jenis_Barang.query.all()

        return render_template('item.html', item = data, data1 = data1)
    return render_template('login.html') 

@app.route('/insertvitem',methods = ['POST'])
def insertvitem():
    if request.method == "POST":
        flash("Data Berhasil Ditambahkan")
        id_barang = request.form['id_barang']
        nama_barang = request.form['nama_barang']
        stok = request.form['stok']
        keterangan = request.form['keterangan']
        id_jenis = request.form['id_jenis']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO barang VALUES (%s, %s, %s,%s,%s)", (id_barang, nama_barang,stok,keterangan,id_jenis))
        mysql.connection.commit()
        return redirect(url_for('VItem'))

@app.route('/updatevitem', methods = ['POST', 'GET'])
def updatevitem():
    if request.method == 'POST':
        id_barang = request.form['id_barang']
        nama_barang = request.form['nama_barang']
        stok = request.form['stok']
        keterangan = request.form['keterangan']
        id_jenis = request.form['id_jenis']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE barang 
        SET nama_barang=%s,  stok=%s, keterangan=%s, id_jenis=%s WHERE id_barang=%s
        """, (  nama_barang,stok,keterangan,id_jenis,id_barang))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('VItem'))

@app.route('/deletevitem/<string:id_barang>', methods = ['POST', 'GET'])
def deletevitem(id_barang):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM barang WHERE id_barang = %s", (id_barang,))
    mysql.connection.commit()
    return redirect(url_for('VItem'))

    #pembukuan
@app.route('/vpembukuan')
def VPembukuan():
    if 'loggedin' in session:

        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Pembukuan.query.order_by(Pembukuan.id_pembukuan.desc()).paginate(page=page, per_page=10)
        data1 = Barang.query.all()

        return render_template('pembukuan.html', pembukuan = data, data1 = data1)
    return render_template('login.html') 

@app.route('/insertvpembukuan',methods = ['POST'])
def insertvpembukuan():
    if request.method == "POST":
        flash("Data Berhasil Ditambahkan")
        id_barang = request.form['id_barang']
        barang_terjual = request.form['barang_terjual']
        harga_jual = request.form['harga_jual']
        harga_beli = request.form['harga_beli']
        laba = (int(harga_jual)-int(harga_beli))
        tanggal_update = request.form['tanggal_update']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pembukuan(id_barang, barang_terjual, harga_jual, harga_beli, laba, tanggal_update) VALUES ( %s, %s,%s,%s,%s,%s)", ( id_barang,barang_terjual,harga_jual,harga_beli,laba,tanggal_update))
        mysql.connection.commit()
        return redirect(url_for('VPembukuan'))

@app.route('/updatevpembukuan', methods = ['POST', 'GET'])
def updatevpembukuan():
    if request.method == 'POST':
        id_pembukuan = request.form['id_pembukuan']
        id_barang = request.form['id_barang']
        barang_terjual = request.form['barang_terjual']
        harga_jual = request.form['harga_jual']
        harga_beli = request.form['harga_beli']
        laba = (int(harga_jual)-int(harga_beli))
        tanggal_update = request.form['tanggal_update']


        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE pembukuan 
        SET id_barang=%s, barang_terjual=%s, harga_jual=%s, harga_beli=%s, laba=%s, tanggal_update=%s WHERE id_pembukuan=%s
        """, (  id_barang,barang_terjual,harga_jual,harga_beli,laba,tanggal_update,id_pembukuan))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('VPembukuan'))

@app.route('/deletevpembukuan/<string:id_pembukuan>', methods = ['POST', 'GET'])
def deletevpembukuan(id_pembukuan):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pembukuan WHERE id_pembukuan = %s", (id_pembukuan,))
    mysql.connection.commit()
    return redirect(url_for('VPembukuan'))

#jenis barang
@app.route('/vjbarang')
def Vjbarang():
    if 'loggedin' in session:

        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Jenis_Barang.query.order_by(Jenis_Barang.id_jenis.desc()).paginate(page=page, per_page=10)

        return render_template('jenisbarang.html', jenisbarang = data)
    return render_template('login.html')

@app.route('/insertvjbarang',methods = ['POST'])
def insertvjbarang():
    if request.method == "POST":
        flash("Data Berhasil Ditambahkan")
        jenis_barang = request.form['jenis_barang']
        bahan = request.form['bahan']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO jenis_barang(jenis_barang, bahan) VALUES (%s, %s)", (jenis_barang, bahan))
        mysql.connection.commit()
        return redirect(url_for('Vjbarang'))

@app.route('/updatevjbarang', methods = ['POST', 'GET'])
def updatevjbarang():
    if request.method == 'POST':
        id_jenis = request.form['id_jenis']
        jenis_barang = request.form['jenis_barang']
        bahan = request.form['bahan']



        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE jenis_barang 
        SET  jenis_barang=%s, bahan=%s WHERE id_jenis=%s
        """, (  jenis_barang,bahan,id_jenis))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('Vjbarang'))

@app.route('/deletevjbarang/<string:id_jenis>', methods = ['POST', 'GET'])
def deletevjbarang(id_jenis):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM jenis_barang WHERE id_jenis = %s", (id_jenis,))
    mysql.connection.commit()
    return redirect(url_for('Vjbarang'))

#users
@app.route('/users')
def users():
    if 'loggedin' in session:

        data = User.query.all()

        return render_template('users.html', users = data)
    return render_template('login.html')

#penerimaan
@app.route('/terima')
def terima():
    if 'loggedin' in session:
        page = request.args.get('page')

        if page and page.isdigit():
            page = int(page)
        else :
            page = 1

        data = Penerimaan.query.order_by(Penerimaan.id_terima.desc()).paginate(page=page, per_page=10)
        data1 = Supplier.query.all()
        data2 = Barang.query.all()

        return render_template('penerimaan.html', terima = data, data1 = data1, data2= data2)
    return render_template('login.html')

@app.route('/insertpenerimaan',methods = ['POST'])
def insertpenerimaan():
    if request.method == "POST":
        flash("Data Berhasil Ditambahkan")
        id_supplier = request.form['id_supplier']
        tgl_terima = request.form['tgl_terima']
        id_barang = request.form['id_barang']
        jumlah_terima = request.form['jumlah_terima']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO penerimaan(id_supplier, tgl_terima, id_barang, jumlah_terima) VALUES (%s, %s, %s, %s)", (id_supplier, tgl_terima, id_barang, jumlah_terima))
        mysql.connection.commit()
        return redirect(url_for('terima'))

@app.route('/updatepenerimaan', methods = ['POST', 'GET'])
def updatepenerimaan():
    if request.method == 'POST':
        id_terima = request.form['id_terima']
        id_supplier = request.form['id_supplier']
        tgl_terima = request.form['tgl_terima']
        id_barang = request.form['id_barang']
        jumlah_terima = request.form['jumlah_terima']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE penerimaan 
        SET  id_supplier=%s, tgl_terima=%s, id_barang=%s, jumlah_terima=%s WHERE id_terima=%s
        """, (  id_supplier,tgl_terima,id_barang,jumlah_terima,id_terima))
        flash("Data Berhasil Diupdate")
        mysql.connection.commit()
        return redirect(url_for('terima'))

@app.route('/deletepenerimaan/<string:id_terima>', methods = ['POST', 'GET'])
def deletepenerimaan(id_terima):

    flash("Data Berhasil Dihapus")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM penerimaan WHERE id_terima = %s", (id_terima,))
    mysql.connection.commit()
    return redirect(url_for('terima'))



