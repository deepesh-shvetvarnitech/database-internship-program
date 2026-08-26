'''
                                         SECTION = A
                                        QUESTION = 1 
SQL INJECTION EK SECURITY PROBLEM HAI JISME ATTACKER USER INPUT K THROUGH SQL QUERY K MEANING KO CHANGE KARNE KI KOSHISH KARTA HAI .

                                         QUESTION  =2
query = f"SELECT * FROM customers WHERE email = '{email}'"
cursor.execute(query)
YEH UNSAFE HAI Q KI EMAIL KO DIRECTLY SQL QUERY K ANDER ADD KIYA JA RHA HAI
AGAR NORMAL EMAIL DE:
deepesh@gmail.com
to query normal rahege
lekin malicious sql input dene pr query ka structure change ho sata hai or attacker unwanted records ko access karne ki koshish kar sakta hai

                                           QUESTION = 3
cursor.execute(
    "SELECT * FROM customers WHERE email = ?",
    (email,)
)
ISLIYE SAFE  HAI Q KI USER KA  INPUT SQL CODE NHI HAI,BALKI DATA  MANA JATA HAI.
? EK PLACEHOLDER HOTA HAI. BAAD MEIN (email) KI  VALUE US PLACEHOLDER M SAFELY PROVIDE HOTA HAI

                                    QUESTION = 4
USER PROVIDED VALUES KO DIRECTLY SQL QUERY M CONCATENATE  NHI  KARNA CHAHIYE    Q KI USER INUT TRUSTED HI HOTA HAI

                                     QUESTION = 5
YE FSTRING SE BEHTAR HAI Q KI VALUES SQL STATEMENT SE SEPERATE REHTE HAI
mane,emial,city ko sql code k roop m interpret nhi kiya jata                                     

                                    

                                         '''
 