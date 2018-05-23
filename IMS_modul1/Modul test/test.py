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
    data_cur_bank = cursor_bank.fetchall()


    if (data_cur_toko1[0]) < (data_cur_toko2[0]):
        print("Terjadi penambahan data")
        selisih_data_toko = data_cur_toko2[0]-data_cur_toko1[0]
        cursor_toko.execute("SELECT * FROM tb_transaksi ORDER BY tanggal_transaksi DESC LIMIT %s",selisih_data_toko)
        data_trans_toko = cursor_toko.fetchall()

        for row in data_trans_toko:
            cursor_bank.execute("INSERT INTO tb_transaksi_toko VALUES(%s, '%s', '%s', '%s', %s, %s)" % (row[0], row[1], row[2], row[3], row))
            db_bank.commit()
    else:
        print("Tidak ada penambahan data")

    if(data_cur_toko1[0] > data_cur_toko2[0]):
        sql_toko = "SELECT id_transaksi FROM tb_transaksi"
        sql_bank = "SELECT id_transaksi_toko FROM tb_transaksi_toko"
        cursor_toko.execute(sql_toko)
        cursor_bank.execute(sql_bank)
        data_transaksi_toko = cursor_toko.fetchall()
        data_transaksi_bank = cursor_bank.fetchall()
        for row1 in data_transaksi_bank:
            delete = True
            for row2 in data_transaksi_toko:
                if(row1[0]==row2[0]):
                    delete = False
                    break
            if(delete == True):
                cursor_bank.execute("DELETE FROM tb_transaksi_toko WHERE id_transaksi_toko = %s" %row1[0])
                db_bank.commit()

    count_db_toko = "select count(id_transaksi) from tb_transaksi"
    cursor_toko.execute(count_db_toko)
    data_cur_toko1 = cursor_toko.fetchone()
    count_db_bank = "select count(id_transaksi_toko) from tb_transaksi_toko"
    cursor_bank.execute(count_db_bank)
    data_cur_bank1 = cursor_bank.fetchone()

    db_toko.rollback()
