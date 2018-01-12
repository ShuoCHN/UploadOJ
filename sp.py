from splinter import Browser
import time,os

location ="D:\\vijos\\data"
url = "http://114.115.144.80/admin/problem/create"
cookie = {'csrftoken':'n4NtLzrmyStbGc9w56sMLdHDMU3nDABwNASfLdxjb7XEzOTzixb02sbenQvtAvxw', 'sessionid':'ry660r2oyjdfmv4akwb8ux5gfu7coefi'}
up_inf = {}
id_list=[ '1012', '1013', '1014', '1015', '1016', '1017', '1018','1019','1020', '1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1029', '1030', '1031', '1032', '1033', '1034', '1035', '1036', '1037', '1038', '1039', '1040', '1041', '1042', '1044', '1045', '1046', '1047', '1048', '1051', '1052', '1053', '1054', '1055', '1056', '1057', '1059', '1060', '1061', '1062', '1063', '1064', '1065', '1066', '1067', '1068', '1069', '1070', '1071', '1072', '1073', '1076', '1078', '1080', '1081', '1082', '1083', '1087', '1089', '1090', '1091', '1092', '1093', '1094', '1095', '1096', '1097', '1098', '1099', '1100', '1101', '1102', '1103', '1104', '1105', '1106', '1107', '1112', '1113', '1114', '1115', '1116', '1117', '1118', '1119', '1120', '1121', '1122', '1123', '1124', '1125', '1126', '1127', '1128', '1129', '1130', '1131', '1132', '1133', '1134', '1136', '1137', '1138', '1139', '1141', '1143', '1144', '1146', '1148', '1151', '1152', '1153', '1154', '1155', '1156', '1157', '1159', '1162', '1164', '1165', '1166', '1167', '1168', '1169', '1171', '1172', '1176', '1178', '1179', '1180', '1181', '1182', '1184', '1185', '1187', '1190', '1192', '1193', '1194', '1195', '1196', '1197', '1198', '1199', '1200', '1201', '1202', '1203', '1204', '1205', '1206', '1208', '1209', '1210', '1211', '1212', '1214', '1215', '1216', '1217', '1218', '1220', '1222', '1223', '1226', '1228', '1229', '1230', '1231', '1232', '1234', '1235', '1236', '1237', '1238', '1242', '1244', '1245', '1246', '1248', '1249', '1250', '1253', '1255', '1257', '1258', '1263', '1264', '1277', '1279', '1280', '1281', '1282', '1283', '1284', '1285', '1286', '1288', '1290', '1291', '1292', '1294', '1297', '1299', '1300', '1301', '1302', '1303', '1304', '1306', '1307', '1308', '1309', '1310', '1311', '1312', '1313', '1314', '1315', '1316', '1317', '1318', '1319', '1320', '1321', '1322', '1323', '1324', '1325', '1327', '1328', '1329', '1331', '1333', '1334', '1335', '1336', '1337', '1338', '1339', '1340', '1341', '1342', '1343', '1344', '1345', '1346', '1347', '1350', '1351', '1352', '1353', '1354', '1355', '1356', '1357', '1359', '1360', '1361', '1362', '1363', '1364', '1365', '1366', '1367', '1368', '1369', '1370', '1371', '1372', '1373', '1375', '1377', '1378', '1379', '1380', '1381', '1382', '1383', '1384', '1385', '1386', '1388', '1389', '1390', '1391', '1393', '1397', '1398', '1399', '1401', '1404', '1405', '1406', '1407', '1408', '1409', '1412', '1414', '1415', '1417', '1419', '1421', '1423', '1424', '1425', '1426', '1427', '1428', '1431', '1432', '1433', '1434', '1436', '1437', '1439', '1441', '1443', '1445', '1446', '1447', '1448', '1449', '1450', '1454', '1461', '1465', '1472', '1474', '1475', '1482', '1484', '1485', '1492', '1493', '1495', '1496', '1497', '1498', '1500', '1501', '1503', '1507', '1512', '1514', '1518', '1519', '1521', '1523', '1524', '1530', '1531', '1535', '1540', '1543', '1544', '1547', '1548', '1549', '1551', '1553', '1556', '1558', '1560', '1562', '1566', '1570', '1571', '1572', '1577', '1579', '1588', '1589', '1594', '1597', '1604', '1607', '1609', '1610', '1613', '1617', '1622', '1623', '1625', '1626', '1627', '1628', '1629', '1632', '1634', '1635', '1639', '1646', '1647', '1648', '1653']

probelms_id ={}

b = Browser('chrome')
b.visit(url)
b.cookies.add(cookie)
b.visit(url)

def uppro(dicti,thid):
    try:

        b.visit(url)



        lis = b.find_by_tag("input")
        time.sleep(0.5)
        lis[0].fill(dicti["displayid"]) #display id
        time.sleep(0.5)
        lis[1].fill(dicti['name']) #title



        text_are = b.find_by_tag("textarea")
        time.sleep(0.2)
        text_are[0].fill(dicti["des"]) #description
        time.sleep(0.2)
        text_are[2].fill(dicti["inpdes"]) #inputdescription
        time.sleep(0.2)
        text_are[4].fill(dicti["outdes"]) #outputdescription

        buttons = b.find_by_tag("button")
        buttons.first.click() #tag button

        lis[26].fill("1000")#time limit
        time.sleep(0.2)
        lis[27].fill("128")#memory limit
        time.sleep(0.2)

        lis = b.find_by_tag("input")
        time.sleep(0.2)
        lis[30].fill("Basic\n")# tag

        text_are[6].fill(dicti["inpsam"]) #input sample
        time.sleep(0.2)
        text_are[7].fill(dicti["outsam"])#output sample
        time.sleep(0.2)
        time.sleep(0.2)
        b.attach_file("file",dicti["ziploc"]) #upload files
        time.sleep(2)
        buttons.last.click()
        time.sleep(1)

    except:
        print(str(thid) + "problems with network problem")
        probelms_id[str(thid)] = "network problems"
        return


def dict(pro_id):
    try:
        path = location+"\\P"+str(pro_id)
        os.chdir(path)
        zip_loc = path+"\\ad.zip"

        file_name = open("Name.txt", "rb")
        str_name = file_name.read().decode("utf8")



        file_des = open("Description.txt","rb")
        str_des = file_des.read().decode("gbk")

        file_inpdes = open("InputFormat.txt", "rb")
        str_inpdes = file_inpdes.read().decode("gbk")
        file_outdes = open("OutputFormat.txt", "rb")
        str_outdes = file_outdes.read().decode("gbk")

        file_inpsample = open("SampleInput.txt", "rb")
        str_inpsample = file_inpsample.read().decode("gbk")
        file_outsample = open("SampleOutput.txt", "rb")
        str_outsample = file_outsample.read().decode("gbk")

        up_inf['displayid']=str(pro_id)
        up_inf['name']=str_name

        up_inf['des']=str_des

        up_inf['inpdes'] = str_inpdes
        up_inf['outdes'] = str_outdes

        up_inf['inpsam'] = str_inpsample
        up_inf['outsam'] = str_outsample

        up_inf['ziploc'] = zip_loc
    except:
        print(str(pro_id)+"problems with dict problem")
        probelms_id[str(pro_id)]="dict problems"
        return 5





def work(con):
    re = 0
    for i in id_list:
        if int(i) < con:
            continue
        else:
            up_inf.clear()
            re = 0
            re = dict(int(i))
            if re != 5:
                uppro(up_inf,i)
        print(i+"has been succeed!")



if __name__=='__main__':
    work(1515)

    print(probelms_id)
