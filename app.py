from flask import Flask , request , render_template
import mysql.connector
app = Flask(__name__)
conn=mysql.connector.connect(host="remotemysql.com",user="HdI94neOEI",password="sF39aYIGxX",database="HdI94neOEI")
#QTwvppCmgD
#HdI94neOEI
cursor=conn.cursor()

########################################### Transfer ##############################################################
@app.route('/transfer')
def transfer():
    return render_template('transfer.html')

@app.route('/amount_transferred')
def amount_transferred():
    cust_id=request.form.get('cust_id')
    sacctyp= request.form.get('S-acctyp')
    tacctyp= request.form.get('T-acctyp')  
    t_amt=request.form.get('t_amt')
    
    cursor.execute("""INSERT INTO `transactions` (`ws_cust_id`,,`ws_src_typ`,`ws_tgt_typ`,`ws_amt`) VALUES ('{}',{}','{}','{}')""".format(cust_id,sacctyp,tacctyp,t_amt))
    conn.commit()
    return render_template('status.html')
########################################### customer updation ##############################################################
    
@app.route('/customer_search')
def customer_search():
	return render_template('customer_search.html')

@app.route('/find_customer',methods=['POST'])
def find_customer():
    ssn_id=request.form.get('ssnid')
    cus_id=request.form.get('customerid')
    cursor.execute("""SELECT * FROM `customer` WHERE `ws_ssn` LIKE '{}' OR `ws_cust_id` LIKE '{}'""".format(ssn_id,cus_id))
    data=cursor.fetchall()
    return render_template('update_customer.html',value=data)

@app.route('/customer_updation',methods=['POST'])
def customer_updation():
    cusid=request.form.get('cust_id')
    name=request.form.get('nname')
    age=request.form.get('nage')
    address1=request.form.get('new_address')
    
    cursor.execute("""UPDATE `customer` SET `ws_name`='{}',`ws_age`='{}' , `ws_adrs`='{}' WHERE `ws_cust_id`='{}'""".format(name,age,address1,cusid))
    conn.commit()
    return render_template('status.html')    
################################################## Account withdrawal ####################################################################
@app.route('/account_search')
def account_search():
	return render_template('account_search.html')

@app.route('/find_account_to_withdraw',methods=['POST'])
def find_account_to_withdraw():
    acct_id=request.form.get('accountid')
    cus_id=request.form.get('customerid')
    cursor.execute("""SELECT * FROM `account` WHERE `ws_acct_id` LIKE '{}' OR `ws_cust_id` LIKE '{}'""".format(acct_id,cus_id))
    data=cursor.fetchall()
    return render_template('account_withdraw.html',value=data)

@app.route('/amount_withdrawal',methods=['POST'])
def amount_withdrawal():
    withdrawal=request.form.get('amt')
    cusid=request.form.get('cust_id')
    cursor.execute("""UPDATE `account` SET `ws_acct_balance`='{}'  WHERE `ws_cust_id`='{}'""".format(withdrawal,cusid))
    conn.commit()
    return render_template('status.html')

################################################## Account Deposit ####################################################################
@app.route('/account_search2')
def account_search2():
	return render_template('account_search2.html')

@app.route('/find_account_to_deposit',methods=['POST'])
def find_account_to_deposit():
    acct_id=request.form.get('accountid')
    cus_id=request.form.get('customerid')
    cursor.execute("""SELECT * FROM `account` WHERE `ws_acct_id` LIKE '{}' OR `ws_cust_id` LIKE '{}'""".format(acct_id,cus_id))
    data=cursor.fetchall()
    return render_template('account_deposit.html',value=data)

@app.route('/amount_deposit',methods=['POST'])
def amount_deposit():
    deposit=request.form.get('amt')
    cusid=request.form.get('cust_id')
    cursor.execute("""UPDATE `account` SET `ws_acct_balance`='{}'  WHERE `ws_cust_id`='{}'""".format(deposit,cusid))
    conn.commit()
    return render_template('status.html')

############################################# Account Creation and deletion ##########################################
@app.route('/create_account')
def create_account():
	return render_template('create_account.html')

@app.route('/account_creation',methods=['POST'])
def account_creation():
    cust_id=request.form.get('cust_id')
    acc_type=request.form.get('acctyp')
    deposit=request.form.get('amt')
    cursor.execute("""INSERT INTO `account` (`ws_cust_id`,`ws_acct_type`,`ws_acct_balance`) VALUES ('{}','{}','{}')""".format(cust_id,acc_type,deposit))    
    conn.commit()
    return render_template('status.html')

@app.route('/delete_account')
def delete_account():
    return render_template('del_acct.html')

@app.route('/account_deletion',methods=['POST'])
def account_deletion():
    acct_id=request.form.get('acc_id')
    acc_type=request.form.get('acctyp')
    cursor.execute("""DELETE FROM `account` WHERE `ws_acct_id` LIKE '{}' AND `ws_acct_type` LIKE '{}'""".format(acct_id,acc_type))
    conn.commit()
    return render_template('status.html')               
############################################ customer creation and deletion ##########################################
@app.route('/create_customer')
def create_customer():
	return render_template('create_customer.html')

@app.route('/delete_customer')
def delete_customer():
	return render_template('delete_customer.html')

   
@app.route('/customer_creation',methods=['POST'])
def customer_creation():
    ssn_id=request.form.get('SSN ID')
    
    name=request.form.get('name')
    age=request.form.get('age')
    address1=request.form.get('address1')
    address2=request.form.get('address2')
    city=request.form.get('city')
    state=request.form.get('state')
    cursor.execute("""INSERT INTO `customer` (`ws_ssn`,`ws_name`,`ws_age`,`ws_adrs`) VALUES ('{}','{}','{}','{},{},{},{}')""".format(ssn_id,name,age,address1,address2,city,state))
    conn.commit()
    return "success"
@app.route('/Home')
def home():
    return render_template('base.html')

@app.route('/customer_deletion',methods=['POST'])
def customer_deletion():
    custid=request.form.get('customerid')
    cursor.execute("""DELETE FROM `customer` WHERE `ws_cust_id` LIKE '{}' """.format(custid))
    conn.commit()
    return render_template('base.html')
####################################login and registration###########################    
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/')
def register():
	return render_template('register.html')    
@app.route('/register_validation',methods=['POST'])
def register_validation():
    username=request.form.get('username')
    password=request.form.get('password')
    cursor.execute("""INSERT INTO  `user_login` VALUES ('{}','{}') """.format(username,password))
    conn.commit()
    return render_template('login.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    username=request.form.get('username')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `user_login` WHERE `username` LIKE '{}' AND `password` LIKE '{}' """.format(username,password))
    users=cursor.fetchall()
    if len(users)>0:
        return render_template('base.html')
    else:
	    return render_template('login.html')		
	
if __name__=="__main__":
	app.run(debug=True)