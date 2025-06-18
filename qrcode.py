import qrcode
upi_id = input("Enter your UPI ID =")
bank_name = input("Enter your bank name: ")
amount = input("Enter the amount to pay: ")

payee_name = f"Recipient%20({bank_name.replace(' ', '%20')})"

phonepe_url = f'upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR&mc=1234'

phonepe_qr= qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
