import cx_Oracle

#conn.cur.execute("CREATE TABLE Account (ACCOUNTUSERNAME	VARCHAR2(15) NOT NULL,ACCOUNTPASSWORD VARCHAR2(15) NOT NULL,AUTOFILLING	NUMBER(1,0)	NOT NULL,AUTOGENERATING	NUMBER(1,0) NOT NULL,PRIMARY KEY (ACCOUNTUSERNAME))")
#conn.cur.execute("CREATE TABLE FOLDER (FOLDERNAME VARCHAR2(15) NOT NULL,FOLDERACCOUNT VARCHAR2(15) NOT NULL,PRIMARY KEY (FOLDERNAME),FOREIGN KEY (FOLDERACCOUNT) REFERENCES Account(ACCOUNTUSERNAME))")
#conn.cur.execute("CREATE TABLE APPACCOUNT (APPUSERNAME VARCHAR2(15) NOT NULL,APPPASSWORD VARCHAR2(15) NOT NULL,APPNAME VARCHAR2(15) NOT NULL,URL VARCHAR2(50) NOT NULL,NOTE	VARCHAR2(100),APPFOLDERNAME VARCHAR2(15) NOT NULL,PRIMARY KEY (APPUSERNAME),FOREIGN KEY (APPFOLDERNAME) REFERENCES FOLDER(FolderName))")
#cur.execute("CREATE TABLE SECURENOTE (NOTETITLE VARCHAR2(15) NOT NULL,TXT VARCHAR2(100) NOT NULL,APPFOLDERNAME VARCHAR2(15) NOT NULL,PRIMARY KEY (NOTETITLE),FOREIGN KEY (APPFOLDERNAME) REFERENCES FOLDER(FolderName)")

# Account
# Sign Up


def InsertIntoAccount(AccountUserName, AccountPassword, AutoFilling, AutoGenerating):
    conn.cur.execute("INSERT INTO ACCOUNT (AccountUserName, AccountPassword, AutoFilling, AutoGenerating) VALUES (" +
                     AccountUserName+","+AccountPassword + ","+str(AutoFilling)+","+str(AutoGenerating)+")")
    conn.commit()


def RemoveFromAccount(AccountUserName):
    conn.cur.execute(
        "DELETE FROM ACCOUNT WHERE AccountUserName = "+AccountUserName)
    conn.commit()


def UpdatePasswordAccount(AccountUserName, AccountPassword):
    conn.cur.execute("UPDATE ACCOUNT SET AccountPassword = " +
                     AccountPassword+" WHERE AccountUserName = "+AccountUserName)
    conn.commit()


def FetchAccountPassword(AccountUserName):
    checkPass = conn.cur.execute(
        "SELECT AccountPassword FROM Account WHERE AccountUserName = "+AccountUserName)
    return checkPass

# Folder


def InsertIntoFolder(FolderName, FolderAccount):
    conn.cur.execute(
        "INSERT INTO FOLDER (FolderName,FolderAccount) VALUES ("+FolderName+","+FolderAccount+")")
    conn.commit()


def RemoveFromFolder(FolderName):
    conn.cur.execute(
        "DELETE FROM APPACCOUNT WHERE APPFOLDERNAME = "+FolderName)
    #  conn.cur.execute("DELETE FROM SE conn.curENOTE WHERE APPFOLDERNAME = "+FolderName)
    conn.cur.execute("DELETE FROM FOLDER WHERE FolderName = "+FolderName)
    conn.commit()

# AppAccount


def InsertIntoAppAccount(AppUserName, AppPassword, AppName, URL, Note, AppFolderName):
    conn.cur.execute("INSERT INTO APPACCOUNT (AppUserName, AppPassword,AppName, URL,Note, AppFolderName) VALUES (" +
                     AppUserName+","+AppPassword+","+AppName+","+URL+","+Note+","+AppFolderName+")")
    conn.commit()


def RemoveFromAppAccount(AppAccountUserName):
    conn.cur.execute(
        "DELETE FROM APPACCOUNT WHERE AppAccountUserName = "+AppAccountUserName)
    conn.commit()


def UpdatePasswordAppAccount(AppAccountUserName, AppAccountPassword):
    conn.cur.execute("UPDATE APPACCOUNT SET AppAccountPassword = " +
                     AppAccountPassword+" WHERE AppAccountUserName = "+AppAccountUserName)
    conn.commit()


def FetchAppAccountRecord(AppAccountUserName):
    rows = conn.cur.execute(
        "SELECT * FROM AppAccount WHERE AppAccountUserName = "+AppAccountUserName)
    return rows


"""
#Se conn.cureNote
def InsertIntoSN( NOTETITLE,TXT,APPFOLDERNAME):
      conn.cur.execute("INSERT INTO SE conn.curENOTE (NOTETITLE, TXT,APPFOLDERNAME) VALUES ("+NOTETITLE+","+TXT+","+APPFOLDERNAME+")")
     conn.commit()
def RemoveFromSN( NOTETITLE):
      conn.cur.execute("DELETE FROM SE conn.curENOTE WHERE NOTETITLE = "+NOTETITLE)
     conn.commit()
def FetchSN( table,AppAccountUserName):
    rows =   conn.cur.execute("SELECT * FROM " +table+" WHERE AppAccountUserName = "+AppAccountUserName)
    return rows
"""


def Fetchall(table):
    conn.cur.execute("SELECT * FROM "+table)
    rows = conn.cur.fetchall()
    return rows


if __name__ == "__main__":
    conn = cx_Oracle.connect('app/app@//localhost:1521/xe')
    conn.commit()
