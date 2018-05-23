import pymysql
import json
import datetime
import time
import dropbox
from dropbox.files import WriteMode

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
with open("toko.json", "w", encoding='utf-8')as outfile:
        try:
            data = json.load(outfile)
        except:
            data = []
with open("bank.json", "w", encoding='utf-8')as outfile:
    try:
        data = json.load(outfile)
    except:
        data = []
def insertTokoJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at):
    with open("toko.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                  'status_transaksi': status_transaksi,
                  'tanggal_transaksi': tanggal_transaksi, 'updated_at': updated_at, 'status_json' : 'insert', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("toko.json", "r+", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, default = myconverter, indent=4)

def deleteTokoJSON(id_transaksi):
    with open("toko.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'status_json' : 'delete', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("toko.json", "w", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, indent=4)

def updateTokoJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, updated_at):
    with open("toko.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                  'status_transaksi': status_transaksi,
                  'updated_at':updated_at, 'status_json' : 'update', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("toko.json", "w", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, default = myconverter, indent=4)

def insertBankJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at):
    with open("bank.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                  'status_transaksi': status_transaksi,
                  'tanggal_transaksi': tanggal_transaksi, 'updated_at': updated_at, 'status_json' : 'insert', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("bank.json", "r+", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, default = myconverter, indent=4)

def deleteBankJSON(id_transaksi):
    with open("bank.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_bank = {'id_transaksi': id_transaksi, 'status_json' : 'delete', 'status_sinkron' : True}
    list_data.append(json_bank)
    with open("bank.json", "w", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, indent=4)

def updateBankJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, updated_at):
    with open("bank.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                  'status_transaksi': status_transaksi,
                  'updated_at':updated_at, 'status_json' : 'update', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("bank.json", "w", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, default = myconverter, indent=4)

def uploadFileDropbx(file):
    # upload file
    dropbx = dropbox.Dropbox("9oOi49Yp5H0AAAAAAAAKE3ezLerI6ENdOnsvxq3lXGhyq942LYI8lQtxZhgXbuen")
    print("Upload " + file)
    with open(file, "rb") as f:
        dropbx.files_upload(f.read(), '/' + file, mode=dropbox.files.WriteMode.overwrite)

def downloadFileDropbox (file):
    # download file
    dropbx = dropbox.Dropbox("9oOi49Yp5H0AAAAAAAAKE3ezLerI6ENdOnsvxq3lXGhyq942LYI8lQtxZhgXbuen")
    print("Download " + file)
    dropbx.files_download_to_file("json-download/" + file, '/' + file)

# Open database connection
db_toko = pymysql.connect("localhost", "root", "", "db_toko")
cursor_toko = db_toko.cursor()
count_db_toko = "select count(id_transaksi) from tb_transaksi"
cursor_toko.execute(count_db_toko)
data_cur_toko1 = cursor_toko.fetchone()

db_bank = pymysql.connect("localhost", "root", "", "db_bank")
cursor_bank = db_bank.cursor()
count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
cursor_bank.execute(count_db_bank)
data_cur_bank1 = cursor_bank.fetchone()

while True:
    delay = 2
    time.sleep(delay)

    cursor_toko.execute(count_db_toko)
    data_cur_toko2 = cursor_toko.fetchone()

    cursor_bank.execute(count_db_bank)
    data_cur_bank2 = cursor_bank.fetchone()

    sql_toko = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
    cursor_toko.execute(sql_toko)
    increment_toko = cursor_toko.fetchone()

    sql_bank = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_bank' AND TABLE_NAME = 'tb_transaksi_toko'"
    cursor_bank.execute(sql_bank)
    increment_bank = cursor_bank.fetchone()

    if (increment_toko[0] == 1):
        cursor_bank.execute("ALTER TABLE `db_bank`.`tb_transaksi_toko` AUTO_INCREMENT=1")
        sql_bank = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
        cursor_bank.execute(sql_bank)
        increment_bank = cursor_bank.fetchone()
        db_bank.commit()
    elif (increment_bank[0] == 1):
        cursor_toko.execute("ALTER TABLE `db_toko`.`tb_transaksi` AUTO_INCREMENT=1")
        sql_toko = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
        cursor_toko.execute(sql_toko)
        increment_toko = cursor_toko.fetchone()
        db_toko.commit()

    if (increment_toko[0] > increment_bank[0]):
        selisih_data_toko = increment_toko[0] - increment_bank[0]
        cursor_toko.execute("SELECT * FROM tb_transaksi ORDER BY tanggal_transaksi DESC LIMIT %s", selisih_data_toko)
        data_trans_toko = cursor_toko.fetchall()
        with open("toko.json", "r", encoding='utf-8')as outfile:
            try:
                data = json.load(outfile)
            except:
                data = []
        for row1 in data_trans_toko:
            insert=True
            for row2 in data:
                if(row1[0] == row2['id_transaksi'] and row2['status_json'] == 'insert'):
                    insert = False
                    break
            if(insert==True):
                print("Terjadi penambahan data json toko")
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at = row1[0], row1[1], row1[2], row1[3], row1[4], row1[5]
                insertTokoJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at)
                uploadFileDropbx("toko.json")

        downloadFileDropbox("toko.json")
        openfile = open("json-download/toko.json", "r")
        data = json.load(openfile)
        for json_toko in data:
            if json_toko['status_json'] == 'insert' and json_toko['status_sinkron'] == True:
                print("Terjadi penambahan data bank")
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at = \
                    json_toko['id_transaksi'], json_toko['nama_member'], json_toko['no_transaksi'], \
                    json_toko['status_transaksi'], json_toko['tanggal_transaksi'], json_toko['updated_at']
                cursor_bank.execute("INSERT INTO tb_transaksi_toko VALUES(%s, '%s', '%s', '%s', '%s', '%s')" % (
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at))
                db_bank.commit()

                openfilee = open("json-download/toko.json", "r+")
                dataa = json.load(openfilee)
                for row in dataa:
                    row['status_sinkron'] = False
                    openfilee.seek(0)
                    json.dump(dataa, openfilee, indent=4)
                    openfilee.truncate()

    if (increment_bank[0] > increment_toko[0]):
        selisih_data_bank = increment_bank[0] - increment_toko[0]
        cursor_bank.execute("SELECT * FROM tb_transaksi_toko ORDER BY tanggal_transaksi DESC LIMIT %s", selisih_data_bank)
        data_trans_bank = cursor_bank.fetchall()
        with open("bank.json", "r", encoding='utf-8')as outfile:
            try:
                data = json.load(outfile)
            except:
                data = []
        for row1 in data_trans_bank:
            insert=True
            for row2 in data:
                if(row1[0] == row2['id_transaksi'] and row2['status_json'] == 'insert'):
                    insert = False
                    break
            if(insert==True):
                print("Terjadi penambahan data json bank")
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at = row1[0], row1[1], row1[2], row1[3], row1[4], row1[5]
                insertBankJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at)
            uploadFileDropbx("bank.json")

        downloadFileDropbox("bank.json")
        openfile = open("json-download/bank.json", "r")
        data = json.load(openfile)
        for json_bank in data:
            if json_bank['status_json'] == 'insert' and json_bank['status_sinkron'] == True:
                print("Terjadi penambahan data toko")
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at = \
                    json_bank['id_transaksi'], json_bank['nama_member'], json_bank['no_transaksi'], \
                    json_bank['status_transaksi'], json_bank['tanggal_transaksi'], json_bank['updated_at']
                cursor_toko.execute("INSERT INTO tb_transaksi VALUES(%s, '%s', '%s', '%s', '%s', '%s')" % (
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at))
                db_toko.commit()

                openfilee = open("json-download/bank.json", "r+")
                dataa = json.load(openfilee)
                for row in dataa:
                    row['status_sinkron'] = False
                    openfilee.seek(0)
                    json.dump(dataa, openfilee, indent=4)
                    openfilee.truncate()

    # else:
    #     print("Tidak ada perubahan data")

    # DELETE
    if (data_cur_toko1[0] < data_cur_bank2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()

        with open("toko.json", "r", encoding='utf-8') as outfile:
            try:
                data = json.load(outfile)
            except:
                data = []

        for row_toko in data_transaksi_bank:
            delete = True
            for row_bank in data_transaksi_toko:
                if (row_toko[0] == row_bank[0]):
                    delete = False
                    break
            if (delete == True):
                for row2 in data:
                    if (row_toko[0] == row2['id_transaksi'] and row2['status_json'] == 'delete'):
                        delete = False
                        break
                if (delete == True):
                    deleteTokoJSON(row_toko[0])
                uploadFileDropbx("toko.json")

        downloadFileDropbox("toko.json")
        openfile = open("json-download/toko.json", "r")
        try:
            data = json.load(openfile)
        except:
            data = []
        for json_toko in data:
            if json_toko['status_json'] == 'delete' and json_toko['status_sinkron'] == True:
                print("Terjadi delete data bank")
                cursor_bank.execute(
                    "DELETE FROM tb_transaksi_toko WHERE id_transaksi_toko = %s" % json_toko['id_transaksi'])
                db_bank.commit()

                openfilee = open("json-download/toko.json", "r+")
                dataa = json.load(openfilee)
                for row in dataa:
                    row['status_sinkron'] = False
                    openfilee.seek(0)
                    json.dump(dataa, openfilee, indent=4)
                    openfilee.truncate()

    if (data_cur_bank1[0] < data_cur_toko2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()

        with open("bank.json", "r", encoding='utf-8') as outfile:
            try:
                data = json.load(outfile)
            except:
                data = []

        for row_toko in data_transaksi_toko:
            delete = True
            for row_bank in data_transaksi_bank:
                if (row_toko[0] == row_bank[0]):
                    delete = False
                    break
            if (delete == True):
                for row2 in data:
                    if (row_toko[0] == row2['id_transaksi'] and row2['status_json'] == 'delete'):
                        delete = False
                        break
                if (delete == True):
                    print("delete json bank")
                    deleteBankJSON(row_toko[0])
                    uploadFileDropbx("bank.json")

        downloadFileDropbox("bank.json")
        openfilee = open("json-download/bank.json", "r")
        try:
            dataa = json.load(openfilee)
        except:
            dataa =[]
        for json_bank in data:
            if json_bank['status_json'] == 'delete' and json_bank['status_sinkron'] == True:
                print("Terjadi delete data bank")
                cursor_toko.execute(
                    "DELETE FROM tb_transaksi WHERE id_transaksi = %s" % json_bank['id_transaksi'])
                db_toko.commit()

                openfilee = open("json-download/bank.json", "r+")
                dataa = json.load(openfilee)
                for row in dataa:
                    row['status_sinkron'] = False
                    openfilee.seek(0)
                    json.dump(dataa, openfilee, indent=4)
                    openfilee.truncate()

    sql_toko = "SELECT * FROM tb_transaksi"
    sql_bank = "SELECT * FROM tb_transaksi_toko"
    cursor_toko.execute(sql_toko)
    cursor_bank.execute(sql_bank)
    data_transaksi_bank = cursor_bank.fetchall()
    data_transaksi_toko = cursor_toko.fetchall()
    with open("toko.json", "r", encoding='utf-8') as outfile:
        try:
            data = json.load(outfile)
        except:
            data = []
    with open("bank.json", "r", encoding='utf-8') as outfile:
        try:
            data_json_bank = json.load(outfile)
        except:
            data_json_bank = []
    for row_toko in data_transaksi_toko:
        for row_bank in data_transaksi_bank:
            if (row_toko[0] == row_bank[0]):

                if (row_toko[5] < row_bank[5]):
                    if (row_toko[1] != row_bank[1] or row_toko[2] != row_bank[2] or row_toko[3] != row_bank[3]):
                        update = True
                        for row_json_bank in data_json_bank:
                            if (row_bank[1] == row_json_bank['nama_member'] and row_bank[2] == row_json_bank['no_transaksi'] and row_bank[3] == row_json_bank['status_transaksi']):
                                update = False
                                break
                        if(update == True):
                            print("Update Data json bank")
                            updateBankJSON(row_bank[0], row_bank[1], row_bank[2], row_bank[3], row_bank[5])
                            uploadFileDropbx("bank.json")

                        downloadFileDropbox("bank.json")
                    openfile = open("json-download/bank.json", "r")
                    try:
                        data = json.load(openfile)
                    except:
                        data = []
                    for json_bank in data:
                        if json_bank['status_json'] == 'update' and json_bank['status_sinkron'] == True:
                            if (row_toko[1] != json_bank['nama_member']):
                                print('update data')
                                cursor_toko.execute(
                                    "UPDATE tb_transaksi SET nama_member = '%s' WHERE id_transaksi = %s" % (
                                        json_bank['nama_member'], json_bank['id_transaksi']))
                                db_toko.commit()

                            if (row_toko[2] != json_bank['no_transaksi']):
                                print('update data')
                                cursor_toko.execute(
                                    "UPDATE tb_transaksi SET no_transaksi = '%s' WHERE id_transaksi = %s" % (
                                        json_bank['no_transaksi'], json_bank['id_transaksi']))
                                db_toko.commit()
                            if (row_toko[3] != json_bank['status_transaksi']):
                                print('update data')
                                cursor_toko.execute(
                                    "UPDATE tb_transaksi SET status_transaksi = '%s' WHERE id_transaksi = %s" % (
                                        json_bank['status_transaksi'], json_bank['id_transaksi']))
                                db_toko.commit()
                            cursor_toko.execute(
                                "UPDATE tb_transaksi SET updated_at = '%s' WHERE id_transaksi = %s" % (
                                    json_bank['updated_at'], json_bank['id_transaksi']))
                            db_toko.commit()

                            openfilee = open("json-download/bank.json", "r+")
                            dataa = json.load(openfilee)
                            for row in dataa:
                                row['status_sinkron'] = False
                                openfilee.seek(0)
                                json.dump(dataa, openfilee, indent=4)
                                openfilee.truncate()

                if row_toko[5] > row_bank[5]:
                    if (row_toko[1] != row_bank[1] or row_toko[2] != row_bank[2] or row_toko[3] != row_bank[3]):
                        update = True
                        for row_json_toko in data:
                            if (row_toko[1] == row_json_toko['nama_member'] and row_toko[2] == row_json_toko['no_transaksi'] and row_toko[3] == row_json_toko['status_transaksi']):
                                update = False
                                break
                        if(update == True):
                            print("Update Data json toko")
                            updateTokoJSON(row_toko[0], row_toko[1], row_toko[2], row_toko[3], row_toko[5])
                            uploadFileDropbx("toko.json")

                    downloadFileDropbox("toko.json")
                    openfile = open("json-download/toko.json", "r")
                    data = json.load(openfile)
                    for json_toko in data:
                        if json_toko['status_json'] == 'update' and json_toko['status_sinkron'] == True:
                            if (row_bank[1] != json_toko['nama_member']):
                                print('update data')
                                cursor_bank.execute(
                                    "UPDATE tb_transaksi_toko SET nama_member = '%s' WHERE id_transaksi_toko = %s" % (
                                        json_toko['nama_member'], json_toko['id_transaksi']))
                                db_bank.commit()

                            if (row_bank[2] != json_toko['no_transaksi']):
                                print('update data')
                                cursor_bank.execute(
                                    "UPDATE tb_transaksi_toko SET no_transaksi = '%s' WHERE id_transaksi_toko = %s" % (
                                        json_toko['no_transaksi'], json_toko['id_transaksi']))
                                db_bank.commit()
                            if (row_bank[3] != json_toko['status_transaksi']):
                                print('update data')
                                cursor_bank.execute(
                                    "UPDATE tb_transaksi_toko SET status_transaksi = '%s' WHERE id_transaksi_toko = %s" % (
                                        json_toko['status_transaksi'], json_toko['id_transaksi']))
                                db_bank.commit()
                            cursor_bank.execute(
                                "UPDATE tb_transaksi_toko SET updated_at = '%s' WHERE id_transaksi_toko = %s" % (
                                    json_toko['updated_at'], json_toko['id_transaksi']))
                            db_bank.commit()

                            openfilee = open("json-download/toko.json", "r+")
                            dataa = json.load(openfilee)
                            for row in dataa:
                                row['status_sinkron'] = False
                                openfilee.seek(0)
                                json.dump(dataa, openfilee, indent=4)
                                openfilee.truncate()

    sql_toko = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
    cursor_toko.execute(sql_toko)
    increment_toko2 = cursor_toko.fetchone()

    count_db_toko = "select count(id_transaksi) from tb_transaksi"
    cursor_toko.execute(count_db_toko)
    data_cur_toko1 = cursor_toko.fetchone()
    count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
    cursor_bank.execute(count_db_bank)
    data_cur_bank1 = cursor_bank.fetchone()

    db_toko.rollback()
    db_bank.rollback()