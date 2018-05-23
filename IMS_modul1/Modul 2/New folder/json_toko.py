import pymysql
import json
import datetime
import time

# Open database connection
db_toko = pymysql.connect("localhost", "root", "", "db_toko")
db_bank = pymysql.connect("localhost", "root", "", "db_bank")

cursor_toko = db_toko.cursor()
cursor_bank = db_bank.cursor()
count_db_toko = "select count(id_transaksi) from tb_transaksi"
cursor_toko.execute(count_db_toko)
data_cur_toko1 = cursor_toko.fetchone()
count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
cursor_bank.execute(count_db_bank)
data_cur_bank1 = cursor_bank.fetchone()

sql_toko = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
cursor_toko.execute(sql_toko)
increment_toko2 = cursor_toko.fetchone()

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
with open("text.json", "w", encoding='utf-8')as outfile:
        try:
            data = json.load(outfile)
        except:
            data = []
def insertJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at):
    with open("text.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                  'status_transaksi': status_transaksi,
                  'tanggal_transaksi': tanggal_transaksi, 'updated_at': updated_at, 'status_json' : 'insert', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("text.json", "r+", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, default = myconverter, indent=4)

def deletetJSON(id_transaksi):
    with open("text.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'status_json' : 'delete', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("text.json", "w", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, indent=4)

def updateJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, updated_at):
    with open("text.json", "r", encoding='utf-8')as outfile:
        try:
            list_data = json.load(outfile)
        except:
            list_data = []
    json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                  'status_transaksi': status_transaksi,
                  'updated_at':updated_at, 'status_json' : 'update', 'status_sinkron' : True}
    list_data.append(json_toko)
    with open("text.json", "w", encoding='utf-8')as outfile:
        json.dump(list_data, outfile, default = myconverter, indent=4)

# def updateNamaJSON(id_transaksi, nama_member, updated_at):
#     json_toko = {'id_transaksi': id_transaksi, 'nama_member': nama_member, 'updated_at': str(updated_at), 'status_json' : 'update', 'status_sinkron' : True}
#     list_data.append(json_toko)
#     with open("text.json", "w", encoding='utf-8')as outfile:
#         json.dump(list_data, outfile, default = myconverter, indent=4)
# def updateNoTransaksiJSON(id_transaksi, no_transaksi, updated_at):
#     json_toko = {'id_transaksi': id_transaksi, 'no_transaksi': no_transaksi, 'updated_at': str(updated_at), 'status_json' : 'update', 'status_sinkron' : True}
#     list_data.append(json_toko)
#     with open("text.json", "w", encoding='utf-8')as outfile:
#         json.dump(list_data, outfile, default = myconverter, indent=4)
# def updateStatusTransaksiJSON(id_transaksi, status_transaksi, updated_at):
#     json_toko = {'id_transaksi': id_transaksi, 'status_transaksi': status_transaksi, 'updated_at': str(updated_at), 'status_json' : 'update', 'status_sinkron' : True}
#     list_data.append(json_toko)
#     with open("text.json", "w", encoding='utf-8')as outfile:
#         json.dump(list_data, outfile, default = myconverter, indent=4)

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

    sql_toko = "SELECT MAX(id_transaksi) from tb_transaksi max"
    cursor_toko.execute(sql_toko)
    max_toko = cursor_toko.fetchone()

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
        print(selisih_data_toko, increment_toko[0], increment_toko[0])
        cursor_toko.execute("SELECT * FROM tb_transaksi ORDER BY tanggal_transaksi DESC LIMIT %s", selisih_data_toko)
        data_trans_toko = cursor_toko.fetchall()
        with open("text.json", "r", encoding='utf-8')as outfile:
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

                print("Terjadi penambahan data toko")
                id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at = row1[0], row1[1], row1[2], row1[3], row1[4], row1[5]
                insertJSON(id_transaksi, nama_member, no_transaksi, status_transaksi, tanggal_transaksi, updated_at)


    # else:
    #     print("Tidak ada perubahan data")

    if (data_cur_toko1[0] < data_cur_bank2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()

        with open("text.json", "r", encoding='utf-8') as outfile:
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
                    deletetJSON(row_toko[0])

    sql_toko = "SELECT * FROM tb_transaksi"
    sql_bank = "SELECT * FROM tb_transaksi_toko"
    cursor_toko.execute(sql_toko)
    cursor_bank.execute(sql_bank)
    data_transaksi_bank = cursor_bank.fetchall()
    data_transaksi_toko = cursor_toko.fetchall()
    with open("text.json", "r", encoding='utf-8') as outfile:
        try:
            data = json.load(outfile)
        except:
            data = []
    for row_toko in data_transaksi_toko:
        for row_bank in data_transaksi_bank:
            if (row_toko[0] == row_bank[0]):
                if row_toko[5] > row_bank[5]:
                    if (row_toko[1] != row_bank[1] or row_toko[2] != row_bank[2] or row_toko[3] != row_bank[3]):
                        update = True
                    for row_json_toko in data:
                        if (row_toko[1] == row_json_toko['nama_member'] and row_toko[2] == row_json_toko['no_transaksi'] and row_toko[3] == row_json_toko['status_transaksi']):
                            update = False
                            break

                    if(update == True):
                        print("Update Data")
                        # print(row_toko[0], row_toko[1], row_toko[2], row_toko[3], row_toko[5])
                        updateJSON(row_toko[0], row_toko[1], row_toko[2], row_toko[3], row_toko[5])

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



