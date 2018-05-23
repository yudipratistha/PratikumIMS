import pymysql
import json
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
        print("delete di toko", increment_bank)
        db_bank.commit()
    elif (increment_bank[0] == 1):
        cursor_toko.execute("ALTER TABLE `db_toko`.`tb_transaksi` AUTO_INCREMENT=1")
        sql_toko = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
        cursor_toko.execute(sql_toko)
        increment_toko = cursor_toko.fetchone()
        print("delete di bank", increment_toko)
        db_toko.commit()

    # print(increment_toko[0], increment_bank[0])
    # print(data_cur_toko1[0], data_cur_bank2[0])
    if (increment_toko[0]) > (increment_bank[0]):
        file="text.json"
        try:
            f = open(file, "r")
            data = json.loads(f.read())
            f.close()
        except:
            data = []
        json_bank = {{'id_transaksi': id_transaksi, 'nama_member': nama_member, 'no_transaksi': no_transaksi,
                      'status_transaksi': status_transaksi,
                      'tanggal_transaksi': str(tanggal_transaksi), 'tanggal_transaksi': str(tanggal_transaksi),
                      'status_json': 'insert'}}

        selisih_data_toko = increment_toko[0] - increment_bank[0]
        print(selisih_data_toko, increment_toko[0], increment_toko[0])
        cursor_toko.execute("SELECT * FROM tb_transaksi ORDER BY tanggal_transaksi DESC LIMIT %s", selisih_data_toko)
        data_trans_toko = cursor_toko.fetchall()

        for row in data_trans_toko:
            print("Terjadi penambahan data toko")

        data.append(json_bank)
        f = open(file, "w")
        f.write(json.dumps(data, indent=4))
        f.close()

    if (data_cur_toko1[0] < data_cur_bank2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()
        for row_toko in data_transaksi_bank:
            delete = True
            for row_bank in data_transaksi_toko:
                if (row_toko[0] == row_bank[0]):
                    delete = False
                    break
            if (delete == True):
                print("delete toko")
                cursor_bank.execute("DELETE FROM tb_transaksi_toko WHERE id_transaksi_toko = %s" % row_toko[0])
                db_bank.commit()

    else:
        print("Tidak ada perubahan data")



