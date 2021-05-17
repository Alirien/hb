
import happybase

HbasePool = happybase.ConnectionPool(
    size=4,
    host='172.20.10.3',
    port=9090,
    table_prefix=None)
f = open('text.txt', 'w',encoding="utf-8")
with HbasePool.connection() as hbase:
    table = hbase.table('umks')
    for key, data in table.scan():
        print(key)
        f.write(str(key)+"\n")
        row = table.row(key, columns=(b'text:text',))
        f.write(row.get(b'text:text').decode('utf-8')+"\n")
print("done")

