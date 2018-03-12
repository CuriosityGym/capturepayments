import razorpay
import time
import os
razorpay_key_id=os.environ['razorpay_key_id']
razorpay_key_secret=os.environ['razorpay_key_secret']
client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))

payment_amount = 1250000

def CapturePayment(paymentID):
    resp = classmethodient.payment.capture(paymentID, payment_amount)
    print("captured")
    print(resp)
    
def requestPaymentsList():
    resp = client.payment.fetch_all()
    items=resp["items"]
    for payment in items:
        print(payment)
        #print("----------------------------------")
        isCaptured=payment["captured"]
        payment_id=payment["id"]
        status=payment["status"]
        print(payment_id)
        #print(str(isCaptured))
        print(status)
        #print(status=="success")
        #if(not isCaptured and status!="failed"):        
        #    print(payment_id)
        #    
        print("Here")

        
while True:
    requestPaymentsList()
    time.sleep(60)
    
