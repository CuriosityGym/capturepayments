import razorpay
import time
import os
razorpay_key_id=os.environ['razorpay_key_id']
razorpay_key_secret=os.environ['razorpay_key_secret']
client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))

payment_amount = 1250000
resp = client.payment.fetch_all()

while True:
    for payment in resp["items"]:
        #print(payment)
        #print("----------------------------------")
        isCaptured=payment["captured"]
        payment_id=payment["id"]
        status=payment["status"]
        print(payment_id + " " +str(isCaptured) + " "+ status)
        #print(status=="success")
        #if(not isCaptured and status!="failed"):        
        #    print(payment_id)
        #    resp = classmethodient.payment.capture(payment_id, payment_amount)
        
    time.sleep(60)
