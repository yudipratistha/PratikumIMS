import time
import pymysql
import time

db_toko = pymysql.connect("localhost", "root", "", "db_toko")
db_bank = pymysql.connect("localhost", "root", "", "db_bank")
cursor_toko = db_toko.cursor()
cursor_bank = db_bank.cursor()
# for i in range(0, totalinc[0]):
#         if jumdata[0]!=jumclone[0]:
#             if idtoko[i][0]>idclone[i][0]:
#                 print("delete sedang berlangsung")
#                 cur_clone.execute("delete from tb_transaksi where id_transaksi=%d" %(idclone[i][0]))
#                 con_clone.commit()
# #                 break
# data = [
#     ("Yudi", "11156wwe5"),
#     ("Yudi", "11156wwe5"),
#     ("Yudi", "11156wwe5")
# ]
#
# for person in data:
#     print(data)
#     cursor_toko.executemany("""INSERT INTO tb_transaksi (nama_member, no_transaksi) VALUES(?, ?, ?, ?, ?, ?)""", data)

# cursor_toko.executemany("""INSERT INTO tb_transaksi (nama_member, no_transaksi)
#                    VALUES(%s, %s)""", [
#                     ('Geetha','Ramam'),
#                     ('Radha','Krishna'),
#                     ('Ramesh','Tiwari'),
#                     ('Govind','Nihalani'),
#                     ('Yousuf','Patel')])
# db_toko.commit()

import pymysql
import time

def new_update(con_toko, con_clone):
    cur_toko = con_toko.cursor()
    cur_clone = con_clone.cursor()

    cur_toko.execute("select count(id_transaksi) from tb_transaksi")
    cur_clone.execute("select count(id_transaksi) from tb_transaksi")

    jumdata = cur_toko.fetchone()
    jumclone = cur_clone.fetchone()

    if jumdata[0]==jumclone[0]:
        i=0
        for i in range(0, jumdata[0]):
            i=i+1
            cur_toko.execute("select updated_at from tb_transaksi where id_transaksi=%d" %i)
            tokoupdate = cur_toko.fetchone()
            con_toko.commit()
            # print("Update toko: %d" %tokoupdate[0])

            cur_clone.execute("select updated_at from tb_transaksi where id_transaksi=%d" %i)
            cloneupdate = cur_clone.fetchone()
            con_clone.commit()
            # print("Update clone: %d" %cloneupdate[0])

            if tokoupdate[0]>cloneupdate[0]:
                print("ada update di toko")
                cur_toko.execute("select id_transaksi, id_pelanggan, no_rek, total_trans, updated_at from tb_transaksi where id_transaksi=%d" %(i))
                select = cur_toko.fetchone()
                id_transaksi = select[0]
                id_pelanggan = select[1]
                no_rek = select[2]
                total_trans = select[3]
                updated_at = select[4]
                con_toko.commit()

                cur_clone.execute("update tb_transaksi set id_pelanggan=%d, no_rek=%d, total_trans=%d, updated_at=%d where id_transaksi=%d" %(id_pelanggan, no_rek, total_trans, updated_at, i))
                con_clone.commit()
                break

            elif cloneupdate[0]>tokoupdate[0]:
                print("ada update di clone")
                cur_clone.execute("select id_transaksi, id_pelanggan, status_lunas, no_rek, updated_at from tb_transaksi where id_transaksi=%d" %i)
                selectclone = cur_clone.fetchone()
                idtrans = selectclone[0]
                idpelanggan = selectclone[1]
                status = selectclone[2]
                norek = selectclone[3]
                updated_at = selectclone[4]
                con_clone.commit()

                cur_toko.execute("update tb_transaksi set id_pelanggan=%d, no_rek=%d, status_lunas=%d, updated_at=%d where id_transaksi=%d" %(idpelanggan, norek, status, updated_at, i))
                con_toko.commit()

            else:
                # print("Tidak ada perubahan data pada ID ke %i" %i)
                i=i+1