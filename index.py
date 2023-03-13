from flask import Flask, render_template, request, redirect
import cx_Oracle
from datetime import datetime

######## 
port=5000
rootPath = "http://localhost:" + str(port)

#Adaug librariile .dll pentru cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\instantclient_21_8")

app = Flask(__name__)

con = cx_Oracle.connect("bd004", "bd004", "bd-dc.cs.tuiasi.ro:1539/orcl")

voluntari = []
detalii = []
voluntariAlumni = []
departamente = []
roluri = []
evenimente = []
sponsori = [0] * 999
parteneri = []

@app.route("/", methods=['POST', 'GET'])
def selects():
    if request.method == 'GET':
        global voluntari
        global detalii
        global voluntariAlumni 
        global departamente
        global roluri
        global evenimente
        global sponsori
        global parteneri

        voluntari.clear()
        detalii.clear()
        voluntariAlumni.clear()
        departamente.clear()
        roluri.clear()
        evenimente.clear()
        sponsori = [0] * 999
        parteneri.clear()

        aux = con.cursor()

        aux.execute('select * from voluntari order by id_voluntar')
        for result in aux:
            voluntar = {}

            voluntar["id_voluntar"] = result[0]
            voluntar["nume"] = result[1]
            voluntar["data_aderare"] = result[2].strftime("%d-%b-%Y")
            voluntar["id_rol"] = result[3]
            voluntar["id_departament"] = result[4]
            voluntari.append(voluntar)
        aux.close()

        aux = con.cursor()
        for vol in voluntari:
            quer = "select * from detalii_vol where id_voluntar = " + str(vol["id_voluntar"])
            aux.execute(quer)
            for result in aux:
                det = {}

                det["id_voluntar"] = result[0]
                det["numar_telefon"] = result[1]
                det["email"] = result[2]
                det["data_nastere"] = result[3].strftime("%d-%b-%Y")
                detalii.append(det)
        aux.close()

        aux = con.cursor()
        aux.execute('select * from voluntari_alumni order by id_voluntar')
        for result in aux:
            alumni = {}

            alumni["id_voluntar"] = result[0]
            alumni["nume"] = result[1]
            alumni["data_aderare"] = result[2].strftime("%d-%b-%Y")
            alumni["data_alumnizare"] = result[3].strftime("%d-%b-%Y")
            alumni["id_rol"] = result[4]
            alumni["numar_telefon"] = result[5]
            alumni["email"] = result[6]
            alumni["data_nastere"] = result[7].strftime("%d-%b-%Y")
            voluntariAlumni.append(alumni)
        aux.close()

        aux = con.cursor()
        aux.execute('select * from departamente order by id_departament')
        for result in aux:
            dept = {}

            dept["id_departament"] = result[0]
            dept["nume_departament"] = result[1]
            departamente.append(dept)
        aux.close()

        aux = con.cursor()
        aux.execute('select * from roluri order by id_rol')
        for result in aux:
            rol = {}

            rol["id_rol"] = result[0]
            rol["denumire_rol"] = result[1]
            roluri.append(rol)
        aux.close()

        aux = con.cursor()
        aux.execute('select * from evenimente order by id_event')
        for result in aux:
            event = {}

            event["id_event"] = result[0]
            event["nume_event"] = result[1]
            event["data_start"] = result[2].strftime("%d-%b-%Y")
            event["data_stop"] = result[3].strftime("%d-%b-%Y")
            event["locatie"] = result[4]
            event["buget"] = result[5]
            evenimente.append(event)
        aux.close()

        aux = con.cursor()
        for event in evenimente:      
            aux.execute("""select nume_partener 
                        from evenimente, parteneri, parteneri_evenimente
                        where parteneri_evenimente.parteneri_id_partener = parteneri.id_partener
                        and parteneri_evenimente.evenimente_id_event = evenimente.id_event
                        and nume_event = :mybv""", mybv=event["nume_event"])

            names = []
            for result in aux:
                names.append(result[0])
            sponsori[event["id_event"]] = names
        aux.close()

        aux = con.cursor()
        aux.execute('select * from parteneri order by id_partener')
        for result in aux:
            part = {}
            
            part["id_partener"] = result[0]
            part["nume_partener"] = result[1]
            parteneri.append(part)

        aux.close()
        return render_template("index.html",rootPath=rootPath, voluntari=voluntari, detalii=detalii, voluntariAlumni=voluntariAlumni, departamente=departamente, roluri=roluri, evenimente=evenimente, sponsori=sponsori, parteneri=parteneri)
    else:
        id = request.form["selectVol"]
        voluntar = {}
        
        aux = con.cursor()
        aux.execute('select nume, data_aderare from voluntari where id_voluntar in ' + id)
        for result in aux:
            voluntar["nume"] = result[0]
            voluntar["data_aderare"] = result[1].strftime("%d-%b-%Y")

        aux.execute('select numar_telefon, email, data_nastere from detalii_vol where id_voluntar in ' + id)
        for result in aux:
            voluntar["numar_telefon"] = result[0]
            voluntar["email"] = result[1]
            voluntar["data_nastere"] = result[2].strftime("%d-%b-%Y")

        values = [str(id), "'" + voluntar["nume"] + "'", "'" + voluntar["data_aderare"] + "'", 'SYSDATE', '50', "'" + voluntar["numar_telefon"] + "'",
                    "'" + voluntar["email"] + "'", "'" + voluntar["data_nastere"] + "'"]
        aux.execute('INSERT INTO voluntari_alumni values (%s)'%(', '.join(values)))
        con.commit()
        aux.close()

        aux = con.cursor()
        aux.execute('delete detalii_vol where id_voluntar = ' + id)
        aux.execute('delete voluntari where id_voluntar = ' + id)
        con.commit()
        aux.close()
        return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    if request.method == 'POST':
        table = request.form["selectTable"]

        match table:
            case "1":
                name = "'" +  request.form['vol.nume'] + "'"
                aderare = "'" + request.form['vol.aderare'] + "'"
                id_rol = request.form['vol.rol']
                id_dep = request.form['vol.dep']
                telefon = "'" + request.form['vol.telefon'] + "'"
                email = "'" + request.form['vol.email'] + "'"
                nastere = "'" + request.form['vol.nastere'] + "'"

                fields = ['nume', 'data_aderare', 'id_rol', 'id_departament']
                values1 = [name, aderare, str(id_rol), str(id_dep)]

                aux = con.cursor()
                #ADAUG DATELE IN  TABLEA VOLUNTARI
                aux.execute('insert into voluntari (%s) values (%s)' % (', '.join(fields), ', '.join(values1)))
                aux.execute('commit')
                aux.close()

                aux = con.cursor()
                #ADAUG DATELE IN TABELA DETALII_VOL
                values2 = [telefon, email, nastere]
                aux.execute('insert into detalii_vol values ((select id_voluntar from voluntari where nume like %s), %s)' %(name, ', '.join(values2)))
                aux.execute('commit')
                aux.close()
            case "2":
                nume_dep = "'" + request.form['dep.nume'] + "'"
                aux = con.cursor()
                aux.execute('insert into departamente(nume_departament) values (%s)'%(nume_dep))
                aux.execute('commit')
                aux.close()
            case "3":
                nume_rol = "'" + request.form['rol.nume'] + "'"
                aux = con.cursor()
                aux.execute('insert into roluri(denumire_rol) values (%s)'%(nume_rol))
                aux.execute('commit')
                aux.close()
            case "4":
                nume_ev = "'" + request.form['ev.nume'] + "'"
                start = "'" + request.form['ev.start'] + "'"
                stop = "'" + request.form['ev.stop'] + "'"
                locatie = "'" + request.form['ev.locatie'] + "'"

                values = [nume_ev, start, stop, locatie, '0']
                aux = con.cursor()
                aux.execute('insert into evenimente(nume_event, data_start, data_stop, locatie_event, buget_event) values (%s)'%(", ".join(values)))
                aux.execute('commit')
                aux.close()
            case "5":
                nume = "'" + request.form['p.nume'] + "'"
                event = "'" + request.form['p.ev'] + "'"
                buget =request.form['p.bani']

                aux = con.cursor()
                aux.execute('insert into parteneri(nume_partener) values (%s)'%(nume))
                aux.execute('commit')

                aux.execute('select id_partener from parteneri where nume_partener = ' + nume)
                id_p = 0
                for result in aux:
                    id_p = result[0]

                aux.execute('insert into parteneri_evenimente values (%s, %s)'%(id_p, event))
                aux.execute('commit')

                aux.execute('update evenimente set buget_event = buget_event + ' + buget + ' where id_event = ' + event)
                aux.close()
            case _:
                print(table)
        return redirect('/')
    else:
        return render_template("add.html", rootPath=rootPath, roluri=roluri, departamente=departamente, evenimente=evenimente)

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        table = request.form["selectTable"]

        match table:
            case "1":
                id_nume = request.form["vol.nume"]

                aux = con.cursor()
                aux.execute('delete detalii_vol where id_voluntar = ' + id_nume)
                aux.execute('commit')
                aux.close()

                aux = con.cursor()
                aux.execute('delete voluntari where id_voluntar = ' + id_nume)
                aux.execute('commit')
                aux.close()
            case "2":
                id_nume = request.form["al.nume"]

                aux = con.cursor()
                aux.execute('delete voluntari_alumni where id_voluntar = ' + id_nume)
                aux.execute('commit')
                aux.close()

            case "3":
                id = request.form["dep.nume"]

                aux = con.cursor()
                aux.execute('delete departamente where id_departament = ' + id)
                aux.execute('commit')
                aux.close()

            case "4":
                id = request.form["rol.nume"]

                aux = con.cursor()
                aux.execute('delete roluri where id_rol = ' + id)
                aux.execute('commit')
                aux.close()

            case "5":
                id = request.form["ev.nume"]

                aux = con.cursor()
                aux.execute('delete parteneri_evenimente where evenimente_id_event = ' + id)
                aux.execute('commit')
                aux.close()

                aux = con.cursor()
                aux.execute('delete evenimente where id_event = ' + id)
                aux.execute('commit')
                aux.close()

            case "6":
                id = request.form["p.nume"]

                aux = con.cursor()
                aux.execute('delete parteneri_evenimente where parteneri_id_partener = ' + id)
                aux.execute('commit')
                aux.close()

                aux = con.cursor()
                aux.execute('delete parteneri where id_partener = ' + id)
                aux.execute('commit')
                aux.close()
            case _:
                print(table)

        return redirect('/')
    else:
        return render_template("delete.html", rootPath=rootPath, voluntari=voluntari, detalii=detalii, voluntariAlumni=voluntariAlumni, departamente=departamente, roluri=roluri, evenimente=evenimente, sponsori=sponsori, parteneri=parteneri)

@app.route('/modify', methods=['POST', 'GET'])
def modify():
    if request.method == 'POST':
        query = request.form["stringN"]
        query2 = request.form["detalii"]

        print(query)
        if(query != "none"):
            aux = con.cursor()
            aux.execute(query)
            con.commit()
            aux.close()

        if(query2 != "none"):
            aux = con.cursor()
            aux.execute(query2)
            con.commit()
            aux.close()

        return redirect('/')
    else:
        return render_template('modify.html', rootPath=rootPath, voluntari=voluntari, detalii=detalii, voluntariAlumni=voluntariAlumni, departamente=departamente, roluri=roluri, evenimente=evenimente, sponsori=sponsori, parteneri=parteneri)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
    con.close()