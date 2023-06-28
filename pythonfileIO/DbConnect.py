import pyodbc


class CrudClass:

    def __init__(self,name,phone,email,address,id):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.id=id
      
        
        
       
    def DBConnection(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=Servername;'
                                'Database=SampleDatabase;'
                                'Trusted_Connection=yes;')
            return conn
        except:
            print("Connection failure !!")
            return ''
        
    def GetRecord(self,conn):
        cursor=conn.cursor()
        sql=str("""Select [CustomerName],[CustomerPhone],[CustomerAddress],[CustomerEmail]
                   FROM dbo.customer where (id={0} or [CustomerName]='{1}')""").format(self.id,self.name)

        cursor.execute(sql)
        results=cursor.fetchall()
        print(results)
        print(cursor.rowcount)
        if(cursor.rowcount!=0):
            for col in cursor:
                print(col)          
       
        
    def AddRecord(self,conn):
        cursor=conn.cursor()
        print(cursor)
        sql=str('''INSERT INTO [dbo].[Customer] ([CustomerName] ,[CustomerPhone],[CustomerAddress] ,[CustomerEmail]) 
                VALUES  ('{0}',{1},'{2}','{3}')''').format(self.name,self.phone,self.address,self.email)
        cursor.execute(sql)
        conn.commit()
        
        print("New Record Inserted!")
        
        
    def UpdateRecord(self,conn):
        cursor=conn.cursor()
        sql=str('''Update [dbo].[Customer] SET [CustomerName]='{0}' ,[CustomerPhone]={1} ,[CustomerAddress]='{2}',[CustomerEmail]='{3}' WHERE id={4}''').format(self.name,self.phone,self.address,self.email,self.id)
        
        cursor.execute(sql)
        conn.commit()
        print("Record Modified")
       
    
    def DeleteRecord(self,conn):
        cursor=conn.cursor()
        sql=str("""Delete from [dbo].[Customer]
            where (id={0} or [CustomerName]='{1}')""").format(self.id,self.name)

        cursor.execute(sql)
        conn.commit()
        print("Record Deleted!")
       
       
        
'''Start Main Function'''    
name= input("Enter the Customer name : ")
phone = input("Enter the Customer Phone : ")
address = input("Enter the Customer Address : ")
email = input("Enter the Customer Email : ") 
id=input("Enter the customer ID :")
objCrudClass=CrudClass(name,phone,email,address,id)
conn=objCrudClass.DBConnection()
'''objCrudClass.AddRecord(conn)'''
'''objCrudClass.GetRecord(conn)'''
'''objCrudClass.UpdateRecord(conn)'''
'''objCrudClass.DeleteRecord'''
conn.close()     
        