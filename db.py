
import cx_Oracle

conn = cx_Oracle.connect('app/app@//localhost:1521/xe')
cur = conn.cursor()


def CreateTables():
    """ Create Tables => Account , AppAccount """
    cur.execute("create table Account (AccountUserName varchar(15) NOT NULL , AccountPassword varchar(15) NOT NULL ,PRIMARY KEY(AccountUserName))")
    conn.commit()
    cur.execute("CREATE table AppAccount(AppName varchar(15) NOT NULL,URL varchar(50),AppUserName varchar(15) NOT NULL,AppPassword varchar(15) NOT NULL,Note varchar(100),AppFolderName varchar(15) NOT NULL,Accountname varchar(15) NOT NULL ,FOREIGN KEY (Accountname) REFERENCES Account(ACCOUNTUSERNAME))")
    conn.commit()


# Account

def InsertIntoAccount(AccountUserName, AccountPassword):
    """ Add new Account"""
    cur.execute("INSERT INTO ACCOUNT (ACCOUNTUSERNAME, ACCOUNTPASSWORD) VALUES (" +
                AccountUserName+","+AccountPassword + ")")
    conn.commit()

# ----------------------------------------------


def UpdatePasswordAccount(AccountUserName, AccountPassword):
    """ Change Account's password"""
    cur.execute("UPDATE ACCOUNT SET ACCOUNTPASSWORD = " +
                AccountPassword+" WHERE ACCOUNTUSERNAME = "+AccountUserName)
    conn.commit()


# AppAccount


def InsertIntoAppAccount(APPNAME, URL, APPUSERNAME, APPPASSWORD, Note, APPFOLDERNAME, ACCOUNTNAME):
    """ Add new Application Account """
    cur.execute("INSERT INTO APPACCOUNT (APPNAME, URL,APPUSERNAME, APPPASSWORD,Note, APPFOLDERNAME,ACCOUNTNAME) VALUES (" +
                APPNAME+","+URL+","+APPUSERNAME+","+APPPASSWORD+","+Note+","+APPFOLDERNAME+","+ACCOUNTNAME+")")
    conn.commit()


def RemoveAppFromAppAccount(APPNAME, AppUserName, FolderName, ACCOUNTNAME):
    """ Delete Application Account"""
    cur.execute("DELETE FROM APPACCOUNT WHERE APPNAME= "+APPNAME+" and APPUSERNAME = " +
                AppUserName+" and APPFOLDERNAME = "+FolderName+" and ACCOUNTNAME = "+ACCOUNTNAME)
    conn.commit()


def RemoveFolderFromAppAccount(FolderName, ACCOUNTNAME):
    """ Delete Application Account"""
    cur.execute("DELETE FROM APPACCOUNT WHERE APPFOLDERNAME = " +
                FolderName+" and ACCOUNTNAME = "+ACCOUNTNAME)
    conn.commit()


def UpdateAppAccount(APPPASSWORD, Note, APPNAME, AppUserName, FolderName, ACCOUNTNAME):
    """ Change Application Account's Password"""
    cur.execute("UPDATE APPACCOUNT SET AppPassword = "+APPPASSWORD+" ,NOTE = "+Note+" WHERE ACCOUNTNAME = " +
                ACCOUNTNAME + " and APPFOLDERNAME = "+FolderName+" and APPNAME = "+APPNAME+" and APPUSERNAME = "+AppUserName)
    conn.commit()


def UpdateFolderName(ACCOUNTNAME, OldFolderName, NewFolderName):
    """ Change Application Account's Password"""
    cur.execute("UPDATE APPACCOUNT SET APPFOLDERNAME = "+NewFolderName +
                " WHERE APPFOLDERNAME = "+OldFolderName+" and ACCOUNTNAME= "+ACCOUNTNAME)
    conn.commit()


def FetchAccount(ACCOUNTNAME, foldername):
    cur.execute("select * from appaccount where ACCOUNTNAME = " +
                ACCOUNTNAME+" and APPFOLDERNAME = "+foldername)
    rows = cur.fetchall()
    return rows


def FetchNote(APPNAME, AppUserName, FolderName, ACCOUNTNAME):
    cur.execute(
        f"select NOTE from appaccount where ACCOUNTNAME = '{ACCOUNTNAME}' and APPFOLDERNAME = '{FolderName}' and APPUSERNAME = '{AppUserName}' and APPNAME = '{APPNAME}'")
    rows = cur.fetchone()
    return rows[0]


def FetchFolders(ACCOUNTNAME):
    cur.execute(
        "select APPFOLDERNAME from appaccount where ACCOUNTNAME = "+ACCOUNTNAME)
    rows = cur.fetchall()
    return rows


def Fetchall(table):
    """ Get all table's data from DB using table name"""
    cur.execute("SELECT * FROM "+table)
    rows = cur.fetchall()
    return rows


def CloseConn():
    """ Close DB  """
    conn.close()


