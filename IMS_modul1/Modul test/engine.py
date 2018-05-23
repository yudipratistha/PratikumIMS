import pymysql
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
        selisih_data_toko = increment_toko[0] - increment_bank[0]
        print(selisih_data_toko, increment_toko[0], increment_toko[0])
        cursor_toko.execute("SELECT * FROM tb_transaksi ORDER BY tanggal_transaksi DESC LIMIT %s", selisih_data_toko)
        data_trans_toko = cursor_toko.fetchall()

        for row in data_trans_toko:
            print("Terjadi penambahan data toko")
            cursor_bank.execute("INSERT INTO tb_transaksi_toko VALUES(%s, '%s', '%s', '%s', '%s', '%s')" % (
            row[0], row[1], row[2], row[3], row[4], row[5]))
            db_bank.commit()

    elif (increment_bank[0]) > (increment_toko[0]):
        selisih_data_bank = increment_bank[0] - increment_toko[0]
        print(selisih_data_bank, increment_toko[0], increment_toko[0])
        cursor_bank.execute("SELECT * FROM tb_transaksi_toko ORDER BY tanggal_transaksi DESC LIMIT %s", selisih_data_bank)
        data_trans_bank = cursor_bank.fetchall()

        for row in data_trans_bank:
            print("Terjadi penambahan data bank")
            cursor_toko.execute("INSERT INTO tb_transaksi VALUES(%s, '%s', '%s', '%s', '%s', '%s')" % (
            row[0], row[1], row[2], row[3], row[4], row[5]))
            db_toko.commit()
    else:
        print("Tidak ada penambahan data")

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
    # print(data_cur_bank2[0], data_cur_toko2)
    elif (data_cur_bank1[0] < data_cur_toko2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()
        for row_toko in data_transaksi_toko:
            delete = True
            for row_bank in data_transaksi_bank:
                if (row_toko[0] == row_bank[0]):
                    delete = False
                    break
            if (delete == True):
                print("delete bank")
                cursor_toko.execute("DELETE FROM tb_transaksi WHERE id_transaksi = %s" % row_toko[0])
                db_toko.commit()

    sql_toko = "SELECT * FROM tb_transaksi"
    sql_bank = "SELECT * FROM tb_transaksi_toko"
    cursor_toko.execute(sql_toko)
    cursor_bank.execute(sql_bank)
    data_transaksi_bank = cursor_bank.fetchall()
    data_transaksi_toko = cursor_toko.fetchall()
    for row_toko in data_transaksi_toko:
        for row_bank in data_transaksi_bank:
            if (row_toko[0] == row_bank[0]):
                if(row_toko[5] < row_bank[5]):
                    if(row_toko[1] != row_bank[1]):
                        cursor_toko.execute("UPDATE tb_transaksi SET nama_member = '%s' WHERE id_transaksi = %s" % (row_bank[1], row_toko[0]))
                        db_toko.commit()
                    if (row_toko[2] != row_bank[2]):
                        cursor_toko.execute("UPDATE tb_transaksi SET no_transaksi = '%s' WHERE id_transaksi = %s" % (row_bank[2], row_toko[0]))
                        db_toko.commit()
                    if (row_toko[3] != row_bank[3]):
                        cursor_toko.execute("UPDATE tb_transaksi SET status_transaksi  = '%s' WHERE id_transaksi = %s" % (row_bank[3], row_toko[0]))
                        db_toko.commit()
                    cursor_bank.execute("UPDATE tb_transaksi_toko SET updated_at = '%s' WHERE id_transaksi_toko = %s" % (row_bank[5], row_toko[0]))
                    db_bank.commit()
                elif(row_toko[5] > row_bank[5]):
                    if (row_toko[1] != row_bank[1]):
                        cursor_bank.execute("UPDATE tb_transaksi_toko SET nama_member = '%s' WHERE id_transaksi_toko = %s" % (row_toko[1], row_toko[0]))
                        db_bank.commit()
                    if (row_toko[2] != row_bank[2]):
                        cursor_bank.execute("UPDATE tb_transaksi_toko SET no_transaksi = '%s' WHERE id_transaksi_toko = %s" % (row_toko[2], row_toko[0]))
                        db_bank.commit()
                    if (row_toko[3] != row_bank[3]):
                        cursor_bank.execute("UPDATE tb_transaksi_toko SET status_transaksi  = '%s' WHERE id_transaksi_toko = %s" % (row_toko[3], row_toko[0]))
                        db_bank.commit()
                    cursor_toko.execute("UPDATE tb_transaksi SET updated_at = '%s' WHERE id_transaksi = %s" % (row_toko[5], row_toko[0]))
                    db_toko.commit()

    count_db_toko = "select count(id_transaksi) from tb_transaksi"
    cursor_toko.execute(count_db_toko)
    data_cur_toko1 = cursor_toko.fetchone()
    count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
    cursor_bank.execute(count_db_bank)
    data_cur_bank1 = cursor_bank.fetchone()

    db_toko.rollback()
    db_bank.rollback()
