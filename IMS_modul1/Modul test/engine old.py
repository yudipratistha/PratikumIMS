import pymysql
import time

db_toko = pymysql.connect("localhost", "root", "", "db_toko")
db_bank = pymysql.connect("localhost", "root", "", "db_bank")
cursor_toko = db_toko.cursor()
cursor_bank = db_bank.cursor()

count_db_toko = "select count(id_transaksi) from tb_transaksi"
cursor_toko.execute(count_db_toko)
data_cursor_toko1 = cursor_toko.fetchone()
count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
cursor_bank.execute(count_db_bank)
data_cursor_bank1 = cursor_bank.fetchone()


while True:
    delay = 2
    time.sleep(delay)

    cursor_toko.execute(count_db_toko)
    data_cursor_toko2 = cursor_toko.fetchone()
    cursor_bank.execute(count_db_bank)
    data_cursor_bank2 = cursor_bank.fetchone()

    sql_toko = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_toko' AND TABLE_NAME = 'tb_transaksi'"
    cursor_toko.execute(sql_toko)
    increment_toko = cursor_toko.fetchone()

    sql_bank = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_bank' AND TABLE_NAME = 'tb_transaksi_toko'"
    cursor_bank.execute(sql_bank)
    increment_bank = cursor_bank.fetchone()

    print("increment", increment_toko[0], increment_bank[0])
    if (increment_toko[0]) > (increment_bank[0]):
        # print("Terjadi penambahan data")

        # print(data_trans_toko)
        cursor_toko.execute("SELECT * FROM tb_transaksi WHERE id_transaksi=%s", increment_bank)
        data_trans_toko = cursor_toko.fetchall()
        # print(data_trans_bank)
        for row in data_trans_toko:
            print(row)
            cursor_bank.execute("INSERT INTO tb_transaksi_toko VALUES(%s, '%s', '%s', '%s', '%s', '%s')" % (
                row[0], row[1], row[2], row[3], row[4], row[5]))
            db_bank.commit()

    elif (increment_bank[0]) > (increment_toko[0]):
        cursor_bank.execute("SELECT * FROM tb_transaksi_toko WHERE id_transaksi_toko=%s", increment_toko)
        data_trans_bank = cursor_bank.fetchall()
        # print(data_trans_bank)
        for row in data_trans_bank:
            print(row)
            cursor_toko.execute("INSERT INTO tb_transaksi VALUES(%s, '%s', '%s', '%s', '%s', '%s')" % (
                row[0], row[1], row[2], row[3], row[4], row[5]))
            db_toko.commit()

    # else:
    #     print("Tidak ada penambahan data")

    print(data_cursor_toko1[0], data_cursor_bank2[0])
    if (data_cursor_toko1[0] < data_cursor_bank2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()
        for row1 in data_transaksi_bank:
            delete = True
            for row2 in data_transaksi_toko:
                if(row1[0] == row2[0]):
                    delete = False
                    break
            if(delete == True):
                print(row1[0], row2[0])
                print("Terjadi Penghapusan Data Toko")
                cursor_bank.execute("DELETE FROM tb_transaksi_toko WHERE id_transaksi_toko = %s" % row1[0])
                db_bank.commit()
    #
    # elif (data_cursor_bank1[0] < data_cursor_toko2[0]):
    #     sql_toko = "SELECT id_transaksi FROM tb_transaksi"
    #     sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
    #     cursor_toko.execute(sql_toko)
    #     cursor_bank.execute(sql_bank)
    #     data_transaksi_toko = cursor_toko.fetchall()
    #     data_transaksi_bank = cursor_bank.fetchall()
    #     for row1 in data_transaksi_toko:
    #         delete = True
    #         for row2 in data_transaksi_bank:
    #             if (row1[0] == row2[0]):
    #                 delete = False
    #                 break
    #         if (delete == True):
    #             print("Terjadi Penghapusan Data Bank")
    #             cursor_toko.execute("DELETE FROM tb_transaksi WHERE id_transaksi = %s" % row1[0])
    #             db_toko.commit()
    # else:
    #     print("Tidak ada pengapusan data")

    count_db_toko = "select count(id_transaksi) from tb_transaksi"
    cursor_toko.execute(count_db_toko)
    data_cursor_toko1 = cursor_toko.fetchone()
    count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
    cursor_bank.execute(count_db_bank)
    data_cursor_bank1 = cursor_bank.fetchone()

    db_toko.rollback()
    db_bank.rollback()
